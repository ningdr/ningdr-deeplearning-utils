import cv2
import os


def read_video(filenames):
    """
    提取帧保存为图片
    :param filenames: 视频文件列表
    :return void
    :author ning.dr@foxmail.com
    """
    for video_full_name in filenames:

        (file_name, _) = os.path.splitext(video_full_name)
        (video_file_path, video_file_full_name) = os.path.split(video_full_name)

        img_path = "{}_images".format(file_name)
        if not os.path.exists(video_full_name):
            # 文件不存在，忽略
            continue
        else:
            if os.path.exists(img_path):
                os.removedirs(img_path)
            os.mkdir(img_path)

        cap = cv2.VideoCapture(video_full_name)

        sum_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f'视频{video_full_name}总帧数是{sum_frame}')

        for cnt in range(0, sum_frame, 1000):
            cap.set(cv2.CAP_PROP_POS_FRAMES, cnt)
            ret, frame = cap.read()
            output = "{0}/{1}__{2}.jpg".format(img_path, video_file_full_name, cnt)
            cv2.imwrite(output, frame)
        cap.release()


if __name__ == "__main__":
    filename = "__your_path__"
    read_video([filename])
