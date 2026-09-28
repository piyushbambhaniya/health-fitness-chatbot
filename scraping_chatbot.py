# ============================================================
#  Web Scraping Rule-Based Health & Fitness Chatbot
#  Libraries : requests, BeautifulSoup4
#  Source    : Wikipedia (en.wikipedia.org)
#  Method    : Scrape topic pages → extract paragraphs →
#              serve relevant sentences via if-else rules
# ============================================================

import requests
from bs4 import BeautifulSoup

# ── Wikipedia Scraper ─────────────────────────────────────────────────────────

def scrape_wikipedia(topic):
    """
    Fetch the Wikipedia page for `topic` and return a list of
    clean paragraph strings (non-empty, longer than 60 chars).
    Returns an empty list on any network or parsing error.
    """
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; ChatbotProject/1.0)"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[Scraper] Could not fetch '{topic}': {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove citation markers, navboxes, and infoboxes for clean text
    for tag in soup.find_all(["sup", "table"]):
        tag.decompose()

    # Grab all <p> tags from the main content area
    content_div = soup.find("div", {"id": "mw-content-text"})
    if not content_div:
        return []

    paragraphs = []
    for p in content_div.find_all("p"):
        text = p.get_text(separator=" ").strip()
        if len(text) > 60:          # skip short / empty paragraphs
            paragraphs.append(text)

    return paragraphs


def search_paragraphs(paragraphs, keywords, max_results=2):
    """
    Return up to `max_results` paragraphs that contain any of
    the given keywords (case-insensitive).
    Falls back to the first paragraph if nothing matches.
    """
    results = []
    for para in paragraphs:
        if any(kw.lower() in para.lower() for kw in keywords):
            results.append(para)
        if len(results) >= max_results:
            break

    if not results and paragraphs:
        results = [paragraphs[0]]   # fallback: intro paragraph

    return results


def format_scraped(paragraphs, intro="Here is what Wikipedia says:\n"):
    """Wrap scraped paragraphs in a readable chatbot response."""
    if not paragraphs:
        return ("Sorry, I could not fetch information right now. "
                "Please check your internet connection.")
    body = "\n\n".join(f"  {p}" for p in paragraphs)
    return f"{intro}\n{body}\n\n[Source: Wikipedia]"


# ── Pre-load Wikipedia pages at startup ──────────────────────────────────────
#   Each entry: topic_key → (wikipedia_article_title, search_keywords)

TOPICS = {
    "exercise":      ("Exercise",               ["exercise", "physical activity", "fitness"]),
    "weight_loss":   ("Weight_loss",            ["weight loss", "calorie", "fat", "obesity"]),
    "muscle":        ("Muscle_hypertrophy",     ["muscle", "hypertrophy", "strength", "protein"]),
    "nutrition":     ("Nutrition",              ["nutrition", "diet", "nutrient", "food"]),
    "protein":       ("Protein_(nutrient)",     ["protein", "amino acid", "muscle", "intake"]),
    "cardio":        ("Aerobic_exercise",       ["cardio", "aerobic", "heart", "endurance"]),
    "hiit":          ("High-intensity_interval_training",
                                                ["HIIT", "interval", "intensity", "sprint"]),
    "sleep":         ("Sleep",                  ["sleep", "rest", "recovery", "circadian"]),
    "bmi":           ("Body_mass_index",        ["BMI", "body mass", "overweight", "obese"]),
    "yoga":          ("Yoga",                   ["yoga", "flexibility", "mindfulness", "pose"]),
    "mental_health": ("Mental_health",          ["mental health", "anxiety", "depression",
                                                 "stress", "well-being"]),
    "hydration":     ("Drinking_water",         ["water", "hydration", "fluid", "dehydration"]),
    "creatine":      ("Creatine",               ["creatine", "supplement", "strength", "ATP"]),
    "stretching":    ("Stretching",             ["stretch", "flexibility", "warm", "range"]),
}

print("Loading knowledge base from Wikipedia... (this may take a moment)")
KB = {}
for key, (article, keywords) in TOPICS.items():
    paras = scrape_wikipedia(article)
    KB[key] = {"paragraphs": paras, "keywords": keywords}
    status = f"{len(paras)} paragraphs" if paras else "FAILED"
    print(f"  [{status:>20}]  {article}")

