# ============================================================
#  Health & Fitness Chatbot — Flask Web Application
#  Run : python app.py
#  Open: http://127.0.0.1:5000
# ============================================================

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ── Rule-Based Response Engine ────────────────────────────────

def get_response(user_input):
    text = user_input.lower().strip()

    # ── Greetings ─────────────────────────────────────────────
    if text in ["hi", "hello", "hey", "good morning", "good afternoon",
                "good evening", "howdy", "hii", "helo"]:
        return ("Hello! 👋 Welcome to the Health & Fitness Chatbot!<br>"
                "Ask me about <b>workouts, diet, weight loss, sleep, cardio, "
                "protein, BMI</b>, and more.<br>"
                "Type <b>help</b> to see all topics.")

    # ── Help ──────────────────────────────────────────────────
    elif text in ["help", "menu", "topics", "options", "what can you do"]:
        return ("Here are all the topics I can help with:<br><br>"
                "💪 Workout / Exercise<br>"
                "⚖️ Weight Loss<br>"
                "🏋️ Muscle Gain<br>"
                "🥗 Diet & Nutrition<br>"
                "🥚 Protein<br>"
                "🏃 Cardio / Aerobic<br>"
                "⚡ HIIT<br>"
                "💧 Hydration<br>"
                "😴 Sleep & Recovery<br>"
                "📏 BMI<br>"
                "🧘 Yoga & Stretching<br>"
                "🧠 Mental Health<br>"
                "💊 Creatine / Supplements<br><br>"
                "Just type a question or keyword!")

    # ── HIIT (before cardio) ──────────────────────────────────
    elif any(w in text for w in ["hiit", "high intensity interval",
                                  "interval training"]):
        return ("⚡ <b>HIIT (High-Intensity Interval Training):</b><br><br>"
                "• Alternates short bursts of max effort with brief rest.<br>"
                "• Example: 30 sec sprint → 30 sec walk × 10 rounds.<br>"
                "• Burns more calories in less time than steady-state cardio.<br>"
                "• Do <b>2–3 sessions per week</b>; avoid consecutive days.<br>"
                "• Great for fat loss and improving cardiovascular fitness.")

    # ── Cardio ────────────────────────────────────────────────
    elif any(w in text for w in ["cardio", "aerobic", "running", "jogging",
                                  "cycling", "swimming", "endurance"]):
        return ("🏃 <b>Cardio / Aerobic Exercise:</b><br><br>"
                "• Strengthens the heart and lungs.<br>"
                "• Burns calories and supports weight management.<br>"
                "• Recommended: <b>150 min moderate</b> OR <b>75 min vigorous</b> per week.<br>"
                "• Options: running, cycling, swimming, dancing, jump rope.<br>"
                "• For weight loss, aim for 200–300 min moderate cardio/week.")

    # ── Creatine / Supplements (before nutrition) ─────────────
    elif any(w in text for w in ["creatine", "supplement", "bcaa",
                                  "pre-workout", "whey protein"]):
        return ("💊 <b>Supplements:</b><br><br>"
                "• <b>Creatine monohydrate</b>: Take 3–5 g/day. Improves strength & power.<br>"
                "• <b>Whey protein</b>: 20–30 g post-workout for muscle recovery.<br>"
                "• <b>Caffeine</b>: Improves endurance and focus.<br>"
                "• <b>Omega-3</b>: Reduces inflammation, supports joint health.<br>"
                "• <b>Vitamin D</b>: Bone health and immunity.<br><br>"
                "⚠️ Always prefer food first — supplements fill gaps.")

    # ── Protein ───────────────────────────────────────────────
    elif any(w in text for w in ["protein", "amino"]):
        return ("🥚 <b>Protein Intake:</b><br><br>"
                "• Sedentary adults: <b>0.8 g / kg</b> body weight<br>"
                "• Active individuals: <b>1.2–1.6 g / kg</b><br>"
                "• Athletes / lifters: <b>1.6–2.2 g / kg</b><br><br>"
                "Best sources: eggs, chicken, fish, tofu, Greek yogurt, lentils, paneer.")

    # ── Weight Loss ───────────────────────────────────────────
    elif any(w in text for w in ["weight loss", "lose weight", "fat loss",
                                  "burn fat", "slim", "reduce weight", "overweight"]):
        return ("⚖️ <b>Weight Loss Tips:</b><br><br>"
                "1. Create a <b>caloric deficit</b> — burn more than you eat.<br>"
                "2. Eat whole foods: vegetables, lean protein, whole grains.<br>"
                "3. Combine <b>cardio + strength training</b>.<br>"
                "4. Sleep 7–9 hours — poor sleep raises hunger hormones.<br>"
                "5. Stay hydrated — thirst is often mistaken for hunger.<br><br>"
                "✅ Aim to lose <b>0.5–1 kg per week</b> for safe, sustainable results.")

    # ── Muscle Gain ───────────────────────────────────────────
    elif any(w in text for w in ["muscle", "hypertrophy", "bulk",
                                  "gain weight", "build muscle", "mass",
                                  "strength training"]):
        return ("🏋️ <b>Muscle / Weight Gain:</b><br><br>"
                "1. Eat in a <b>caloric surplus</b> (300–500 extra kcal/day).<br>"
                "2. Protein: <b>1.6–2.2 g / kg</b> body weight daily.<br>"
                "3. Lift heavy with <b>progressive overload</b>.<br>"
                "4. Compound lifts: bench press, deadlift, squat, overhead press.<br>"
                "5. Rest — muscles grow <i>during recovery</i>, not in the gym.")

    # ── Exercise / Workout ────────────────────────────────────
    elif any(w in text for w in ["workout", "exercise", "gym", "training",
                                  "working out", "fitness", "physical activity",
                                  "beginner", "days per week", "how many days"]):
        if "beginner" in text or "start" in text or "new" in text:
            return ("💪 <b>Beginner Workout Plan:</b><br><br>"
                    "• Start with <b>3 days/week</b> of full-body workouts.<br>"
                    "• Focus on: squats, push-ups, lunges, rows, planks.<br>"
                    "• Rest at least 1 day between sessions.<br>"
                    "• Consistency beats intensity — show up regularly!")
        elif "home" in text:
            return ("🏠 <b>Home Workout Exercises:</b><br><br>"
                    "• Push-ups — chest & triceps<br>"
                    "• Squats & lunges — legs<br>"
                    "• Plank — core<br>"
                    "• Mountain climbers — cardio + core<br>"
                    "• Glute bridges — glutes & hamstrings<br><br>"
                    "No equipment needed! 💪")
        else:
            return ("💪 <b>Balanced Workout Plan:</b><br><br>"
                    "• Strength training: <b>2–3× per week</b><br>"
                    "• Cardio: <b>2–3× per week</b><br>"
                    "• Stretching / flexibility: <b>daily</b><br><br>"
                    "Beginners: 3 days | Intermediate: 4 days | Advanced: 5–6 days.<br>"
                    "Always take <b>1–2 rest days</b> per week.")

    # ── Nutrition / Diet ──────────────────────────────────────
    elif any(w in text for w in ["nutrition", "diet", "food", "meal",
                                  "calorie", "calories", "eat", "nutrient"]):
        if "how many calories" in text or "calorie intake" in text:
            return ("🥗 <b>Daily Calorie Needs:</b><br><br>"
                    "• Weight loss: <b>1,500–1,800 kcal</b><br>"
                    "• Maintenance: <b>2,000–2,200 kcal</b><br>"
                    "• Weight gain: <b>2,500–3,000 kcal</b><br><br>"
                    "Use a <b>TDEE calculator</b> online for your exact number.")
        else:
            return ("🥗 <b>Healthy Nutrition Guide:</b><br><br>"
                    "✅ Lean proteins: chicken, fish, eggs, legumes<br>"
                    "✅ Complex carbs: oats, brown rice, sweet potato<br>"
                    "✅ Healthy fats: avocado, nuts, olive oil<br>"
                    "✅ Fruits & vegetables (fibre + micronutrients)<br>"
                    "❌ Limit: processed food, sugary drinks, trans fats<br><br>"
                    "Follow the <b>80/20 rule</b>: 80% clean, 20% flexible.")

    # ── Hydration ─────────────────────────────────────────────
    elif any(w in text for w in ["water", "hydration", "hydrate",
                                  "drink water", "fluid", "dehydration"]):
        return ("💧 <b>Hydration Guidelines:</b><br><br>"
                "• General rule: <b>~8 glasses (2 litres)</b> per day.<br>"
                "• Active people: <b>3–4 litres</b>, more in hot weather.<br>"
                "• Drink water before, during, and after workouts.<br>"
                "• Signs of dehydration: dark urine, fatigue, headache.<br>"
                "• 💡 Tip: Carry a water bottle as a constant reminder!")

    # ── Sleep & Recovery ──────────────────────────────────────
    elif any(w in text for w in ["sleep", "rest", "recovery",
                                  "rest day", "overtraining"]):
        return ("😴 <b>Sleep & Recovery:</b><br><br>"
                "• Adults need <b>7–9 hours</b> of sleep per night.<br>"
                "• Athletes may benefit from up to <b>10 hours</b>.<br>"
                "• Take <b>1–2 rest days</b> per week from intense training.<br>"
                "• Active recovery: light walking, yoga, swimming.<br>"
                "• Eat protein after workouts to aid muscle repair.<br>"
                "• Stretch and foam-roll to reduce soreness.")

    # ── BMI ───────────────────────────────────────────────────
    elif any(w in text for w in ["bmi", "body mass index", "healthy weight",
                                  "obese", "obesity", "ideal weight"]):
        return ("📏 <b>BMI (Body Mass Index):</b><br><br>"
                "• Underweight : BMI &lt; 18.5<br>"
                "• Normal      : BMI 18.5 – 24.9<br>"
                "• Overweight  : BMI 25 – 29.9<br>"
                "• Obese       : BMI ≥ 30<br><br>"
                "📐 Formula: <b>BMI = weight(kg) ÷ height(m)²</b><br>"
                "⚠️ BMI doesn't account for muscle mass — use as a guide only.")

    # ── Yoga / Stretching ─────────────────────────────────────
    elif any(w in text for w in ["yoga", "stretch", "stretching",
                                  "flexibility", "mobility", "warm up",
                                  "cool down", "pose", "meditation"]):
        return ("🧘 <b>Yoga & Stretching:</b><br><br>"
                "• Warm up with <b>5–10 min light cardio</b> before workouts.<br>"
                "• Cool down with static stretches (hold <b>20–30 sec</b> each).<br>"
                "• Yoga 2–3× per week improves range of motion & flexibility.<br>"
                "• Key muscles: hamstrings, hip flexors, chest, shoulders.<br>"
                "• Never bounce during static stretches — risk of injury.")

    # ── Mental Health ─────────────────────────────────────────
    elif any(w in text for w in ["mental health", "anxiety", "depression",
                                  "stress", "motivation", "mood",
                                  "mindset", "well-being", "wellbeing"]):
        return ("🧠 <b>Exercise & Mental Health:</b><br><br>"
                "• Just <b>30 min of moderate exercise</b> releases endorphins.<br>"
                "• Regular activity reduces anxiety and depression symptoms.<br>"
                "• Set small, achievable goals to build confidence.<br>"
                "• Try mindfulness or meditation alongside fitness.<br>"
                "• If struggling, speak to a healthcare professional. 💙")

    # ── Goodbye ───────────────────────────────────────────────
    elif any(w in text for w in ["bye", "goodbye", "exit", "quit",
                                  "see you", "later", "thanks", "thank you"]):
        return ("Thanks for chatting! 🏃‍♂️<br>"
                "Stay active, eat well, and get enough sleep.<br>"
                "<b>Goodbye! 👋</b>")

    # ── Fallback ──────────────────────────────────────────────
    else:
        return ("🤔 I didn't quite understand that.<br>"
                "Try asking about: <b>workout, diet, weight loss, protein, "
                "cardio, sleep, hydration, yoga, mental health, BMI, HIIT, "
                "creatine</b>.<br>Type <b>help</b> for the full topic list.")


# ── Flask Routes ──────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"response": "Please type a message."})
    bot_response = get_response(user_message)
    return jsonify({"response": bot_response})


# ── Entry Point ───────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("  Health & Fitness Chatbot")
    print("  Open: http://127.0.0.1:5000")
    print("=" * 50)
    app.run(debug=True)
