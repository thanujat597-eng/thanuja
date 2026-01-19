import tkinter as tk
from tkinter import ttk, messagebox

# ---------- DATA ----------
cities = ["Coimbatore", "Chennai", "Bangalore", "Madurai", "Ooty"]

transport_options = [
    ("Electric Train", "5h 30m", "Low", "★★★★★"),
    ("E-Bus", "7h 00m", "Medium", "★★★★"),
    ("Petrol Car", "6h 15m", "High", "★★"),
    ("Flight", "1h 00m", "Very High", "★")
]

# ---------- MAIN WINDOW ----------
app = tk.Tk()
app.title("🌿 Eco-Travel AI")
app.geometry("400x500")

# ---------- PAGE 1 ----------
tk.Label(app, text="Eco-Friendly Travel", font=("Arial", 18, "bold")).pack(pady=20)

tk.Label(app, text="From").pack()
from_city = ttk.Combobox(app, values=cities)
from_city.set("Coimbatore")
from_city.pack()

tk.Label(app, text="To").pack(pady=10)
to_city = ttk.Combobox(app, values=cities)
to_city.set("Chennai")
to_city.pack()

# ---------- NEXT PAGE ----------
def show_transport():
    if from_city.get() == to_city.get():
        messagebox.showerror("Error", "From and To cannot be same")
        return

    transport_window = tk.Toplevel(app)
    transport_window.title("Choose Transport")
    transport_window.geometry("450x400")

    tk.Label(
        transport_window,
        text=f"{from_city.get()} ➜ {to_city.get()}",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    for mode, time, carbon, rating in transport_options:
        btn = tk.Button(
            transport_window,
            text=f"{mode}\nTime: {time} | Carbon: {carbon}\nRating: {rating}",
            width=50,
            height=3,
            command=lambda m=mode: show_summary(m)
        )
        btn.pack(pady=5)

def show_summary(mode):
    messagebox.showinfo(
        "Trip Summary",
        f"Selected Mode: {mode}\nEco-friendly travel helps reduce carbon footprint 🌱"
    )

tk.Button(app, text="Next: Choose Transport", bg="green", fg="white",
          command=show_transport).pack(pady=30)

app.mainloop()
