import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import math


class SpatialDesktop:

    def __init__(self):

        pygame.init()

        self.display = (1100,750)

        pygame.display.set_mode(
            self.display,
            pygame.DOUBLEBUF | pygame.OPENGL
        )

        gluPerspective(45, self.display[0]/self.display[1], 0.1, 50)

        glTranslatef(0,0,-6)

        self.cursor = [0,0,0]

        self.dragging = None

        self.windows = [
            {"name":"Browser","pos":[-2,1,0]},
            {"name":"Music","pos":[0,1,0]},
            {"name":"Files","pos":[2,1,0]},
            {"name":"Terminal","pos":[-1,-1,0]},
            {"name":"Notes","pos":[1,-1,0]}
        ]

    def update_cursor(self, landmarks):

        if len(landmarks) != 21:
            return

        x = landmarks[8][0]*4-2
        y = -(landmarks[8][1]*3-1.5)

        depth = abs(landmarks[8][2])*5

        self.cursor = [x,y,depth]

    def pinch(self, landmarks):

        thumb = landmarks[4]
        index = landmarks[8]

        d = math.sqrt(
            (thumb[0]-index[0])**2 +
            (thumb[1]-index[1])**2
        )

        return d < 0.03

    def update(self, landmarks):

        if len(landmarks) != 21:
            return

        self.update_cursor(landmarks)

        pinching = self.pinch(landmarks)

        cx,cy,cz = self.cursor

        if pinching and self.dragging is None:

            for w in self.windows:

                wx,wy,wz = w["pos"]

                dist = math.sqrt(
                    (cx-wx)**2 +
                    (cy-wy)**2
                )

                if dist < 0.8:
                    self.dragging = w
                    break

        if not pinching:
            self.dragging = None

        if self.dragging is not None:

            self.dragging["pos"][0] = cx
            self.dragging["pos"][1] = cy

    def draw_window(self, position):

        x,y,z = position

        glPushMatrix()

        glTranslatef(x,y,-z)

        glBegin(GL_QUADS)

        glColor3f(0.3,0.6,1)

        size = 0.7

        glVertex3f(-size, size, 0)
        glVertex3f(size, size, 0)
        glVertex3f(size,-size, 0)
        glVertex3f(-size,-size,0)

        glEnd()

        glPopMatrix()

    def draw_cursor(self):

        x,y,z = self.cursor

        glPushMatrix()

        glTranslatef(x,y,-z)

        glColor3f(0,1,0)

        quad = gluNewQuadric()

        gluSphere(quad,0.15,16,16)

        glPopMatrix()

    def render(self):

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        for w in self.windows:
            self.draw_window(w["pos"])

        self.draw_cursor()

        pygame.display.flip()