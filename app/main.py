from fastapi import FastAPI, HTTPException, Query
from contextlib import asynccontextmanager
import httpx
from sqlmodel import Session, select
from database import engine

from coingecko import get_market_data, get_coin_data, search_coins
from risk import calculate_risk
from database import create_db_and_tables
from models import RiskAnalysis
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(
    title="RiskScope API",
    description="Cryptocurrency Risk Analysis API",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to RiskScope API",
        "status": "Running"
    }


@app.get("/coins")
async def get_coins():

    try:
        coins = await get_market_data()
        return coins

    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=502,
            detail=f"CoinGecko API error: {e.response.status_code}"
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Could not connect to CoinGecko"
        )


@app.get("/coins/{coin_id}")
async def get_coin(coin_id: str):

    try:
        coin = await get_coin_data(coin_id)

        if coin is None:
            raise HTTPException(
                status_code=404,
                detail="Coin not found"
            )

        return coin

    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=502,
            detail=f"CoinGecko API error: {e.response.status_code}"
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Could not connect to CoinGecko"
        )
    
@app.get("/coins/{coin_id}/risk")
async def analyze_coin_risk(coin_id: str):

    try:
        coin = await get_coin_data(coin_id)

        if coin is None:
            raise HTTPException(
                status_code=404,
                detail="Coin not found"
            )

        risk_result = calculate_risk(coin)

        analysis = RiskAnalysis(
            coin_name=coin["name"],
            symbol=coin["symbol"],
            current_price=coin["current_price"],
            risk_score=risk_result["risk_score"],
            risk_level=risk_result["risk_level"]
        )

        with Session(engine) as session:
            session.add(analysis)
            session.commit()
            session.refresh(analysis)

        return {
            "id": analysis.id,
            "coin": coin["name"],
            "symbol": coin["symbol"],
            "current_price": coin["current_price"],
            "market_cap": coin["market_cap"],
            "volume": coin["total_volume"],
            "price_change_24h": coin["price_change_percentage_24h"],
            "risk_score": risk_result["risk_score"],
            "risk_level": risk_result["risk_level"],
            "message": "Risk analysis saved successfully"
        }

    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=502,
            detail=f"CoinGecko API error: {e.response.status_code}"
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Could not connect to CoinGecko"
        )
    
@app.get("/search")
async def search_coin(
    query: str = Query(..., min_length=2)
):

    try:
        results = await search_coins(query)

        if not results:
            raise HTTPException(
                status_code=404,
                detail="No coins found"
            )

        return {
            "query": query,
            "total_results": len(results),
            "coins": results
        }

    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=502,
            detail=f"CoinGecko API error: {e.response.status_code}"
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Could not connect to CoinGecko"
        )
@app.get("/compare")
async def compare_coins(
    coin1: str,
    coin2: str
):

    try:
        first_coin = await get_coin_data(coin1)
        second_coin = await get_coin_data(coin2)

        if first_coin is None or second_coin is None:
            raise HTTPException(
                status_code=404,
                detail="One or both coins not found"
            )

        first_risk = calculate_risk(first_coin)
        second_risk = calculate_risk(second_coin)

        return {
            "coin_1": {
                "name": first_coin["name"],
                "price": first_coin["current_price"],
                "market_cap": first_coin["market_cap"],
                "volume": first_coin["total_volume"],
                "price_change_24h": first_coin["price_change_percentage_24h"],
                "risk_score": first_risk["risk_score"],
                "risk_level": first_risk["risk_level"]
            },
            "coin_2": {
                "name": second_coin["name"],
                "price": second_coin["current_price"],
                "market_cap": second_coin["market_cap"],
                "volume": second_coin["total_volume"],
                "price_change_24h": second_coin["price_change_percentage_24h"],
                "risk_score": second_risk["risk_score"],
                "risk_level": second_risk["risk_level"]
            }
        }

    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=502,
            detail=f"CoinGecko API error: {e.response.status_code}"
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Could not connect to CoinGecko"
            
        )
@app.get("/history")
async def get_analysis_history():

    with Session(engine) as session:
        statement = select(RiskAnalysis)
        results = session.exec(statement).all()

        return results