import urllib.request as urq
import time

def get_url(url) :
    return str(urq.urlopen(url).read().decode('utf-8'))

def get_data(url2data) :
    a = url2data.find("font-weight: 400;\">")
    b = url2data.find("font-weight: 400;\">โซน<",a+1)
    
    return url2data[a:b+24]

url = "https://www.xn--82czag4co0a7bg7cpj1c3gpi.com/%E0%B8%A8%E0%B8%B1%E0%B8%9E%E0%B8%97%E0%B9%8C%E0%B8%A0%E0%B8%B2%E0%B8%A9%E0%B8%B2%E0%B8%AD%E0%B8%B1%E0%B8%87%E0%B8%81%E0%B8%A4%E0%B8%A9/"
Data = get_data(get_url(url))

def main():
    ans = []
    Datanew = Data
    while True:
        a = Datanew.find("font-weight: 400;\">", 0)
        b = Datanew.find("<", a+1)
        c = Datanew.find("font-weight: 400;\">", b+1)
        d = Datanew.find("<", c+1)
        ans.append(f'"{Datanew[a+19:b]}":"{Datanew[c+19:d]}"')
        if len(ans) == 3832 : break
        Datanew = Datanew[d+1::]
    print(len(ans),"word")
    return ans

def test():
    k = 0
    Datanew = Data
    while True:
        a = Datanew.find("font-weight: 400;\">", 0)
        b = Datanew.find("<", a+1)
        c = Datanew.find("font-weight: 400;\">", b+1)
        d = Datanew.find("<", c+1)
        print(f'{Datanew[a+19:b]}: {Datanew[c+19:d]}')
        k += 1
        if k == 3832 : break
        Datanew = Datanew[d+1::]
    return print(f"{k} คำ")

def write_file():
    fio = open("data_for_vocab_game","w")
    fio.write(",".join(main()))
    fio.close()
    return print("finish for write file")
    
start = time.time()
#write_file()
test()
stop = time.time()
print("total time :",round(stop-start,2),"วินาที")