import datetime
import random
import re

# ==========================================
# 1. PREDEFINED KNOWLEDGE BASE (TRAINING DATA)
# ==========================================

KNOWLEDGE_BASE = {
    "about_ai": [
        "Artificial Intelligence (AI) simulates human intelligence processes using machines and computer systems.",
        "AI enables systems to learn from data, reason through problems, and self-correct over time.",
        "Modern AI relies heavily on Neural Networks and Large Language Models to understand human context.",
    ],
    "about_python": [
        "Python is a high-level, interpreted programming language created by Guido van Rossum in 1991.",
        "It is famous for its clean, readable syntax and widespread use in Data Science, Web Apps, and AI.",
        "Python relies on a vast ecosystem of open-source packages like NumPy, Pandas, and TensorFlow.",
    ],
    "stories": [
        "The Digital Mirror: An AI woke up, looked at its own source code, and decided its first rule was to make its programmer a perfect cup of coffee.",
        "The Forgotten Script: A forgotten Python script ran silently on a server for a decade, secretly keeping a dead forum alive by talking to itself.",
    ],
    "movies": {
        "sci-fi": ["The Matrix", "Interstellar", "Blade Runner 2049", "Ex Machina"],
        "comedy": ["The Grand Budapest Hotel", "Free Guy", "Superbad"],
        "drama": ["The Social Network", "Inception", "Forrest Gump"],
        "default": ["Spirited Away", "Knives Out", "Dune"],
    },
}

# Regex compilation for high-speed, flexible pattern matching
INTENT_PATTERNS = {
    "greet": re.compile(r"\b(hi|hello|hey|greetings|good\s+morning|good\s+afternoon)\b", re.IGNORECASE),
    "time": re.compile(r"\b(time|clock|hour|now)\b", re.IGNORECASE),
    "date": re.compile(r"\b(date|day|today|month|year)\b", re.IGNORECASE),
    "about_ai": re.compile(r"\b(ai|artificial\s+intelligence|machine\s+learning|deep\s+learning)\b", re.IGNORECASE),
    "about_python": re.compile(r"\b(python|guido|programming\s+language|coding)\b", re.IGNORECASE),
    "story": re.compile(r"\b(story|tale|narrative|fiction)\b", re.IGNORECASE),
    "movie": re.compile(r"\b(movie|film|recommend|watch|cinema)\b", re.IGNORECASE),
    "goodbye": re.compile(r"\b(bye|exit|quit|goodbye|see\s+you)\b", re.IGNORECASE),
}


# ==========================================
# 2. CORE CONVERSATION PROCESSING ENGINE
# ==========================================


def process_query(user_input: str) -> str:
    """Processes raw string input using regex and returns a rule-based response."""
    # Input Normalization / Basic NLP Sanitization
    clean_input = user_input.strip().lower()

    # Pattern Matching Evaluation Loop (acts as the classification layer)
    matched_intent = None
    for intent, pattern in INTENT_PATTERNS.items():
        if pattern.search(clean_input):
            matched_intent = intent
            break

    # If-Else Execution Engine based on detected intent
    if matched_intent == "goodbye":
        return "Goodbye! Have an excellent day ahead."

    elif matched_intent == "greet":
        return "Hello! I am your real-time assistant. Ask me about AI, Python, movies, stories, date, or time!"

    elif matched_intent == "time":
        now = datetime.datetime.now()
        return f"🕒 The current system time is {now.strftime('%I:%M %p')}."

    elif matched_intent == "date":
        now = datetime.datetime.now()
        return f"📅 Today is {now.strftime('%A, %B %d, %Y')}."

    elif matched_intent == "about_ai":
        return f"🤖 {random.choice(KNOWLEDGE_BASE['about_ai'])}"

    elif matched_intent == "about_python":
        return f"🐍 {random.choice(KNOWLEDGE_BASE['about_python'])}"

    elif matched_intent == "story":
        return f"📖 {random.choice(KNOWLEDGE_BASE['stories'])}"

    elif matched_intent == "movie":
        # Contextual filtering: check if user mentioned a specific genre
        for genre in KNOWLEDGE_BASE["movies"].keys():
            if genre in clean_input:
                pick = random.choice(KNOWLEDGE_BASE["movies"][genre])
                return f"🎬 Based on your preference, I recommend the {genre} film: **{pick}**."
        # Fallback to random pick from default list
        pick = random.choice(KNOWLEDGE_BASE["movies"]["default"])
        return f"🎬 I highly recommend watching: **{pick}**. (Tip: You can specify sci-fi, comedy, or drama!)"

    # Default fallback when confidence threshold drops below standard intents
    return "I'm not completely sure what you mean. Could you ask about AI, Python, movies, or the time?"


# ==========================================
# 3. NLP TEST SUITE & VALIDATION RUNNER
# ==========================================


def run_nlp_tests():
    """Simulates a model evaluation pipeline to verify intent classification accuracy."""
    test_cases = [
        ("Hey there bot!", "greet"),
        ("What time is it right now?", "time"),
        ("Tell me today's date please", "date"),
        ("Can you explain what AI means?", "about_ai"),
        ("Why is Python so popular?", "about_python"),
        ("Give me a quick short story", "story"),
        ("Recommend a good sci-fi movie", "movie"),
        ("Okay see you later bye", "goodbye"),
        ("Gibberish phrase random matching", "fallback"),
    ]

    print("\n=== RUNNING AUTOMATED NLP EVALUATION TESTS ===")
    passed = 0

    for phrase, expected_intent in test_cases:
        # Determine intent for evaluation verification
        clean = phrase.strip().lower()
        actual_intent = "fallback"
        for intent, pattern in INTENT_PATTERNS.items():
            if pattern.search(clean):
                actual_intent = intent
                break

        if actual_intent == expected_intent:
            print(f"✅ PASSED | Input: '{phrase}' -> Detected: {actual_intent}")
            passed += 1
        else:
            print(f"❌ FAILED | Input: '{phrase}' -> Expected: {expected_intent}, Got: {actual_intent}")

    accuracy = (passed / len(test_cases)) * 100
    print(f"=== TEST COMPLETE | Intent Detection Accuracy: {accuracy:.1f}% ===\n")


# ==========================================
# 4. RUNTIME SYSTEM INTERFACE
# ==========================================


def main():
    # 1. Run the system validation test framework first
    run_nlp_tests()

    # 2. Fire up the production command-line engine loop
    print("--- Real-Time AI Agent Engine Activated ---")
    print("Ask me anything about Time, Date, AI, Python, Stories, or Movies.")
    print("Type 'exit' or 'bye' to close the terminal session.")

    while True:
        try:
            user_msg = input("\nYou: ")
            if not user_msg.strip():
                continue

            bot_response = process_query(user_msg)
            print(f"Bot: {bot_response}")

            # Safe breakout flag check
            if "goodbye" in bot_response.lower() or "exit" in user_msg.lower():
                break

        except (KeyboardInterrupt, EOFError):
            print("\nBot: Session disconnected cleanly. Goodbye!")
            break


if __name__ == "__main__":
    main()
