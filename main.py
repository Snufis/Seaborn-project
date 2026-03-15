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



plt.figure(figsize=(8,6))

#Matematyka vs Czytanie (podzial wg płci)
sns.scatterplot(
    data=df,
    x="math_score",
    y="reading_score",
    hue="gender",
    palette={
            "male":"#4C72B0",
            "female":"#F39112"
            }
)

plt.title("Matematyka vs Czytanie(gender)")
plt.xlabel("Wynik z matematyki")
plt.ylabel("Wynik z czytania")
plt.tight_layout()
plt.savefig("charts/03-scatter-math-reading.png")
plt.show()

plt.figure(figsize=(16,6))

#wynik przez płeć boxploty
plt.subplot(1,3,1)
sns.boxplot(data=df, x="gender", y="math_score")
plt.title("Matematyka")

plt.subplot(1,3,2)
sns.boxplot(data=df, x="gender", y="reading_score")
plt.title("Czytanie")

plt.subplot(1,3,3)
sns.boxplot(data=df, x="gender", y="writing_score")
plt.title("Pisanie")

plt.tight_layout()
plt.savefig("charts/04-boxplot-gender.png")
plt.show()


plt.figure(figsize=(7,5))

#wpływ kursu przygotow.
sns.barplot(
    data=df,
    x="test_preparation_course",
    y="math_score",
    palette="Set2"
)
plt.title("Wpływ kursu przygotowawczego na wynik z matematyki")
plt.xlabel("Kurs przygotowawczy")
plt.ylabel("Średni wynik")

plt.tight_layout()
plt.savefig("charts/05-barplot-test-prep.png")
plt.show()

### LATER
sns.heatmap(df[["math_score","reading_score","writing_score"]].corr(), annot=True)
plt.show()

sns.violinplot(data=df, x="gender", y="math_score")
plt.show()

sns.pairplot(df, hue="gender")
plt.show()