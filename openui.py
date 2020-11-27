import sys  #
import dlib
import face_recognition  #人脸识别模块
from os import listdir  # 地址 用于打开位置
import cv2  #打开摄像头
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QGraphicsDropShadowEffect
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTimer, QThread, Qt
from PyQt5.QtGui import *
from time import time   #用于计算时间差 可以用来计算一个模块运行的时间
from datetime import datetime
import os
import numpy as np
from glob import glob
import time
from designer_1120 import Ui_MainWindow
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow,QApplication

class MyMainWindow(QMainWindow,Ui_MainWindow):
    # 第一个参数是该窗口的类型。第二个参数是该窗口对象
    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        # 无边框
        # self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        # # # 背景透明（就是ui中黑色背景的那个控件）
        # self.setAttribute(Qt.WA_TranslucentBackground, True)

        # 添加阴影
        # effect = QGraphicsDropShadowEffect(self)
        # effect.setBlurRadius(12)
        # effect.setOffset(0, 0)
        # effect.setColor(Qt.gray)
        # self.setGraphicsEffect(effect)
        self.init_ui()

        # 加上简单的移动功能

    def mousePressEvent(self, event):
        """鼠标点击事件"""
        if event.button() == Qt.LeftButton:
            self.mPos = event.pos()
        event.accept()

    def mouseReleaseEvent(self, event):
        '''鼠标弹起事件'''
        self.mPos = None
        event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.mPos:
            self.move(self.mapToGlobal(event.pos() - self.mPos))
        event.accept()

    def init_ui(self):
        self.detector = dlib.get_frontal_face_detector()  # 获得人脸框位置的检测器
        self.predictor = dlib.shape_predictor("model/shape_predictor_68_face_landmarks.dat")
        self.input_path = 'face_warehouse/'
        self.output_path = 'face_synthesis/'
        self.del_face_wareh(self.input_path)
        self.del_face_wareh('face_compare/')
        self.del_face_wareh('face_current/')
        self.video_btn = 0  # 用去区分打开摄像头和人脸识别 当打开人脸识别按钮的时候 video_btn 就会变成1  这样的话 关闭人脸识别 摄像头还是处于打开的状态
        self.timer_camera = QTimer()  # 需要定时器刷新摄像头界面
        self.cap = cv2.VideoCapture()
        self.cap.open(0)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
        self.timer_camera.start(30)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
        self.closed_pic()
        self.place_holder()
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息', 5000)
        # 为控件添加提示信息
        self.setToolTip('你好啊')
        # self.closeButton.clicked.connect(self.close) # 关闭窗口
        self.timer_camera.timeout.connect(lambda: self.video_source())  # 对打开摄像头2 按钮进行连接函数
        # self.pushButton_5.setEnabled(False)
        self.pushButton_4.clicked.connect(self.face_warehouse_btn)  # 人脸入库 连接函数
        self.pushButton_5.clicked.connect(self.face_recognition_btn)  # 人脸识别按钮连接函数 调用face_recogniton_btn
        # self.show()
        # self.label_4.setOpenExternalLinks(True) #　True 浏览器打开 False 调用槽函数
        self.label_4.setText('<a href=" "><img src="img/cc.png"></a>')

    # def click_1(self):
    #     self.thread_1 = Thread_1()  # 创建线程
    #     self.thread_1.start()  # 开始线程


    def video_source(self):  # 打开摄像头123  这三个按钮 的响应函数 词函数只是提供一个rtsp地址实际的打开摄像头的函数还是下面的btn_opoen_cam_click
        self.show_camera()

    def face_recognition_btn(self):  # 人脸识别按钮  通过video_btn的值来控制
        if self.video_btn==0:
            self.video_btn=1
            self.pushButton_5.setText(u'关闭人脸识别')
            self.show_camera()
        elif self.video_btn==1:
            self.video_btn=0
            self.pushButton_5.setText(u'打开人脸识别')
            self.closed_pic()
            self.show_camera()

    def rect_to_bb(self,rect):
        self.x = rect.left()
        self.y = rect.top()
        self.w = rect.right() - self.x
        self.h = rect.bottom() - self.y
        return (self.x, self.y, self.w, self.h)

    def len_list(self, path):
        img_num = len(os.listdir(path))
        img_list = os.listdir(path)
        return img_num, img_list

    def face_show(self, input_path, output_path):
        img_num, img_list = self.len_list(input_path)
        img_arr_list = []
        # img_blank_re = self.rs_black()
        for i in range(0, img_num):
            img_name = os.path.join(input_path, img_list[i])
            img = cv2.imread(img_name)
            img = cv2.resize(img, (145, 145))
            img_arr_list.append(img)
        img_arr_list = img_arr_list[::-1]
        if len(img_arr_list) == 1:
            h_all = img_arr_list[0]
        elif len(img_arr_list) ==2:
            h_all = np.concatenate(img_arr_list[: 2], 1)
        elif len(img_arr_list) == 3:
            img_black = cv2.imread('img/01.png')
            img_black_res = cv2.resize(img_black, (145, 145))
            img_arr_list.append(img_black_res)
            img0 = np.concatenate(img_arr_list[: 2], 1)
            img1 = np.concatenate(img_arr_list[2:], 1)
            h_all = np.concatenate([img0, img1], 0)
        elif len(img_arr_list) == 4:
            img0 = np.concatenate(img_arr_list[: 2], 1)
            img1 = np.concatenate(img_arr_list[2:], 1)
            h_all = np.concatenate([img0, img1], 0)
        img_num_output, img_list_output = self.len_list(output_path)
        if img_num_output >= 1:
            os.remove(os.path.join(output_path, img_list_output[0]))
        name_time = datetime.now().strftime("%Y%m%d%H%M%S")
        output_f = output_path + name_time + '.jpg'
        cv2.imwrite(output_f, h_all)
        picture = QPixmap(output_f)
        self.label_6.setPixmap(picture)

    def face_warehouse_btn(self):
        output_f = self.input_path + datetime.now().strftime("%Y%m%d%H%M%S") + '.jpg'
        ret, frame = self.cap.read()
        self.rects = self.detector(frame, 1)
        if len(self.rects) == 1:
            for (i, self.rect) in enumerate(self.rects):
                (self.x, self.y, self.w, self.h) = self.rect_to_bb(self.rect)
                cropped = frame[self.y:self.y + self.h, self.x:self.x + self.w]
                cv2.rectangle(frame, (self.x, self.y), (self.x + self.w, self.y + self.h), (0, 255, 0), 3)
                frame = self.key_port(frame)
                cv2.imwrite(output_f, cropped)
                load_image = face_recognition.load_image_file(output_f)
                img_encoding = face_recognition.face_encodings(load_image)
                if len(img_encoding) == 0:
                    QMessageBox.information(self, "Information",
                                            self.tr('录入失败,请重新录入!' + '\n' +
                                                    '注意：' + '\n' +
                                                    '1.请面对镜头 ' + '\n' +
                                                    '2.请勿遮挡 ' + '\n' +
                                                    '3.请单人录入'))
                    os.remove(output_f)
                else:
                    QMessageBox.information(self, "Information",
                                            self.tr("录入成功!"))
                    self.pushButton_5.setEnabled(True)
                    img_num, self.img_list = self.len_list(self.input_path)
                    if img_num > 4:
                        os.remove(os.path.join(self.input_path, self.img_list[0]))
                    self.face_show(self.input_path, self.output_path)
        else:
            QMessageBox.information(self, "Information",
                                    self.tr('录入失败,请重新录入!' + '\n'+
                                            '注意：' + '\n'+
                                            '1.请面对镜头 ' + '\n'+
                                            '2.请勿遮挡 ' + '\n'+
                                            '3.请单人录入'))

    def open_pic(self):
        open_pixmap = QPixmap('img/1113.png')
        open_scaredPixmap = open_pixmap.scaled(888, 280)
        self.label_5.setPixmap(open_scaredPixmap)
        self.label_3.setText("校门打开")

    def closed_pic(self):
        open_pixmap = QPixmap('img/1114.png')
        open_scaredPixmap = open_pixmap.scaled(888, 280)
        self.label_5.setPixmap(open_scaredPixmap)
        self.label_3.setText("校门关闭")

    def place_holder(self):
        ph_pixmap = QPixmap('img/02.png')
        self.label_11.setPixmap(ph_pixmap)

    def key_port(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #　gray表示灰度图
        dets = self.detector(gray, 1)
        for face in dets:
            shape = self.predictor(gray, face)
            for pt in shape.parts():
                pt_pos = (pt.x, pt.y)
                cv2.circle(frame, pt_pos, 2, (0, 0, 255), 2)
        return frame

    def product_name_write_file(self, file_path, cropped_fra):
        name_tim = datetime.now().strftime("%Y%m%d%H%M%S")
        current_output_path = os.path.join(file_path, name_tim + '.jpg')
        cv2.imwrite(current_output_path, cropped_fra)
        return current_output_path, name_tim

    def frame_resize(self, img_path, fx, fy):
        face_current_frame = cv2.imread(img_path)
        frame_res = cv2.resize(face_current_frame, (fx, fy))
        return frame_res

    def write_compare_img(self, compare_list, cropped_frame, list_ind):
        # 当前人脸存储路径
        face_current_output, name_time = self.product_name_write_file('face_current', cropped_frame)
        face_current_img = self.frame_resize(face_current_output, 100, 100)
        compare_list.append(face_current_img)
        # 获取人脸库人脸加入到对比list
        face_warehouse_img = self.frame_resize(os.path.join('face_warehouse', self.img_list[list_ind]),
                                               100, 100)
        compare_list.append(face_warehouse_img)
        # 拼接当前人脸和数据库人脸
        face_warehouse_img = np.concatenate(compare_list[: 2], 1)
        compare_list.clear()
        face_compare_output = os.path.join('face_compare', name_time + '.jpg')
        cv2.imwrite(face_compare_output, face_warehouse_img)

    def show_camera(self):  #展示摄像头画面并进行人脸识别的功能
        if self.video_btn==0:    #在前面就设置了video_btn为0 为了在人脸识别的时候直接把这个值给改了 这样人脸识别和摄像头展示就分开了
            while (self.cap.isOpened()):
                ret, self.image = self.cap.read()
                QApplication.processEvents()  #这句代码告诉QT处理来处理任何没有被处理的事件，并且将控制权返回给调用者  让代码变的没有那么卡
                show = cv2.resize(self.image, (500, 285))
                show = cv2.cvtColor(show,cv2.COLOR_BGR2RGB)  # 这里指的是显示原图
                # opencv 读取图片的样式，不能通过Qlabel进行显示，需要转换为Qimage QImage(uchar * data, int width,
                self.showImage = QImage(show.data, show.shape[1], show.shape[0],
                                        QImage.Format_RGB888)
                self.label_7.setPixmap(QPixmap.fromImage(self.showImage))
        elif self.video_btn==1:
            # 这段代码是 获取photo文件夹中 人的信息
            filepath = 'face_warehouse'
            filename_list = listdir(filepath)
            known_face_names = []
            known_face_encodings = []
            for filename in filename_list:  # 依次读入列表中的内容
                QApplication.processEvents()
                if filename.endswith('jpg'):  # 后缀名'jpg'匹对
                    known_face_names.append(filename[:-4])  # 把文件名字的后四位.jpg去掉获取人名
                    file_str = 'face_warehouse/' + filename
                    a_images = face_recognition.load_image_file(file_str)
                    a_face_encoding = face_recognition.face_encodings(a_images)[0]
                    known_face_encodings.append(a_face_encoding)
            face_names = []
            compare_list_1 = []
            compare_list_2 = []
            compare_list_3 = []
            compare_list_4 = []
            process_this_frame = True
            tmp_switch = 0
            while (self.cap.isOpened()):
                num_warehouse, list_warehouse = self.len_list('face_warehouse/')
                if num_warehouse == 0:
                    tmp_switch = 1
                ret, frame = self.cap.read()
                QApplication.processEvents()
                # 改变摄像头图像的大小，图像小，所做的计算就少
                small_frame = cv2.resize(frame, (0, 0), fx=0.33, fy=0.33)
                # opencv的图像是BGR格式的，而我们需要是的RGB格式的，因此需要进行一个转换。
                rgb_small_frame = small_frame[:, :, ::-1]
                self.rects = self.detector(frame, 1)
                if len(self.rects) == 1:
                    for (i, self.rect) in enumerate(self.rects):
                        (self.x, self.y, self.w, self.h) = self.rect_to_bb(self.rect)
                        cropped = frame[self.y:self.y + self.h, self.x:self.x + self.w]
                        # cv2.rectangle(frame, (self.x, self.y), (self.x + self.w, self.y + self.h), (0, 0, 0), 2)
                        frame = self.key_port(frame)
                if process_this_frame:
                    QApplication.processEvents()
                    # 根据encoding来判断是不是同一个人，是就输出true，不是为flase
                    face_locations = face_recognition.face_locations(rgb_small_frame)
                    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                    face_names = []
                    for face_encoding in face_encodings:
                        # 默认为unknown
                        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                        self.similarity = face_recognition.face_distance(known_face_encodings, face_encoding)
                        # 阈值太低容易造成无法成功识别人脸，太高容易造成人脸识别混淆 默认阈值tolerance为0.6
                        name = "Unknown"
                        if True in set(matches):
                            first_match_index = matches.index(True)
                            name = known_face_names[first_match_index]
                            self.open_pic()
                        else:
                            self.closed_pic()
                        face_names.append(name)
                process_this_frame = not process_this_frame
                if not face_names:
                    self.closed_pic()
                if tmp_switch == 0:
                    img_num_warehouse, img_list_warehouse = self.len_list('face_warehouse/')
                    if img_num_warehouse == 1:
                        QApplication.processEvents()
                        # 保存对比图
                        self.write_compare_img(compare_list_1, cropped, -1)
                        # 展示对比图和相似度
                        img_num_compare, img_list_compare = self.len_list('face_compare/')
                        picture = QPixmap(os.path.join('face_compare/', img_list_compare[-1]))
                        self.label_11.setPixmap(picture)
                        self.label_15.setText(str(round(self.similarity[0], 4)))
                    if img_num_warehouse == 2:
                        QApplication.processEvents()
                        self.write_compare_img(compare_list_1, cropped, -1)
                        time.sleep(1)
                        self.write_compare_img(compare_list_2, cropped, -2)
                        img_num_compare, img_list_compare = self.len_list('face_compare/')
                        picture = QPixmap(os.path.join('face_compare/', img_list_compare[-1]))
                        self.label_12.setPixmap(picture)
                        self.label_15.setText(str(round(self.similarity[0], 4)))
                        picture = QPixmap(os.path.join('face_compare/', img_list_compare[-2]))
                        self.label_11.setPixmap(picture)
                        self.label_16.setText(str(round(self.similarity[1], 4)))
                    if img_num_warehouse == 3:
                        QApplication.processEvents()
                        self.write_compare_img(compare_list_1, cropped, -1)
                        time.sleep(1)
                        self.write_compare_img(compare_list_2, cropped, -2)
                        time.sleep(1)
                        self.write_compare_img(compare_list_3, cropped, -3)
                        img_num_compare, img_list_compare = self.len_list('face_compare/')
                        picture = QPixmap(os.path.join('face_compare/', img_list_compare[-3]))
                        self.label_11.setPixmap(picture)
                        self.label_15.setText(str(round(self.similarity[0], 4)))
                        picture = QPixmap(os.path.join('face_compare/', img_list_compare[-2]))
                        self.label_12.setPixmap(picture)
                        self.label_16.setText(str(round(self.similarity[1], 4)))
                        picture = QPixmap(os.path.join('face_compare/', img_list_compare[-1]))
                        self.label_13.setPixmap(picture)
                        self.label_17.setText(str(round(self.similarity[2], 4)))
                    if img_num_warehouse == 4:
                        QApplication.processEvents()
                        self.write_compare_img(compare_list_1, cropped, -1)
                        time.sleep(1)
                        self.write_compare_img(compare_list_2, cropped, -2)
                        time.sleep(1)
                        self.write_compare_img(compare_list_3, cropped, -3)
                        time.sleep(1)
                        self.write_compare_img(compare_list_4, cropped, -4)
                        img_num_compare, img_list_compare = self.len_list('face_compare/')
                        picture = QPixmap(os.path.join('face_compare/', img_list_compare[-4]))
                        self.label_11.setPixmap(picture)
                        self.label_15.setText(str(round(self.similarity[0], 4)))
                        picture = QPixmap(os.path.join('face_compare/', img_list_compare[-3]))
                        self.label_12.setPixmap(picture)
                        self.label_16.setText(str(round(self.similarity[1], 4)))
                        picture = QPixmap(os.path.join('face_compare/', img_list_compare[-2]))
                        self.label_13.setPixmap(picture)
                        self.label_17.setText(str(round(self.similarity[2], 4)))
                        picture = QPixmap(os.path.join('face_compare/', img_list_compare[-1]))
                        self.label_14.setPixmap(picture)
                        self.label_18.setText(str(round(self.similarity[3], 4)))
                    self.del_face_wareh('face_current/')
                    if img_num_compare > 4:
                        os.remove(os.path.join('face_compare/', img_list_compare[0]))
                        os.remove(os.path.join('face_compare/', img_list_compare[1]))
                        os.remove(os.path.join('face_compare/', img_list_compare[2]))
                        os.remove(os.path.join('face_compare/', img_list_compare[3]))
                    tmp_switch = 1
                self.label_7.setPixmap(QPixmap.fromImage(self.showImage))
                show_video = cv2.resize(frame, (500, 285))
                show_video = cv2.cvtColor(show_video, cv2.COLOR_BGR2RGB)  # 这里指的是显示原图
                # opencv 读取图片的样式，不能通过Qlabel进行显示，需要转换为Qimage QImage(uchar * data, int width,
                self.showImage = QImage(show_video.data, show_video.shape[1], show_video.shape[0], QImage.Format_RGB888)
            # print('打开人脸识别所需要的时间', time() - self.t2)
    def del_face_wareh(self,path):
        file_path_list = glob(path + r'*')
        for file_path in file_path_list:
            try:
                os.remove(file_path)
            except:
                try:
                    os.rmdir(file_path)
                except:
                    self.del_face_wareh(file_path)
                    os.rmdir(file_path)

    def closeEvent(self, QCloseEvent):
        #  使用QMessageBox提示
        reply = QMessageBox.warning(self, "温馨提示", "是否退出？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if (reply == QMessageBox.Yes):
            self.del_face_wareh(self.input_path)
            self.del_face_wareh('face_compare/')
            self.del_face_wareh('face_synthesis/')
            self.del_face_wareh('face_current/')
            self.cap.release()
            QCloseEvent.accept()
        if (reply == QMessageBox.No):
            QCloseEvent.ignore()


    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(newLeft,newTop)

if __name__=="__main__" :
    app = QtWidgets.QApplication(sys.argv)
    myWin=MyMainWindow()
    myWin.center()
    myWin.show()
    # print('打开ui界面所需时间',time()-t)
    sys.exit(app.exec_())


