import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("COINGECKO_API_KEY")

BASE_URL = "https://api.coingecko.com/api/v3"


async def get_market_data():

    url = f"{BASE_URL}/coins/markets"

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "price_change_percentage": "24h"
    }

    headers = {
        "x-cg-demo-api-key": API_KEY
    }

    async with httpx.AsyncClient() as client:

        response = await client.get(
            url,
            params=params,
            headers=headers,
            timeout=20
        )

        response.raise_for_status()

        return response.json()


async def get_coin_data(coin_id: str):

    url = f"{BASE_URL}/coins/markets"

    params = {
        "vs_currency": "usd",
        "ids": coin_id,
        "price_change_percentage": "24h"
    }

    headers = {
        "x-cg-demo-api-key": API_KEY
    }

    async with httpx.AsyncClient() as client:

        response = await client.get(
            url,
            params=params,
            headers=headers,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        if not data:
            return None

        return data[0]
    
async def search_coins(query: str):

    url = f"{BASE_URL}/search"

    params = {
        "query": query
    }

    headers = {
        "x-cg-demo-api-key": API_KEY
    }

    async with httpx.AsyncClient() as client:

        response = await client.get(
            url,
            params=params,
            headers=headers,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        return data.get("coins", [])[:10]