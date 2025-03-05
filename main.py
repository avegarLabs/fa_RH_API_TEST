from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import httpx
import uvicorn

app = FastAPI()


@app.get("/")
async def redirect_to_swagger():    
    return RedirectResponse(url="/docs")


@app.get("/directions")
async def directions_from_api():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/api/hr/directions/")
        return response.json()


@app.get("/personal")
async def personal_from_api():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/api/hr/personal/")
        return response.json()


@app.get("/charges")
async def charges_from_api():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/api/hr/charges/")
        return response.json()


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=4200
    )
