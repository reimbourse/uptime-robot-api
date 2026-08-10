from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.api.v1.router import api_v1_router

app = FastAPI(title='Uptime Robot API')
app.include_router(api_v1_router)

@app.get('/', include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url='/docs', status_code=307)