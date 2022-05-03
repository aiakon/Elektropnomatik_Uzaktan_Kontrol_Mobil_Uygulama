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
               " konumunu değiştiren rölelere denir.",
               "•	Öncelikle START butonuna basıldığında K0 rölesi mühürlenmektedir ve K0 anahtarı kapalı konumda "
               "olacağından dolayı sistem çalışmaya başlayacaktır. İlk olarak piston S1 konumunda olacağı için S1 "
               "anahtarı kapalı konumda olacak ve YV0 valf selenoidi aktifleşerek pistonu ileri hareket ettirecektir.",
               "•	Ardından piston S2 konumuna geldiğinde S2 anahtarı kapanacak ve Z0 zaman rölesine elektrik enerjisi "
               "göndererek çalışmaya başlamasını sağlayacaktır.Zaman rölesi belirlenen süre olan 0.5 saniye bekledikten"
               " sonra Z0 anahtarını kapalı konuma geçirerek YV1 valf selenoidinin aktifleşmesini sağlayarak pistonun "
               "geri dönmesini sağlayacaktır. Bu sayede piston ileri gidip 3 saniye bekleyip geri dönme döngüsünü "
               "yapmış olacaktır. STOP butonuna basılmadığı sürece piston bu döngüde çalışmaya devam eder.",
               # 4.Deney [3,4,5]

               "•	Bu deneyde pistonun hem ileri giderken hem de geri dönerken beklemesini sağlayan kumanda devresini "
               "inceleyeceğiz.",
               "•	Öncelikle START butonuna basılarak K0 rölesinin mühürlenmesi sağlanır ve K0 "
               "anahtarı kapalı konuma geçtiği için sistem çalışmaya başlar. Piston başlangıç konumu olarak S1 "
               "konumunda olduğu için S1 anahtarı kapalı konumda olur ve Z0 zaman rölesine elektrik enerjisini ileterek"
               " zaman rölesinin çalışmasını sağlar.",
               "•	Z0 zaman rölesi 0.8 saniye bekledikten sonra Z0 anahtarını kapalı konumuna "
               "geçirerek YV0 valf selenoidinin aktifleşmesini sağlar ve piston ileri gitmeye başlar.",
               "•	Piston S2 konumuna geldiğinde S2 anahtarı kapalı konuma geçer ve Z1 zaman rölesine elektrik "
               "enerjisini ileterek çalışmasını sağlar.",
               "•	Z1 zaman rölesi 0.6 saniye bekledikten sonra Z1 anahtarını kapalı konumuna geçirerek YV1 valf "
               "selenoidinin aktifleşmesini sağlar ve piston geri döner.",        # 5.Deney [6,7,8,9,10]

               "•	Bu deneyde sayıcı röleleri inceleyeceğiz. Devre şematiğinde gördüğümüz C0 ismine sahip sembol "
               "sayıcı rölenin sembolüdür. Röledeki A1 ve A2 pinleri sayılması istenen sinyalin giriş ve çıkışlarıdır."
               " R1 ve R2 pinleri ise sayıcı rölenin reset pinlerinin giriş ve çıkışlarıdır. A1 pinine her sinyal "
               "geldiğinde sayıcı röle bunu algılayarak saymaya başlar ve rölenin ayarlandığı sayıya ulaşınca sayıcı "
               "röleye bağlı olan anahtarın konumunu değiştirir. Reset pini olan R1 pinine bir sinyal gelmediği sürece"
               " sayıcı röle bulunduğu konumda kalmaya devam eder.",
               "•	Öncelikle START butonuna basılarak K0 rölesinin mühürlenmesi sağlanır ve K0 anahtarı kapalı "
               "konuma geçtiği için sistem çalışmaya başlar. Piston başlangıç konumu olarak S1 konumunda olduğu için"
               " S1 anahtarı kapalı konumda olur ve YV0 selenoid valfinin aktifleşmesini sağlar bu sayede piston ileri "
               "gitmeye başlar.",
               "•	Piston S2 konumuna geldiğinde S2 anahtarı kapalı konuma geçer ve hem YV1 selenoid valfi"
               " aktifleşerek geri dönmesi sağlanır hem de C1 sayıcı rölesine sinyal giderek rölenin sayması sağlanır."
               " Sayıcı röle 3 kere sinyal saydığında C1 kapalı anahtarını açık konumuna getirerek YV0’ın "
               "aktifleşmesini engeller bu sayede döngü durdurulmuş olunur. Bu deney setinde C1 sayıcı rölesi "
               "resetlenmediği için döngüyü baştan başlatmak için sistemi baştan başlatmak gerekir. Bu durumu ileriki "
               "deneylerde göreceğiz.",      # 6.Deney [11,12,13]

               "•	Bu deneyde zaman ve sayıcı rölelerinin birlikte kullanımını inceleyeceğiz. Bir önceki deneyde "
               "anlattığımız üzere sayıcı rölelerin resetlenmesi için R1 pinine bir sinyal göndermemiz gerekli. Bu pine"
               " göndereceğimiz sinyal zaman rölesinin anahtarından geçmekte.",
               "•	Öncelikle START butonuna basılarak K0 rölesinin mühürlenmesi sağlanır ve K0 anahtarı kapalı konuma"
               " geçtiği için sistem çalışmaya başlar. Piston başlangıç konumu olarak S1 konumunda olduğu için S1 "
               "anahtarı kapalı konumda olur ve YV0 selenoid valfinin aktifleşmesini sağlar bu sayede piston ileri "
               "gitmeye başlar.",
               "•	Piston S2 konumuna geldiğinde S2 anahtarı kapalı konuma geçer ve hem YV1 selenoid valfi "
               "aktifleşerek geri dönmesi sağlanır hem de C1 sayıcı rölesine sinyal giderek rölenin sayması sağlanır.",
               "•	Sayıcı röle 3 kere sinyal saydığında C1 kapalı anahtarını açık konumuna getirerek YV0’ın "
               "aktifleşmesini bir süre engeller ve aynı süre boyunca C1 açık anahtarını da kapalı konuma getirerek "
               "Z0 zaman rölesinin çalışmasını sağlar.",
               "•	Zaman rölesinde belirlenen süre tamamlandıktan sonra Z0 zaman rölesinin anahtarı kapalı konuma "
               "geçerek C1 sayıcı rölesinin sıfırlanmasını sağlar ve bu sayede döngü tamamlanmış olur.",
               # 7.Deney [14,15,16,17,18]

               "•	Bu deneyde sayıcı röleyi START butonu ile sıfırlamayı ve sayıcı röle ile zaman rölesinin farklı "
               "bir kullanımını öğreneceğiz.",
               "•	Öncelikle START butonuna basılarak K0 rölesinin mühürlenmesi sağlanır ve K0 anahtarı kapalı konuma"
               " geçtiği için sistem çalışmaya başlar. Piston, başlangıç konumu olarak S1 konumunda olduğu için "
               "başlangıçta S1 anahtarı kapalı konumdadır ve dolayısıyla Z0 zaman rölesi çalışmaya başlar. ",
               "•	Zaman rölesinde belirlenen süre dolduğunda Z0 anahtarı tetiklenerek kapalı konuma geçer ve YV0 "
               "valf selenoidinin aktifleştirerek pistonun ileriye hareket etmesini sağlar. ",
               "•	Piston S2 konumuna geldiğinde S2 anahtarı tetiklenerek kapalı konuma geçer ve Z1 zaman rölesinin "
               "çalışmasını sağlar. ",
               "•	Z1 zaman rölesi belirlenen süre kadar bekledikten sonra Z1 anahtarını tetikleyerek kapalı "
               "konuma geçirir ve YV1 valf selenoidinin aktifleştirerek pistonun geriye dönmesini sağlar. Piston geriye"
               " dönerken aynı zamanda sayıcı röleye bir sinyal göndererek ileri-geri döngüsünü 1 kere tamamladığını "
               "bildirir.",
               "•	Sistem 3 defa ileri-geri döngüsünü yaptıktan sonra sayıcı röle "
               "kendisine bağlı olan C1 kapalı anahtarını açık konuma getirir ve sistemin gücünü sağlayan K0’ın "
               "mührünü kırarak sistemi kapatmış olur. Sistemin baştan çalışmasını sağlamak için START butonuna "
               "tekrar basılır bu sayede hem C1 sayıcı rölesine reset sinyali gitmiş olur hem de K0 rölesinin "
               "mühürlenmesi sağlanarak sistemin çalışması sağlanır.",      # 8.Deney [19,20,21,22,23,24]

               "•	Bu deneyde kumanda devresi ile 2 pistonu kontrol etmeyi öğreneceğiz. 2 pistonu birbirinden "
               "bağımsız olarak kontrol etmek için kumanda devresine paralel bir şekilde YV2 ve YV3 valf selenoidlerini"
               " eklememiz yeterli.",
               "•	Öncelikle START butonuna basarak K0 rölesinin mühürlenmesini sağlanır ve K0 anahtarı kapalı konuma"
               " geçer bu sayede sistem çalışmaya başlar. 2 pistona ait valf selenoidleri birbirinden bağımsız olarak"
               " çalışacağı için aslında 3. Deneydeki sistemin 2 farklı pistona ait kumanda devrelerinin birleşimi "
               "olarak düşünebiliriz. Başlangıçta, piston S1 konumundayken S1 anahtarı kapalı konuma geçerek YV0 valf "
               "selenoidinin aktifleşmesini sağlar ve 1. piston ileri gitmeye başlar.\n\n•	Piston S2 konumuna "
               "geldiğinde ise S2 anahtarı kapalı konuma geçerek YV1 valf selenoidinin aktifleşmesini sağlayarak 1. "
               "pistonun geri gitmesini sağlar. ",
               "•	Aynı şekilde başlangıçta, piston S3 konumundayken S3 anahtarı kapalı konuma geçerek YV2 valf "
               "selenoidinin aktifleşmesini sağlar ve 2. piston ileri gitmeye başlar.\n\n•	Piston S4 konumuna "
               "geldiğinde ise S4 anahtarı kapalı konuma geçerek YV3 valf selenoidinin aktifleşmesini sağlayarak 2. "
               "pistonun geri gitmesini sağlar.",      # 9.Deney [25,26,27]
               ""

               ]