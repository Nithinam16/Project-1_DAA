import math
import matplotlib.pyplot as plt
import time
import numpy as np

def run_algorithm(n):
    a = np.arange(2000) + 1
    b = np.arange(2000) + 2
    
    j = 5.0
    Sum = 0
    
    while j < np.log(n):  # Outer loop
        k = 5.0
        while k < n:      # Inner loop
            # use modulo to stay within array bounds
            Sum += a[int(j) % len(a)] * b[int(k) % len(b)]
            k = k ** 1.5
            k = int(k)
        j = 1.2 * j
        j = int(j)
    
    return Sum

# Odd n values
n_values = [
    1001,       # 10³ + 1
    2003,       # 2×10³ + 3
    5007,       # 5×10³ + 7
    10009,      # 10⁴ + 9
    20011,      # 2×10⁴ + 11
    50013,      # 5×10⁴ + 13
    100017,     # 10⁵ + 17
    200019,     # 2×10⁵ + 19
    500021,     # 5×10⁵ + 21
    1000023,    # 10⁶ + 23
    2000027,    # 2×10⁶ + 27
    5000031,    # 5×10⁶ + 31
    10000037,   # 10⁷ + 37
    20000041,   # 2×10⁷ + 41
    50000047,   # 5×10⁷ + 47
    100000053,  # 10⁸ + 53
    200000059,  # 2×10⁸ + 59
    500000063,  # 5×10⁸ + 63
    1000000067, # 10⁹ + 67
    2000000071, # 2×10⁹ + 71
    5000000077, # 5×10⁹ + 77
    10000000079 # 10¹⁰ + 79
]

exp_times = []
successful_n_values = []

for n in n_values:
    if math.log(n) > 5:
        start = time.perf_counter()
        run_algorithm(n)
        end = time.perf_counter()
        time_taken = end - start
        exp_times.append(time_taken)
        successful_n_values.append(n)

theoretical_vals = [math.log(math.log(n)) ** 2 for n in successful_n_values]

# Scale theoretical values to match experimental times
exp_avg = sum(exp_times) / len(exp_times)
theo_avg = sum(theoretical_vals) / len(theoretical_vals)
scale_factor = exp_avg / theo_avg
scaled_theoretical = [val * scale_factor for val in theoretical_vals]

plt.figure(figsize=(14, 7))

# Plot against log(n)
log_n_values = [math.log(n) for n in successful_n_values]

plt.plot(log_n_values, exp_times, 'bo-', label='Experimental Time', linewidth=2, markersize=6)
plt.plot(log_n_values, scaled_theoretical, 'ro-', label='Scaled Theoretical O((log log n)²)', linewidth=2, markersize=6)

plt.xlabel('log(n)')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity: O((log log n)²) - Odd n values')

plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()

print("n\t\t\tTime (s)\tScaled Theoretical")
print("-" * 70)
for i, n in enumerate(successful_n_values):
    print(f"{n:>15,}\t{exp_times[i]:.8f}\t{scaled_theoretical[i]:.8f}")

print(f"\nTotal data points: {len(successful_n_values)}")
print(f"Scale factor (constant): {scale_factor:.6f}")
