import os
from dotenv import load_dotenv
from typing import List

load_dotenv() # On injecte le contenu du fichier .env que os.getenv() va les lire/récup.

class Settings:
    # ---------------------------------------------------------
    # ---------Partie-----------Database-----------------------
    # ---------------------------------------------------------
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: int = int(os.getenv("DB_PORT", 5432))
    DB_NAME: str = os.getenv("DB_NAME", "risk_analytics")
    
    @property
    def DATABASE_URL(self) -> str:
        if not self.DB_PASSWORD:
            raise ValueError("DB_PASSWORD requis")
        return (
            f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
            f"?sslmode=require&connect_timeout=10"
        )
    
    # Pool settings
    POOL_SIZE: int = 10
    POOL_MAX_OVERFLOW: int = 20
    POOL_TIMEOUT: int = 30
    
    # Scraping
    SPOT_TICKERS: List[str] = [
        "AAPL", "MSFT", "GOOGL", "TSLA", "AMZN", 
        "META", "NVDA", "JPM", "BAC", "GS"
    ]
    FUTURES_TICKERS: List[str] = [
        "ES=F",   # S&P 500 futures
        "NQ=F",   # NASDAQ futures
        "GC=F",   # Gold futures
        "CL=F",   # Crude oil futures
    ]
    LOOKBACK_DAYS: int = 365  # 1 an historique
    
    # Risk params
    VAR_CONFIDENCE: float = 0.95  # 95% VaR
    VAR_HORIZON_DAYS: int = 1     # 1-day VaR
    RISK_FREE_RATE: float = 0.045 # 4.5% taux sans risque

settings = Settings()
