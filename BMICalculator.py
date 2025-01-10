# BMI Calculator
def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / height^2 (m^2)
    bmi = weight / (height ** 2)
    return bmi

def categorize_bmi(bmi):
    # Categorize BMI based on standard BMI ranges
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"
def get_health_recommendation(bmi):
    """
    Provide health recommendations based on the BMI value.
    """
    if bmi < 18.5:
        return "Underweight: You may need to gain weight. Consider a balanced diet rich in nutrients."
    elif 18.5 <= bmi < 24.9:
        return "Normal weight: Maintain your current lifestyle and continue eating healthily."
    elif 25 <= bmi < 29.9:
        return "Overweight: Aim for moderate exercise and a balanced diet to reach a healthier weight."
    else:
        return "Obese: Consult a healthcare provider for personalized advice on weight management."

print("Welcome to the BMI Calculator with Health Recommendations!")
# Input from user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Display results
print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {categorize_bmi(bmi)}")
recommendation = get_health_recommendation(bmi)
print(f"Health Recommendation: {recommendation}")




