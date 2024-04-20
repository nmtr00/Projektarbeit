import cv2
from object_detector import *
from contours_identifier import *
from point_detector import *
# Load the video file
video_path = "D:\Downloads\MASK_Test0003.avi"
cap = cv2.VideoCapture(video_path)  # Replace 'your_video_file.mp4' with your video file path

# Check if the video file opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('measured.avi', fourcc, fps, (frame_width, frame_height))

#Load Object Detector

detector = HomogeneousBgDetector()
while True:
    #Read a frame from the vieeo
    ret, frame = cap.read()

    if not ret:
        print("End of video.")
        break
    # Detect objects
    contours = detector.detect_object(frame)

    # Instantiate ContourAnalyzer
    analyzer = ContourAnalyzer()

    # Get contour indices
    contours_idx = analyzer.get_contour_indices(frame, contours)
    print(contours_idx)


    if len(contours_idx)>1:
        # Identify left and right contours
        left_contour, right_contour = analyzer.get_left_and_right_contours(contours)

        #Measure distance between two points
        measure = PointMeasure()
        distance = measure.distance_width(frame, 30, left_contour, right_contour)
        # print("Distance between points in pixels:", distance)
    cv2.imshow("Image", frame)  #Display the frame

    # Write the processed frame to the output video
    out.write(frame)

    # Check for key press; If 'q' is pressed, exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   
# Release the video capture object and close all windows
cap.release()
out.release()
cv2.destroyAllWindows()
