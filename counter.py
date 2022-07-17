import tkinter as tk


def add_stock():
    num_stock = stock.get() + 1
    stock.set(num_stock)
    stock_label['text'] = 'ストック数:{}杯'.format(stock.get())

def sub_stock():
    num_stock = stock.get() - 1
    stock.set(num_stock)
    stock_label['text'] = 'ストック数:{}杯'.format(stock.get())
    num_total = total.get() + 1
    total.set(num_total)
    total_label['text'] = '飲んだ数:{}杯'.format(total.get())

def add_total():
    num_total = total.get() + 1
    total.set(num_total)
    total_label['text'] = '飲んだ数:{}杯'.format(total.get())

def sub_total():
    num_total = total.get() - 1
    total.set(num_total)
    total_label['text'] = '飲んだ数:{}杯'.format(total.get())

def reset_stock():
    stock.set(0)
    stock_label['text'] = 'ストック数:{}杯'.format(stock.get())

def reset_total():
    total.set(0)
    total_label['text'] = '飲んだ数:{}杯'.format(total.get())

#### 画面設定 ####
base = tk.Tk()
base.title('何屋カウンター')
canvas = tk.Canvas(base, width=400, height=100)
canvas.pack()

#### 飲酒カウント ####
total = tk.IntVar()
stock = tk.IntVar()
total.set(0)
stock.set(0)

#### 表示ラベル ####
total_label = tk.Label(anchor='center')
total_label.place(x=100, y=20)
total_label['text'] = '飲んだ数:{}杯'.format(total.get())
stock_label = tk.Label(anchor='center')
stock_label.place(x=240, y=20)
stock_label['text'] = 'ストック数:{}杯'.format(stock.get())

#### ボタン設定####
botton_sub_stock = tk.Button(base, text='-', command=sub_stock)
botton_sub_total = tk.Button(base, text='-', command=sub_total)
botton_add_stock = tk.Button(base, text='+', command=add_stock)
botton_add_total = tk.Button(base, text='+', command=add_total)
botton_reset_stock = tk.Button(base, text='reset', command=reset_stock)
botton_reset_total = tk.Button(base, text='reset', command=reset_total)

#### ボタン配置 ####
botton_sub_total.place(x=70, y=50)
botton_reset_total.place(x=110, y=50)
botton_add_total.place(x=170, y=50)
botton_sub_stock.place(x=220, y=50)
botton_reset_stock.place(x=260, y=50)
botton_add_stock.place(x=320, y=50)


base.mainloop()