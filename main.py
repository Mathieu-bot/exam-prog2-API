from fastapi import FastAPI
from api.routes import router


app = FastAPI(title="Exam-prog2-API", description="First exam api. 2025-July-31", version="0.1.0")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)