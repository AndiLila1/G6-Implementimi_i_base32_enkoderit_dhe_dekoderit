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

  ttk.Radiobutton(
            controls,
            text="Decode",
            value="decode",
            variable=self.mode,
        ).grid(row=0, column=1, padx=(0, 16), pady=4, sticky="w")

        ttk.Button(controls, text="Puno", command=self.process_text).grid(
            row=0, column=2, padx=(10, 8), pady=4
        )
        ttk.Button(controls, text="Pastro", command=self.clear_fields).grid(
            row=0, column=3, padx=8, pady=4
        )
        ttk.Button(controls, text="Kopjo rezultatin", command=self.copy_result).grid(
            row=0, column=4, padx=8, pady=4
        )

input_frame = ttk.LabelFrame(container, text="Hyrja", padding=14)
input_frame.pack(fill="both", expand=True, pady=(0, 12))

self.input_text = tk.Text(
    input_frame,
    wrap="word",
    height=10,
    font=("Consolas", 11),
    relief="solid",
    borderwidth=1,
)
self.input_text.pack(fill="both", expand=True)

output_frame = ttk.LabelFrame(container, text="Rezultati", padding=14)
output_frame.pack(fill="both", expand=True)

self.output_text = tk.Text(
    output_frame,
    wrap="word",
    height=10,
    font=("Consolas", 11),
    relief="solid",
    borderwidth=1,
    state="disabled",
)
self.output_text.pack(fill="both", expand=True)

footer = ttk.Label(
    container,
    text="Program i thjeshtë desktop me Python Tkinter.",
    font=("Segoe UI", 9),
)
footer.pack(anchor="e", pady=(10, 0))


def process_text(self) -> None:
    raw_text = self.input_text.get("1.0", "end").strip()
    if not raw_text:
        messagebox.showwarning("Mungon teksti", "Shkruaj tekst për ta përpunuar.")
        return

    try:
        if self.mode.get() == "encode":
            result = base64.b32encode(raw_text.encode("utf-8")).decode("ascii")
        else:
            normalized = raw_text.replace(" ", "").upper()
            decoded = base64.b32decode(normalized, casefold=True)
            result = decoded.decode("utf-8")
    except Exception as exc:
        messagebox.showerror("Gabim", f"Nuk u përpunua teksti:\n{exc}")
        return

    self._set_output(result)

