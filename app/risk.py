import math


def _scale(value, low, high):
    """value low'a eşitse 0, high'a eşitse 1 döner (arası lineer, dışı kırpılır)."""
    if high == low:
        return 0.0
    return max(0.0, min(1.0, (value - low) / (high - low)))


def calculate_risk(coin):
    # Veri None gelirse 0 kabul et
    price_change = abs(coin.get("price_change_percentage_24h") or 0)
    market_cap = coin.get("market_cap") or 0
    volume = coin.get("total_volume") or 0

    # log10(0) hata verir, o yüzden en az 1 al
    log_cap = math.log10(max(market_cap, 1))
    log_vol = math.log10(max(volume, 1))

    # 1) Fiyat oynaklığı (0-35): %15 ve üzeri değişim tam puan
    volatility_score = _scale(price_change, 0, 15) * 35

    # 2) Market cap riski (0-30): 10 milyon $ = en riskli, 2 trilyon $ = en az riskli
    cap_score = (1 - _scale(log_cap, 7, 12.3)) * 30

    # 3) Likidite riski (0-25): 1 milyon $ hacim = en riskli, 10 milyar $ = en az riskli
    liquidity_score = (1 - _scale(log_vol, 6, 10)) * 25

    # 4) Taban risk (10): kripto hiçbir zaman sıfır riskli değildir
    base_risk = 10

    score = round(base_risk + volatility_score + cap_score + liquidity_score)
    score = max(0, min(score, 100))

    if score >= 55:
        level = "High"
    elif score >= 25:
        level = "Medium"
    else:
        level = "Low"

    return {
        "risk_score": score,
        "risk_level": level,
        "breakdown": {
            "volatility": round(volatility_score, 1),
            "market_cap": round(cap_score, 1),
            "liquidity": round(liquidity_score, 1),
            "base": base_risk,
        },
    }