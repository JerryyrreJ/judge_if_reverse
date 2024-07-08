import batch_video2frame
import judge_if_reverse_hash
import os

def main():
    # Ask for the root folder path
    root_folder = input("Please enter the root folder path: ")

    # Ask user to select the mode
    print("Select a mode:\n1: Only run batch_video2frame\n2: Only run judge_if_reverse_hash\nPress Enter for default (both)")
    mode = input("Please enter your choice (1, 2, or Enter for default): ")
    
    # Decide which modules to run based on user's choice
    if mode == "1":
        batch_video2frame.process_video_folder(root_folder)
    elif mode == "2":
        frame_folders = [os.path.join(root_folder, name) for name in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, name))]
        for frame_folder in frame_folders:
            judge_if_reverse_hash.process_frame_folder(frame_folder, root_folder)
    else:
        batch_video2frame.process_video_folder(root_folder)
        frame_folders = [os.path.join(root_folder, name) for name in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, name))]
        for frame_folder in frame_folders:
            judge_if_reverse_hash.process_frame_folder(frame_folder, root_folder)

if __name__ == "__main__":
    main()