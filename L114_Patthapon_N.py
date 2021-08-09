from tkinter import *
from tkinter import ttk
import math
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
import matplotlib.pyplot as plt
from datetime import date
btc_rate = BtcConverter()
currency_rate = CurrencyRates()

def BMI_window_main(e):
    # Func สำหรับคำนวณ
    def BMI_cal():
        x = float(text_box_weight.get()) / math.pow(float(text_box_height.get()) / 100, 2)
        if x < 18.5:
            label_result.configure(text="ผอมเกินไป")
        elif x < 22.9:
            label_result.configure(text="น้ำหนักปกติ")
        elif x < 24.9:
            label_result.configure(text="น้ำหนักเกิน")
        elif x < 29.9:
            label_result.configure(text="อ้วน")
        elif x >= 30:
            label_result.configure(text="อ้วนมาก")
    # หน้าต่างการคำนวณค่า BMI
    BMI_window = Tk()
    BMI_window.title("การคำนวณค่า BMI")
    # ความสูง
    label_height = Label(BMI_window, text="ส่วนสูง (cm.)", font=("Angsana New", 18))
    label_height.grid(row=0, column=0)
    text_box_height = Entry(BMI_window)
    text_box_height.grid(row=0, column=1, padx=10)
    # น้ำหนัก
    label_weigth = Label(BMI_window, text="น้ำหนัก (kg.)", font=("Angsana New", 18))
    label_weigth.grid(row=1, column=0, padx=10)
    text_box_weight = Entry(BMI_window)
    text_box_weight.grid(row=1, column=1)
    # ปุ่มคำนวณ
    calculate_button = Button(BMI_window, text="คำนวณ",bg='lime',command=BMI_cal, font=("Angsana New", 18), width=7, height=1)
    calculate_button.grid(row=2, column=0)
    # ผลลัพธ์
    label_result = Label(BMI_window, text="ผลลัพธ์", font=("Angsana New", 18))
    label_result.grid(row=2, column=1)
    # ปุ่ม กลับสู่เมนูหลัก
    button_back = Button(BMI_window, text="กลับสู่เมนูหลัก", bg='sky blue', command=BMI_window.withdraw, font=("Angsana New", 18), width=15, height=1)
    button_back.grid(row=3, columnspan=2, pady=10)


def convert_amount_main(e):
    # Func สำหรับการแปลงค่าเงิน
    def result_currency():
        result = (currency_rate.convert(first_currency_box.get(), second_currency_box.get(),float(currency_amount.get())))
        result_label.configure(text=("%.2f") % (result))
    # ค่าเงินเริ่มต้น
    convert_amount_window = Tk()
    convert_amount_window.title("การแปลงค่าเงิน")
    first_currency_label = Label(convert_amount_window, text="First Currency", font=("Angsana New", 18))
    first_currency_label.grid(row=0, column=0)
    first_currency_box = ttk.Combobox(convert_amount_window,values=list(currency_rate.get_rates('')),width=20, state='readonly')
    first_currency_box.current(29)
    first_currency_box.grid(row=1, column=0, padx=10, pady=10)
    label_amount = Label(convert_amount_window, text="Please Enter Amount", font=("Angsana New", 18))
    label_amount.grid(row=2, column=0)
    # ช่องสำหรับคีย์ค่าเงิน
    currency_amount = Entry(convert_amount_window)
    currency_amount.grid(row=3, column=0)
    # ค่าเงินที่ต้องการแปลง
    second_currency_label = Label(convert_amount_window, text="Second Currency", font=("Angsana New", 18))
    second_currency_label.grid(row=0, column=1)
    second_currency_box = ttk.Combobox(convert_amount_window,values=list(currency_rate.get_rates("")), state='readonly')
    second_currency_box.current(0)
    second_currency_box.grid(row=1, column=1, padx=10, pady=10)
    # ปุ่ม Convert
    convert_button = Button(convert_amount_window, text="Convert", bg="lime", command=result_currency, font=("Angsana New", 18), width=10, height=1)
    convert_button.grid(row=4, column=0, padx=10, pady=10)
    # ปุ่ม กลับสู่เมนูหลัก
    button_back = Button(convert_amount_window, text="กลับสู่เมนูหลัก", bg='sky blue', command=convert_amount_window.withdraw, font=("Angsana New", 18), width=15, height=1)
    button_back.grid(row=4, column=1, padx=10, pady=10)

    # ผลลัพธ์
    result_label = Label(convert_amount_window, text="Result", font=("Angsana New", 18))
    result_label.grid(row=3, column=1)


