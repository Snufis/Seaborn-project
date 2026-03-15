import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("StudentsPerformanceKeggle.csv")

df.columns = df.columns.str.replace(" ", "_").str.replace("/", "_")

df['avg_score'] = df[['math_score', 'reading_score', 'writing_score']].mean(axis=1)


plt.figure(figsize=(16, 5))

#matma
plt.subplot(1, 3, 1)
sns.histplot(df["math_score"], kde=True, color="#4C72B0", bins=20)
plt.title("Matematyka")

#czytanie
plt.subplot(1, 3, 2)
sns.histplot(df["reading_score"], kde=True, color="#F39112", bins=20)
plt.title("Czytanie")

#pisanie
plt.subplot(1, 3, 3)
sns.histplot(df["writing_score"], kde=True, color="#55A868", bins=20)
plt.title("Pisanie")

plt.tight_layout()
plt.savefig("charts/01-dystrybucja-wynikow.png")
plt.show()


plt.figure(figsize=(9, 5))

#matma
sns.kdeplot(df["math_score"], label="Matematyka", color="#4C72B0")
#czytanie
sns.kdeplot(df["reading_score"], label="Czytanie", color="#F39112")
#pisanie
sns.kdeplot(df["writing_score"], label="Pisanie", color="#55A868")

plt.legend()
plt.title("Porownanie rozkładów wynikow")
plt.tight_layout()
plt.savefig("charts/02-kde-porownanie.png")
plt.show()