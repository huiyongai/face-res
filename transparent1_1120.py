from PIL import Image
from PIL import ImageDraw
import os
import numpy as np

def transparent_background(path):
    try:
        img = Image.open(path)
        img = img.convert("RGBA")  # 转换获取信息
        pixdata = img.load()
        color_no = get_convert_middle(path) + 30  # 抠图的容错值

        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if pixdata[x, y][0] > color_no and pixdata[x, y][1] > color_no and pixdata[x, y][2] > color_no and \
                        pixdata[x, y][3] > color_no:
                    pixdata[x, y] = (255, 255, 255, 0)

        if not path.endswith('png'):
            os.remove(path)
            replace_path_list = path.split('.')
            replace_path_list = replace_path_list[:-1]
            path = '.'.join(replace_path_list) + '.png'

        img.save(path)
        img.close()
    except Exception as e:
        return path


def get_convert_middle(img_path):
    I = Image.open(img_path)
    L = I.convert('L')
    im = np.array(L)
    im4 = 255.0 * (im / 255.0) ** 2  # 对图像的像素值求平方后得到的图像
    middle = (int(im4.min()) + int(im4.max())) / 2
    return middle# 调用 transparent_background, 传入图片路径, 该方法把图片修改后替换了源文件


if __name__ == '__main__':
    transparent_background('img/cc.png')

# from PIL import Image
# pic = Image.open('img/cc.png')
# pic = pic.convert('RGBA') # 转为RGBA模式
# width,height = pic.size
# array = pic.load() # 获取图片像素操作入口
# for i in range(width):
#     for j in range(height):
#         pos = array[i,j] # 获得某个像素点，格式为(R,G,B,A)元组
#         # 如果R G B三者都大于240(很接近白色了，数值可调整)
#         isEdit = (sum([1 for x in pos[0:3] if x > 240]) == 3)
#         if isEdit:
#             # 更改为透明
#             array[i,j] = (255,255,255,0)
#
# # 保存图片
# pic.save('result.png')