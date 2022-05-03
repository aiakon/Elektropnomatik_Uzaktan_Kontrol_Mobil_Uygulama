# python main.py -m screen:ipad
# Yapılacaklar: global stopflag'i self.variable yap.

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
import cv2
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import threading
from kivy.properties import StringProperty
from kivy.core.window import Window
import socket
from os.path import exists

class MainPage(Screen):
    def start_tcp(self):
        y = threading.Thread(target=self.tcp, daemon=True)  # Setup thread
        y.start()  # Starts thread

    def tcp(self):
        global s
        host = self.tcpip.text
        port = int(self.port.text)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            # s.sendall(b'Hello, world')
            while True:
                # s.sendall(b'Hello, world')
                data = s.recv(1024)
                datastr = data.decode("utf-8")
                self.location_infotxt.text = self.location_infotxt.text + "\n" + datastr


class ExercisePage(Screen):
    pass


class CamPage(Screen):
    def __init__(self, **kwargs):
        super(CamPage, self).__init__(**kwargs)

    def on_pre_enter(self):
        global capture
        print("1")
        self.capture = cv2.VideoCapture(f'http://192.168.1.23:81/stream')
        self.my_camera = KivyCamera(capture=self.capture, fps=30)
        self.add_widget(self.my_camera)
        print("2")

    def on_pre_leave(self):
        self.capture.release()
    pass


class ExercisePopUp(Screen):
    img_ico = StringProperty("./img/testico1.png")

    def on_enter(self, *args):
        print(self.var)
        if self.var == 100:
            self.location_info.text = "3 Defa İleri-Geri Döngüsü Yapan,\n" \
                                         "İleri Gittiğinde 1sn Bekleyen Devre:\n"
        elif self.var == 200:
            self.location_info.text = "İleri gittiğinde 1 Saniye,\n" \
                                         "Geri geldiğinde 2 Saniye Bekleyen,\n" \
                                         "Döngüye Beklemeden Başlayan Devre.\n"

    def testico(self):
        self.var += 1
        if self.var%2 == 1:
            self.my_ico1.source = './img/testico2.png'

        else:
            self.my_ico1.source = './img/testico1.png'

    def deneme(self):
        global stopflag, s
        stopflag = False    # Stop flag for Thread
        pill2kill = threading.Event()
        if self.var == 100:
            s.sendall(b'm')
        if self.var==200:
            y = threading.Thread(target=self.second_deney, daemon=True)  # Setup thread
            y.start()  # Starts thread

    def stopbutton(self):
        global stopflag, s
        s.sendall(b'z')

        pass
    pass


class CircuitPage(Screen):
    img_src = StringProperty("./img/100.png")

    def on_enter(self, *args):
        print(self.var)
        self.my_image1.source = f'./img/{self.var}.png'



class CircuitPage2(Screen):
    img2_src = StringProperty("./img/test100.png")

    def image_source(self):
        if exists(f"./img/test{self.var}.png"):
            self.my_image2.source = f'./img/{self.var}.png'
        elif not exists(f"./img/test{self.var}.png"):
            self.var = 3500


    pass


class Player(Screen):

    def on_enter(self, *args):
        print(self.var)
        self.my_video.source = f'./img/{self.var}.mp4'
        pass

    pass


class PlcPage(Screen):
    pass


class KivyCamera(Image):

    def __init__(self, capture, fps, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # convert it to texture
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tobytes()
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = image_texture


class MyApp(App):
    Window.size = (1280, 720)
    pass


if __name__ == '__main__':
    MyApp().run()