
from PIL import Image
from PIL import ImageDraw
import numpy as np
import cv2
def circle_corder_image(face_frame, pic_o_path):
    # face_frame = cv2.imread(pic_i_path)
    face_frame_rgb = face_frame[:, :, ::-1]
    np_img = Image.fromarray(face_frame_rgb)
    im = np_img.convert("RGB")
    # im = Image.open(pic_i_path).convert("RGBA")
    rad = 100  # 设置半径
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    # im.save(pic_o_path)
    # im.show()
    cv2.imwrite(pic_o_path,np.array(im))

if __name__ == '__main__':
    # circle_new()
    in_path = 'img/1114.png'
    out_path = 'img/11222.png'




    circle_corder_image(in_path, out_path)