import cv2
import os
import csv
from object_detector import *
from contours_identifier import *
from point_detector import *
from tqdm import tqdm
#Parameters
input_folder = "O:\Projektarbeit\Converted to Mask with ImageJ"
output_folder = "O:\Projektarbeit\Analyzed"
output_data = "O:\Projektarbeit\Measured_values"
pixels_per_mm =27.6063
x_correction = -2
min_area1 = 5000


def video_format(video, name, output):
    cap = cv2.VideoCapture(video)  # Replace 'your_video_file.mp4' with your video file path

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
    out = cv2.VideoWriter(f'{output}\ANALYZED_{name}', fourcc, fps, (frame_width, frame_height))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return out, cap, total_frames

def get_data(filename, output_folder, frame_number, distance_pixels, distance_mm, left_x, right_x, fps):
    # Create or open the CSV file in append mode
    csv_file_path = os.path.join(output_folder, filename + ".csv")
    with open(csv_file_path, 'a', newline='') as csvfile:
        
        writer = csv.writer(csvfile, delimiter=';') # Write the distance value with semi-colon as delimiter
        # Check if the file is empty
        file_empty = os.stat(csv_file_path).st_size == 0
        
        # Write column names if the file is empty
        if file_empty:
            writer.writerow(['Timestamp', 'Distance (mm)', 'Distance (pixels)', 'Left Point', 'Right Point'])
        # Write the timestamp and distance value
        timestamp = frame_number / fps
        writer.writerow([timestamp, distance_pixels, distance_mm, left_x, right_x])

# Function to delete all files in a directory
def delete_files_in_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

# Function to create loading bar
# def create_loading_bar(total_frames):
#     return tqdm(total=total_frames, desc="Processing", unit="frames")



def process_videos(video_path, filename, out, cap, total_frames, filename_without_extension, loading_bar):
    # Load the video file
    # out, cap, total_frames = video_format(video_path, filename, output_folder)
    filename_without_extension = os.path.splitext(filename)[0]  # Extract filename without extension
     # Get total number of frames in the video
    frame_count = 0


    # Define cropping parameters (x, y, width, height)
    x1, y1, w1, h1 = 75, 600, 1750, 180
    x2, y2, w2, h2 = 925, 925, 50, 275
    while True:
        #Read a frame from the vieeo
        ret, frame = cap.read()
        if not ret:
            print("/n End of video.")
            break
        cropped_frame2 = frame[y2:y2+h2, x2:x2+w2] # Crop the frame for contact width 
        cropped_frame1 = frame[y1:y1+h1, x1:x1+w1] 
        #Detect contours
        detector_width = HomogeneousBgDetector() #Load Object Detector
        
        contours_width = detector_width.detect_object(cropped_frame1, min_area1) # Detect objects

        # detector_height = HomogeneousBgDetector()
        # contour_height = detector_height.detect_object(cropped_frame2, 2000)
        #Analyzer
        analyzer_width = ContourAnalyzer() # Instantiate ContourAnalyzer
        contours_idx = analyzer_width.get_contour_indices(cropped_frame1, contours_width)   # Get contour indices 
        # print(contours_idx)

        if len(contours_idx)>1:
            # Identify left and right contours
            left_contour, right_contour = analyzer_width.get_left_and_right_contours(contours_width)

            #Measure distance between two points
            measure = PointMeasure()
            distance_mm, distance_pixels, left_x, right_x = measure.distance_width(cropped_frame1, pixels_per_mm, left_contour, right_contour, x_correction)
            # print("Distance:", distance)  # Print distance before passing it to get_data

            #Safety feature : to eliminate the cases where the two correct coutours can not be picked up 
            if distance_mm < 20:
                distance_mm = 0
                distance_pixels = 0
        else:
            distance_mm = 0
            distance_pixels = 0
         # Get frame number
        frame_number = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        fps = cap.get(cv2.CAP_PROP_FPS)
        get_data(filename_without_extension, output_data, frame_number, distance_pixels, distance_mm, left_x, right_x, fps)  # Write data to CSV file
        # # Draw a rectangle around the cropped region on the original frame
        # cv2.rectangle(frame, (x1, y1), (x1+w1, y1+h1), (0, 255, 0), 2)
        # cv2.circle(frame, (int(x1+w1/2), int(y1+h1/2)), 5, (0, 0, 255), -1)
        
        # # Mark the frame
        # cv2.rectangle(frame, (x2, y2), (x2+w2, y2+h2), (0, 255, 0), 2)
        # cv2.circle(frame, (int(x2+w2/2), int(y2+h2/2)), 5, (0, 0, 255), -1)


        # cv2.imshow("Original Video", frame)  # Display the original frame




        # Write the processed frame to the output video       
        out.write(frame)
           # Calculate and print processing percentage
        frame_count += 1
        # progress = (frame_count / total_frames) * 100
        # print(f"{progress:.2f}% complete", end="\r")
        loading_bar.update(1)  # Update progress bar

        # Check for key press; If 'q' is pressed, exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break   
    # Release the video capture object and close all windows
    cap.release()
    out.release()
    cv2.destroyAllWindows()
   


# Delete all files in the output folder
delete_files_in_directory(output_folder)
delete_files_in_directory(output_data)

# def main():
#     for filename in os.listdir(input_folder):
#         if filename.endswith(".avi") or filename.endswith(".mp4"):
#             video_path = os.path.join(input_folder, filename)
#             print("Processing video:", filename)
#             out, cap, total_frames = video_format(video_path, filename, output_folder)
#             filename_without_extension = os.path.splitext(filename)[0]
#             loading_bar = tqdm(total=total_frames, desc="Processing", unit="frames")  # Create loading bar
            
#             process_videos(video_path, filename, out, cap, total_frames, filename_without_extension, loading_bar)
            
#             loading_bar.close()  # Close the progress bar after processing
def main():
    for filename in os.listdir(input_folder):
        if filename.endswith(".avi") or filename.endswith(".mp4"):
            video_path = os.path.join(input_folder, filename)
            print("Processing video:", filename)
            out, cap, total_frames = video_format(video_path, filename, output_folder)
            filename_without_extension = os.path.splitext(filename)[0]
            total_frames_for_loading_bar = min(total_frames, 200)  # Set a maximum of 200 frames for the loading bar
            with tqdm(total=total_frames_for_loading_bar, desc="Processing", unit="frames", bar_format="{l_bar}{bar}{r_bar}", ncols=100) as loading_bar:  # Create yellow loading bar
                process_videos(video_path, filename, out, cap, total_frames, filename_without_extension, loading_bar)

            # No need to close loading_bar here, it's automatically closed when exiting the "with" block


# Call the main function to start processing
if __name__ == "__main__":
    main()
