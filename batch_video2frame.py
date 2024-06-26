import os
import cv2
from tqdm import tqdm

def process_video(video_path, output_folder):
    # 读取视频文件
    video = cv2.VideoCapture(video_path)

    # 获取视频总帧数
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # 从视频路径中提取文件名
    video_filename = os.path.basename(video_path)

    count = 0

    # 使用tqdm创建进度条
    with tqdm(total=total_frames, desc=f"Processing {video_filename}") as pbar:
        # 遍历每一帧
        while True: 
            success, frame = video.read() 
            if not success:
                break

            # 文件名直接使用帧数，不进行位数格式化
            frame_name = f"{count}.jpg"

            # 保存图片
            path = os.path.join(output_folder, frame_name)
            cv2.imwrite(path, frame)
            
            # 更新进度条而不是打印消息
            pbar.update(1)

            count += 1
            
    # 打印视频处理完成的消息
    print(f"Completed processing {video_filename}")

def process_video_folder(video_folder):
    for filename in os.listdir(video_folder):
        if filename.endswith(".mp4"):
            video_path = os.path.join(video_folder, filename)
            output_folder = os.path.join(video_folder, filename.split('.')[0] + "_frame")

            # 创建frame文件夹
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            process_video(video_path, output_folder)

video_folder = r"D:\6.25\new" # 视频文件夹路径
process_video_folder(video_folder)