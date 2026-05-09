# 🐾 QwenPaw Persistent: Perpetual AI Workspace on Hugging Face

Unlock the full power of **QwenPaw** on Hugging Face Spaces without losing your data. This repository provides a seamless integration with **Supabase Storage** to ensure your chat history, API keys, and project files are persisted forever.

## 🚀 Why this project?
By default, Hugging Face Spaces use ephemeral storage—meaning every time the Space restarts, all your data (chats, files, settings) is wiped clean. This project solves that by automatically syncing your entire workspace to a Supabase bucket every 5 minutes.

## 🛠️ Step 1: Supabase Setup (Your Cloud Hard Drive)
1.  **Create a Project:** Sign up at [Supabase.com](https://supabase.com) and create a new project.
2.  **Create a Bucket:** Go to **Storage** -> **New Bucket**. Name it `qwenpaw-data`.
3.  **Get Your Keys:** Go to **Project Settings** -> **API**. You will need:
    *   `Project URL`
    *   `service_role` key (Do NOT share this key publicly!)

## 📦 Step 2: Hugging Face Setup
1.  **Create a Space:** Go to [Hugging Face](https://huggingface.co/new-space).
2.  **Configuration:**
    *   Select **Docker**.
    *   Choose **Blank** or connect to this GitHub repository.
3.  **Set Secrets (CRITICAL):** Go to **Settings** -> **Variables and Secrets**. Add the following:
    *   `SUPABASE_URL`: Your Supabase Project URL.
    *   `SUPABASE_KEY`: Your Supabase `service_role` key.
    *   `QWENPAW_AUTH_ENABLED`: `true`
    *   `QWENPAW_AUTH_USERNAME`: `admin` (or your choice).
    *   `QWENPAW_AUTH_PASSWORD`: `YourSecurePassword`.

## 📂 Included Files
*   `Dockerfile`: Custom build script to handle auto-restore and periodic sync.
*   `sync.py`: The core synchronization engine between HF and Supabase.
*   `requirements.txt`: Necessary Python drivers for Supabase.

## 💡 How to use
Once deployed, QwenPaw will automatically download your latest backup upon startup. Every 5 minutes, it will save your current state (including new landing pages or agents) back to Supabase.

To manually trigger a backup at any time, simply tell the bot:
> "Run shell command: `python3 /app/sync.py upload`"

## 🛡️ Security Note
Keep your Space **Private** if you want maximum security. All sensitive keys are stored in Hugging Face Secrets, which are encrypted and hidden from unauthorized users.

---
Built with ❤️ for the AI community.
