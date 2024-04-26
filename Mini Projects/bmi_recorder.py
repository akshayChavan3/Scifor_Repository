import datetime
x = datetime.datetime(2020, 5, 17)

print(x)
def calculate_bmi(height, weight):
    """
    Function to calculate BMI based on height and weight.

    Args:
    - height (float): Height in meters.
    - weight (float): Weight in kilograms.

    Returns:
    - float: Calculated BMI.
    """
    return weight / (height ** 2)

def record_bmi_with_datetime(height, weight):
    """
    Function to record BMI along with height, weight, and date-time in a text file.

    Args:
    - height (float): Height in meters.
    - weight (float): Weight in kilograms.
    """
    bmi = calculate_bmi(height, weight)
    current_datetime = datetime.datetime.now()

    try:
        with open("bmi.txt", "a") as file:
            file.write(f"Date-Time: {current_datetime}, Height: {height} m, Weight: {weight} kg, BMI: {bmi:.2f}\n")
        print("BMI recorded successfully.")
    except Exception as e:
        print(f"An error occurred while recording BMI: {e}")

# Example usage:
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

record_bmi_with_datetime(height, weight)
