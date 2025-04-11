from fastapi import FastAPI, HTTPException, status


def make_app() -> FastAPI:
    app = FastAPI()

    @app.get("/test", status_code=status.HTTP_200_OK)
    def broken_endpoint():
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @app.get("/healthz", status_code=status.HTTP_200_OK)
    def health_endpoint():
        pass

    return app
