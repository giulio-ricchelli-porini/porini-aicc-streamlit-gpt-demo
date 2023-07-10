import openai
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from lib.statics import PROMPT_TEMPLATE, ANALYZER_COLORS


class GPTReviewer:
    def __init__(self, cols, azure_openai_gpt_deployment):
        self.cols = cols
        self.engine = azure_openai_gpt_deployment

    def text_analysis(self, chat):
        prompt = PROMPT_TEMPLATE.format(chat=chat)

        completion = openai.Completion.create(
            engine=self.engine, prompt=prompt, temperature=0.7, max_tokens=1024, n=1, stop=["<|im_end|>", "<|im_start|>"]
        )
        response = completion.choices[0].text

        data = {}
        for line in response.split("\n"):
            key, value = line.split(": ")
            data[key] = [value]
        df = pd.DataFrame(columns=self.cols)
        for col in df.columns:
            try:
                df.loc[0, col] = data[col][0]
            except KeyError:
                df.loc[0, col] = None

        return df


class Analyzer:
    def __init__(self, df):
        self.df = df
        self.color = ANALYZER_COLORS[0]
        self.colors = ANALYZER_COLORS

    def process_data(self):
        self.df["User's Name"] = self.df["User's Name"].str.title()
        self.df["Type of flight"] = self.df["Type of flight"].str.title()
        self.df["Flight from"] = self.df["Flight from"].str.title()
        self.df["Flight to"] = self.df["Flight to"].str.title()
        self.df["Budget"] = self.df["Budget"].str.extract("(\d+)").astype(float)
        self.df = self.df.replace("None", np.nan)

    def word_cloud(self):
        wc_columns = ["Type of flight", "Flight from", "Flight to", "Class", "Animals"]
        df2 = self.df[wc_columns].fillna("")
        text = " ".join(df2.astype(str).values.flatten())
        plt.figure(figsize=(10, 4), facecolor="white")
        wordcloud = WordCloud(background_color="white").generate(text)
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        return plt.gca().get_figure()

    def flights_by_departure(self):
        departure_count = self.df["Flight from"].value_counts()
        plt.figure(figsize=(6, 5))
        sns.set_style("whitegrid")
        sns.barplot(x=departure_count.values, y=departure_count.index, color=self.color)
        plt.title("Count of Flights by Departure City", fontsize=17)
        plt.xlabel("Count", fontsize=16)
        plt.ylabel("City", fontsize=16)
        plt.xticks(range(0, max(departure_count.values) + 1, 1), fontsize=16)
        plt.yticks(fontsize=16)
        return plt.gca().get_figure()

    def flights_by_destination(self):
        destination_count = self.df["Flight to"].value_counts()
        plt.figure(figsize=(6, 5))
        sns.set_style("whitegrid")
        sns.barplot(x=destination_count.values, y=destination_count.index, color=self.color)
        plt.title("Count of Flights by Destination City", fontsize=17)
        plt.xlabel("Count", fontsize=16)
        plt.ylabel("City", fontsize=16)
        plt.xticks(range(0, max(destination_count.values) + 1, 1), fontsize=16)
        plt.yticks(fontsize=16)
        return plt.gca().get_figure()

    def animals_types(self):
        animal_count = self.df["Animals"].value_counts()
        plt.figure(figsize=(5, 2))
        sns.set_style("whitegrid")
        sns.barplot(x=animal_count.values, y=animal_count.index, color=self.color, orient="horizontal")
        plt.title("Flights with Animals", fontsize=12)
        plt.xlabel("Count", fontsize=11)
        plt.ylabel("Animals", fontsize=11)
        plt.xticks(range(0, max(animal_count.values) + 1, 1), fontsize=11)
        plt.yticks(fontsize=11)
        return plt.gca().get_figure()

    def pie_with_animals(self):
        flights_with_animals = len(self.df["Animals"]) - self.df["Animals"].isna().sum()
        flights_without_animals = self.df["Animals"].isna().sum()
        proportions = [flights_with_animals, flights_without_animals]
        cols = self.colors[: len(proportions)]

        plt.figure(figsize=(5, 2), facecolor="white")
        sns.set_palette("pastel")
        sns.set_style("whitegrid")
        plt.pie(
            proportions,
            labels=["With animals", "Without animals"],
            colors=cols,
            autopct="%1.1f%%",
            textprops={"fontsize": 8, "color": "black", "bbox": {"facecolor": "white"}},
        )
        plt.title("Proportion of Flights with/without Animals", fontsize=9)
        legend = plt.legend(
            title="Animals",
            labels=["With animals", "Without animals"],
            loc="upper left",
            bbox_to_anchor=(1, 0.5),
            framealpha=0.2,
            title_fontsize=8,
            fontsize=8,
        )
        legend.get_frame().set_facecolor("grey")
        return plt.gca().get_figure()

    def plot_2_figures(self):
        fig, axs = plt.subplots(1, 2, figsize=(12, 4), gridspec_kw={"width_ratios": [1, 1]})

        departure_dates = pd.to_datetime(self.df["Departure date"].dropna(), format="%d/%m/%Y")
        sns.set_style("ticks")
        departure_ax = axs[0]
        departure_ax.hist(departure_dates, color=self.color, alpha=1)
        departure_ax.axvline(x=departure_dates.mean(), color="red", linestyle="--")
        departure_ax.set_title("Distribution of Departure Dates", fontsize=15)
        departure_ax.set_xlabel("Departure Date", fontsize=14)
        departure_ax.set_ylabel("Count", fontsize=14)
        yticks = np.arange(0, departure_ax.get_ylim()[1], 1)
        departure_ax.set_yticks(yticks)
        departure_ax.tick_params(axis="x", labelsize=14, rotation=45)
        departure_ax.tick_params(axis="y", labelsize=14)
        departure_kde_ax = departure_ax.twinx()
        sns.kdeplot(departure_dates, color="#96c01e", ax=departure_kde_ax, lw=2)
        departure_kde_ax.set_ylabel("Density", fontsize=14)
        departure_kde_ax.set_yticks([])
        departure_kde_ax.tick_params(axis="y", labelsize=14)

        return_dates = pd.to_datetime(self.df["Return date"].dropna(), format="%d/%m/%Y")
        sns.set_style("ticks")
        return_ax = axs[1]
        return_ax.hist(return_dates, color=self.color, alpha=0.8)
        return_ax.axvline(x=return_dates.mean(), color="red", linestyle="--")
        return_ax.set_title("Distribution of Departure Dates", fontsize=15)
        return_ax.set_xlabel("Departure Date", fontsize=14)
        return_ax.set_ylabel("Count", fontsize=14)
        yticks = np.arange(0, return_ax.get_ylim()[1], 1)
        return_ax.set_yticks(yticks)
        return_ax.tick_params(axis="x", labelsize=14, rotation=45)
        return_ax.tick_params(axis="y", labelsize=14)
        return_kde_ax = return_ax.twinx()
        sns.kdeplot(return_dates, color="#96c01e", ax=return_kde_ax, lw=2)
        return_kde_ax.set_ylabel("Density", fontsize=14)
        return_kde_ax.set_yticks([])
        return_kde_ax.tick_params(axis="y", labelsize=14)
        fig.tight_layout()
        return fig

    def popular_cities(self):
        cities = pd.concat([self.df["Flight from"], self.df["Flight to"]])
        city_counts = cities.value_counts()
        top_cities = city_counts[:10]

        plt.figure(figsize=(6, 3))
        sns.set_style("whitegrid")
        sns.barplot(x=top_cities.values, y=top_cities.index, color=self.color)
        plt.title("Top 10 Most Popular Departure and Arrival Cities", fontsize=15)
        plt.xlabel("Number of Flights", fontsize=14)
        plt.ylabel("City", fontsize=14)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        return plt.gca().get_figure()
