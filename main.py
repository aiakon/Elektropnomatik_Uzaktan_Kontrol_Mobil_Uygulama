# python main.py -m screen:ipad
# Yapılacaklar: global stopflag'i self.variable yap.

# 16 satır, 1 satırda 30 adet a var.

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
import cv2
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import threading
from kivy.properties import StringProperty, BooleanProperty
from kivy.core.window import Window
import socket
from os.path import exists

description = ["•	START Butonuna basıldığında K0 Rölesi aktive olur ve kendisine bağlı K0 NO anahtarını kapalı "
               "konumuna getirir. START butonu ile K0 anahtarı paralel olarak bağlandığı için START butonu açık "
               "konumda olsa dahi +24V kaynaktan gelen akım K0 anahtarı üzerinden akarak rölenin sürekli aktif "
               "konumda kalmasını sağlar. Bu duruma rölenin mühürlenmesi adı verilir. Röleyi tekrardan kapatmak "
               "için STOP butonuna basılması gereklidir. \n\n•	NO (Normally Open) Anahtar: Normal konumunda yani "
               "enerjilendirilmediği durumda açık konumda olan anahtara denir.",    # 1.Deney [0]

               "•	Devre şemasının sağ tarafında görülen piston devresinde yukarıdan aşağıya saymak gerekirse, 1 "
               "adet çift etkili silindir piston, pistonun altında 5/2 selenoid valf, valfin altında bakım ünitesi ve"
               " onun altında da basınçlı hava kaynağı bulunmaktadır.\n\n•	Bu deneyde START butonuna basıldığında K0"
               " anahtarının kapandığını, YV0 valf selenoidine enerji gittiğini ve dolayısıyla pistonun ileri gittiğini"
               " görmekteyiz. Piston geri konumuna dönmemektedir çünkü pistona bağlı selenoid valfin sağdan kumandasını"
               " kontrol etmemekteyiz. Bir sonraki deneyde pistonu hem ileri hem de geri şekilde kontrol etmeyi "
               "göreceğiz.",        # 2.Deney [1]

               "•	Bu deneyde sınır anahtarlarının kullanımını ve pistonu iki yönlü bir şekilde kontrol etmeyi "
               "öğreneceğiz. Pistonun üzerinde gördüğünüz S1 ve S2 yazıları sınır anahtarlarının sensörleridir. Piston"
               " bu konuma geldiğinde sınır anahtarı NC ise açık konuma, NO ise kapalı konuma geçer.\n\n•	Devrede "
               "görüldüğü üzere piston S1 konumundayken S1 anahtarı kapalı konuma geçerek YV0 valf selenoidinin "
               "aktifleşmesini sağlar ve piston ileri gitmeye başlar. Piston S2 konumuna geldiğinde ise S2 anahtarı "
               "kapalı konuma geçerek YV1 valf selenoidinin aktifleşmesini sağlayarak pistonun geri gitmesini sağlar. "
               "STOP butonuna basıncaya kadar bu çalışma döngüsü devam eder.",      # 3.Deney [2]

               "•	Bu deneyde zaman rölelerini inceleyeceğiz. Kumanda devresinde gördüğünüz Z0 ismiyle bulunan sembol"
               " zaman rölesinin sembolüdür. Zaman röleleri enerjilendirildikten belirli bir süre sonra anahtarlarının"
               " konumunu değiştiren rölelere denir.\n•	Öncelikle START butonuna basıldığında K0 rölesi "
               "mühürlenmektedir ve K0 anahtarı kapalı konumda olacağından dolayı sistem çalışmaya başlayacaktır. İlk"
               " olarak piston S1 konumunda olacağı için S1 anahtarı kapalı konumda olacak ve YV0 valf selenoidi "
               "aktifleşerek pistonu ileri hareket ettirecektir. Ardından piston S2 konumuna geldiğinde S2 anahtarı "
               "kapanacak ve Z0 zaman rölesine elektrik enerjisi göndererek çalışmaya başlamasını sağlayacaktır.",
               "Zaman rölesi belirlenen süre olan 0.5 saniye bekledikten sonra Z0 anahtarını kapalı konuma geçirerek "
               "YV1 valf selenoidinin aktifleşmesini sağlayarak pistonun geri dönmesini sağlayacaktır. Bu sayede piston"
               " ileri gidip 3 saniye bekleyip geri dönme döngüsünü yapmış olacaktır. STOP butonuna basılmadığı sürece"
               " piston bu döngüde çalışmaya devam eder.",      # 4.Deney [3,4]

               "•	Bu deneyde pistonun hem ileri giderken hem de geri dönerken beklemesini sağlayan kumanda devresini "
               "inceleyeceğiz.\n\n•	Öncelikle START butonuna basılarak K0 rölesinin mühürlenmesi sağlanır ve K0 "
               "anahtarı kapalı konuma geçtiği için sistem çalışmaya başlar. Piston başlangıç konumu olarak S1 "
               "konumunda olduğu için S1 anahtarı kapalı konumda olur ve Z0 zaman rölesine elektrik enerjisini ileterek"
               " çalışmasını sağlar.",
               "Z0 zaman rölesi 0.8 saniye bekledikten sonra Z0 anahtarını kapalı konumuna "
               "geçirerek YV0 valf selenoidinin aktifleşmesini sağlar ve piston ileri gitmeye başlar. Piston S2"
               " konumuna geldiğinde S2 anahtarı kapalı konuma geçer ve Z1 zaman rölesine elektrik enerjisini ileterek"
               " çalışmasını sağlar. Z1 zaman rölesi 0.6 saniye bekledikten sonra Z1 anahtarını kapalı konumuna "
               "geçirerek YV1 valf selenoidinin aktifleşmesini sağlar ve piston geri döner.",        # 5.Deney [5,6]

               "•	Bu deneyde sayıcı röleleri inceleyeceğiz. Devre şematiğinde gördüğümüz C0 ismine sahip sembol "
               "sayıcı rölenin sembolüdür. Röledeki A1 ve A2 pinleri sayılması istenen sinyalin giriş ve çıkışlarıdır."
               " R1 ve R2 pinleri ise sayıcı rölenin reset pinlerinin giriş ve çıkışlarıdır. A1 pinine her sinyal "
               "geldiğinde sayıcı röle bunu algılayarak saymaya başlar ve rölenin ayarlandığı sayıya ulaşınca sayıcı "
               "röleye bağlı olan anahtarın konumunu değiştirir. Reset pini olan R1 pinine bir sinyal gelmediği sürece"
               " sayıcı röle bulunduğu konumda kalmaya devam eder.",
               "•	Öncelikle START butonuna basılarak K0 rölesinin mühürlenmesi sağlanır ve K0 anahtarı kapalı "
               "konuma geçtiği için sistem çalışmaya başlar. Piston başlangıç konumu olarak S1 konumunda olduğu için"
               " S1 anahtarı kapalı konumda olur ve YV0 selenoid valfinin aktifleşmesini sağlar bu sayede piston ileri "
               "gitmeye başlar. Piston S2 konumuna geldiğinde S2 anahtarı kapalı konuma geçer ve hem YV1 selenoid valfi"
               " aktifleşerek geri dönmesi sağlanır hem de C1 sayıcı rölesine sinyal giderek rölenin sayması sağlanır."
               " Sayıcı röle 3 kere sinyal saydığında C1 kapalı anahtarını açık konumuna getirerek YV0’ın "
               "aktifleşmesini engeller bu sayede döndü durdurulmuş olunur. Bu deney setinde C1 sayıcı rölesi "
               "resetlenmediği için döngüyü baştan başlatmak için sistemi baştan başlatmak gerekir. Bu durumu ileriki "
               "deneylerde göreceğiz.",      # 6.Deney [7,8]

               "•	Bu deneyde zaman ve sayıcı rölelerinin birlikte kullanımını inceleyeceğiz. Bir önceki deneyde "
               "anlattığımız üzere sayıcı rölelerin resetlenmesi için R1 pinine bir sinyal göndermemiz gerekli. Bu pine"
               " göndereceğimiz sinyal zaman rölesinin anahtarından geçmekte.\n\n•	Öncelikle START butonuna basılarak "
               "K0 rölesinin mühürlenmesi sağlanır ve K0 anahtarı kapalı konuma geçtiği için sistem çalışmaya başlar."
               " Piston başlangıç konumu olarak S1 konumunda olduğu için S1 anahtarı kapalı konumda olur ve YV0 "
               "selenoid valfinin aktifleşmesini sağlar bu sayede piston ileri gitmeye başlar.",
               "Piston S2 konumuna geldiğinde S2 anahtarı kapalı konuma geçer ve hem YV1 selenoid valfi aktifleşerek "
               "geri dönmesi sağlanır hem de C1 sayıcı rölesine sinyal giderek rölenin sayması sağlanır. Sayıcı röle"
               " 3 kere sinyal saydığında C1 kapalı anahtarını açık konumuna getirerek YV0’ın aktifleşmesini bir süre"
               " engeller ve aynı süre boyunca C1 açık anahtarını da kapalı konuma getirerek Z0 zaman "
               "rölesinin çalışmasını sağlar. Zaman rölesinde belirlenen süre tamamlandıktan sonra Z0 zaman rölesinin "
               "anahtarı kapalı konuma geçerek C1 sayıcı rölesinin sıfırlanmasını sağlar ve bu "
               "sayede döngü tamamlanmış olur.",      # 7.Deney [9,10]

               "•	Bu deneyde sayıcı röleyi START butonu ile sıfırlamayı ve sayıcı röle ile zaman rölesinin "
               "farklı bir kullanımını öğreneceğiz.\n\n•	Öncelikle START butonuna basılarak K0 rölesinin "
               "mühürlenmesi sağlanır ve K0 anahtarı kapalı konuma geçtiği için sistem çalışmaya başlar. Piston, "
               "başlangıç konumu olarak S1 konumunda olduğu için başlangıçta S1 anahtarı kapalı konumdadır ve "
               "dolayısıyla Z0 zaman rölesi çalışmaya başlar. Zaman rölesinde belirlenen süre dolduğunda Z0 anahtarı "
               "tetiklenerek kapalı konuma geçer ve YV0 valf selenoidinin aktifleştirerek pistonun ileriye hareket "
               "etmesini sağlar. Piston S2 konumuna geldiğinde S2 anahtarı tetiklenerek kapalı konuma geçer ve Z1 zaman"
               " rölesinin çalışmasını sağlar.  ",
               "Z1 zaman rölesi belirlenen süre kadar bekledikten sonra Z1 anahtarını tetikleyerek kapalı "
               "konuma geçirir ve YV1 valf selenoidinin aktifleştirerek pistonun geriye dönmesini sağlar. Piston "
               "geriye dönerken aynı zamanda sayıcı röleye bir sinyal göndererek ileri-geri döngüsünü 1 kere "
               "tamamladığını bildirir. Sistem 3 defa ileri-geri döngüsünü yaptıktan sonra sayıcı röle kendisine "
               "bağlı olan C1 kapalı anahtarını açık konuma getirir ve sistemin gücünü sağlayan K0’ın mührünü "
               "kırarak sistemi kapatmış olur. Sistemin baştan çalışmasını sağlamak için START butonuna tekrar basılır"
               " bu sayede hem C1 sayıcı rölesine reset sinyali gitmiş olur hem de K0 rölesinin mühürlenmesi "
               "sağlanarak sistemin çalışması sağlanır.",      # 8.Deney [11,12]

               ]
