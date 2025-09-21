import math

def firebrick_count(D, t=2.5, W=4.5, H_b=9, H_s=54):
    """
    Calculate firebrick count for a cylindrical shaft.

    Parameters:
    D (float): inner bore diameter (inches)
    t (float): brick thickness, radial (default 2.5 in)
    W (float): brick width around circumference (default 4.5 in)
    H_b (float): brick height when stood upright (default 9 in)
    H_s (float): desired shaft height (inches, default 54 in)

    Returns:
    dict: course count, bricks per course, total bricks
    """
    # Midline circumference
    C = math.pi * (D + 2 * t)
    
    # Bricks per course
    N_c = math.ceil(C / W)
    
    # Number of courses
    N_courses = math.ceil(H_s / H_b)
    
    # Total bricks
    N_total = N_c * N_courses
    
    return {
        "bore_diameter_in": D,
        "shaft_height_in": H_s,
        "bricks_per_course": N_c,
        "number_of_courses": N_courses,
        "total_bricks": N_total
    }

# Example calculation: 12" bore, 54" tall shaft
example = firebrick_count(12, H_s=54)
example
