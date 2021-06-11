from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep

init()

n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]

try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

def banner():
    import random
    # fancy logo
    b = [
    '   #####     #    ######  #######',
    '  #     #   # #   #     # #     #',
    '  #        #   #  #     # #     #', 
    '   #####  #     # ######  #     #', 
    '        # ####### #     # #     #', 
    '  #     # #     # #     # #     #', 
    '   #####  #     # ######  #######' 
    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
    print('=============SABO==============')
    print(f'   Version: 1.0 | Tác giả: Sabo{n}\n')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    banner()
    print(lg+'[1] Thêm tài khoản mới'+n)
    print(lg+'[2] Lọc tất cả các tài khoản bị cấm'+n)
    print(lg+'[3] Xóa các tài khoản cụ thể'+n)
    print(lg+'[4] Cập nhật code của bạn'+n)
    print(lg+'[5] Quit'+n)
    a = int(input('\nNhập sự lựa chọn của bạn: '))
    if a == 1:
        new_accs = []
        with open('vars.txt', 'ab') as g:
            number_to_add = int(input(f'\n{lg} [~] Enter number of accounts to add: {r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{lg} [~] Enter Phone Number: {r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{lg} [i] Đã lưu tất cả tài khoản vào tệp vars.txt')
            clr()
            print(f'\n{lg} [*] Đăng nhập tài khoản mới\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                c.start(number)
                print(f'{lg}[+] Đăng nhập thành công')
                c.disconnect()
            input(f'\n Nhấn enter để chuyển đến menu chính...')

        g.close()
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] Không có tài khoản! Vui lòng thêm một số và thử lại')
            sleep(3)
        else:
            for account in accounts:
                phone = str(account[0])
                client = TelegramClient(f'sessions/{phone}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+] Enter the code: '))
                        print(f'{lg}[+] {phone} không bị banned{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' đã bị banned!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'Chúc mừng! Không có tài khoản bị banned')
                input('\nNhấn enter để chuyển đến menu chính...')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('vars.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[i] Đã xóa tất cả tài khoản bị banned'+n)
                input('\nNhấn enter để chuyển đến menu chính...')

    elif a == 3:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{lg}[i] Chọn một tài khoản để xóa\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[0]}{n}')
            i += 1
        index = int(input(f'\n{lg}[+] Nhập một lựa chọn: {n}'))
        phone = str(accs[index][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('vars.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] Tài khoản đã bị xóa{n}')
        input(f'\nNhấn enter để chuyển đến menu chính...')
        f.close()
    elif a == 4:
        # thanks to github.com/th3unkn0n for the snippet below
        print(f'\n{lg}[i] Kiểm tra các bản cập nhật...')
        try:
            # https://raw.githubusercontent.com/Cryptonian007/Astra/main/version.txt
            version = requests.get('https://raw.githubusercontent.com/ryostar/TOOL-ADDMEMBER/main/version.txt')
        except:
            print(f'{r} Bạn không kết nối với Internet')
            print(f'{r} Vui lòng kết nối với internet và thử lại')
            exit()
        if float(version.text) > 1.1:
            prompt = str(input(f'{lg}[~] Cập nhật có sẵn [Phiên bản {version.text}]. Tải xuống?[y/n]: {r}'))
            if prompt == 'y' or prompt == 'yes' or prompt == 'Y':
                print(f'{lg}[i] Đang tải xuống bản cập nhật...')
                if os.name == 'nt':
                    os.system('del add.py')
                    os.system('del manager.py')
                else:
                    os.system('rm add.py')
                    os.system('rm manager.py')
                #os.system('del scraper.py')
                os.system('curl -l -O https://raw.githubusercontent.com/ryostar/TOOL-ADDMEMBER/main/add.py')
                os.system('curl -l -O https://raw.githubusercontent.com/ryostar/TOOL-ADDMEMBER/main/manager.py')
                print(f'{lg}[*] Đã cập nhật lên phiên bản: {version.text}')
                input('Nhấn enter để thoát ...')
                exit()
            else:
                print(f'{lg}[!] Cập nhật bị hủy.')
                input('Nhấn enter để truy cập menu chính ...')
        else:
            print(f'{lg}[i] Code của bạn đã được cập nhật')
            input('Nhấn enter để truy cập menu chính ...')
    elif a == 5:
        clr()
        banner()
        exit()
