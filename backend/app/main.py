from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import products, categories, sales

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SmartMart API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://smartmart-solutions-murex.vercel.app/"], # Domínio do seu Next.js
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"], # Permite todos os headers
)

app.include_router(products.router)
app.include_router(categories.router)
app.include_router(sales.router)

@app.get("/")
def root():
    return {"status": "SmartMart API running"}
