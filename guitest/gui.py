import os, sys, shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


CONVERT_TYPE = ["---select---","PotPlayer", "Galaxy", "Steam"]


# フォルダ指定の関数
def dirdialog_click(entry):
    # 入力値がない場合、現在フォルダを初期ディレクトリに設定
    iDir = os.path.abspath(os.path.dirname(__file__)) if entry.get() == "" else entry.get()
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    # OKが押された場合パスを返す(キャンセルは変更なし)
    if iDirPath:
        entry.set(iDirPath)


def launch(**kwargs):
    class Args():
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
            self.type = CONVERT_TYPE.index(self.type)

    args = Args(**kwargs)

    try:
        import rename_screenshots_gui
        rename_screenshots_gui.main(args)
        from tkinter import messagebox
        messagebox.showinfo("Success", "Success")
    except Exception as e:
        from tkinter import messagebox
        messagebox.showerror("Error", str(e))

# use tk to get the directory
root = tk.Tk()
root.title("test")

# Frame1の作成
frame1 = ttk.Frame(root, padding=10)
frame1.grid(row=0, column=0, columnspan=2)

# 「フォルダ参照」ラベルの作成
label1 = ttk.Label(frame1, text="フォルダ参照")
label1.pack(anchor=tk.NW)

# 「フォルダ参照」エントリーの作成
path_entry = tk.StringVar()
IDirEntry = ttk.Entry(frame1, textvariable=path_entry, width=50)
IDirEntry.pack(side=tk.LEFT)

# 「フォルダ参照」ボタンの作成
IDirButton = ttk.Button(frame1, text="参照", command=lambda: dirdialog_click(path_entry))
IDirButton.pack(side=tk.LEFT)

# Frame2の作成
frame2 = ttk.Frame(root, padding=10)
frame2.grid(row=1, column=0, columnspan=2)

# 「出力フォルダ」ラベルの作成
label2 = ttk.Label(frame2, text="出力フォルダ")
label2.pack(anchor=tk.NW)

# 「出力フォルダ」エントリーの作成
outdir_entry = tk.StringVar()
IDirEntry = ttk.Entry(frame2, textvariable=outdir_entry, width=50)
IDirEntry.pack(side=tk.LEFT)

# 「出力フォルダ」ボタンの作成
IDirButton = ttk.Button(frame2, text="参照", command=lambda: dirdialog_click(outdir_entry))
IDirButton.pack(side=tk.LEFT)

# Frame3の作成
frame3 = ttk.Frame(root, padding=10)
frame3.grid(row=2, column=0, sticky=tk.W)

# create choicebox
label3 = ttk.Label(frame3, text="変換元")
label3.pack(anchor=tk.NW)
choicebox = ttk.Combobox(frame3,
                            values=CONVERT_TYPE,
                            state="readonly",
                            width=20)
choicebox.current(0)
choicebox.pack(side=tk.LEFT)

# Frame4の作成
frame4 = ttk.Frame(root, padding=10)
frame4.grid(row=2, column=1, sticky=tk.W)

# create prefix entry
label4 = ttk.Label(frame4, text="Prefix")
label4.pack(anchor=tk.NW)
prefix_entry = tk.StringVar()
prefixEntry = ttk.Entry(frame4, textvariable=prefix_entry, width=20)
prefixEntry.pack(anchor=tk.NW)

# Frame5の作成
frame5 = ttk.Frame(root, padding=10)
frame5.grid(row=3, column=0, columnspan=2, sticky=tk.E)

# create launch button
printButton = ttk.Button(frame5, text="実行", command=lambda: launch(path=path_entry.get(),
                                                                    outdir=outdir_entry.get(),
                                                                    prefix=prefix_entry.get(),
                                                                    type=choicebox.get()))
printButton.pack(side=tk.LEFT)

# 終了ボタンの作成
endButton = ttk.Button(frame5, text="終了", command=exit)
endButton.pack(side=tk.LEFT)

root.mainloop()
