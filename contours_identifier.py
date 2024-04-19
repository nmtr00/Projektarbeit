import cv2
class Boundarylines():
    def __init__(self):
        pass
    def draw_boundary_lines(img, contours):
        #Countour indizes list
        contours_idx = []
        
        for cnt in contours:
            #Draw polygon for boundary contours with blue lines
            cv2.polylines(img, [cnt], True, (255, 0, 0), 2)

            # #Get rectangle
            # rect = cv2.minAreaRect(cnt)
            # (x, y), (w, h) , angle = rect
            # cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)

            # box = cv2.boxPoints(rect)
            # box = np.int0(box)

            # cv2.polylines(img, [box], True, (0, 255, 0), 2) # Draw a box outside the contour
            # print(box)
        contours = sorted(contours, key = lambda x: cv2.boundingRect(x)[0])

        #List contours
        for idx, contour in enumerate(contours):
            contours_idx.append(idx)
            