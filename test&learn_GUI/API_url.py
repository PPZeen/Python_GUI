import tkinter as tk
import requests

H = 500 # กำหนดค่าตัวแปรความสูงหน้าต่างโปรแกรม
W = 800 # ตัวแปรความกว้าง

root = tk.Tk()

canvas = tk.Canvas(root, height=H, width=W)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text='ตกลง', font=40, command=lambda: get_data(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg= '#80c1ff', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 18), anchor='nw', justify='left')
label.place(relwidth=1, relheight=1)

def data_response(data):
    try:
        prov = data['จังหวัด']
        name = data['ชื่อหน่วยงานการแพทย์ฉุกเฉินจังหวัด']
        num = data['เครือข่ายที่']
        long = data['LONGITUDE']
        lat = data['LATITUDE']
        final_str = 'จังหวัด: %s \nชื่อหน่วยงาน: %s \nหมายเลขหน่วยงาน: %s \nลองติจูด: %s \nละติจูด: %s' % (str(prov),str(name),str(num), str(long), str(lat))
    except:
        final_str = 'There was a problem'
    return final_str

def get_data(province):
    url = 'http://opend.openservice.in.th/search_virtuoso/api/dataset/query?dsname=vir_212_1527501632&path=vir_212_1527501632&loadAll=1&type=json&limit=100&offset=0'
    r = requests.get(url)
    r_json = r.json()['data']
    data = next(item for item in r_json if item["จังหวัด"] == province)
    label['text'] = data_response(data)

root.mainloop()