import numpy as np
import matplotlib.pyplot as plt

# Define the data
data = np.array([110, 118, 130, 121, 125, 123, 120, 112, 105, 126])

# Define the number of simulations
n_simulations = 500000

# Define a function to generate a bootstrap sample
def generate_bootstrap_sample(data):
    bootstrap_sample = np.zeros_like(data)
    for i in range(len(data)):
        random_index = np.random.randint(0, len(data), size=1)[0]
        bootstrap_sample[i] = data[random_index]
    return bootstrap_sample

# Generate the bootstrap samples
bootstrap_samples = np.array([generate_bootstrap_sample(data) for i in range(n_simulations)])

# Calculate the mean of each bootstrap sample
bootstrap_means = np.array([np.mean(bootstrap_sample) for bootstrap_sample in bootstrap_samples])

# Calculate the mean and the 95% confidence interval of the bootstrap means
mean_of_means = np.mean(bootstrap_means)
interval = np.percentile(bootstrap_means, [2.5, 97.5])

# Print the results
print("Mean distribution:", bootstrap_means)
print("Interval of mean (95% confidence):", interval)
print("Mean of mean distribution:", mean_of_means)

# Plot the mean distribution
plt.hist(bootstrap_means, bins=100)
plt.axvline(x=mean_of_means, color='r', linestyle='--', label='Mean of mean distribution')
plt.axvline(x=interval[0], color='g', linestyle='--', label='Lower bound of interval')
plt.axvline(x=interval[1], color='g', linestyle='--', label='Upper bound of interval')
plt.legend()
plt.title('Bootstrap Mean Distribution')
plt.xlabel('Mean')
plt.ylabel('Frequency')
plt.show()
