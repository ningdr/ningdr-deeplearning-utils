import cv2
import os


def fill_picture_index(cnt: int):
    fill_len = 8 - len(str(cnt))
    return "".zfill(fill_len) + str(cnt)


def read_video(video_path: str):
    """
    提取帧保存为图片
    :param video_path: 视频文件路径
    :return void
    :author ning.dr@foxmail.com
    """
    file_list = os.listdir(video_path)
    for video_full_name in file_list:
        (file_name, _) = os.path.splitext(video_full_name)
        img_path = video_path + file_name + "_image/"
        full = video_path + video_full_name
        if not os.path.exists(full):
            # 文件不存在，忽略
            continue
        cap = cv2.VideoCapture(full)
        sum_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f'视频{video_full_name}总帧数是{sum_frame}')
        if sum_frame == 0:
            continue
        if os.path.exists(img_path):
            os.removedirs(img_path)
        os.mkdir(img_path)
        for cnt in range(2200, sum_frame, 73):
            cap.set(cv2.CAP_PROP_POS_FRAMES, cnt)
            ret, frame = cap.read()
            picture_name = fill_picture_index(cnt)
            output = img_path + file_name + "_" + picture_name + ".jpg"
            cv2.imwrite(output, frame[0:720, 0:1280])
        cap.release()


if __name__ == "__main__":
    path = input("请输入视频路径：")
    read_video(path)
