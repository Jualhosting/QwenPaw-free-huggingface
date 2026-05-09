import os
import subprocess
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

BACKUP_FILE = "qwenpaw_backup.tar.gz"
BUCKET_NAME = "qwenpaw-data"
DIRS_TO_BACKUP = [".qwenpaw", ".qwenpaw.secret"]

def archive_data():
    print(f"Sedang mengompres data sistem dan secret...")
    try:
        subprocess.run(["tar", "-czf", BACKUP_FILE, "-C", "/root"] + DIRS_TO_BACKUP, check=True)
    except Exception as e:
        print(f"Gagal kompres: {e}")

def upload_to_supabase():
    archive_data()
    print(f"Mengupload backup ke Supabase...")
    with open(BACKUP_FILE, "rb") as f:
        supabase.storage.from_(BUCKET_NAME).upload(path=BACKUP_FILE, file=f, file_options={"x-upsert": "true"})
    print("Upload Berhasil!")

def download_from_supabase():
    print("Mencoba mendownload backup...")
    try:
        res = supabase.storage.from_(BUCKET_NAME).download(BACKUP_FILE)
        with open(BACKUP_FILE, "wb") as f:
            f.write(res)
        subprocess.run(["tar", "-xzf", BACKUP_FILE, "-C", "/root"], check=True)
        print("Restore Berhasil!")
    except Exception as e:
        print(f"Belum ada backup: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "upload":
            upload_to_supabase()
        elif sys.argv[1] == "download":
            download_from_supabase()
