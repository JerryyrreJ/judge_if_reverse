import os
import cv2
from tqdm import tqdm

def process_video(video_path, output_folder):
    # Read the video file
    video = cv2.VideoCapture(video_path)

    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Extract the filename from the video path
    video_filename = os.path.basename(video_path)

    count = 0

    # Create a progress bar using tqdm
    with tqdm(total=total_frames, desc=f"Processing {video_filename}") as pbar:
        # Iterate through each frame
        while True: 
            success, frame = video.read()
            if not success:
                break

            # Use the frame count as the filename without formatting for digits
            frame_name = f"{count}.jpg"

            # Save the image
            path = os.path.join(output_folder, frame_name)
            cv2.imwrite(path, frame)
            
            # Update the progress bar instead of printing messages
            pbar.update(1)

            count += 1
            
    # print the filename after the progress bar is completed
    print(f"Completed processing {video_filename}")

def process_video_folder(video_folder):
    for filename in os.listdir(video_folder):
        if filename.endswith(".mp4"):
            video_path = os.path.join(video_folder, filename)
            output_folder = os.path.join(video_folder, filename.split('.')[0] + "_frame")

            # Create the output folder if it does not exist
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            process_video(video_path, output_folder)