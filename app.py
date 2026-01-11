import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2
import pandas as pd
from analytics import barplot_branch_compare, barplot_gender_compare

# ===== Подключение к базе =====

conn = psycopg2.connect(
    host="localhost",
    database="postgres", 
    user="postgres",
    password="1234",
    port=5432
)
cur = conn.cursor()

# ===== Главное окно =====

class Mannning_Table:
    def __init__(self, root):
        self.root = root
        self.root.title("Штатная книга")
        root.geometry("1100x800")
root = tk.Tk()

# ===== Поля ввода =====
form_frame = ttk.Frame(root)
form_frame.pack(side="left", anchor="nw", padx=20, pady=20)

ttk.Label(form_frame, text="Должность:").pack(anchor='nw')
name_entry = ttk.Entry(root)
name_entry.pack(anchor='nw',padx=10)


ttk.Label(form_frame, text="ФИО:").pack(anchor='nw')
age_entry = ttk.Entry(root)
age_entry.pack(anchor='nw',padx=10)


ttk.Label(form_frame, text="Пол:").pack(anchor='nw')
age_entry = ttk.Entry(root)
age_entry.pack(anchor='nw',padx=10)


ttk.Label(form_frame, text="Оклад:").pack(anchor='nw')
age_entry = ttk.Entry(root)
age_entry.pack(anchor='nw',padx=10)


ttk.Label(form_frame, text="%квартальной премии:").pack(anchor='nw')
age_entry = ttk.Entry(root)
age_entry.pack(anchor='nw',padx=10)


ttk.Label(form_frame, text="%годовой премии:").pack(anchor='nw')
age_entry = ttk.Entry(root)
age_entry.pack(anchor='nw',padx=10)


ttk.Label(form_frame, text="Годовой доход:").pack(anchor='nw')
age_entry = ttk.Entry(root)
age_entry.pack(anchor='nw',padx=10)


ttk.Label(form_frame, text="Среднемесячный доход:").pack(anchor='nw')
age_entry = ttk.Entry(root)
age_entry.pack(anchor='nw',padx=10)


ttk.Label(form_frame, text="Филиал:").pack(anchor='nw')
age_entry = ttk.Entry(root)
age_entry.pack(anchor='nw',padx=10)

# ===== Функции =====

def clear_fields():

    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)


def refresh_table():

    for row in table.get_children():
        table.delete(row)
    cur.execute("SELECT * FROM manning_table ORDER BY id")
    for row in cur.fetchall():
        table.insert("", "end", values=row)


def add_data():

    position= position_entry.get()
    name = name_entry.get()
    sex = sex_entry.get()
    salary= salary_entry.get()
    perc_qua_bonus= perc_qua_bonus.get()   
    perc_annnual_bonus= perc_annnual_bonus.get() 
    annual_salary= annual_salary.get() 
    monthly_aver_salary= monthly_aver_salary.get() 
    branch= branch.get() 

    if position == "" or salary == "":
        messagebox.showwarning("Ошибка", "Пожалуйста, заполните все поля")
        return
    cur.execute("INSERT INTO manning_table (position,name,sex,salary,perc_qua_bonus,perc_annnual_bonus,annual_salary,monthly_aver_salary,branch) VALUES (%s, %s)", (position,name,sex,salary,perc_qua_bonus,perc_annnual_bonus,annual_salary,monthly_aver_salary,branch))
    conn.commit()
    refresh_table()
    clear_fields()


def update_data():
    
    selected = table.focus()
    if not selected:
        messagebox.showwarning("Ошибка", "Выберите строку для изменения")
        return
    position= position_entry.get()
    name = name_entry.get()
    sex = sex_entry.get()
    salary= salary_entry.get()
    perc_qua_bonus= perc_qua_bonus.get()   
    perc_annnual_bonus= perc_annnual_bonus.get() 
    annual_salary= annual_salary.get() 
    monthly_aver_salary= monthly_aver_salary.get() 
    branch= branch.get() 

    row_id = table.item(selected, "values")[0]
    cur.execute("UPDATE manning_table SET position=%s,name=%s,sex=%s,salary=%s,perc_qua_bonus=%s,perc_annnual_bonus=%s,annual_salary=%s,monthly_aver_salary=%s,branch=%s WHERE id=%s", (position,name,sex,salary,perc_qua_bonus,perc_annnual_bonus,annual_salary,monthly_aver_salary,branch, row_id))
    conn.commit()
    refresh_table()
    clear_fields()


def delete_data():

    selected = table.focus()
    if not selected:
        messagebox.showwarning("Ошибка", "Выберите строку для удаления")
        return
    row_id = table.item(selected, "values")[0]
    cur.execute("DELETE FROM manning_table WHERE id=%s", (row_id,))
    conn.commit()
    refresh_table()
    clear_fields()


def export_to_excel():

    cur.execute("SELECT * FROM manning_table ORDER BY id")
    rows = cur.fetchall()
    df = pd.DataFrame(rows, columns=["ID", "Должность", "Имя", "Пол", "Оклад", "%квартальной премии", "%годовой премии", "Годовой доход", "Среднемесячный доход", "Филиал"])
    df.to_excel("users.xlsx", index=False)
    messagebox.showinfo("Успех", "Данные успешно экспортированы в users.xlsx")


# ===== Кнопки =====
button_frame = ttk.Frame(root)
button_frame.pack(side="right", anchor="nw", padx=20, pady=20)

tk.Button(button_frame, text="Добавить", command=add_data, bg="lightgreen", fg="black").pack(anchor='ne', padx=16)
tk.Button(button_frame, text="Удалить", command=delete_data, bg="lightcoral", fg="black").pack(anchor='ne',padx=16, pady=5)
tk.Button(button_frame, text="Обновить", command=update_data, bg="lightblue", fg="black").pack(anchor='ne',padx=16, pady=5)
tk.Button(button_frame, text="Очистить поля", command=clear_fields).pack(anchor='ne',padx=16, pady=5)
tk.Button(button_frame, text="Экспорт в Excel", command=export_to_excel).pack(anchor='ne',padx=16, pady=5)
tk.Button(button_frame, text="Анализ дохода по полу", command=barplot_gender_compare).pack(anchor='ne',padx=16, pady=5)
tk.Button(button_frame, text="Анализ дохода по филиалам", command=barplot_branch_compare).pack(anchor='ne',padx=16, pady=5)


# ===== Таблица =====

table = ttk.Treeview(root, columns=("id", "position", "name", "sex","salary","perc_qua_bonus","perc_annnual_bonus","annual_salary","monthly_aver_salary","branch"), show="headings")

table.heading("id", text="ID")
table.heading("position", text="Должность")
table.heading("name", text="Имя")
table.heading("sex", text="Пол")
table.heading("salary", text="Оклад")
table.heading("perc_qua_bonus", text="%квартальной премии")
table.heading("perc_annnual_bonus", text="%годовой премии")
table.heading("annual_salary", text="Годовой доход")
table.heading("monthly_aver_salary", text="Среднемесячный доход")
table.heading("branch", text="Филиал")

table.pack(fill="both", expand=True, padx=10, pady=10)



# ===== Загрузка данных при старте =====

refresh_table()



# ===== Запуск окна =====

root.mainloop()