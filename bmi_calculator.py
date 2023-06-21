# python basic program 2
# author sunil paudel
#email: sunilpaudel313@gmail.com
# support this repo and do up voting

#logic => weight/hight*height

def calculate_bmi(weight, height):
    """
    Calculates the Body Mass Index (BMI) given weight in kilograms and height in meters.
    """
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interprets the BMI value and returns a corresponding weight status category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Example usage:
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

bmi = calculate_bmi(weight, height)
weight_status = interpret_bmi(bmi)

print("BMI:", round(bmi, 2))
print("Weight status:", weight_status)
