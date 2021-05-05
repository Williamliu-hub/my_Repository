from tkinter import *
from tkinter import ttk
import requests
import json
'''
'''
class Application(Tk):
    def __init__(self):
        super().__init__()

        self.title('翻译')
        self.geometry('540x380')
        self.resizable(False, False)
        self.init_widgets()

    def init_widgets(self):
        trans_type1List = ["自动检测", "中文", "英文"]
        trans_type2List = ["中文", "英文"]

        label1 = Label(self, text='翻译成——>', font=('微软雅黑', 14))
        label1.place(x=168, y=8, width=120, height=33)

        trans_button = Button(self, text='翻译', command=self.translate_text)
        trans_button.place(x=450, y=8, width=70, height=33)

        self.type_dict = {
            "自动检测": "auto-detect",
            "中文": "zh-Hans",
            "英文": "en"
        }

        self.trans_type1 = ttk.Combobox(self, values=trans_type1List, font=('微软雅黑', 14))
        self.trans_type1.current(0)
        self.trans_type1.bind("<Key>", lambda e: "break")
        self.trans_type1.place(x=16, y=8, width=130, height=33)

        self.trans_type2 = ttk.Combobox(self, values=trans_type2List, font=('微软雅黑', 14))
        self.trans_type2.current(1)
        self.trans_type2.place(x=310, y=8, width=130, height=33)

        self.origin_text = Text(self, font=('微软雅黑', 14))
        self.origin_text.insert("1.0", "原文")
        self.origin_text.place(x=0, y=56, width=540, height=150)

        self.trans_text = Text(self, font=('微软雅黑', 14))
        self.trans_text.insert("1.0", "翻译")
        self.trans_text.configure(state=DISABLED)
        self.trans_text.place(x=0, y=210, width=540, height=180)

    def translate_text(self):
        text = self.origin_text.get("1.0", "end")
        type1 = self.type_dict[self.trans_type1.get()]
        type2 = self.type_dict[self.trans_type2.get()]

        self.trans_text.configure(state=NORMAL)
        self.trans_text.delete("1.0", "end")
        self.trans_text.insert("1.0", self.translate(text, type1, type2))
        self.trans_text.configure(state=DISABLED)

    def translate(self, text, type1, type2):
        url = "https://cn.bing.com/ttranslatev3?isVertical=1&&IG=B82C0E46ED384A0FA9E24E5DBFE84EBF&IID=translator.5024.1"
        form_data = {
            "fromLang": f"{type1}",
            "text": f"{text}",
            "to": f"{type2}"
        }
        headers = {
            "user-agent": 'Mozilla/5.0 (Windows NT 10; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94412.3 Safari/537.36'
        }
        res = requests.post(url, data=form_data, headers=headers)
        content = json.loads(res.text)

        return content[0]["translations"][0]["text"]


if __name__ == '__main__':
    app = Application()
    app.mainloop()
