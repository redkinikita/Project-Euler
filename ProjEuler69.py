func={}

def Factor(n):
	Ans=[]
	d=2
	while d*d<=n:
		if n%d==0:
			Ans.append(d)
			n//=d
		else:
			d+=1
	if n>=1:
		Ans.append(n)
	return Ans

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

for i in range(2,1000000):
	mas=1
	k=set(Factor(i))
	for j in k:
		mas*=(j/(j-1))
	func[i]=mas
	
print(get_key(func, max(func.values())))

natali.gadiuk@gmail.com
vladko3000@gmail.com
natali.gadiuk@gmail.com
cs16003@s.inf.shizuoka.ac.jp
allahgholipoursolareclipe78@gmail.com
valentynandriichuk@ukr.net
Виталий Антоненко
aoki.toru@shizuoka.ac.jp
avdeionok.ira@gmail.com
benramache.said@gmail.com
alexvntu@gmail.com
ihordobry@gmail.com
mike_bondar@iop.kiev.ua
Volodymyr Borovytsky
vitalik2012bortnik@gmail.com
Viktor Borysyuk
burlachenko@univ.kiev.ua
laurent.cario@cnrs-imn.fr
yevheniia.chernukha.etu@univ-lemans.fr
V. Chornii
kamal choudhary
igor.tesV@gmail.com
rostyslav.danylo@ensta-paristech.fr
igordacen@gmail.com
davidenko@univ.kiev.ua
DEHGHANI@KASHANU.AC.IR
o.o.dyachkova@gmail.com
igor_dmitruk@univ.kiev.ua
Iryna Doroshenko
binomustyglobal@gmail.com
tsd65088@st.yamagata-u.ac.jp
citral_66@yahoo.com
gamayunova@ilt.kharkov.ua
Tanya Gorkavenko
vitaliy.goryashko@physics.uu.se
gt.tkr1127.brg13@gmail.com
naveens222@rediffmail.com
hayakawa.mamoru.15@shizuoka.ac.jp
cs16079@s.inf.shizuoka.ac.jp
kase.hiroki@shizuoka.ac.jp
Олексій Гудзь
iqra@szu.edu.cn
oksanka.isayeva@gmail.com
valentina_ivankova@ukr.net
etienne.janod@cnrs-imn.fr
조영달
Dr. Susheel Kalia
kambe.kensuke.14@shizuoka.ac.jp
Netram Kaurav
larisa.khalanchuk@tsatu.edu.ua
Аліна Ходько
Kolbasow@pactech.de
skooi@mit.edu
olhakravchuk2018@gmail.com
vasyl.kravets@manchester.ac.uk
ellipso@ukr.net
olegkukochka@gmail.com
cs16023@s.inf.shizuoka.ac.jp
kurlov@pdi-berlin.de
guillaume.lambert@ensta-paristech.fr
amina.larabi8@gmail.com
talen@univ.kiev.ua
Євгеній Левченко
artem.levchuk.etu@univ-lemans.fr
lizunov.vyacheslav@gmail.com
lizunov.vyacheslav@gmail.com
logvin-alina97@ukr.net
podgurskiymassimo@gmail.com
realcrystallab@univ.kiev.ua
mimura.hidenori@shizuoka.ac.jp
mokrinskaya@ukr.net
smorozov@imperial.ac.uk
mouradph@gmail.com
nadvornik@karlov.mff.cuni.cz
ohtake.ryota.15@shizuoka.ac.jp
ozerov@magnet.fsu.edu
paiuk@ua.fm
iud14@ukr.net
pobiedina@hlr.ua
yuri.yeromenko@gmail.com
poprugko@univ.kiev.ua
pvm13031997@gmail.com
Prorok V.V.
i.pruben34s@gmai.com
mykhailo.rakov@univ.kiev.ua
Redkov2000@gmail.com
reza.rasoolzadeh@yahoo.com
riazantceva.v@gmail.com
riazantceva.v@gmail.com
sgr@univ.kiev.ua
g.yu.rudko@gmail.com
Ruslan Ryskulov
alancash777@gmail.com
andser@amu.edu.pl
georgii.shamuilov@physics.uu.se
Андрей Щербаков
Olena Shynkarenko
yevhen.shynkarenko@empa.ch
stassluta@gmail.com
igordacen@gmail.com
serikof14@i.ua
alexander.stronski@gmail.com
tabata.kento.15@shizuoka.ac.jp
teplirin@gmail.com
teplirin@gmail.com
bineyammulugetabineyam@gmail.com
tkacholyalya@gmail.com
vlad040495@gmail.com
ttm15520@st.yamagata-u.ac.jp
tsx14841@st.yamagata-u.ac.jp
VAJEDIFAHIMESADAT@GMAIL.COM
yevhenii.vaskivskyi@ijs.si
Tonya Vasileva
vvvit@ukr.net
alena.vertsanova@gmail.com
v.mitsa@gmail.com
vorobjov.official@gmail.com
yamakado@yz.yamagata-u.ac.jp
yamakado@yz.yamagata-u.ac.jp
yamakado@yz.yamagata-u.ac.jp
yamakawa@cs.kumamoto-u.ac.jp
uv365nm@ukr.net
Vasil Yavas
yuri.yeromenko@gmail.com
吉田司
vladira_19@ukr.net
vulfar42@gmail.com
yaroslav.znamenshchykov@gmail.com
nenadnex@gmail.com
anya.lisova.lao@gmail.com
Redkov2000@gmail.com
king.krollie@gmail.com
bogdan.kosharuk@gmail.com
danyliuk.andrew@elitar.rv.ua
muzykantova.kate@gmail.com
w1th3r0@gmail.com
annarashko12@gmail.com
andrievskiyarik@gmail.com
995nik@gmail.com
ketchupvika@gmail.com
kashko.pavlo@gmail.com
sofiamelnik2002@gmail.com
kl.irina10@gmail.com
pm949745@gmail.com
lol.gomaster@mail.ru
werest.rew@gmail.com
smyrf200323@gmail.com
muzykantova.kate@gmail.com
maksimlitovchenko11.03@gmail.com
i.vyshniak.2004@gmail.com
andrej20050206@gmail.com
arosukmisa073@gmail.com
kiienko.romaniuk@gmail.com
suairia@ukr.net
dlvelychko.uk18@kubg.edu.ua
kiril.mosiychuk@gmail.com
k.ilya.v.2005@gmail.com
linsin@ukr.net
kirilyukvolodimir2003@gmail.com
vovan123456789080@gmail.com
ivamarta2002@gmail.com
Fikusguy007@gmail.com
myron.sukhanov@gmail.com
dionisiy04@gmail.com
stomatik20053@gmail.com
endotech84@gmail.com
tatjana.ogar@gmail.com
ivamasha2002@gmail.com
gritzenkomiroslav@gmail.com
ivan.andriievskyi@gmail.com
bublyk1000@gmail.com
fhyfv2457@gmail.com
karleonev@gmail.com
muzykantova.kate@gmail.com
dianna.k.23.09@gmail.com
sechkarg@gmail.com
kechaofficial@gmail.com
krasnayastal@gmail.com
vlad0s91k@gmail.com
andriyp365@ukr.net
grinvols@gmail.com
muzykantova.kate@gmail.com
kl.irina@gmail.com
andrey_simonov@icloud.com
danielreznik3@gmail.com
zasobaalenaa@gmail.com
korpach.nazar@Gmail.com
linsin@ukr.net
muzykantova.kate@gmail.com
kiriukhin.kiril@gmail.com
valerochka.boyko@gmail.com
Siriuspngn@gmail.com
ttbi@ua.fm
elenatomchuk72@gmail.com
suairia@ukr.net
vasjok1488@gmail.com
s80674191139@gmaio.com
shtepa.v@yahoo.com
Evristika@i.ua
grani20@ukr.net
c.ilyas@hotmail.fr
necaticelik1@hotmail.com
andre-edmund.mysyrowicz@ensta-paristech.fr
rysalla4ka@ukr.net
rostyslav.danylo@ensta-paristech.fr
vvvit@ukr.net
dmtdemirag@gmail.com
dmtdemirag@gmail.com
n.margaryan@polytechnic.am
andrii_misiura@ukr.net
Владимир Сендюк
Tonya Vasileva
olbychos@gmail.com
Olga Bordian
alicemetale@gmail.com
Онанко
Онанко
aburin@tulane.edu
Виталий Антоненко
SVS97@i.ua
avdeionok.ira@gmail.com
vitali_gogoberidze@hotmail.com
shardfotechcomltd@yahoo.com
ivan.smalyukh@colorado.edu
vasyl.kravets@manchester.ac.uk
Ірина Вікторівна Бар'яхтар
Онанко
Онанко
Galina Dovbeshko
Ірина Вікторівна Бар'яхтар
intercalant@univ.kiev.ua
tip.eldar@gmail.com
natali.gadiuk@gmail.com
anya.lisova.lao@gmail.com
rkarapinar@mehmetakif.edu.tr
rkarapinar@mehmetakif.edu.tr
Volodymyr Borovytsky
lmeln@ukr.net
realcrystallab@univ.kiev.ua
romanenkokiril@meta.ua
romanenkokiril@meta.ua
Iluha110604@Gmail.com
sashaniasha2003@gmail.com
vitalik_bortnik@ukr.net
undante@mail.ru
aeserebr@gmail.com
paiuk@ua.fm
Liubov Revutska
Dmytro Averin
sgr@univ.kiev.ua
sgr@univ.kiev.ua
kindled@knu.ua
lerka 1883
dianagurova37@gmail.com
Viktor Borysyuk
skyper@online.ua
geniyco@gmail.com
pvm13031997@gmail.com
irene.shyan@gmail.com
oksanagoncharova19@gmail.com
tsegelna_anna@ukr.net
snezhana.bilonoga16@gmail.com
Lneere1@gmail.com
Петро (spiritofspirt@gmail.com)
nakagawa.hisaya.14@shizuoka.ac.jp
sakaida.kohei.23@gmail.com
logvin-alina97@ukr.net
Prorok V.V.
kononenko.vadim96@gmail.com
f.kinzerskyi@gmail.com
chukova@univ.kiev.ua
space-researcher@i.ua
uv365nm@ukr.net
Olena Vertsanova
Онанко
svitlana levchenko
kovalyova_marianna@ukr.net
fraginao@gmail.com
i.pruben34s@gmail.com
nickolaibubalo@gmail.com
maryna-okhrimenko@ukr.net
vadym685@gmail.com
Дмитрий Гнатюк
maryna-okhrimenko@ukr.net
kamal choudhary
anya.lisova.lao@gmail.com
