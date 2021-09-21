import os


def change_filename(file_path: str, next_index: int):
    file_list = os.listdir(file_path)
    print(file_list)
    for old_name in file_list:
        old_name = file_path + old_name
        new_name = path + os.sep + fill_filename(str(next_index)) + ".mkv"
        os.rename(old_name, new_name)
        next_index += 1
    print("下一个索引：" + str(next_index))


def fill_filename(last_name: str):
    length = len(last_name)
    fill_len = 8 - length
    name = "cf"
    while fill_len > 0:
        name += "0"
        fill_len -= 1
    return name + last_name


if __name__ == "__main__":
    path = input("请输入文件路径:")
    # 下一个索引：31
    next_index = input("请输入索引：")
    change_filename(path, int(next_index))
