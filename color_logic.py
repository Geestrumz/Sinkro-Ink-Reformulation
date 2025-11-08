from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie2000

def calculate_delta_e_2000(lab1_tuple, lab2_tuple):
    """
    Calculates the Delta E 2000 difference between two LAB colors.

    :param lab1_tuple: A tuple (L, a, b) for the first color.
    :param lab2_tuple: A tuple (L, a, b) for the second color.
    :return: The Delta E 2000 value.
    """
    try:
        # Create LabColor objects
        color1 = LabColor(lab_l=lab1_tuple[0], lab_a=lab1_tuple[1], lab_b=lab1_tuple[2])
        color2 = LabColor(lab_l=lab2_tuple[0], lab_a=lab2_tuple[1], lab_b=lab2_tuple[2])

        # Calculate Delta E
        delta_e = delta_e_cie2000(color1, color2)
        return delta_e
    except Exception as e:
        print(f"Error calculating Delta E: {e}")
        return None

# Example usage:
# lab1 = (50, 20, -30)
# lab2 = (52, 21, -32)
# delta_e_value = calculate_delta_e_2000(lab1, lab2)
# if delta_e_value is not None:
#     print(f"Delta E 2000: {delta_e_value:.2f}")