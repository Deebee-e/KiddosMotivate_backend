from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes.user_data_routes import auth_router

# Create the FastAPI application instance
app = FastAPI(title="Kiddo Motivate Backend Routes", docs_url="/docs")

# CORS configuration
app.add_middleware(
            CORSMiddleware,
            allow_origins = ["http://localhost:5173"],
            allow_credentials=True,
            allow_methods=["GET", "POST", "PUT", "DELETE"],
            allow_headers=["*"]
        )

# Include routers
app.include_router(auth_router, prefix="/api/v1", tags=["User Auth"])
