import json
import os
import sqlite3
import sys
from tkinter import *
from tkinter import messagebox

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True
import pyperclip


def reload_data():
    sql = 'select * from history_msg'
    conn = sqlite3.connect(os.path.join(os.path.dirname(sys.argv[0]), "kafka_info.db"))
    cursor = conn.cursor()


def rightKey(event, tree):
    item = tree.selection()
    selection_value = tree.item(item[0], "values")
    data = {
        'topic': selection_value[0],
        'partition': selection_value[1],
        'offset': selection_value[2],
        'timestamp': selection_value[3],
        'timestamp_type': selection_value[4],
        'value': selection_value[5]
    }
    pyperclip.copy(json.dumps(data))
    messagebox.showinfo("成功", "内容已经成功复制到剪切板～")


def dict_factory(cursor, row):
    # 将游标获取的数据处理成字典返回
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class HistoryMsgFrame(object):
    def __init__(self, key):
        self.key = key
        self.root = Toplevel()
        self.root.title(self.key + ' 历史消息')
        self.center_window(self.root, 720, 290)  # 设置窗口大小
        self.creat_page()  # 创建页面

    def center_window(self, root, w, h):
        """
        窗口居于屏幕中央
        :param root: root
        :param w: 窗口宽度
        :param h: 窗口高度
        :return:
        """
        # 获取屏幕 宽、高
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()

        # 计算 x, y 位置
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def creat_page(self):

        self.frame = Frame(self.root)
        self.tree = ttk.Treeview(self.frame, columns=['1', '2', '3', '4', '5', '6'], show='headings')

        self.tree.column('1', width=100, anchor='center')
        self.tree.column('2', width=100, anchor='center')
        self.tree.column('3', width=100, anchor='center')
        self.tree.column('4', width=100, anchor='center')
        self.tree.column('5', width=100, anchor='center')
        self.tree.column('6', width=200, anchor='center')
        self.tree.heading('1', text='topic')
        self.tree.heading('2', text='partition')
        self.tree.heading('3', text='offset')
        self.tree.heading('4', text='timestamp')
        self.tree.heading('5', text='timestamp_type')
        self.tree.heading('6', text='value')
        # 加载数据
        # reload_tree_data(self.tree)
        self.tree.grid()

        # ----vertical scrollbar------------
        vbar = ttk.Scrollbar(self.frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=vbar.set)
        # self.tree.grid(row=0, column=0, sticky=N)
        # vbar.grid(row=0, column=1, sticky=NS)
        self.tree.pack(fill=BOTH, side=LEFT, expand=1)
        vbar.pack(fill=Y, side=LEFT)
        self.frame.pack(fill=BOTH, expand=1)
        sql = "select * from history_msg where col_key = '%s'" % self.key
        conn = sqlite3.connect(os.path.join(os.path.dirname(sys.argv[0]), "kafka_info.db"))
        conn.row_factory = dict_factory
        cursor = conn.cursor()
        cursor.execute(sql)
        values = cursor.fetchall()
        data = []
        for value in values:
            # 'col_key','topic','partition','offset','timestamp_str','timestamp_type','value'
            data.append([value['topic'], value['partition'], value['offset'], value['timestamp_str'], value['timestamp_type'], value['value']])
        for item in data:
            tu = []
            for it in item:
                if it is not None:
                    tu.append(it)
            self.tree.insert('', 'end', values=tu)
        # self.frame.bind("<Button-3>", )
        self.tree.bind('<Double-1>', lambda event: rightKey(event, self.tree))  # 表格绑定左键双击事件
        self.root.mainloop()  # 显示子页面
