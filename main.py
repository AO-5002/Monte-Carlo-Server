from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers import simulations
app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your Next.js frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    simulations.router,
    prefix="/simulate",
    tags=["simulate"],
)

