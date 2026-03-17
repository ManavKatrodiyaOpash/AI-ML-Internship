import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# -------------------------------
# PAGE CONFIG
# -------------------------------

st.set_page_config(
    page_title="WhatsApp Chat Analyzer",
    page_icon="💬",
    layout="wide"
)

# -------------------------------
# HEADER
# -------------------------------

st.title("💬 WhatsApp Chat Analyzer")
st.markdown("Analyze your WhatsApp chats with beautiful statistics and insights.")
st.divider()

# -------------------------------
# SIDEBAR
# -------------------------------

st.sidebar.title("📊 Analyzer Controls")
uploaded_file = st.sidebar.file_uploader("Upload WhatsApp Chat (.txt file)")

# -------------------------------
# MAIN PROCESS
# -------------------------------

if uploaded_file is not None:

    try:
        bytes_data = uploaded_file.getvalue()
        data = bytes_data.decode("utf-8")

        df = preprocessor.preprocess(data)

    except:
        st.error("Invalid file format. Please upload a WhatsApp exported chat.")
        st.stop()

    # -------------------------------
    # USER SELECTION
    # -------------------------------

    user_list = df["user"].unique().tolist()

    if "group_notification" in user_list:
        user_list.remove("group_notification")

    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Select User", user_list)

    if st.sidebar.button("Show Analysis"):

        with st.spinner("Analyzing chat..."):

            # -------------------------------
            # TOP STATISTICS
            # -------------------------------

            num_messages, num_words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)

            st.subheader("📌 Top Statistics")

            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Messages", num_messages)
            col2.metric("Words", num_words)
            col3.metric("Media", num_media_messages)
            col4.metric("Links", num_links)

            st.divider()

            # -------------------------------
            # MONTHLY TIMELINE
            # -------------------------------

            st.subheader("📈 Monthly Timeline")

            timeline = helper.monthly_timeline(selected_user, df)

            fig = px.line(
                timeline,
                x="time",
                y="message",
                markers=True,
                title="Messages Over Time"
            )

            st.plotly_chart(fig, use_container_width=True)

            # -------------------------------
            # DAILY TIMELINE
            # -------------------------------

            st.subheader("📅 Daily Timeline")

            daily_timeline = helper.daily_timeline(selected_user, df)

            fig = px.line(
                daily_timeline,
                x="only_date",
                y="message",
                markers=True
            )

            st.plotly_chart(fig, use_container_width=True)

            st.divider()

            # -------------------------------
            # ACTIVITY MAP
            # -------------------------------

            st.subheader("📊 Activity Map")

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("### Most Busy Day")

                busy_day = helper.week_activity_map(selected_user, df)

                fig = px.bar(
                    x=busy_day.index,
                    y=busy_day.values,
                    labels={'x': 'Day', 'y': 'Messages'}
                )

                st.plotly_chart(fig, use_container_width=True)

            with col2:

                st.markdown("### Most Busy Month")

                busy_month = helper.month_activity_map(selected_user, df)

                fig = px.bar(
                    x=busy_month.index,
                    y=busy_month.values,
                    labels={'x': 'Month', 'y': 'Messages'}
                )

                st.plotly_chart(fig, use_container_width=True)

            st.divider()

            # -------------------------------
            # HEATMAP
            # -------------------------------

            st.subheader("🔥 Weekly Activity Heatmap")

            user_heatmap = helper.activity_heatmap(selected_user, df)

            fig, ax = plt.subplots(figsize=(10, 5))
            sns.heatmap(user_heatmap, ax=ax)

            st.pyplot(fig)

            st.divider()

            # -------------------------------
            # BUSIEST USERS
            # -------------------------------

            if selected_user == "Overall":

                st.subheader("👥 Most Busy Users")

                x, new_df = helper.most_busy_users(df)

                col1, col2 = st.columns(2)

                with col1:

                    fig = px.bar(
                        x=x.index,
                        y=x.values,
                        labels={'x': 'User', 'y': 'Messages'}
                    )

                    st.plotly_chart(fig, use_container_width=True)

                with col2:

                    st.dataframe(new_df)

            st.divider()

            # -------------------------------
            # WORD CLOUD
            # -------------------------------

            st.subheader("☁ Word Cloud")

            df_wc = helper.create_wordcloud(selected_user, df)

            fig, ax = plt.subplots(figsize=(8, 8))
            ax.imshow(df_wc)
            ax.axis("off")

            st.pyplot(fig)

            st.divider()

            # -------------------------------
            # MOST COMMON WORDS
            # -------------------------------

            st.subheader("📝 Most Common Words")

            most_common_df = helper.most_common_words(selected_user, df)

            fig = px.bar(
                most_common_df,
                x="Count",
                y="Words",
                orientation="h"
            )

            st.plotly_chart(fig, use_container_width=True)

            st.dataframe(most_common_df)

            st.divider()

            # -------------------------------
            # EMOJI ANALYSIS
            # -------------------------------

            st.subheader("😂 Emoji Analysis")

            emoji_df = helper.emoji_helper(selected_user, df)

            col1, col2 = st.columns(2)

            with col1:

                st.dataframe(emoji_df)

            with col2:

                fig = px.pie(
                    emoji_df.head(10),
                    values="Count",
                    names="Emojis",
                    title="Top Emojis"
                )

                st.plotly_chart(fig, use_container_width=True)