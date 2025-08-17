from googlesearch import search
import subprocess
import platform
import shutil
import webbrowser
import time


def web_searcher():
    print("Write 'exit' to close the web search mode")

    while True:
        query = input("What do you need? ")
        if query.lower() == "exit":
            print("Exiting web search mode...")
            break

    elif device == "darwin":
        chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        if os.path.exists(chrome_path):
            subprocess.Popen([chrome_path, "--new-window", url])
        else:
            raise FileNotFoundError(
                "Chrome not found at expected path on macOS.")

        device = platform.system().lower()

        # Determine Chrome path based on OS
        chrome_path = None
        if device == "windows":
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        elif device == "darwin":  # macOS
            chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        elif device == "linux":
            chrome_path = shutil.which(
                "google-chrome") or shutil.which("chrome") or shutil.which("chromium-browser")

        # Open URL
        try:
            if chrome_path and shutil.which(chrome_path) or platform.system().lower() != "linux" and os.path.exists(chrome_path):
                subprocess.Popen([chrome_path, "--new-window", url])
            else:
                # fallback to default browser
                # new=2 → open in new tab if possible
                webbrowser.open(url, new=2)
        except Exception as e:
            print(f"Failed to open browser: {e}")

        time.sleep(1)  # slight pause between searches
