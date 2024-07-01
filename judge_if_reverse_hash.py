import numpy as np
from PIL import Image
import imagehash
import os
from tqdm import tqdm

def calculate_hamming_distance(hash1, hash2):
    return hash1 - hash2

def get_frame_hash(frame_folder, frame_index):
    frame = Image.open(f"{frame_folder}/{frame_index}.jpg")
    hash_value = imagehash.average_hash(frame)
    return hash_value

def get_frame_distance(frame_folder, frame_index1, frame_index2):
    hash1 = get_frame_hash(frame_folder, frame_index1)
    hash2 = get_frame_hash(frame_folder, frame_index2)
    distance = calculate_hamming_distance(hash1, hash2)
    return distance

def get_similar_frame_ranges(frame_folder, threshold):
    # This function analyzes frames and identifies ranges of similar frames based on a threshold.
    # It returns a list of tuples, each representing a range of similar frames.
    start_frame = 0
    total_frames = 100  # Assume total_frames is determined earlier in the code
    frame_ranges = []

    folder_name = os.path.basename(frame_folder)
    with tqdm(total=total_frames - 1, desc=f"Analyzing frames in {folder_name}") as pbar:
        while start_frame < total_frames - 1:
            for i in tqdm(range(start_frame + 1, total_frames), leave=False):
                distance = get_frame_distance(frame_folder, i - 1, i)  # Assume this function is defined elsewhere
                if distance > threshold:
                    frame_ranges.append((start_frame, i - 1))
                    start_frame = i
                    pbar.update(i - pbar.n)  # Update the main progress bar
                    break
            else:
                frame_ranges.append((start_frame, total_frames - 1))
                break

    return frame_ranges

def process_frame_folder(frame_folder):
    threshold = 0
    frame_ranges = get_similar_frame_ranges(frame_folder, threshold)

    # Filter ranges that are at least 10 frames long
    filtered_frame_ranges = [frame_range for frame_range in frame_ranges if frame_range[1] - frame_range[0] >= 10]

    print(filtered_frame_ranges)

    # Ensure the output directory exists in the root folder
    root_folder = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(root_folder, "output")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Write the result to a file in the output directory
    output_file_path = os.path.join(output_dir, f"{os.path.basename(frame_folder)}.txt")
    with open(output_file_path, "w") as file:
        for frame_range in filtered_frame_ranges:
            file.write(str(frame_range) + "\n")