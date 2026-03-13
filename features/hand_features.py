import math
import numpy as np


class HandFeatures:

    def __init__(self):
        pass

    def extract(self, landmarks):

        if len(landmarks) != 21:
            return None

        points = np.array(landmarks)

        coords = self.normalize(points)

        distances = self.compute_distances(points)

        angles = self.compute_angles(points)

        features = np.concatenate([coords, distances, angles])

        return features

    def normalize(self, points):

        wrist = points[0]

        normalized = []

        for p in points:

            x = p[0] - wrist[0]
            y = p[1] - wrist[1]
            z = p[2] - wrist[2]

            normalized.extend([x, y, z])

        return np.array(normalized)

    def compute_distances(self, points):

        pairs = [
            (4,8),(4,12),(4,16),(4,20),
            (8,12),(12,16),(16,20),
            (0,8),(0,12),(0,16),(0,20),
            (5,9),(9,13),(13,17),
            (5,17)
        ]

        dists = []

        for a,b in pairs:

            x1,y1,_ = points[a]
            x2,y2,_ = points[b]

            d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

            dists.append(d)

        return np.array(dists)

    def compute_angles(self, points):

        triplets = [
            (0,1,2),(1,2,3),(2,3,4),
            (0,5,6),(5,6,7),(6,7,8),
            (0,9,10),(9,10,11),(10,11,12),
            (0,13,14),(13,14,15),(14,15,16),
            (0,17,18),(17,18,19),(18,19,20)
        ]

        angles = []

        for a,b,c in triplets:

            angle = self.angle(points[a], points[b], points[c])

            angles.append(angle)

        return np.array(angles)

    def angle(self, A,B,C):

        ax,ay,_ = A
        bx,by,_ = B
        cx,cy,_ = C

        BA = np.array([ax-bx, ay-by])
        BC = np.array([cx-bx, cy-by])

        cos_angle = np.dot(BA,BC)/(np.linalg.norm(BA)*np.linalg.norm(BC)+1e-6)

        angle = math.acos(np.clip(cos_angle,-1.0,1.0))

        return angle