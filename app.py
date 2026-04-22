import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Trader Sentiment Dashboard", layout="wide")

st.title("📊 Bitcoin Sentiment vs Trader Performance Dashboard")

# Load data
@st.cache_data
def load_data():
    trades = pd.read_csv("historical_data.csv")
    sentiment = pd.read_csv("fear_greed.csv")

    trades['Timestamp IST'] = pd.to_datetime(trades['Timestamp IST'], errors='coerce')
    trades['date'] = trades['Timestamp IST'].dt.date

    sentiment['date'] = pd.to_datetime(sentiment['date']).dt.date

    df = pd.merge(trades, sentiment[['date', 'classification']], on='date', how='left')

    df['profit'] = df['Closed PnL']
    df['win'] = df['profit'] > 0
    df['Size USD'] = pd.to_numeric(df['Size USD'], errors='coerce')

    return df

df = load_data()

# Sidebar filter
st.sidebar.header("🔍 Filters")
sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    options=df['classification'].dropna().unique(),
    default=df['classification'].dropna().unique()
)

filtered_df = df[df['classification'].isin(sentiment_filter)]

# Metrics
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Trades", len(filtered_df))
col2.metric("Avg Profit", round(filtered_df['profit'].mean(), 2))
col3.metric("Win Rate", round(filtered_df['win'].mean() * 100, 2))

# Profit Distribution
st.subheader("📈 Profit Distribution")

fig1, ax1 = plt.subplots()
sns.boxplot(x='classification', y='profit', data=filtered_df, ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# Trade Count
st.subheader("📊 Trade Count by Sentiment")

fig2, ax2 = plt.subplots()
sns.countplot(x='classification', data=filtered_df, ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

# Buy vs Sell
st.subheader("🔄 Buy vs Sell Analysis")

buy_sell = pd.crosstab(filtered_df['classification'], filtered_df['Side'])

fig3, ax3 = plt.subplots()
sns.heatmap(buy_sell, annot=True, fmt='d', ax=ax3)
st.pyplot(fig3)

# Trade Size
st.subheader("💰 Average Trade Size")

size = filtered_df.groupby('classification')['Size USD'].mean()

fig4, ax4 = plt.subplots()
size.plot(kind='bar', ax=ax4)
plt.xticks(rotation=45)
st.pyplot(fig4)