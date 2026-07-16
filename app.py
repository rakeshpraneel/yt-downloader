from fastapi import FastAPI, HTTPException
import get_file

app = FastAPI()

@app.get("/download")
async def download():
    try:
        get_file.download_video()
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))