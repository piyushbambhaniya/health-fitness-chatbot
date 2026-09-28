# ============================================================
#  Rule-Based Health & Fitness Chatbot
#  Topic  : Health & Fitness
#  Method : if-else conditions on user input keywords
# ============================================================

def get_response(user_input):
    """
    Analyse the user's input and return an appropriate response
    using rule-based if-else conditions.
    """
    # Normalise input: lowercase and strip whitespace
    text = user_input.lower().strip()

    # ── Greetings ────────────────────────────────────────────
    if text in ["hi", "hello", "hey", "good morning", "good afternoon",
                "good evening", "howdy"]:
        return ("Hello! Welcome to the Health & Fitness Chatbot. 💪\n"
                "You can ask me about workouts, diet, weight loss, sleep, "
                "hydration, and more!\n"
                "Type 'help' to see what I can answer.")

    # ── Help / Menu ───────────────────────────────────────────
    elif text in ["help", "menu", "options", "what can you do", "topics"]:
        return (
            "Here are the topics I can help you with:\n"
            "  1. Workout / Exercise\n"
            "  2. Weight Loss / Gain\n"
            "  3. Diet / Nutrition\n"
            "  4. Protein & Supplements\n"
            "  5. Hydration / Water Intake\n"
            "  6. Sleep & Recovery\n"
            "  7. Cardio\n"
            "  8. Stretching / Flexibility\n"
            "  9. Mental Health & Fitness\n"
            " 10. BMI\n"
            "Just type a question or keyword!"
        )

    # ── Workout / Exercise ────────────────────────────────────
    elif any(word in text for word in ["workout", "exercise", "gym", "training",
                                        "lift", "weight training", "strength",
                                        "working out", "days per week",
                                        "how many days"]):
        if "beginner" in text or "start" in text or "new" in text:
            return ("For beginners, start with 3 days a week of full-body workouts.\n"
                    "Focus on compound movements: squats, push-ups, lunges, and rows.\n"
                    "Rest at least one day between sessions to allow muscle recovery.")
        elif "how many days" in text or "frequency" in text or "per week" in text:
            return ("Most people benefit from working out 3–5 days per week.\n"
                    "Beginners: 3 days | Intermediate: 4 days | Advanced: 5–6 days.\n"
                    "Always include at least 1–2 rest days for recovery.")
        elif "home" in text:
            return ("Great home workout exercises include:\n"
                    "  • Push-ups (chest & triceps)\n"
                    "  • Squats and lunges (legs)\n"
                    "  • Plank (core)\n"
                    "  • Mountain climbers (cardio + core)\n"
                    "  • Glute bridges (glutes & hamstrings)\n"
                    "No equipment needed!")
        else:
            return ("A balanced workout plan includes:\n"
                    "  • Strength training (2–3× per week)\n"
                    "  • Cardio (2–3× per week)\n"
                    "  • Flexibility / stretching (daily)\n"
                    "Consistency is more important than intensity. Stay regular!")

    # ── Weight Loss ───────────────────────────────────────────
    elif any(word in text for word in ["weight loss", "lose weight", "fat loss",
                                        "burn fat", "slim", "reduce weight"]):
        return ("Key principles of weight loss:\n"
                "  1. Caloric deficit — burn more calories than you consume.\n"
                "  2. Eat whole foods: vegetables, lean protein, whole grains.\n"
                "  3. Do both cardio AND strength training.\n"
                "  4. Sleep 7–9 hours; poor sleep raises hunger hormones.\n"
                "  5. Stay hydrated — sometimes thirst feels like hunger.\n"
                "Aim to lose 0.5–1 kg per week for sustainable results.")

    # ── Weight Gain / Muscle Gain ─────────────────────────────
    elif any(word in text for word in ["weight gain", "gain weight", "bulk",
                                        "muscle", "build muscle", "mass"]):
        return ("To gain weight / build muscle:\n"
                "  1. Eat in a caloric surplus (300–500 extra calories/day).\n"
                "  2. Prioritise protein: 1.6–2.2 g per kg of body weight.\n"
                "  3. Lift heavy with progressive overload.\n"
                "  4. Compound lifts: bench press, deadlift, squat, overhead press.\n"
                "  5. Rest adequately — muscles grow during recovery, not in the gym.")

    # ── Protein & Supplements (checked BEFORE diet to avoid substring false matches) ──
    elif any(word in text for word in ["protein", "supplement", "whey",
                                        "creatine", "bcaa", "pre-workout"]):
        if "protein" in text and ("how much" in text or "need" in text or
                                   "daily" in text):
            return ("Recommended daily protein intake:\n"
                    "  • Sedentary adults  : 0.8 g / kg body weight\n"
                    "  • Active individuals: 1.2–1.6 g / kg body weight\n"
                    "  • Athletes / lifters: 1.6–2.2 g / kg body weight\n"
                    "Good sources: eggs, chicken, fish, tofu, Greek yogurt, lentils.")
        elif "creatine" in text:
            return ("Creatine monohydrate is one of the most researched supplements.\n"
                    "  • Take 3–5 g per day consistently.\n"
                    "  • Helps increase strength and power output.\n"
                    "  • Safe for most healthy adults.\n"
                    "  • Stay well-hydrated while using it.")
        elif "whey" in text:
            return ("Whey protein is a fast-digesting protein ideal post-workout.\n"
                    "  • 20–30 g post-workout helps muscle recovery.\n"
                    "  • Not essential if you meet protein needs through food.\n"
                    "  • Alternatives: pea protein, soy protein (for vegans).")
        else:
            return ("Common fitness supplements:\n"
                    "  • Whey / plant protein — convenient protein source\n"
                    "  • Creatine — strength & power\n"
                    "  • Caffeine — endurance & focus\n"
                    "  • Omega-3 — joint health & inflammation\n"
                    "  • Vitamin D — bone health & immunity\n"
                    "Always prefer food first; supplements fill gaps.")

    # ── Diet / Nutrition ──────────────────────────────────────
    elif any(word in text for word in ["diet", "nutrition", "eat", "food",
                                        "meal", "calorie", "calories"]):
        if "how many calories" in text or "calorie intake" in text:
            return ("Daily calorie needs vary by goal:\n"
                    "  • Weight loss  : 1,500–1,800 kcal (average adult)\n"
                    "  • Maintenance  : 2,000–2,200 kcal\n"
                    "  • Weight gain  : 2,500–3,000 kcal\n"
                    "Use a TDEE calculator for a personalised number.")
        elif "healthy" in text or "best food" in text or "what to eat" in text:
            return ("Focus on nutrient-dense foods:\n"
                    "  \u2705 Lean proteins: chicken, fish, eggs, legumes\n"
                    "  \u2705 Complex carbs: oats, brown rice, sweet potato\n"
                    "  \u2705 Healthy fats: avocado, nuts, olive oil\n"
                    "  \u2705 Vegetables & fruits (fibre + micronutrients)\n"
                    "  \u274c Limit: processed foods, sugary drinks, trans fats")
        else:
            return ("Good nutrition follows the 80/20 rule:\n"
                    "  80% whole, minimally processed foods\n"
                    "  20% flexibility for enjoyment\n"
                    "Eat balanced meals with protein, carbs, and fats at every sitting.")

    # ── Hydration / Water ─────────────────────────────────────
    elif any(word in text for word in ["water", "hydration", "hydrate",
                                        "drink water", "fluid"]):
        return ("Hydration guidelines:\n"
                "  • General rule : ~8 glasses (2 litres) per day.\n"
                "  • Active people: 3–4 litres, more in hot climates.\n"
                "  • Drink water before, during, and after workouts.\n"
                "  • Signs of dehydration: dark urine, fatigue, headache.\n"
                "  • Tip: carry a water bottle as a constant reminder!")

    # ── Sleep & Recovery ──────────────────────────────────────
    elif any(word in text for word in ["sleep", "rest", "recovery",
                                        "rest day", "overtraining"]):
        if "how many hours" in text or "sleep hours" in text:
            return ("Adults need 7–9 hours of sleep per night.\n"
                    "Athletes or heavy trainers may benefit from up to 10 hours.\n"
                    "Sleep is when your muscles repair and grow — never skip rest!")
        else:
            return ("Recovery tips:\n"
                    "  • Sleep 7–9 hours every night.\n"
                    "  • Take 1–2 rest days per week from intense training.\n"
                    "  • Use active recovery: light walking, yoga, swimming.\n"
                    "  • Eat protein after workouts to aid muscle repair.\n"
                    "  • Stretch and foam-roll to reduce soreness.")

    # ── Cardio ────────────────────────────────────────────────
    elif any(word in text for word in ["cardio", "running", "jogging",
                                        "cycling", "swimming", "aerobic",
                                        "hiit", "treadmill"]):
        if "hiit" in text or "high intensity" in text:
            return ("HIIT (High-Intensity Interval Training):\n"
                    "  • Alternates short bursts of max effort with brief rest.\n"
                    "  • Example: 30 sec sprint → 30 sec walk × 10 rounds.\n"
                    "  • Burns more calories in less time than steady-state cardio.\n"
                    "  • Do 2–3 sessions per week; avoid consecutive days.")
        elif "how long" in text or "duration" in text:
            return ("Cardio duration recommendations:\n"
                    "  • Minimum: 150 min moderate OR 75 min vigorous per week.\n"
                    "  • For weight loss: aim for 200–300 min moderate per week.\n"
                    "  • Split into 30–60 min sessions for manageability.")
        else:
            return ("Cardio benefits:\n"
                    "  • Burns calories and supports weight management.\n"
                    "  • Strengthens the heart and lungs.\n"
                    "  • Reduces risk of heart disease, diabetes, and hypertension.\n"
                    "Options: running, cycling, swimming, dancing, jump rope.\n"
                    "Pick one you enjoy — consistency beats perfection!")

    # ── Stretching / Flexibility ──────────────────────────────
    elif any(word in text for word in ["stretch", "stretching", "flexibility",
                                        "yoga", "mobility", "warm up", "cool down"]):
        return ("Stretching & flexibility tips:\n"
                "  • Warm up with 5–10 min of light cardio before workouts.\n"
                "  • Cool down with static stretches (hold 20–30 sec each).\n"
                "  • Yoga or mobility work 2–3× per week improves range of motion.\n"
                "  • Key muscles to stretch: hamstrings, hip flexors, chest, shoulders.\n"
                "  • Never bounce during static stretches — risk of injury.")

    # ── Mental Health & Fitness ───────────────────────────────
    elif any(word in text for word in ["stress", "mental health", "anxiety",
                                        "depression", "motivation", "mood",
                                        "mental", "mindset"]):
        return ("Exercise and mental health:\n"
                "  • Just 30 min of moderate exercise releases endorphins.\n"
                "  • Regular activity reduces symptoms of anxiety and depression.\n"
                "  • Set small, achievable goals to build confidence and motivation.\n"
                "  • Try mindfulness or meditation alongside your fitness routine.\n"
                "  • If struggling, speak to a healthcare professional — fitness "
                "is one part of overall wellness.")

    # ── BMI ───────────────────────────────────────────────────
    elif any(word in text for word in ["bmi", "body mass index", "healthy weight",
                                        "ideal weight", "overweight", "obese"]):
        return ("BMI (Body Mass Index) categories:\n"
                "  • Underweight : BMI < 18.5\n"
                "  • Normal      : BMI 18.5 – 24.9\n"
                "  • Overweight  : BMI 25 – 29.9\n"
                "  • Obese       : BMI ≥ 30\n"
                "Formula: BMI = weight(kg) ÷ height(m)²\n"
                "Note: BMI doesn't account for muscle mass — use it as a guide only.")

    # ── Goodbye ───────────────────────────────────────────────
    elif any(word in text for word in ["bye", "goodbye", "exit", "quit",
                                        "see you", "later", "thanks", "thank you"]):
        return ("Thanks for chatting! Stay active, eat well, and rest enough. 🏃‍♂️\n"
                "Remember: small daily improvements lead to big results. Goodbye! 👋")

    # ── Fallback ──────────────────────────────────────────────
    else:
        return ("I'm not sure I understand that. 🤔\n"
                "Try asking about: workout, diet, weight loss, protein, cardio,\n"
                "sleep, hydration, stretching, mental health, or BMI.\n"
                "Type 'help' for the full topic list.")


# ── Main Loop ─────────────────────────────────────────────────────────────────
def main():
    print("=" * 60)
    print("   HEALTH & FITNESS CHATBOT   ")
    print("   Type 'bye' or 'exit' to quit   ")
    print("=" * 60)
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

        # Exit condition
        if any(word in user_input.lower() for word in
               ["bye", "goodbye", "exit", "quit"]):
            break


if __name__ == "__main__":
    main()
