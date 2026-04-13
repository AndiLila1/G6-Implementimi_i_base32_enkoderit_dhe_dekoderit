import base64
import tkinter as tk
from tkinter import messagebox, ttk


class Base32App:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Base32 Encoder / Decoder")
        self.root.geometry("760x540")
        self.root.minsize(680, 480)
        self.root.configure(bg="#f4f7fb")

        self.mode = tk.StringVar(value="encode")

        self._build_ui()


