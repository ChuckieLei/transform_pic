import cv2
import os


def transform(input_path, output_path):
    for root, dirs, files in os.walk(input_path):
        for name in files:
            file = os.path.join(root, name)
            print('transform' + name)
            im = cv2.imread(file)
            if output_path:
                cv2.imwrite(os.path.join(output_path, name.replace('jpg', 'png')), im)
            else:
                cv2.imwrite(file.replace('jpg', 'png'), im)


if __name__ == '__main__':
    input_path = input("请输入目标文件夹: ")

    output_path = input("请输入输出文件夹： (回车则输出到原地址)")
    if not os.path.exists(input_path):
        print("文件夹不存在!")
    else:
        print("Start to transform!")
        transform(input_path, output_path)
        print("Transform end!")

