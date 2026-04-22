# 📊 Bitcoin Market Sentiment vs Trader Performance Analysis

## 🚀 Overview
This project explores the relationship between **Bitcoin market sentiment (Fear vs Greed)** and **trader performance** using historical trading data from Hyperliquid.

The objective is to uncover how sentiment influences:
- Profitability (PnL)
- Trading behavior
- Risk-taking patterns

Additionally, an interactive **Streamlit dashboard** is built to visualize and explore insights dynamically.

---

## 📁 Dataset Description

### 1. Bitcoin Fear & Greed Index
- `date` – Date of sentiment
- `classification` – Market sentiment  
  *(Extreme Fear, Fear, Greed, Extreme Greed)*
- `value` – Sentiment score

### 2. Historical Trader Data (Hyperliquid)
- `Account` – Trader wallet address
- `Coin` – Asset traded
- `Execution Price` – Trade price
- `Size USD` – Trade size
- `Side` – Buy/Sell
- `Timestamp IST` – Trade time
- `Closed PnL` – Profit/Loss

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone <your-repo-link>
cd bitcoin-sentiment-analysis

pip install -r requirements.txt

run: 
jupyter notebook
bitcoin_sentiment_trader_analysis.ipynb

Run Dashboard
streamlit run app.py

📊 Output Visualizations

The project includes:

Profit distribution (boxplots)
Average profit comparison
Win rate charts
Trade count analysis
Buy vs Sell heatmap
Correlation matrix

(All visualizations available in the notebook and dashboard)


Conclusion
This analysis demonstrates that market sentiment significantly impacts trading outcomes.
Incorporating sentiment signals into trading strategies can improve decision-making, optimize risk, and enhance profitability.