import cv2
import os
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


        