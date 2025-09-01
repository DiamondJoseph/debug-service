from fastapi import FastAPI, HTTPException, status


def make_app() -> FastAPI:
    app = FastAPI()

    @app.get("/test", status_code=status.HTTP_200_OK)
    def broken_endpoint():
        return {}

    @app.get("/healthz", status_code=status.HTTP_200_OK)
    def health_endpoint():
        pass

    return app
