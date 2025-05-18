def painism_rule(input_text):
    """
    Calculates a pain vs pleasure score from the input text.
    Positive score means more pain than pleasure (pain > 3x pleasure).
    """
    text = input_text.lower()  # Lowercase for easy matching

    pain_words = ['pain', 'suffering', 'hurt', 'harm', 'damage', 'sad', 'unhappy']
    pleasure_words = ['pleasure', 'happy', 'joy', 'good', 'comfort', 'love']

    # Count how many pain and pleasure words appear in the text
    pain_count = sum(text.count(word) for word in pain_words)
    pleasure_count = sum(text.count(word) for word in pleasure_words)

    # Calculate score: pain minus 3 times pleasure (your painism rule)
    score = pain_count - 3 * pleasure_count

    return score


def make_decision(pain_score, input_text):
    """
    Makes a moral judgment based on:
    1) Sam Harris’s Objective Morality (promoting conscious well-being, truth, no harm)
    2) Practical Painism (pain outweighs pleasure by 3x is immoral)
    Returns: verdict, confidence (percentage), list of reasons, summary string
    """

    text = input_text.lower()

    # Objective Morality keywords (promoting well-being and avoiding harm)
    wellbeing_keywords = ["help", "heal", "protect", "support", "educate", "truth", "honest", "science", "evidence"]
    harm_keywords = ["exploit", "abuse", "manipulate", "neglect", "harm", "kill", "rape", "destroy"]

    promotes_wellbeing = any(word in text for word in wellbeing_keywords)
    causes_harm = any(word in text for word in harm_keywords)

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
        confidence = min(90 + pain_score * 5, 100)  # Confidence capped at 100%
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

    summary = (
        "Judgment based on Sam Harris-style objective morality: "
        "Does the action promote the well-being of conscious creatures using truth and logic? "
        "Painism is applied secondarily to detect if suffering outweighs pleasure by a 3:1 ratio."
    )

    return verdict, confidence, reasons, summary


def evaluate_morality(input_text):
    """
    Wrapper function that takes input text, calculates pain score,
    then makes a moral decision.
    """
    pain_score = painism_rule(input_text)
    return make_decision(pain_score, input_text)