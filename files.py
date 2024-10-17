from tkinter.filedialog import askopenfilename, asksaveasfilename
from platform import system
from tkinter import Tk


def open_file_as(file_type: str | None = None) -> str:
    """Ask the user to select a file to open"""
    root = Tk()
    root.withdraw()
    root.focus_force()
    root.lift()
    if file_type is None or system() == "Darwin":
        file_path = askopenfilename(parent=root)
    else:
        file_types = {
            "image": [("Image file", "*.png;*.jpg;*.jpeg;*.ico;*.gif;*.bmp"), ("All files", "*")],
            "msave": [("Micdustry save file", "*.msav"), ("All files", "*")],
            None: [("All files", "*")]
        }[file_type]
        file_path = askopenfilename(parent=root, filetypes=file_types)
    root.update()

    return file_path if file_path else ""


def save_file_as(file_type: str | None = None) -> str:
    """Ask the user to select a file to save"""
    root = Tk()
    root.withdraw()
    root.focus_force()
    root.lift()
    if file_type is None or system() == "Darwin":
        file_path = asksaveasfilename(parent=root)
    else:
        file_types = {
            "image": [("Image file", "*.png;*.jpg;*.jpeg;*.ico;*.gif;*.bmp"), ("All files", "*")],
            "msave": [("Micdustry save file", "*.msav"), ("All files", "*")],
            None: [("All files", "*")]
        }[file_type]
        file_path = asksaveasfilename(parent=root, filetypes=file_types)
    root.update()
    return file_path if file_path else ""
