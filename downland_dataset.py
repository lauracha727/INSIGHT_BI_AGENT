import os
import subprocess
import zipfile

from config import KAGGLE_DATASET, DATABASE_PATH

DATABASE_FOLDER = os.path.dirname(DATABASE_PATH)
os.makedirs(DATABASE_FOLDER, exist_ok=True)

if not os.path.exists(DATABASE_PATH):

    print("📥 Descargando dataset...")

    subprocess.run([
        "kaggle",
        "datasets",
        "download",
        "-d",
        KAGGLE_DATASET,
        "-p",
        DATABASE_FOLDER
    ], check=True)

    zip_file = os.path.join(
        DATABASE_FOLDER,
        "e-commerce-dataset-by-olist-as-an-sqlite-database.zip"
    )

    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(DATABASE_FOLDER)

    print("✅ Dataset descargado correctamente.")

else:

    print("✅ Dataset ya existe.")