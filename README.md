# RiskScope – Cryptocurrency Risk Analysis API

## 1. Project Overview

RiskScope is a cryptocurrency risk analysis application developed using Python and FastAPI.

The application retrieves real-time cryptocurrency market data from CoinGecko API and provides market information, risk analysis, coin search, and comparison features.

## 2. Technologies Used

- Python 3.12
- FastAPI
- SQLModel
- SQLite
- HTTPX
- CoinGecko API
- Uvicorn

## 3. Project Structure

```text
RiskScope/
│
├── app/
│   ├── main.py
│   ├── coingecko.py
│   ├── database.py
│   ├── models.py
│   └── risk.py
│
├── .env
├── requirements.txt
├── riskscope.db
└── README.md
```

## 4. Features

- Cryptocurrency market data retrieval
- Individual coin details
- Cryptocurrency search
- Risk score calculation
- Risk level classification (Low, Medium, High)
- Comparison between two cryptocurrencies
- SQLite database integration
- Historical risk analysis records
- Automatic API documentation with Swagger UI

## 5. API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/coins` | Retrieve top 10 cryptocurrencies |
| GET | `/coins/{coin_id}` | Get coin details |
| GET | `/coins/{coin_id}/risk` | Analyze cryptocurrency risk |
| GET | `/history` | Retrieve previous analyses |
| GET | `/search?query=bitcoin` | Search cryptocurrencies |
| GET | `/compare?coin1=bitcoin&coin2=ethereum` | Compare two cryptocurrencies |

## 6. Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd RiskScope
```

Create a virtual environment:

```bash
py -3.12 -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 7. Environment Variables

Create a `.env` file in the project root directory.

Add your CoinGecko Demo API key:

```env
COINGECKO_API_KEY=your_api_key_here
```

Do not share or upload your API key.

## 8. Run the Application

Start the development server:

```bash
fastapi dev app/main.py
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

## 9. Database

RiskScope uses SQLite with SQLModel to store cryptocurrency risk analysis records.

Each analysis stores:

- Coin name
- Symbol
- Current price
- Risk score
- Risk level
- Analysis date

## 10. Risk Analysis

The application calculates a risk score based on selected market indicators:

- Price change
- Market capitalization
- Trading volume

The score ranges from 0 to 100 and is classified into Low, Medium, and High risk levels.

The scoring algorithm is an educational model and does not represent professional financial advice.

## 11. Project Purpose

This project was developed for educational purposes to practice REST API development, external API integration, database management, and cryptocurrency market data analysis.
