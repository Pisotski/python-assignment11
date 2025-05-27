# %% assgn11

import os
import sqlite3

import pandas as pd
import matplotlib.pyplot as plt

current_path = os.path.abspath(__file__)
root_path = current_path[
    : current_path.index("python_homework") + len("python_homework")
]
db_path = os.path.join(root_path, "db", "lesson.db")

with sqlite3.connect(db_path) as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    print("Database created and connected successfully.")

cursor = conn.cursor()


def load_employees(cursor):
    cursor.execute(
        """
SELECT last_name, SUM(price * quantity) AS revenue FROM employees e JOIN orders o ON e.employee_id = o.employee_id JOIN line_items l ON o.order_id = l.order_id JOIN products p ON l.product_id = p.product_id GROUP BY e.employee_id;"""
    )
    rows = cursor.fetchall()
    df = pd.DataFrame(rows)
    return df


# %% task1
sales = load_employees(cursor)

pd_plot = sales.plot.bar(x=0, y=1, rot=90)
plt.title("Revenue by Employee")
plt.xlabel("Last Name")
plt.ylabel("Revenue")
plt.show()

# %%