class MainPage(Screen):

    def start_tcp(self, *args):
        y = threading.Thread(target=self.tcp, daemon=True)  # Setup thread
        y.start()  # Starts thread

    def tcp(self):
        try:
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
        except Exception as e:
            Clock.schedule_once(self.start_tcp, 0.01)
            print("Reconnecting", e)


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
        if self.var == 100:
            self.location_info.text = "3 Defa İleri-Geri Döngüsü Yapan,\n" \
                                      "İleri Gittiğinde 1sn Bekleyen Devre:\n"
        elif self.var == 200:
            self.location_info.text = "İleri gittiğinde 1 Saniye,\n" \
                                      "Geri geldiğinde 2 Saniye Bekleyen,\n" \
                                      "Döngüye Beklemeden Başlayan Devre.\n"

    def testico(self):
        self.var += 1
        if self.var % 2 == 1:
            self.my_ico1.source = './img/testico2.png'

        else:
            self.my_ico1.source = './img/testico1.png'

    def send_data(self):
        global s
        try:
            data_container = ["q", "Q", "w", "W", "e", "E", "r", "R", "t", "T", "y", "Y", "p", "P", "a", "A", "s", "S",
                              "d", "D", "f", "F", "g", "G", "h"]
            s.sendall(bytes(data_container[int(self.var / 100) - 1], 'ascii'))
            # if self.var == 100:
            #     s.sendall(b'w')
        except Exception as e:
            print("pass")

    def stopbutton(self):
        global stopflag, s
        s.sendall(b'z')

        pass

    pass