def BTC_main(e):
    # Func สำหรับการแปลง BTC
    def result_btc_currency():
        result_btc = btc_rate.convert_btc_to_cur(float(currency_btc_amount.get()), second_currency_btc.get())
        result_btc_to.configure(text=("%.2f") % (result_btc))

    # Func สำหรับการแสดงกราฟ
    def graph_btc():
        year = int(input_year.get())
        month = int(input_month.get())
        day = int(input_day.get())
        start_date = date(year, month, day)
        end_date = date(year + 1, month, day)
        result_price_list = btc_rate.get_previous_price_list(second_currency_btc.get(), start_date, end_date)
        date_result = result_price_list.keys()
        rate_result = result_price_list.values()
        plt.figure("BTC graph")
        plt.title("The graph shows the change in price BTC")
        plt.plot(date_result, rate_result)
        plt.xlabel("Date")
        plt.ylabel("BTC / Rate")
        plt.show()
    # หน้าต่าง Bitcoin Price
    btc_window = Tk()
    btc_window.title("Bitcoin Price")
    # ช่องสำหรับคีย์ค่าจำนวน Bitcoin
    btc_currency_label = Label(btc_window, text="BTC Currency", font=("Angsana New", 18), padx=10)
    btc_currency_label.grid(row=0, column=0)
    currency_btc_amount = Entry(btc_window)
    currency_btc_amount.grid(row=1, column=0, padx=10)
    # ค่าเงินที่ต้องการแปลง
    second_currency_label = Label(btc_window, text="Currency", font=("Angsana New", 18), padx=10)
    second_currency_label.grid(row=0, column=1)
    second_currency_btc = ttk.Combobox(btc_window, values=[
                                       "USD",
                                       "JPY",
                                       "EUR",
                                       "THB",
                                       "IDR",
                                       "BGN",
                                       "ILS",
                                       "GBP",
                                       "AUD",
                                       "CHF",
                                       "HKD"], state='readonly')
    second_currency_btc.current(3)
    second_currency_btc.grid(row=1, column=1, padx=10)
    # ปุ่ม convert bitcoin to currency
    convert_btc_button = Button(btc_window, text="Convert", bg="lime", command=result_btc_currency,font=("Angsana New", 18), width=10, height=1)
    convert_btc_button.grid(row=4, column=0, padx=10, pady=10)
    # ปุ่ม แสดงGraph
    graph_btc_button = Button(btc_window, text="Graph", bg="blue", command=graph_btc,font=("Angsana New", 18), width=10, height=1)
    graph_btc_button.grid(row=4, column=1, padx=10, pady=10)
    # ปุ่ม กลับสู่เมนูหลัก
    button_back = Button(btc_window, text="กลับสู่เมนูหลัก", bg='sky blue', command=btc_window.withdraw, font=("Angsana New", 18),width=15, height=1)
    button_back.grid(row=4, column=2, padx=10, pady=10)

    # ช่องสำหรับคีย์ค่า ปี, เดือน, วัน
    year_lebel = Label(btc_window, text="Year").grid(row=3, column=0, sticky=W, padx=10, pady=10)
    input_year = Entry(btc_window, width=8)
    input_year.grid(row=3, column=0)
    month_lebel = Label(btc_window, text="Month").grid(row=3, column=1, sticky=W, pady=10)
    input_month = Entry(btc_window, width=8)
    input_month.grid(row=3, column=1)
    day_label = Label(btc_window, text="Day").grid(row=3, column=2, sticky=W, pady=10)
    input_day = Entry(btc_window, width=8)
    input_day.grid(row=3, column=2)
    # text คำเตือน
    text_to = Label(btc_window, text="*กรุณาเลือกก่อนปี 2013", fg="red",font=("angsana new", 15))
    text_to.grid(row=2, column=0)
    text_to_2 = Label(btc_window, text="(โปรแกรมจะแสดงผลตั้งแต่วันที่เลือกไม่เกิน 1 ปี)", fg="red",font=("angsana new", 15))
    text_to_2.grid(row=2, column=1)
    # ผลลัพธ์
    result_btc_label = Label(btc_window, text="Result", font=("Angsana New", 18), padx=10)
    result_btc_label.grid(row=0, column=2)
    result_btc_to = Label(btc_window, text="$$$", font=("Angsana New", 18), padx=10, pady=10)
    result_btc_to.grid(row=1, column=2)

