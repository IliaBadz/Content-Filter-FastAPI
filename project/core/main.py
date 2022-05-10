from fastapi import FastAPI, status

from app.routers import filter


app = FastAPI()

app.include_router(filter.router)


@app.get("/health", status_code=status.HTTP_200_OK)
async def health():
    return {"message": "successful launch"}
