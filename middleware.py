import time
from fastapi import Request, FastAPI
from logger import logger

app = FastAPI()

@app.middleware("http")
async def medical_appointment_middleware(request: Request, call_next):
    logger.info("Starting=============")
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(f"ended. process time: {process_time}")
    return response
