import uvicorn, git, os
from fastapi import FastAPI, APIRouter
from fastapi.openapi.utils import get_openapi
from controller.ToxicityAnalysisController import toxicity_analysis_controller

app = FastAPI()
app.include_router(toxicity_analysis_controller)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    current_branch = git.repo.Repo(os.getcwd(), search_parent_directories=True).active_branch
    commit = current_branch.commit
    commit_msg = commit.message.split('\n')[0]
    version = f"{commit.hexsha[:7]} in {current_branch.name} by {commit.author}: {commit_msg}"

    openapi_schema = get_openapi(
        title="Server Management",
        version=version,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema

app.openapi = custom_openapi

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")