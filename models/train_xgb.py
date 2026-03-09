# models/train_xgb.py
import os
import pandas as pd
import joblib
from xgboost import XGBRegressor

def train(city):
    path = f"data/weather/{city.replace(' ','_')}_current.csv"
    if not os.path.exists(path):
        print("Arquivo não encontrado:", path)
        return
    df = pd.read_csv(path).fillna(0)
    # Usamos a temperatura como feature e target apenas para teste rápido
    if 'temp' not in df.columns:
        print("Coluna 'temp' não encontrada em", path)
        return
    X = df[['temp']].values
    y = df['temp'].values
    model = XGBRegressor(n_estimators=10, verbosity=0)
    model.fit(X, y)
    os.makedirs("models/outputs", exist_ok=True)
    out_path = "models/outputs/xgb_model.joblib"
    joblib.dump(model, out_path)
    print("Modelo salvo em", out_path)

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--city", required=True)
    args = p.parse_args()
    train(args.city)
