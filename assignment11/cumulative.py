# %% Task 2: A Line Plot with Pandas
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

# %% Task 1: A Line Plot with Pandas

cursor = conn.cursor()


def total_item_price(cursor):

    cursor.execute(
        """
            SELECT o.order_id, 
                SUM(li.quantity * p.price) AS total_price
            FROM orders AS o
            JOIN line_items AS li ON o.order_id = li.order_id
            JOIN products AS p ON li.product_id = p.product_id
            GROUP BY o.order_id; 
        """
    )
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=["order_id", "total_price"])

    # def cumulative(row):
    #     totals_above = df["total_price"][0 : row.name + 1]
    #     return totals_above.sum()

    # df["cumulative"] = df.apply(cumulative, axis=1)
    # df.plot.line()
    # return df
    df["cumulative"] = df["total_price"].cumsum()
    df.plot(x="order_id", y="cumulative", kind="line", marker="o")
    plt.title("Cumulative Revenue by Order")
    plt.xlabel("Order ID")
    plt.ylabel("Cumulative Revenue")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


total_item_price(cursor)


# %%
