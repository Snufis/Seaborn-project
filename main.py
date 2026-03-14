import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("StudentsPerformanceKeggle.csv")


sns.histplot(data=df, x="math score", bins=30, legend= True, hue ='lunch',multiple="layer")
plt.savefig("charts/Relational Plots/histplot.png")


sns.lineplot(data=df, x="math score", y="reading score", hue="gender")
plt.savefig("charts/Relational Plots/lineplot.png")


sns.scatterplot(data=df, x="math score", y="writing score", hue="gender")
plt.savefig("charts/Relational Plots/scatterplot.png")


sns.relplot(data =df,x="math score", y = "writing score", kind="scatter")
plt.savefig("charts/Relational Plots/relplot.png")




plt.show()

