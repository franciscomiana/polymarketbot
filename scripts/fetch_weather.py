# scripts/fetch_weather.py
import os
import argparse
import pandas as pd
from datetime import datetime

def fetch_dummy(city):
    # Gera uma linha de dados de exemplo com timestamp
    now = datetime.utcnow().isoformat()
    df = pd.DataFrame([{"city": city, "temp": 20.0, "dt": now}])
    return df

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--city", required=True)
    args = p.parse_args()

    df = fetch_dummy(args.city)
    os.makedirs("data/weather", exist_ok=True)
    out = f"data/weather/{args.city.replace(' ','_')}_current.csv"
    df.to_csv(out, index=False)
    print(f"Saved {out}")
