import json
from datetime import datetime, date
import tkinter as tk
from tkinter import filedialog, messagebox

# Store certificates
certificates = []

# Check status
def get_status(expiry_date):
    today = date.today()
    days = (expiry_date - today).days

    if days < 0:
        return "EXPIRED"
    elif days <= 30:
        return "EXPIRING SOON"
    else:
        return "SAFE"

# Load JSON (GUI)
def load_json_gui():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    
    if not file_path:
        return

    try:
        with open(file_path, "r") as f:
            data = json.load(f)

        certificates.clear()
        for cert in data:
            certificates.append(cert)

        messagebox.showinfo("Success", "Certificates loaded successfully!")

    except:
        messagebox.showerror("Error", "Failed to load file!")

# Show status (GUI)
def show_status_gui():
    if not certificates:
        messagebox.showwarning("Warning", "No certificates loaded!")
        return

    result = ""

    for cert in certificates:
        expiry_date = datetime.strptime(cert["expiry_date"], "%Y-%m-%d").date()
        status = get_status(expiry_date)

        result += f"{cert['domain']} → {status}\n"

    messagebox.showinfo("Certificate Status", result)

# GUI Window
def run_gui():
    root = tk.Tk()
    root.title("Certificate Monitor")
    root.geometry("400x200")

    tk.Label(root, text="Digital Certificate Monitor", font=("Arial", 14)).pack(pady=10)

    tk.Button(root, text="Load JSON File", command=load_json_gui, width=20).pack(pady=5)
    tk.Button(root, text="Check Certificate Status", command=show_status_gui, width=25).pack(pady=5)
    tk.Button(root, text="Exit", command=root.destroy, width=10).pack(pady=10)

    root.mainloop()

# Run GUI directly
if __name__ == "__main__":
    run_gui()