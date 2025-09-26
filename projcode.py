import math
import matplotlib.pyplot as plt
import time

# Example function implementing the pseudocode
def experimental_runtime(n):
    # Initialize dummy arrays
    a = list(range(n))
    b = list(range(n))
    
    Sum = 0
    j = 5  # corresponds to int j = 5
    start = time.perf_counter()
    
    while j < math.log(n):  # while (j < log n)
        k = 5  # corresponds to int k = 5
        while k < n:  # while (k < n)
            Sum += a[int(j)] * b[int(k)]  # Sum += a[j]*b[k]
            k = k ** 1.5  # k = k^1.5
        j = 1.2 * j  # j = 1.2 * j
    
    end = time.perf_counter()
    return end - start


# n values that work with log(n) constraint
n_values = [
     300,500,800,1200, 2000, 3500, 6000, 10000, 20000, 40000, 70000,
    120000, 200000, 350000, 500000, 750000, 1000000, 1500000, 2000000, 2500000, 3000000
]


print("Measuring experimental runtimes...")

exp_times = []

for n in n_values:
    start = time.perf_counter()
    run_algorithm(n)
    end = time.perf_counter()
    exp_times.append(end - start)

# Theoretical values for O((log log n)²)
theoretical_vals = []
for n in n_values:
    if n > math.e and math.log(n) > 1:
        log_log_n = math.log(math.log(n))
        theo_val = (log_log_n ** 2)
    #else:
        #theo_val = 0.1
    theoretical_vals.append(theo_val)

# Scale theoretical values to match experimental times
exp_avg = sum(exp_times) / len(exp_times)
theo_avg = sum(theoretical_vals) / len(theoretical_vals)
scale_factor = exp_avg / theo_avg
scaled_theoretical = [val * scale_factor for val in theoretical_vals]

# Plotting
plt.figure(figsize=(10, 6))
n_labels = [f"{n:,}" for n in n_values]

plt.plot(n_labels, exp_times, 'bo-', label='Experimental (Measured Time)', linewidth=2, markersize=6)
plt.plot(n_labels, scaled_theoretical, 'ro-', label='Scaled Theoretical O((log log n)²)', linewidth=2, markersize=6)

plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Experimental vs Theoretical Results\nTime Complexity: O((log log n)²)')
plt.legend()
plt.grid(True, alpha=0.3)

plt.ylim(0, max(exp_times) * 1.2)
plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.8f'))

plt.tight_layout()
plt.show()

# Print results
print("n\t\tExperimental Time (s)\tTheoretical\tScaled Theoretical")
print("-" * 80)
for i, n in enumerate(n_values):
    print(f"{n:>8,}\t{exp_times[i]:.8f}\t{theoretical_vals[i]:.4f}\t{scaled_theoretical[i]:.8f}")

print(f"\nScale factor: {scale_factor:.6f}")
