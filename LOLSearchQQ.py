import tkinter as tk
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

def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)

root = tk.Tk()
root.title("信息查询")
root.geometry("600x600")  # 修改窗口大小

title_label = tk.Label(root, text="LOL信息查询", font=("Arial", 24, "bold"))  # 调整标题字体大小
title_label.pack(pady=10)

lol_label = tk.Label(root, text="请输入LOL昵称：", font=("Arial", 16))  # 调整标签字体大小
lol_label.pack()

lol_entry = tk.Entry(root, font=("Arial", 16), width=30)  # 调整输入框字体大小
lol_entry.pack(pady=5)

query_button = tk.Button(root, text="查询", font=("Arial", 16), command=query_info)  # 调整按钮字体大小
query_button.pack(pady=10)

qq_result_label = tk.Label(root, text="", font=("Arial", 16))  # 调整结果显示字体大小
qq_result_label.pack(pady=10)

copy_qq_button = tk.Button(root, text="复制QQ号", font=("Arial", 16))  # 调整按钮字体大小
copy_qq_button.pack(pady=5)

phone_label = tk.Label(root, text="", font=("Arial", 16))  # 调整结果显示字体大小
phone_label.pack(pady=10)

copy_phone_button = tk.Button(root, text="复制手机号", font=("Arial", 16))  # 调整按钮字体大小
copy_phone_button.pack(pady=5)

author_label = tk.Label(root, text="Powered by EKKOJQ", font=("Arial", 14))  # 调整作者信息字体大小
author_label.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
