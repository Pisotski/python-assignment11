# %%
# Load dataset
import plotly.data as pldata
import plotly.express as px

df = pldata.wind()


# Convert 'strength' column to numeric representation
def convert_strength(s):
    if "+" in s:
        return float(s.replace("+", "")) + 0.5
    else:
        s = s.replace("-", "+")
        avg = eval(s) / 2
        return avg


df["strength"] = df["strength"].apply(convert_strength)
df["strength"] = df["strength"].astype("float")

print(df.head())

# %% # Returns a DataFrame.  plotly.data has a number of sample datasets included.
fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Strength vs. Frequency",
    hover_data=["strength", "frequency", "direction"],
)
fig.write_html("wind.html", auto_open=True)

# %%
