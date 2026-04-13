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

        def _build_ui(self) -> None:
            container = ttk.Frame(self.root, padding=20)
            container.pack(fill="both", expand=True)

            title = ttk.Label(
                container,
                text="Base32 Encoder / Decoder",
                font=("Segoe UI", 20, "bold"),
            )
            title.pack(anchor="center", pady=(0, 8))

            subtitle = ttk.Label(
                container,
                text="Shkruaj tekstin dhe zgjidh Encode ose Decode.",
                font=("Segoe UI", 10),
            )
            subtitle.pack(anchor="center", pady=(0, 18))

            controls = ttk.LabelFrame(container, text="Veprimet", padding=14)
            controls.pack(fill="x", pady=(0, 14))

            ttk.Radiobutton(
                controls,
                text="Encode",
                value="encode",
                variable=self.mode,
            ).grid(row=0, column=0, padx=(0, 16), pady=4, sticky="w")



