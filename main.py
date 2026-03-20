import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

sns.set_style("whitegrid")
sns.set_context("notebook")

df = pd.read_csv("StudentsPerformanceKeggle.csv")

df.columns = df.columns.str.replace(" ", "_").str.replace("/", "_")

df['avg_score'] = df[['math_score', 'reading_score', 'writing_score']].mean(axis=1)


plt.figure(figsize=(16, 5))

#matma
plt.subplot(1, 3, 1)
sns.histplot(df["math_score"], kde=True, color="#4C72B0", bins=20)
plt.title("Matematyka")
plt.xlabel("Wynik")
plt.ylabel("Liczba uczniów")

#czytanie
plt.subplot(1, 3, 2)
sns.histplot(df["reading_score"], kde=True, color="#F39112", bins=20)
plt.title("Czytanie")
plt.xlabel("Wynik")
plt.ylabel("Liczba uczniów")

#pisanie
plt.subplot(1, 3, 3)
sns.histplot(df["writing_score"], kde=True, color="#55A868", bins=20)
plt.title("Pisanie")
plt.xlabel("Wynik")
plt.ylabel("Liczba uczniów")

plt.tight_layout()
plt.savefig("charts/01-dystrybucja-wynikow.png")
plt.show()


plt.figure(figsize=(9, 5))

sns.kdeplot(df["math_score"], label="Matematyka", color="#003385")
sns.kdeplot(df["reading_score"], label="Czytanie", color="#AD6200")
sns.kdeplot(df["writing_score"], label="Pisanie", color="#00851F")

plt.legend()
plt.title("Porownanie rozkładów wynikow")
plt.xlabel("Wynik")
plt.ylabel("Gęstość")
plt.tight_layout()
plt.savefig("charts/02-kde-porownanie.png")
plt.show()


plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=df,
    x="math_score",
    y="reading_score",
    hue="gender",
    palette={
        "male": "#4C72B0",
        "female": "#F39112"
    }
)

plt.title("Matematyka vs Czytanie (gender)")
plt.xlabel("Wynik z matematyki")
plt.ylabel("Wynik z czytania")
plt.tight_layout()
plt.savefig("charts/03-scatter-math-reading.png")
plt.show()


plt.figure(figsize=(16, 6))

plt.subplot(1, 3, 1)
sns.boxplot(data=df, x="gender", y="math_score")
plt.title("Matematyka")

plt.subplot(1, 3, 2)
sns.boxplot(data=df, x="gender", y="reading_score")
plt.title("Czytanie")

plt.subplot(1, 3, 3)
sns.boxplot(data=df, x="gender", y="writing_score")
plt.title("Pisanie")

plt.tight_layout()
plt.savefig("charts/04-boxplot-gender.png")
plt.show()


plt.figure(figsize=(7, 5))

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


corr = df[["math_score", "reading_score", "writing_score"]].corr()

plt.figure(figsize=(6, 5))
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Korelacje między wynikami")
plt.tight_layout()
plt.savefig("charts/06-heatmap.png")
plt.show()


plt.figure(figsize=(7, 5))
sns.violinplot(data=df, x="gender", y="math_score")
plt.title("Rozkład wyników z matematyki (gender)")
plt.tight_layout()
plt.savefig("charts/07-violin.png")
plt.show()


sns.pairplot(df, hue="gender")
plt.savefig("charts/08-pairplot.png")
plt.show()


sns.lmplot(
    data=df,
    x="math_score",
    y="reading_score",
    hue="gender",
    height=6,
    aspect=1.2
)

plt.title("matematyka vs czytanie(regresja)")
plt.tight_layout()
plt.savefig("charts/09-lmplot.png")
plt.show()