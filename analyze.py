import pandas as pd
import plotly.express as px

path = "data/sample/RC-lecciondecocina.csv"

df = pd.read_csv(path, index_col=0)

# transform values to string length

df = df.applymap(lambda x: len(x), na_action="ignore")

# plot

fig = px.imshow(df, labels=dict(x="Oración", y="Párrafo", color="Extensión"))
fig.show()
