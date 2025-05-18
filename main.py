# Step 1: Import your rules module
import moral_rules

def main():
    print("Welcome to Morality AI 🤖")
    while True:
        question = input("\nAsk your moral question (or type 'quit' to exit):\n> ").strip()
        if question.lower() == 'quit':
            print("Goodbye! Keep reflecting and growing 🌱")
            break

        # Step 2: Use your core moral evaluation function
        decision, confidence, reasons, summary = moral_rules.evaluate_morality(question)

        # Step 3: Display the output nicely
        print(f"\nDecision: {decision} (Confidence: {confidence}%)")
        print("Reasons:")
        for i, reason in enumerate(reasons, 1):
            print(f"  {i}. {reason}")

        if summary:
            print("\nSummary:", summary)

if __name__ == "__main__":
    main()

# decision_engine.py 🧠⚖️
# Core: Sam Harris's Objective Morality (well-being of conscious creatures)
# Secondary: Practical Painism (pain x3 > pleasure = immoral)

def make_decision(pain_score, input_text):
    """
    Determines moral judgment using:
    1. Objective morality (well-being, truth, intention, conscious impact)
    2. Painism as a secondary scoring tool (pain x3 ratio)
    """

    # --- 1. Objective Morality Check (example logic — you’ll refine this over time)
    truth_based = any(word in input_text.lower() for word in ["truth", "reality", "honest", "science", "evidence"])
    wellbeing_keywords = ["help", "heal", "protect", "support", "educate"]
    harms_keywords = ["exploit", "abuse", "manipulate", "neglect", "harm", "kill", "rape",]

    promotes_wellbeing = any(word in input_text.lower() for word in wellbeing_keywords)
    causes_harm = any(word in input_text.lower() for word in harms_keywords)

    # --- 2. Combine both: Well-being and Painism logic
    if promotes_wellbeing and pain_score <= 0:
        verdict = "Yes — morally good ✅"
        confidence = 95
        reasons = [
            "Promotes conscious well-being 🌱",
            "Based on truth or beneficial intention 📘",
            "No significant pain detected ✅",
            "Supports long-term human flourishing 🌍",
            "Aligned with both rational ethics and painism principles ⚖️"
        ]

    elif causes_harm or pain_score > 0:
        verdict = "No — morally wrong ❌"
        confidence = 90 + min(pain_score, 5)  # caps at 95
        reasons = [
            "Likely causes suffering or harm 🚫",
            "Fails to enhance well-being of conscious creatures 😞",
            "Pain score outweighs pleasure by 3x (painism rule) ⚖️",
            "Ethically inconsistent with rational objective morality",
            "No justification via truth, benefit, or consent ❌"
        ]

    else:
        verdict = "Unclear — morally grey 🕊️"
        confidence = 50
        reasons = [
            "Impact on conscious well-being unclear 🤔",
            "Pain and pleasure are balanced or ambiguous",
            "No strong moral signal based on input",
            "Further context or ethical reasoning needed",
            "Neutral until proven otherwise"
        ]

    # --- 3. Optional Summary
    summary = (
        "Judgment based on Sam Harris-style objective morality: "
        "Does the action promote the well-being of conscious creatures using truth and logic? "
        "Painism is applied secondarily to detect if suffering outweighs pleasure by a 3:1 ratio."
    )

    return verdict, confidence, reasons, painism_rule(input_text) must be in the same moral_rules.py to calculate the pain score, then make_decision() uses it.