# python main.py -m screen:ipad
# Yapılacaklar: global stopflag'i self.variable yap.

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
import cv2
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import requests
import time
import threading
from kivy.properties import StringProperty
from datetime import datetime


class MainPage(Screen):
    pass


class ExercisePage(Screen):

    def deney1(self):
        global var
        self.location_infotxt.text = "3 Defa İleri-Geri Döngüsü Yapan,\n" \
                                     "İleri Gittiğinde 1sn Bekleyen Devre:\n"
        var = 100

    def deney2(self):
        global var
        self.location_infotxt.text = "İleri gittiğinde 1 Saniye,\n" \
                                     "Geri geldiğinde 2 Saniye Bekleyen,\n" \
                                     "Döngüye Beklemeden Başlayan Devre.\n"
        var = 200

    def on_leave(self, *args):
        pass


class CamPage(Screen):
    def __init__(self, **kwargs):
        super(CamPage, self).__init__(**kwargs)

    def on_pre_enter(self):
        global capture
        self.capture = cv2.VideoCapture(f'{self.link}/stream')
        self.my_camera = KivyCamera(capture=self.capture, fps=30)
        self.add_widget(self.my_camera)

    def on_pre_leave(self):
        self.capture.release()
    pass


class ExercisePopUp(Screen):
    img_ico = StringProperty("./img/testico1.png")
    var = 0

    def testico(self):
        self.var += 1
        if self.var%2 == 1:
            self.my_ico1.source = './img/testico2.png'

        else:
            self.my_ico1.source = './img/testico1.png'

    def first_deney(self):
        global stopflag

        for x in range(0,3):
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")
            self.location_infotxt.text = self.location_infotxt.text + "\n\t\t\t\t\t\t" + f"{x+1}. döngü"
            a = requests.get(f'{self.link}/gpio12On')  # Led1 is ON
            self.location_infotxt.text = self.location_infotxt.text + "\n" + "1. Piston ileride\t\t" + dt_string
            # print('acik')
            for _ in range(0, 10):  # Stops working thread
                time.sleep(0.1)  # time is adjustable
                if stopflag:
                    return
            a = requests.get(f'{self.link}/gpio12Off')  # Led1 is OFF
            a = requests.get(f'{self.link}/gpio13On')  # Led2 is ON
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")
            self.location_infotxt.text = self.location_infotxt.text + "\n" + "1. Piston geride\t\t" + dt_string
            # print('kapali')
            for _ in range(0, 2):  # Stops working thread
                time.sleep(0.1)
                if stopflag:
                    return
            a = requests.get(f'{self.link}/gpio13Off')  # Led2 is OFF
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        self.location_infotxt.text = self.location_infotxt.text + "\n" + "---> Döngü Tamamlandı." \
                                                                           "\t\t" + dt_string + "\n"

    def second_deney(self):
        global stopflag
        x = 0
        while(1):
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")
            self.location_info.text = self.ids.location_info.text + "\n\t\t\t\t\t\t" + f"{x+1}. döngü"
            a = requests.get('http://192.168.1.16:80/GPIO12ON')  # Led1 is ON
            a = requests.get('http://192.168.1.16/GPIO12ON')
            self.ids.location_info.text = self.ids.location_info.text + "\n" + "1. Piston ileride\t\t" + dt_string
            # print('acik')
            for _ in range(0, 10):  # Stops working thread
                time.sleep(0.1)  # time is adjustable
                if stopflag:
                    return
            a = requests.get('http://192.168.1.16:80/GPIO12OFF')  # Led1 is OFF
            a = requests.get('http://192.168.1.16/GPIO12OFF')
            a = requests.get('http://192.168.1.16:80/GPIO13ON')  # Led2 is ON
            a = requests.get('http://192.168.1.16/GPIO13ON')
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")
            self.ids.location_info.text = self.ids.location_info.text + "\n" + "1. Piston geride\t\t" + dt_string
            # print('kapali')
            for _ in range(0, 20):  # Stops working thread
                time.sleep(0.1)
                if stopflag:
                    return
            a = requests.get('http://192.168.1.16:80/GPIO13OFF')  # Led2 is OFF
            a = requests.get('http://192.168.1.16/GPIO13OFF')
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")
            x += 1

    def deneme(self):
        global stopflag
        stopflag = False    # Stop flag for Thread
        pill2kill = threading.Event()
        if var == 100:
            y = threading.Thread(target=self.first_deney, daemon=True)   # Setup thread
            y.start()   # Starts thread
        if var==200:
            y = threading.Thread(target=self.second_deney, daemon=True)  # Setup thread
            y.start()  # Starts thread

    def stopbutton(self):
        global stopflag
        stopflag = True
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        self.location_infotxt.text = self.location_infotxt.text + "\n" + "---> Döngü Durduruldu." \
                                                                           "\t\t" + dt_string + "\n"
        pass
    pass


class CircuitPage(Screen):
    img_src = StringProperty("./img/test100.png")

    def on_enter(self, *args):
        global var
        if var==100:
            self.my_image1.source = './img/test100.png'
        if var==200:
            self.my_image1.source = './img/test200.png'

    def test(self):
        global var
        if var == 100:
            self.manager.current = 'player'
        if var == 200:
            self.manager.current = 'player2'
    pass


class CircuitPage2(Screen):
    img2_src = StringProperty("./img/test100.png")

    def on_enter(self, *args):
        #global var       # Kontrol et
        #var -=1
        CircuitPage2.deneme(self)
        '''global var
        print(var)
        if var==10:
            self.ids.my_image.source = './img/test100.png'
            self.ids.my_image.reload()
        if var==20:
            self.ids.my_image.source = './img/test200.png'
            self.ids.my_image.reload()'''

    def deneme(self):
        global var
        var += 1

        self.my_image2.source = f'./img/test{var}.png'

        '''if var==11:
            self.ids.my_image.source = './img/test101.png'
            self.ids.my_image.reload()
        if var==12:
            self.ids.my_image.source = './img/test102.png'
            self.ids.my_image.reload()'''

    def minus(self):
        global var, sm
        var -= 1
        if (var%10) == 0:
            self.manager.current = 'player'
        else:
            var -= 1
            CircuitPage2.deneme(self)
    pass


class Player(Screen):
    pass

class Player2(Screen):
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
            buf = buf1.tostring()
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = image_texture


class MyApp(App):
    pass


if __name__ == '__main__':
    MyApp().run()