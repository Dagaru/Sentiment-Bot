import matplotlib.pyplot as plt
import statistics
# Test data
test_times = [827,
721,
682,
507,
523,
832,
533,
721,
714,
668,
658,
674,
685,
655,
746,
700
]

# Calculate mean, median and standard deviation
mean = statistics.mean(test_times) 
median = statistics.median(test_times) 
std_dev = statistics.stdev(test_times) 


print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)


# Create a histogram
plt.hist(test_times, bins=10)

# Add labels and title
plt.xlabel('Test Times (seconds)')
plt.ylabel('Frequency')
plt.title('DOF Test Times')

# Add mean, median, and standard deviation as vertical lines
plt.axvline(x=mean, color='red', label='Mean')
plt.axvline(x=median, color='green', label='Median')
plt.axvline(x=mean-std_dev, color='orange', linestyle='--', label='Standard Deviation')
plt.axvline(x=mean+std_dev, color='orange', linestyle='--')

# Add legend
plt.legend()

# Show plot
plt.show()