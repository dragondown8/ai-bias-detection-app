import os
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from .utils import save_upload_file
from analysis import run_full_analysis
from config import UPLOAD_FOLDER

app = FastAPI(title="Bernadette's AI Bias Detection Tool")

# Allow CORS for your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    try:
        file_path = save_upload_file(file)
        result = run_full_analysis(file_path)
        return result
    except Exception as e:
        return {"error": f"Analysis failed: {str(e)}"}