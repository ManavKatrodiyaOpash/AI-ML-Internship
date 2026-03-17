import pandas as pd
import re


def preprocess(data):

    pattern = r"\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s?(?:am|pm)?\s-\s"

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({
        "message_dates": dates,
        "messages": messages
    })

    df["message_dates"] = pd.to_datetime(
        df["message_dates"],
        format="%d/%m/%Y, %I:%M %p - ",
        errors="coerce"
    )

    df.rename(columns={"message_dates": "date"}, inplace=True)

    users = []
    messages = []

    for message in df["messages"]:

        entry = re.split(r"([\w\W]+?):\s", message)

        if len(entry) > 1:

            users.append(entry[1])
            messages.append(entry[2])

        else:

            users.append("group_notification")
            messages.append(entry[0])

    df["user"] = users
    df["message"] = messages

    df.drop(columns=["messages"], inplace=True)

    # -------------------------------
    # DATE FEATURES
    # -------------------------------

    df["year"] = df["date"].dt.year
    df["month_num"] = df["date"].dt.month
    df["month"] = df["date"].dt.month_name()

    df["day"] = df["date"].dt.day
    df["day_name"] = df["date"].dt.day_name()

    df["hour"] = df["date"].dt.hour
    df["minute"] = df["date"].dt.minute

    df["only_date"] = df["date"].dt.date

    # -------------------------------
    # TIME PERIOD
    # -------------------------------

    period = []

    for hour in df["hour"]:

        if hour == 23:
            period.append("23-00")

        elif hour == 0:
            period.append("00-01")

        else:
            period.append(f"{hour}-{hour+1}")

    df["period"] = period

    df.drop(columns=["date"], inplace=True)

    return df