print("Ready!\n")


# ── Rule-Based Response Engine ────────────────────────────────────────────────

def get_response(user_input):
    text = user_input.lower().strip()

    # ── Greetings ────────────────────────────────────────────
    if text in ["hi", "hello", "hey", "good morning", "good afternoon",
                "good evening", "howdy"]:
        return ("Hello! I am a Health & Fitness Chatbot powered by Wikipedia. 💪\n"
                "Ask me about exercise, weight loss, nutrition, sleep, cardio,\n"
                "protein, HIIT, yoga, mental health, hydration, BMI, and more!\n"
                "Type 'help' to see all topics.")

    # ── Help ─────────────────────────────────────────────────
    elif text in ["help", "menu", "topics", "options", "what can you do"]:
        return ("Topics I can answer (powered by live Wikipedia scraping):\n"
                "  • Exercise / Workout\n"
                "  • Weight Loss\n"
                "  • Muscle Gain / Hypertrophy\n"
                "  • Nutrition / Diet\n"
                "  • Protein\n"
                "  • Cardio / Aerobic Exercise\n"
                "  • HIIT\n"
                "  • Sleep & Recovery\n"
                "  • BMI\n"
                "  • Yoga & Flexibility\n"
                "  • Mental Health\n"
                "  • Hydration / Water\n"
                "  • Creatine / Supplements\n"
                "  • Stretching\n"
                "Just ask a question or type a keyword!")

    # ── HIIT (check before cardio to avoid partial match) ────
    elif any(w in text for w in ["hiit", "high intensity interval",
                                  "interval training"]):
        paras = search_paragraphs(KB["hiit"]["paragraphs"],
                                  KB["hiit"]["keywords"])
        return format_scraped(paras,
            "Here is what Wikipedia says about HIIT (High-Intensity Interval Training):\n")

    # ── Cardio / Aerobic ─────────────────────────────────────
    elif any(w in text for w in ["cardio", "aerobic", "running", "jogging",
                                  "cycling", "swimming", "endurance"]):
        paras = search_paragraphs(KB["cardio"]["paragraphs"],
                                  KB["cardio"]["keywords"])
        return format_scraped(paras, "Here is what Wikipedia says about Cardio:\n")

    # ── Creatine / Supplements (before nutrition to avoid 'eat' false match) ─
    elif any(w in text for w in ["creatine", "supplement", "bcaa",
                                  "pre-workout", "whey"]):
        paras = search_paragraphs(KB["creatine"]["paragraphs"],
                                  KB["creatine"]["keywords"])
        return format_scraped(paras, "Here is what Wikipedia says about Creatine:\n")

    # ── Protein ──────────────────────────────────────────────
    elif any(w in text for w in ["protein", "amino acid", "whey protein"]):
        paras = search_paragraphs(KB["protein"]["paragraphs"],
                                  KB["protein"]["keywords"])
        return format_scraped(paras, "Here is what Wikipedia says about Protein:\n")

    # ── Weight Loss ──────────────────────────────────────────
    elif any(w in text for w in ["weight loss", "lose weight", "fat loss",
                                  "burn fat", "slim", "reduce weight",
                                  "overweight"]):
        paras = search_paragraphs(KB["weight_loss"]["paragraphs"],
                                  KB["weight_loss"]["keywords"])
        return format_scraped(paras, "Here is what Wikipedia says about Weight Loss:\n")

    # ── Muscle / Hypertrophy ─────────────────────────────────
    elif any(w in text for w in ["muscle", "hypertrophy", "bulk",
                                  "gain weight", "build muscle", "strength training"]):
        paras = search_paragraphs(KB["muscle"]["paragraphs"],
                                  KB["muscle"]["keywords"])
        return format_scraped(paras, "Here is what Wikipedia says about Muscle Hypertrophy:\n")

    # ── Exercise / Workout (general) ─────────────────────────
    elif any(w in text for w in ["exercise", "workout", "gym", "training",
                                  "working out", "fitness", "physical activity"]):
        paras = search_paragraphs(KB["exercise"]["paragraphs"],
                                  KB["exercise"]["keywords"])
        return format_scraped(paras, "Here is what Wikipedia says about Exercise:\n")

    # ── Nutrition / Diet / Food ──────────────────────────────
    elif any(w in text for w in ["nutrition", "diet", "food", "meal",
                                  "calorie", "calories", "eat", "nutrient"]):
        paras = search_paragraphs(KB["nutrition"]["paragraphs"],
                                  KB["nutrition"]["keywords"])
        return format_scraped(paras, "Here is what Wikipedia says about Nutrition:\n")

    # ── Hydration / Water ────────────────────────────────────
    elif any(w in text for w in ["water", "hydration", "hydrate",
                                  "drink water", "fluid", "dehydration"]):
        paras = search_paragraphs(KB["hydration"]["paragraphs"],
                                  KB["hydration"]["keywords"])
        return format_scraped(paras, "Here is what Wikipedia says about Hydration:\n")

    # ── Sleep & Recovery ─────────────────────────────────────
    elif any(w in text for w in ["sleep", "rest", "recovery", "rest day",
                                  "overtraining", "circadian"]):
        paras = search_paragraphs(KB["sleep"]["paragraphs"],
                                  KB["sleep"]["keywords"])
        return format_scraped(paras, "Here is what Wikipedia says about Sleep:\n")

    # ── BMI ──────────────────────────────────────────────────
    elif any(w in text for w in ["bmi", "body mass index", "healthy weight",
                                  "obese", "obesity"]):
        paras = search_paragraphs(KB["bmi"]["paragraphs"],
                                  KB["bmi"]["keywords"])
        return format_scraped(paras, "Here is what Wikipedia says about BMI:\n")

    # ── Yoga / Flexibility ───────────────────────────────────
    elif any(w in text for w in ["yoga", "flexibility", "stretch",
                                  "mobility", "warm up", "cool down",
                                  "pose", "meditation"]):
        # try stretching KB first, yoga if stretch not matched
        if any(w in text for w in ["yoga", "pose", "meditation"]):
            paras = search_paragraphs(KB["yoga"]["paragraphs"],
                                      KB["yoga"]["keywords"])
            return format_scraped(paras, "Here is what Wikipedia says about Yoga:\n")
        else:
            paras = search_paragraphs(KB["stretching"]["paragraphs"],
                                      KB["stretching"]["keywords"])
            return format_scraped(paras, "Here is what Wikipedia says about Stretching:\n")

    # ── Mental Health ────────────────────────────────────────
    elif any(w in text for w in ["mental health", "anxiety", "depression",
                                  "stress", "motivation", "mood",
                                  "mindset", "well-being", "wellbeing"]):
        paras = search_paragraphs(KB["mental_health"]["paragraphs"],
                                  KB["mental_health"]["keywords"])
        return format_scraped(paras, "Here is what Wikipedia says about Mental Health:\n")

    # ── Goodbye ──────────────────────────────────────────────
    elif any(w in text for w in ["bye", "goodbye", "exit", "quit",
                                  "see you", "later", "thanks", "thank you"]):
        return ("Thanks for using the Health & Fitness Chatbot! 🏃‍♂️\n"
                "Stay active, eat well, and get enough sleep. Goodbye! 👋")

    # ── Fallback ─────────────────────────────────────────────
    else:
        return ("I did not understand that. 🤔\n"
                "Try keywords like: exercise, weight loss, protein, cardio,\n"
                "sleep, hydration, yoga, mental health, BMI, HIIT, creatine.\n"
                "Type 'help' for the full list.")


# ── Main Loop ─────────────────────────────────────────────────────────────────

def main():
    print("=" * 62)
    print("   HEALTH & FITNESS CHATBOT  (Wikipedia-Powered)   ")
    print("   Type 'bye' or 'exit' to quit                    ")
    print("=" * 62)
    print()

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nChatbot: Goodbye! Stay healthy! 👋")
            break

        if not user_input:
            print("Chatbot: Please type something. Type 'help' for topics.\n")
            continue

        response = get_response(user_input)
        print(f"\nChatbot: {response}\n")

        if any(w in user_input.lower() for w in ["bye", "goodbye", "exit", "quit"]):
            break


if __name__ == "__main__":
    main()
