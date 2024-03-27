import pandas as pd
import spacy
import ast
import csv
import matplotlib.pyplot as plt
from pathlib import Path

def clean_and_extract_adjectives(csv_path):
    nlp = spacy.load("en_core_web_trf")
    df = pd.read_csv(csv_path)
    text = df["Speech"].astype(str)
    adjectives = []

    for strings in text:
        doc = nlp(strings)
        adj_list = [token.text for token in doc if token.pos_ == "ADJ"]
        adjectives.append(adj_list if adj_list else pd.NA)

    df["Adjectives_Spacy"] = adjectives
    return df

def plot_adjective_frequency(df, column_name="Adjectives_Spacy"):
    all_adjs = sum(df[column_name].dropna().tolist(), [])
    adj_freq = pd.Series(all_adjs).value_counts()

    top_n = 10
    adj_freq.head(top_n).plot(kind="bar", color="skyblue", figsize=(10, 6))
    plt.title(f"Top {top_n} Most Frequent Adjectives")
    plt.xlabel("Adjective")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    dir = Path.cwd()
    social_csv_path = dir.parent / "Data" / "Master Children Description Data - Master Social description.csv"
    
    social_df = clean_and_extract_adjectives(social_csv_path)
    plot_adjective_frequency(social_df)

if __name__ == "__main__":
    main()

