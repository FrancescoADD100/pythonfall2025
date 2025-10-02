"""Objective: Create a BMI calculator that takes a user's weight and height, calculates their BMI, and categorizes it as underweight, normal weight, overweight, or obese.
BMI Categories (Adults)
Body Mass Index (BMI) is a simple screening measure calculated from height and weight. Use these ranges for adult classification; pediatric BMI uses age-/sex-specific percentiles.
✅ Quick reference: Standard adult BMI categories
BMI levels
BMI (kg/m²)	Category
Below 18.5	Underweight
18.5 – 24.9	Normal weight (Healthy range)
25.0 – 29.9	Overweight
30.0 – 34.9	Obesity class I (Moderate)
35.0 – 39.9	Obesity class II (Severe)
≥ 40.0	Obesity class III (Very severe)
Calculate BMI
# Metric
BMI = weight_kg / (height_m ** 2)
# US (pounds & inches)
BMI = (weight_lb / (height_in ** 2)) * 703
Screening tool only; does not distinguish muscle from fat or fat distribution.
Adults ≥ 20 years; use pediatric growth charts for children/teens.
Pair with other measures when available (e.g., waist circumference, body composition).
Requirements:
Global Variables:
Conversion constants for weight (1 lb = 0.453592 kg) and height (1 in = 0.0254 m).
Main Function:
Prompt the user for their weight in pounds and height in inches.
Convert the inputs to metric units using global conversion constants.
Calculate BMI using the formula bmi = weight / (height * height).
Determine the BMI category based on standard ranges.
Display the BMI value and category.
Commenting:
Include comments to explain key parts of the code."""

# Conversion constants
lb_to_kg = 0.453592
in_to_m = 0.0254
def main():
    # Prompt user for weight and height
    weight_lb = float(input("Enter your weight in pounds: "))
    height_in = float(input("Enter your height in inches: "))

    # Convert to metric units
    weight_kg = weight_lb * lb_to_kg
    height_m = height_in * in_to_m

    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight (Healthy range)"
    elif 25 <= bmi < 30:
        category = "Overweight"
    elif 30 <= bmi < 35:
        category = "Obesity class I (Moderate)"
    elif 35 <= bmi < 40:
        category = "Obesity class II (Severe)"
    else:
        category = "Obesity class III (Very severe)"

    # Display BMI and category
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")
main()