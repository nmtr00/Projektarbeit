import cv2
from object_detector import *
from contours_identifier import *
from point_detector import *
from video_format import video_format
# Load the video file
video_path = "D:\Downloads\MASK_Test0003.avi"
out, cap = video_format(video_path)

#Load Object Detector
detector = HomogeneousBgDetector()

# Define cropping parameters (x, y, width, height)
x, y, w, h = 200, 800, 1500, 200 
while True:
    #Read a frame from the vieeo
    ret, frame = cap.read()

    if not ret:
        print("End of video.")
        break

    # Crop the frame
    cropped_frame = frame[y:y+h, x:x+w]
   
    # Detect objects
    contours = detector.detect_object(cropped_frame)

    # Instantiate ContourAnalyzer
    analyzer = ContourAnalyzer()

    # Get contour indices
    contours_idx = analyzer.get_contour_indices(cropped_frame, contours)
    print(contours_idx)


    if len(contours_idx)==2:
        # Identify left and right contours
        left_contour, right_contour = analyzer.get_left_and_right_contours(contours)

        #Measure distance between two points
        measure = PointMeasure()
        distance = measure.distance_width(cropped_frame, 30, left_contour, right_contour)
        # print("Distance between points in pixels:", distance)
    # Draw a rectangle around the cropped region on the original frame
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
     # Mark the frame
    cv2.circle(frame, (int(x+w/2), int(y+h/2)), 5, (0, 0, 255), -1)
    cv2.imshow("Original Video", frame)  # Display the original frame

    # Write the processed frame to the output video
    out.write(frame)

    # Check for key press; If 'q' is pressed, exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   
# Release the video capture object and close all windows
cap.release()
out.release()
cv2.destroyAllWindows()
