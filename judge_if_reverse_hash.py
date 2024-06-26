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
    frame_ranges = []
    total_frames = len([name for name in os.listdir(frame_folder) if os.path.isfile(os.path.join(frame_folder, name))])
    start_frame = 0

    folder_name = os.path.basename(frame_folder)
    with tqdm(total=total_frames - 1, desc=f"Analyzing frames in {folder_name}") as pbar:
        while start_frame < total_frames - 1:
            for i in tqdm(range(start_frame + 1, total_frames), leave=False):
                distance = get_frame_distance(frame_folder, i - 1, i)
                if distance > threshold:
                    frame_ranges.append((start_frame, i - 1))
                    start_frame = i
                    pbar.update(i - pbar.n)  # 更新主进度条
                    break
            else:
                frame_ranges.append((start_frame, total_frames - 1))
                break

    return frame_ranges

def process_frame_folder(frame_folder):
    threshold = 0
    frame_ranges = get_similar_frame_ranges(frame_folder, threshold)

    # 筛选长度至少为10帧的范围
    filtered_frame_ranges = [frame_range for frame_range in frame_ranges if frame_range[1] - frame_range[0] >= 10]

    print(filtered_frame_ranges)

    # 将结果写入文件
    with open(f"{frame_folder}.txt", "w") as file:
        for frame_range in filtered_frame_ranges:
            file.write(str(frame_range) + "\n")

root_folder = r"D:\6.25\new" # 你的根文件夹路径
frame_folders = [os.path.join(root_folder, name) for name in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, name))]

for frame_folder in frame_folders:
    process_frame_folder(frame_folder)