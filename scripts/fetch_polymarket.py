# scripts/fetch_polymarket.py
import os
import argparse
import pandas as pd

def fetch_markets(query, limit=5):
    # Esqueleto seguro: gera dados de exemplo para testar o fluxo
    rows = []
    for i in range(limit):
        rows.append({
            "market_id": f"m{i}",
            "question": f"{query} example {i}",
            "implied_prob": 0.5,
            "volume": 0
        })
    return pd.DataFrame(rows)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--query", required=True)
    p.add_argument("--limit", type=int, default=5)
    args = p.parse_args()

    df = fetch_markets(args.query, args.limit)
    os.makedirs("data/polymarket", exist_ok=True)
    out = f"data/polymarket/markets_{args.query.replace(' ','_')}.csv"
    df.to_csv(out, index=False)
    print(f"Saved {out}")
