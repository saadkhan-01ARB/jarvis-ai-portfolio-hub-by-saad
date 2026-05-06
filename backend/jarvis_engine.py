import webbrowser
from datetime import datetime
import wikipedia

# =========================
# MEMORY SYSTEM (NEW)
# =========================
memory = {
    "name": "Saad",
    "last_command": None,
    "history": []
}


def remember(cmd, response):
    memory["last_command"] = cmd
    memory["history"].append((cmd, response))

    # keep only last 10 chats
    if len(memory["history"]) > 10:
        memory["history"].pop(0)


# =========================
# FAST ACTION BRAIN
# =========================
def fast_brain(cmd):
    cmd = cmd.lower()

    if "youtube" in cmd:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    if "google" in cmd:
        webbrowser.open("https://google.com")
        return "Opening Google"

    if "time" in cmd:
        return "Current time is " + datetime.now().strftime("%H:%M:%S")

    if "my name" in cmd:
        return f"Your name is {memory['name']}"

    return None


# =========================
# WIKIPEDIA BRAIN (IMPROVED)
# =========================
def wiki_brain(cmd):
    try:
        cmd = cmd.lower()

        query = cmd.replace("what is", "").replace("who is", "").strip()

        results = wikipedia.search(query)

        if not results:
            return None

        page = results[0]

        return wikipedia.summary(page, sentences=2)

    except:
        return None


# =========================
# SMART FALLBACK BRAIN
# =========================
def offline_brain(cmd):
    cmd = cmd.lower()

    if "hello" in cmd:
        return f"Hello {memory['name']} 👋 I am Jarvis."

    if "how are you" in cmd:
        return "I am running at full performance ⚡"

    if "your name" in cmd:
        return "I am Jarvis, your AI assistant."

    return "I couldn't fully understand. Try rephrasing."


# =========================
# MAIN HYBRID BRAIN (FINAL)
# =========================
def process_command(cmd):

    if not cmd:
        return "No command received"

    # STEP 1: FAST ACTIONS
    result = fast_brain(cmd)
    if result:
        remember(cmd, result)
        return result

    # STEP 2: WIKIPEDIA KNOWLEDGE
    result = wiki_brain(cmd)
    if result:
        remember(cmd, result)
        return result

    # STEP 3: OFFLINE INTELLIGENCE
    result = offline_brain(cmd)
    remember(cmd, result)
    return result