import random

def calculate_calories(age, gender, weight, height, activity):
    if gender == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_factor = {
        "low": 1.2,
        "medium": 1.55,
        "high": 1.9
    }

    return int(bmr * activity_factor[activity])


def generate_diet(calories, health):

    # 🌱 Healthy food database
    healthy_foods = {
        "breakfast": [
            "Oats with fruits",
            "Sprouts salad",
            "Vegetable upma",
            "Idli with sambar",
            "Whole wheat toast with peanut butter",
            "Fruit bowl with nuts"
        ],
        "lunch": [
            "Brown rice with dal & vegetables",
            "Chapati with mixed vegetable curry",
            "Vegetable khichdi",
            "Curd rice with salad",
            "Millet rice with vegetables"
        ],
        "dinner": [
            "Vegetable soup",
            "Steamed vegetables",
            "Light chapati & sabzi",
            "Paneer with salad",
            "Clear lentil soup"
        ]
    }

    advice = []

    # 🩺 Health-specific filtering
    if health == "diabetes":
        advice = [
            "Avoid sugar, sweets and white rice.",
            "Eat small meals at regular intervals.",
            "Prefer low glycemic index foods."
        ]
        healthy_foods["breakfast"] = [
            "Oats",
            "Sprouts salad",
            "Vegetable omelette",
            "Fruit bowl (low sugar fruits)"
        ]
        healthy_foods["lunch"] = [
            "Brown rice with dal",
            "Chapati with vegetables",
            "Vegetable khichdi"
        ]
        healthy_foods["dinner"] = [
            "Vegetable soup",
            "Steamed vegetables",
            "Salad"
        ]

    elif health == "bp":
        advice = [
            "Reduce salt intake.",
            "Avoid fried and processed foods.",
            "Consume potassium-rich foods."
        ]
        healthy_foods["breakfast"] += ["Banana", "Low-fat curd"]
        healthy_foods["dinner"] = [
            "Soup without salt",
            "Steamed vegetables",
            "Salad"
        ]

    elif health == "obesity":
        advice = [
            "Avoid junk food and sugary drinks.",
            "Increase fiber and protein intake.",
            "Exercise at least 30 minutes daily."
        ]
        healthy_foods["breakfast"] = [
            "Oats",
            "Sprouts salad",
            "Fruit bowl"
        ]
        healthy_foods["lunch"] = [
            "Chapati with vegetables",
            "Vegetable khichdi"
        ]
        healthy_foods["dinner"] = [
            "Soup",
            "Steamed vegetables"
        ]

    elif health == "underweight":
        advice = [
            "Increase calorie intake using healthy foods.",
            "Eat frequent small meals.",
            "Include nuts, dairy and protein."
        ]
        healthy_foods["breakfast"] += ["Milk with nuts", "Banana shake"]
        healthy_foods["lunch"] += ["Rice with dal & ghee"]
        healthy_foods["dinner"] += ["Paneer curry"]

    else:
        advice = [
            "Maintain a balanced diet.",
            "Drink 2–3 liters of water daily.",
            "Exercise regularly."
        ]

    # 🎯 Multiple options for user
    return {
        "Breakfast": random.sample(healthy_foods["breakfast"], 3),
        "Lunch": random.sample(healthy_foods["lunch"], 3),
        "Dinner": random.sample(healthy_foods["dinner"], 3)
    }, advice
