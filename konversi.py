import tkinter as tk
from tkinter import ttk, messagebox

def convert_length(value, from_unit, to_unit):
    length_units = { 
        'meter': 1,
        'kilometer': 1000,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'mile': 1609.34,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254,
    }
    return value * length_units[from_unit] / length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'kilogram': 1,
        'gram': 0.001,
        'milligram': 0.000001,
        'ton': 1000,
        'pound': 0.453592,
        'ounce': 0.0283495
    }
    return value * weight_units[from_unit] / weight_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return value + 273.15
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return value - 273.15
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        return (value - 273.15) * 9/5 + 32
    else:
        return value

def convert_volume(value, from_unit, to_unit):
    volume_units = {
        'liter': 1,
        'milliliter': 0.001,
        'cubic_meter': 1000,
        'cubic_centimeter': 0.001,
        'gallon': 3.78541,
        'pint': 0.473176,
        'quart': 0.946353
    }
    return value * volume_units[from_unit] / volume_units[to_unit]

def convert():
    try:
        value = float(entry_value.get())
    except ValueError:
        messagebox.showerror("Input Error", "Nilai harus berupa angka.")
        return

    unit_type = combo_type.get()
    from_unit = combo_from.get()
    to_unit = combo_to.get()

    if unit_type == "Panjang":
        result = convert_length(value, from_unit, to_unit)
    elif unit_type == "Berat":
        result = convert_weight(value, from_unit, to_unit)
    elif unit_type == "Suhu":
        result = convert_temperature(value, from_unit, to_unit)
    elif unit_type == "Volume":
        result = convert_volume(value, from_unit, to_unit)
    else:
        messagebox.showerror("Input Error", "Jenis konversi tidak valid.")
        return
    
    
    label_result.config(text=f"Result: {result:.4f} {to_unit}")

def update_units(*args):
    unit_type = combo_type.get()
    units = {
        'Panjang': ['meter', 'kilometer', 'centimeter', 'millimeter', 'mile', 'yard', 'foot', 'inch'],
        'Berat': ['kilogram', 'gram', 'milligram', 'ton', 'pound', 'ounce'],
        'Suhu': ['celsius', 'fahrenheit', 'kelvin'],
        'Volume': ['liter', 'milliliter', 'cubic_meter', 'cubic_centimeter', 'gallon', 'pint', 'quart']
    }
    combo_from['values'] = units.get(unit_type, [])
    combo_to['values'] = units.get(unit_type, [])

app = tk.Tk()
app.title("Aplikasi Konversi Satuan")


style = ttk.Style()
style.theme_use('clam')  
style.configure('TFrame', background='#e6f2ff')
style.configure('TLabel', background='#e6f2ff', font=('Arial', 12))
style.configure('TButton', background='#66b3ff', font=('Arial', 12))
style.configure('TCombobox', font=('Arial', 12))
style.configure('TEntry', font=('Arial', 12))

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Jenis Konversi:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
combo_type = ttk.Combobox(frame, values=["Panjang", "Berat", "Suhu", "Volume"], state="readonly")
combo_type.grid(row=0, column=1, padx=5, pady=5)
combo_type.bind("<<ComboboxSelected>>", update_units)

ttk.Label(frame, text="Nilai:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
entry_value = ttk.Entry(frame)
entry_value.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame, text="Dari:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
combo_from = ttk.Combobox(frame, state="readonly")
combo_from.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame, text="Ke:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
combo_to = ttk.Combobox(frame, state="readonly")
combo_to.grid(row=3, column=1, padx=5, pady=5)

button_convert = ttk.Button(frame, text="Konversi", command=convert)
button_convert.grid(row=4, column=0, columnspan=2, pady=10)

label_result = ttk.Label(frame, text="Result: ")
label_result.grid(row=5, column=0, columnspan=2, pady=10)

update_units()

app.mainloop()
