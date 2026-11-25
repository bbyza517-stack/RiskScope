# RiskScope – Cryptocurrency Risk Analysis API

RiskScope is a REST API developed with **Python and FastAPI** to analyze cryptocurrency market data and estimate risk levels.

The application retrieves market information from the CoinGecko API and provides cryptocurrency search, detailed coin information, risk analysis, comparison, and historical analysis records.

## Features

- Retrieve the top 10 cryptocurrencies by market data
- Get detailed information about individual cryptocurrencies
- Search for cryptocurrencies by name
- Calculate risk scores between 0 and 100
- Classify risk levels as Low, Medium, or High
- Compare two cryptocurrencies
- Store risk analysis results in an SQLite database
- Retrieve previous analysis records
- Access interactive API documentation through Swagger UI

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.12 | Main programming language |
| FastAPI | REST API development |
| CoinGecko API | Cryptocurrency market data |
| HTTPX | Asynchronous HTTP requests |
| SQLModel | Database models and ORM |
| SQLite | Data storage |
| Uvicorn | ASGI server |
| python-dotenv | Environment variable management |

## Project Structure

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
├── .gitignore
├── requirements.txt
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns the API welcome message |
| GET | `/coins` | Retrieves the top 10 cryptocurrencies |
| GET | `/coins/{coin_id}` | Returns detailed coin information |
| GET | `/coins/{coin_id}/risk` | Calculates and stores a coin's risk analysis |
| GET | `/search?query=bitcoin` | Searches for cryptocurrencies |
| GET | `/compare?coin1=bitcoin&coin2=ethereum` | Compares two cryptocurrencies |
| GET | `/history` | Retrieves previously saved risk analyses |

## Risk Analysis Model

RiskScope calculates a risk score using selected cryptocurrency market indicators:

- **Price Volatility:** Evaluates the absolute 24-hour price change.
- **Market Capitalization:** Considers the market capitalization of the cryptocurrency.
- **Trading Volume:** Evaluates trading volume as a liquidity indicator.

The scoring model uses the following maximum point allocations:

| Factor | Maximum Points |
|---|---:|
| Price Volatility | 35 |
| Market Capitalization | 30 |
| Trading Volume | 25 |
| Base Risk | 10 |
| **Total** | **100** |

The final score is classified into three risk levels:

| Score | Risk Level |
|---|---|
| 0–24 | Low |
| 25–54 | Medium |
| 55–100 | High |

This is an educational risk estimation model and should not be considered professional financial advice.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/bbyza517-stack/RiskScope.git
cd RiskScope
```

### 2. Create a virtual environment

```bash
py -3.12 -m venv venv
```

### 3. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file in the root directory of the project and add your CoinGecko API key:

```env
COINGECKO_API_KEY=your_api_key_here
```

**Important:** Keep your API key private. Do not upload your `.env` file to GitHub.

## Running the Application

Start the development server:

```bash
fastapi dev app/main.py
```

After starting the server, the API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

RiskScope provides interactive API documentation through Swagger UI.

Open the following address in your browser:

```text
http://127.0.0.1:8000/docs
```

You can test the available endpoints directly from the Swagger interface.

## Database

RiskScope uses **SQLite** and **SQLModel** to store historical risk analysis results.

Each saved analysis includes:

- Coin name
- Symbol
- Current price
- Risk score
- Risk level
- Analysis date

The `/history` endpoint provides access to previously stored analysis records.

## Project Purpose

RiskScope was developed as an educational software engineering project to practice REST API development, asynchronous programming, external API integration, database management, and data analysis.

The project demonstrates how cryptocurrency market data can be retrieved, processed, analyzed, and stored through a structured REST API.
