import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from iam_app.api.admin_routes import admin_router
from iam_app.api.user_routes import router
app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Your API",
        version="1.0.0",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            # فرض کنیم همه endpoint هایی که auth دارن
            openapi_schema["paths"][path][method]["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
app.include_router(router)
app.include_router(admin_router)


logging.basicConfig(level=logging.INFO)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

if __name__ == "__main__":
    import uvicorn
    try:
        uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)

    except Exception as first_error:
        print(f"Primary host failed: {first_error}")

        try:
            uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True, log_level="debug")

        except Exception as fallback_error:
            print(f"Fallback host also failed: {fallback_error}")