class CircuitPage(Screen):
    img_src = StringProperty("./img/100.png")

    def on_enter(self, *args):
        self.my_image1.source = f'./img/{self.var}.png'


class CircuitPage2(Screen):
    img2_src = StringProperty("./img/100.png")
    file_exists = BooleanProperty(True)

    def on_enter(self, *args):
        self.image_source()

    def check_file(self):
        if exists(f"./img/{self.var}.png"):
            if self.var == 101:
                self.txt_input.text = description[0]
            if self.var == 201:
                self.txt_input.text = description[1]
            if self.var == 301:
                self.txt_input.text = description[2]
            if self.var == 401:
                self.txt_input.text = description[3]
            if self.var == 402:
                self.txt_input.text = description[4]
            if self.var == 501:
                self.txt_input.text = description[5]
            if self.var == 502:
                self.txt_input.text = description[6]
            if self.var == 601:
                self.txt_input.text = description[7]
            if self.var == 602:
                self.txt_input.text = description[8]
            if self.var == 701:
                self.txt_input.text = description[9]
            if self.var == 702:
                self.txt_input.text = description[10]
            if self.var == 801:
                self.txt_input.text = description[11]
            if self.var == 802:
                self.txt_input.text = description[12]
            self.file_exists = True
        elif not exists(f"./img/{self.var}.png"):
            self.file_exists = False

    def image_source(self):
        self.check_file()
        if self.file_exists is True:
            self.my_image2.source = f'./img/{self.var}.png'
        elif self.file_exists is False:
            pass

    pass


class Player(Screen):

    def on_enter(self, *args):
        self.my_video.source = f'./img/{self.var}.mp4'
        pass

    pass


class PlcPage(Screen):
    file_exists = BooleanProperty(True)

    def on_enter(self, *args):
        self.image_source()

    def check_file(self):
        if exists(f"./img/{self.var}.png"):
            self.file_exists = True
        elif not exists(f"./img/{self.var}.png"):
            self.file_exists = False

    def image_source(self):
        self.check_file()
        if self.file_exists is True:
            self.my_image3.source = f'./img/{self.var}.png'
        elif self.file_exists is False:
            pass

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