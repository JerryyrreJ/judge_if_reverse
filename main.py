import batch_video2frame
import judge_if_reverse_hash
import os

def main():
    # Ask for the root folder path
    root_folder = input("Please enter the root folder path: ")
    
    # Call the main function from file1.py
    batch_video2frame.process_video_folder(root_folder)
    
    # Call the main function from file2.py
    frame_folders = [os.path.join(root_folder, name) for name in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, name))]

    for frame_folder in frame_folders:
        judge_if_reverse_hash.process_frame_folder(frame_folder)

if __name__ == "__main__":
    main()