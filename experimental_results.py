num_items = []
CBFs_times = []
brute_force_times = []

#iterating for n, where n/100 is a fraction of a version1 document
for n in range(1,101):
    text = version_1[:int((n/100)*len(version_1))]
    num_items.append(len(text))
    
    #time to calculate the score using CBFs
    start = time.time()
    percentage = detect_plagiarism(text, text, 0.01)
    end = time.time()
    CBFs_times.append(end-start)
    
    #time to calculate the score using brute force
    start = time.time()
    percentage = brute_force_plagiarism(text, text, 4)
    end = time.time()
    brute_force_times.append(end-start)



#plotting the running time vs. number of words for CBFs data structure
plt.plot(num_items, CBFs_times)
plt.title(f"The running time using CBFs data structure for fpr = 0.01.")
plt.xlabel("Number of words.")
plt.ylabel("Running time.")
plt.show()


#I got index 23 by calculating 20,000/8461-1 = 23.6-1 = ±23, where len(version_1) = 8461
print(f"The experimental result for number of words of 20,0000 is {CBFs_times[23]}")
print(f"The expected result for number of words of 40,000 is {2*CBFs_times[23]}")
print(f"The actual result for number of words of 40,000 is {CBFs_times[46]}.")
theor = 2*CBFs_times[23]
exper = CBFs_times[46]
print(f"The precision of the theoretical answer is {round(((1 - abs(theor-exper)/theor)*100),1)}%.")


#plotting the running time vs. number of words for brute force approach
plt.plot(num_items, brute_force_times)
plt.title(f"The running time using brute force approach.")
plt.xlabel("Number of words.")
plt.ylabel("Running time.")
plt.show()


print(f"The experimental result for number of words of 20,0000 is {brute_force_times[23]}")
print(f"The expected result for number of words of 40,000 is {4*brute_force_times[23]}")
print(f"The actual result for number of words of 40,000 is {brute_force_times[46]}.")
theor = 4*brute_force_times[23]
exper = brute_force_times[46]
print(f"The precision of the theoretical answer is {round(((1 - abs(theor-exper)/theor)*100),1)}%.")
