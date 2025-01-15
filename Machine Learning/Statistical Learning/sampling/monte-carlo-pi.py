import random

def monte_carlo_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        # Generate random point (x, y) inside the square
        x, y = random.random(), random.random()
        
        # Check if the point is inside the unit circle
        if x**2 + y**2 <= 1:
            inside_circle += 1
    
    # Estimate pi
    # ratio = area of circle / area of square = (pi * r^2) / ((2r)^2) = pi / 4
    # Hence, pi = 4 * ratio
    ratio = inside_circle / num_samples
    pi_estimate = 4 * ratio
    return pi_estimate

# Run the simulation with a large number of samples
num_samples = 1000000
pi_estimate = monte_carlo_pi(num_samples)

# Print the estimated value of pi up to 10 digits
print(f"Estimated value of pi: {pi_estimate:.10f}")