def select_main():
    # หน้าต่าง Select menu
    select_window = Tk()
    select_window.title("Select menu")
    button1 = Button(select_window, text="การคำนวณค่า BMI", bg="steel blue", font=("angsana new", 20), width=20, height=1)
    button1.grid(row=1, column=1, padx=10, pady=10)
    button1.bind('<Button-1>', BMI_window_main)
    button2 = Button(select_window, text="การแปลงค่าเงิน", bg="steel blue", font=("angsana new", 20), width=20, height=1)
    button2.grid(row=2, column=1, padx=10, pady=10)
    button2.bind('<Button-1>', convert_amount_main)
    button3 = Button(select_window, text="Bitcoin prices", bg="steel blue", font=("angsana new", 20), width=20, height=1)
    button3.grid(row=3, column=1, padx=10, pady=10)
    button3.bind('<Button-1>', BTC_main)
    button4 = Button(select_window, text="Sign out",command=select_window.withdraw, bg="steel blue", font=("angsana new", 20), width=20, height=1)
    button4.bind('<Button-1>', menu_main)
    button4.grid(row=4, column=1, padx=10, pady=10)
    label_main = Label(select_window, text="*โปรดเลือกเมนูด้านล่าง", width=20, fg="red", font=("angsana new", 18))
    label_main.grid(row=0, column=1)

def menu_main(e):
    def login(e):
        u = username_box.get()
        p = password_box.get()
        if u == "admin" and p == "1234":
            print("login complete")
            menu_window.withdraw()
            return select_main()
        else:
            print("login failed")
            print("admin , 1234")
            log_in_status.configure(text="*login failed")

    menu_window = Tk()
    menu_window.title("Login")
    username_label = Label(menu_window, text="Please enter your username", font=("Angsana New", 18))
    username_label.grid(row=1, column=0)
    username_box = Entry(menu_window, width=35)
    username_box.grid(row=2, column=0, padx=10)
    password_label = Label(menu_window, text="Please enter your password", font=("Angsana New", 18))
    password_label.grid(row=3, column=0)
    password_box = Entry(menu_window, width=35)
    password_box.grid(row=4, column=0, padx=10)

    log_in_status = Label(menu_window, text="", font=("Angsana New", 15), fg='red', padx=10)
    log_in_status.grid(row=0, column=0)

    log_in_button = Button(menu_window, text="Login", bg="lime", font=("Angsana New", 18), width=10, height=1)
    log_in_button.bind('<Button-1>', login)
    log_in_button.grid(row=5, column=0, padx=10, pady=10, sticky=W)
    button_exit = Button(menu_window, text="Exit", bg='sky blue', command=menu_window.quit, font=("Angsana New", 18),width=10, height=1)
    button_exit.grid(row=5, column=0, padx=10, sticky=E)

well_main = Tk()
well_main.title("Wellcome")
well_label = Label(well_main, text="*กรุณากดที่ปุ่มด้านล่างเพื่อเริ่มใช้งานโปรแกรม", font=("Angsana New", 16),fg='red')
well_label.grid(row=0, column=0,  padx=10)
click_button = Button(well_main, text="Start", command=well_main.withdraw, bg="green", font=("Angsana New", 18), width=10, height=1)
click_button.bind('<Button-1>', menu_main)
click_button.grid(row=1, column=0, pady=10, padx=10)

well_main.mainloop()