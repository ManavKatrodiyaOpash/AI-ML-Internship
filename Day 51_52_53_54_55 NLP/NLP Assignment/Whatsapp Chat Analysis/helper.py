import pandas as pd
from urlextract import URLExtract
from wordcloud import WordCloud
from collections import Counter
import emoji

extract = URLExtract()

# -------------------------------
# FETCH STATS
# -------------------------------

def fetch_stats(selected_user, df):

    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    # messages
    num_messages = df.shape[0]

    # words (faster method)
    words = " ".join(df["message"]).split()

    # media
    num_media_messages = df[df["message"] == "<Media omitted>\n"].shape[0]

    # links
    links = []
    for message in df["message"]:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)


# -------------------------------
# BUSY USERS
# -------------------------------

def most_busy_users(df):

    x = df["user"].value_counts().head()

    new_df = (
        df["user"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
        .reset_index()
    )

    new_df.columns = ["name", "percentage"]

    return x, new_df


# -------------------------------
# WORD CLOUD
# -------------------------------

def create_wordcloud(selected_user, df):

    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    temp = df[df["user"] != "group_notification"]
    temp = temp[temp["message"] != "<Media omitted>\n"]
    temp = temp.copy()

    with open("stop_hinglish.txt", "r", encoding="utf-8") as f:
        stop_words = set(f.read().split())

    remove_words = {
        "<this", "edited>", "message", "deleted",
        "this", "omitted", "group", "notification", "https"
    }

    def remove_stop_words(message):

        words = []

        for word in message.lower().split():

            if word not in stop_words and word not in remove_words:
                words.append(word)

        return " ".join(words)

    temp["message"] = temp["message"].apply(remove_stop_words)

    wc = WordCloud(
        width=800,
        height=400,
        min_font_size=10,
        background_color="white"
    )

    df_wc = wc.generate(temp["message"].str.cat(sep=" "))

    return df_wc


# -------------------------------
# MOST COMMON WORDS
# -------------------------------

def most_common_words(selected_user, df):

    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    temp = df[df["user"] != "group_notification"]
    temp = temp[temp["message"] != "<Media omitted>\n"]

    with open("stop_hinglish.txt", "r", encoding="utf-8") as f:
        stop_words = set(f.read().split())

    remove_words = {
        "<this", "edited>", "message", "deleted",
        "this", "omitted", "group", "notification", "https"
    }

    words = []

    for message in temp["message"]:
        for word in message.lower().split():

            if word not in stop_words and word not in remove_words:
                words.append(word)

    most_common_df = pd.DataFrame(
        Counter(words).most_common(20),
        columns=["Words", "Count"]
    )

    return most_common_df


# -------------------------------
# EMOJI ANALYSIS
# -------------------------------

def emoji_helper(selected_user, df):

    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    emojis = []

    for message in df["message"]:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    emoji_df = pd.DataFrame(
        Counter(emojis).most_common(20),
        columns=["Emojis", "Count"]
    )

    return emoji_df


# -------------------------------
# MONTHLY TIMELINE
# -------------------------------

def monthly_timeline(selected_user, df):

    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    timeline = df.groupby(
        ["year", "month_num", "month"]
    ).count()["message"].reset_index()

    time = []

    for i in range(timeline.shape[0]):
        time.append(
            timeline["month"][i] + "-" + str(timeline["year"][i])
        )

    timeline["time"] = time

    return timeline


# -------------------------------
# DAILY TIMELINE
# -------------------------------

def daily_timeline(selected_user, df):

    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    daily = df.groupby("only_date").count()["message"].reset_index()

    return daily


# -------------------------------
# WEEK ACTIVITY
# -------------------------------

def week_activity_map(selected_user, df):

    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    return df["day_name"].value_counts()


# -------------------------------
# MONTH ACTIVITY
# -------------------------------

def month_activity_map(selected_user, df):

    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    return df["month"].value_counts()


# -------------------------------
# HEATMAP
# -------------------------------

def activity_heatmap(selected_user, df):

    if selected_user != "Overall":
        df = df[df["user"] == selected_user]

    heatmap = df.pivot_table(
        index="day_name",
        columns="period",
        values="message",
        aggfunc="count"
    )

    days = [
        "Monday","Tuesday","Wednesday",
        "Thursday","Friday","Saturday","Sunday"
    ]

    heatmap = heatmap.reindex(days)

    return heatmap