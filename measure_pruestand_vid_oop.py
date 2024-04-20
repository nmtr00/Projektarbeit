import cv2
import os
from object_detector import *
from contours_identifier import *
from point_detector import *
from video_format import video_format

# Folder containing video files
folder_path = "F:\Projektarbeit\Raw data"

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".avi") or filename.endswith(".mp4"):  # Add more video formats if needed
        video_path = os.path.join(folder_path, filename)
        print("Processing video:", video_path)


    # Load the video file
    out, cap = video_format(video_path)


    # Define cropping parameters (x, y, width, height)
    x1, y1, w1, h1 = 150, 800, 1600, 180
    x2, y2, w2, h2 = 925, 925, 50, 275
    while True:
        #Read a frame from the vieeo
        ret, frame = cap.read()
        if not ret:
            print("End of processing.")
            break
        cropped_frame2 = frame[y2:y2+h2, x2:x2+w2] # Crop the frame for contact width measurement
        cropped_frame1 = frame[y1:y1+h1, x1:x1+w1] # Crop the frame for contact width measurement
        #Detect contours
        detector_width = HomogeneousBgDetector() #Load Object Detector
        detector_height = HomogeneousBgDetector()
        contours_width = detector_width.detect_object(cropped_frame1, 1500) # Detect objects
        contour_height = detector_height.detect_object(cropped_frame2, 2000)
        #Analyzer
        analyzer_width = ContourAnalyzer() # Instantiate ContourAnalyzer
        contours_idx = analyzer_width.get_contour_indices(cropped_frame1, contours_width)   # Get contour indices 
        # print(contours_idx)


        if len(contours_idx)>1:
            # Identify left and right contours
            left_contour, right_contour = analyzer_width.get_left_and_right_contours(contours_width)

            #Measure distance between two points
            measure = PointMeasure()
            distance = measure.distance_width(cropped_frame1, 30, left_contour, right_contour, 15)
            # print("Distance between points in pixels:", distance)

        # Draw a rectangle around the cropped region on the original frame
        #cv2.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (0, 255, 0), 2)
        #cv2.circle(frame, (int(x1+w1/2), int(y1+h1/2)), 5, (0, 0, 255), -1)
        
        # # Mark the frame
        # cv2.rectangle(frame, (x2, y2), (x2+w2, y2+h2), (0, 255, 0), 2)
        # cv2.circle(frame, (int(x2+w2/2), int(y2+h2/2)), 5, (0, 0, 255), -1)


        # cv2.imshow("Original Video", frame)  # Display the original frame

        # Write the processed frame to the output video
        out.write(frame)

        # Check for key press; If 'q' is pressed, exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break   
    # Release the video capture object and close all windows
    cap.release()
    out.release()
    cv2.destroyAllWindows()
