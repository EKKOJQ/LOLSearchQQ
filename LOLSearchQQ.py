import tkinter as tk
from tkinter import ttk
import requests
def query_info():
    lol_name = lol_entry.get()

    # 查询LOL信息
    url_lol = "https://zy.xywlapi.cc/lolname"
    params_lol = {"name": lol_name}

    try:
        response_lol = requests.get(url_lol, params=params_lol)
        data_lol = response_lol.json()

        if data_lol["status"] == 200:
            qq = data_lol["qq"]
            game_name = data_lol["name"]
            daqu = data_lol["daqu"]
            qq_result_label.config(text=f"QQ号: {qq}\n游戏名: {game_name}\n游戏大区: {daqu}")

            # 设置复制QQ号按钮
            copy_qq_button.config(command=lambda: copy_to_clipboard(qq))

            # 查询QQ信息
            url_qq = "https://zy.xywlapi.cc/qqapi"
            params_qq = {"qq": qq}

            try:
                response_qq = requests.get(url_qq, params=params_qq)
                data_qq = response_qq.json()

                if data_qq["status"] == 200:
                    phone = data_qq["phone"]
                    phonediqu = data_qq["phonediqu"]
                    phone_label.config(text=f"绑定号码: {phone}\n号码地区: {phonediqu}")

                    # 设置复制手机号按钮
                    copy_phone_button.config(command=lambda: copy_to_clipboard(phone))

                else:
                    phone_label.config(text=f"QQ查询失败: {data_qq['message']}")

            except Exception as e:
                phone_label.config(text=f"QQ查询出错: {str(e)}")

        else:
            qq_result_label.config(text=f"LOL查询失败: {data_lol['message']}")

    except Exception as e:
        qq_result_label.config(text=f"LOL查询出错: {str(e)}")

def query_phone():
    qq_number = qq_entry.get()

    # 查询QQ信息
    url_qq = "https://zy.xywlapi.cc/qqapi"
    params_qq = {"qq": qq_number}

    try:
        response_qq = requests.get(url_qq, params=params_qq)
        data_qq = response_qq.json()

        if data_qq["status"] == 200:
            phone = data_qq["phone"]
            phonediqu = data_qq["phonediqu"]
            phone_result_label.config(text=f"手机号码: {phone}\n号码地区: {phonediqu}")

            # 设置复制手机号按钮
            copy_phone_button_2.config(command=lambda: copy_to_clipboard(phone))

        else:
            phone_result_label.config(text=f"QQ查询失败: {data_qq['message']}")

    except Exception as e:
        phone_result_label.config(text=f"QQ查询出错: {str(e)}")

def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)

root = tk.Tk()
root.title("信息查询")
root.geometry("600x400")
root.configure(background="#ECECEC")  # 设置背景颜色为微信的背景色

# 创建样式
style = ttk.Style()
style.configure("Custom.TButton", foreground="white", background="#07C160", font=("Arial", 12, "bold"))  # 设置按钮样式为微信绿色

# 创建顶层框架
top_frame = ttk.Frame(root)
top_frame.pack(pady=10)

# 信息查询标题
title_label = ttk.Label(top_frame, text="信息查询", font=("Arial", 24, "bold"))
title_label.pack()

# 查询LOL信息部分
lol_frame = ttk.LabelFrame(root, text="查询LOL信息")
lol_frame.pack(pady=10, padx=10)

lol_label = ttk.Label(lol_frame, text="请输入LOL昵称：")
lol_label.grid(row=0, column=0, padx=5, pady=5)

lol_entry = ttk.Entry(lol_frame, width=30)
lol_entry.grid(row=0, column=1, padx=5, pady=5)

query_button = ttk.Button(lol_frame, text="查询LOL信息", style="Custom.TButton", command=query_info)
query_button.grid(row=1, column=0, columnspan=2, pady=10)

qq_result_label = ttk.Label(lol_frame, text="")
qq_result_label.grid(row=2, column=0, columnspan=2, pady=10)

copy_qq_button = ttk.Button(lol_frame, text="复制QQ号", style="Custom.TButton", command=lambda: copy_to_clipboard(phone_number))
copy_qq_button.grid(row=3, column=0, columnspan=2, pady=5)

phone_label = ttk.Label(lol_frame, text="")
phone_label.grid(row=4, column=0, columnspan=2, pady=10)

copy_phone_button = ttk.Button(lol_frame, text="复制手机号", style="Custom.TButton", command=lambda: copy_to_clipboard(phone_number))
copy_phone_button.grid(row=5, column=0, columnspan=2, pady=5)

# 查询手机号码部分
phone_frame = ttk.LabelFrame(root, text="查询手机号码")
phone_frame.pack(pady=10, padx=10)

qq_label = ttk.Label(phone_frame, text="请输入QQ号码：")
qq_label.grid(row=0, column=0, padx=5, pady=5)

qq_entry = ttk.Entry(phone_frame, width=30)
qq_entry.grid(row=0, column=1, padx=5, pady=5)

query_phone_button = ttk.Button(phone_frame, text="查询手机号码", style="Custom.TButton", command=query_phone)
query_phone_button.grid(row=1, column=0, columnspan=2, pady=10)

phone_result_label = ttk.Label(phone_frame, text="")
phone_result_label.grid(row=2, column=0, columnspan=2, pady=10)

copy_phone_button_2 = ttk.Button(phone_frame, text="复制手机号", style="Custom.TButton", command=lambda: copy_to_clipboard(phone_number))
copy_phone_button_2.grid(row=3, column=0, columnspan=2, pady=5)

# 作者信息
author_label = ttk.Label(root, text="Powered by EKKOJQ", font=("Arial", 14))
author_label.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
