import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

# === Merge PDFs ===
def merge_pdfs():
    files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if not files:
        return
    merger = PdfMerger()
    for pdf in files:
        merger.append(pdf)
    out_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if out_file:
        merger.write(out_file)
        merger.close()
        messagebox.showinfo("Success", f"Merged PDF saved as:\n{out_file}")

# === Split PDF ===
def split_pdf():
    file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not file:
        return
    reader = PdfReader(file)
    total_pages = len(reader.pages)

    def do_split():
        try:
            start = int(start_entry.get()) - 1
            end = int(end_entry.get())
            if start < 0 or end > total_pages or start >= end:
                raise ValueError("Invalid page range")
            writer = PdfWriter()
            for i in range(start, end):
                writer.add_page(reader.pages[i])
            out_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if out_file:
                with open(out_file, "wb") as f:
                    writer.write(f)
                messagebox.showinfo("Success", f"Split PDF saved as:\n{out_file}")
            split_win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    split_win = tk.Toplevel(root)
    split_win.title("Split PDF")
    tk.Label(split_win, text=f"Total pages: {total_pages}").pack(pady=5)
    tk.Label(split_win, text="Start page:").pack()
    start_entry = tk.Entry(split_win)
    start_entry.pack()
    tk.Label(split_win, text="End page:").pack()
    end_entry = tk.Entry(split_win)
    end_entry.pack()
    tk.Button(split_win, text="Split", command=do_split).pack(pady=5)

# === GUI ===
root = tk.Tk()
root.title("PDF Tool (Basic)")

tk.Button(root, text="Merge PDFs", width=25, command=merge_pdfs).pack(pady=10)
tk.Button(root, text="Split PDF", width=25, command=split_pdf).pack(pady=10)

root.mainloop()
