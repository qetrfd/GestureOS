import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("GestureOS Drag Test")

clock = pygame.time.Clock()


class Box:

    def __init__(self, x, y, color):

        self.rect = pygame.Rect(x, y, 120, 120)

        self.color = color

        self.dragging = False

    def draw(self):

        pygame.draw.rect(
            screen,
            self.color,
            self.rect,
            border_radius=15
        )


boxes = [

    Box(150,150,(56,189,248)),
    Box(350,260,(34,197,94)),
    Box(600,180,(244,63,94)),
    Box(750,400,(234,179,8))

]


running = True

selected = None

offset_x = 0
offset_y = 0


while running:

    screen.fill((15,23,42))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mx, my = pygame.mouse.get_pos()

            for box in boxes:

                if box.rect.collidepoint(mx, my):

                    selected = box

                    offset_x = mx - box.rect.x
                    offset_y = my - box.rect.y

                    box.dragging = True

        if event.type == pygame.MOUSEBUTTONUP:

            if selected:
                selected.dragging = False

            selected = None

    if selected and selected.dragging:

        mx, my = pygame.mouse.get_pos()

        selected.rect.x = mx - offset_x
        selected.rect.y = my - offset_y

    for box in boxes:
        box.draw()

    pygame.display.flip()

    clock.tick(60)


pygame.quit()