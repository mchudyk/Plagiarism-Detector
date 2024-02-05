# Counting Bloom Filters: Implementation and Analysis

## Summary

### 1. Counting Bloom Filters (CBFs)

#### 1.1 Hashing and Hash Functions
Hashing transforms a key into an index in a hash table, which stores key-value pairs. Hash functions are deterministic, should distribute indexes uniformly to minimize collisions, and are crucial in minimizing false positives in Bloom Filters.

#### 1.2 Bloom Filters
A probabilistic data structure for set membership testing, offering "possibly in set" or "definitely not in set" responses. It uses an array of bits and multiple hash functions but doesn't support value deletion.

#### 1.3 Counting Bloom Filters
An extension of Bloom Filters using counters instead of bits, allowing for value deletion. It operates similarly to Bloom Filters but increments or decrements counter values during insertion or deletion.

#### 1.4 CBFs Analysis
The time complexity of operations in CBFs primarily depends on the number of hash functions, resulting in `O(k)` complexity for insertion, search, and deletion, where `k` is the number of hash functions.

### 2. Real-world Applications

#### 2.1 Malicious Accounts Detection
Detecting and storing suspicious accounts in CBFs allows for efficient and dynamic management of account reputations.

#### 2.2 Checking for Free Usernames
CBFs efficiently handle username availability checks in large databases, favoring time efficiency with acceptable false-positive rates.

### 3. Implementation in Python

#### 3.1 Class Initialization and Parameters
The `CountingBloomFilter` class is initialized with a false-positive rate and the number of items, determining the memory size and the number of hash functions.

#### 3.2 Hash Functions Definition
Hash functions are designed to be deterministic and uniformly distribute indexes. An example function uses prime numbers and polynomial accumulation.

#### 3.3 Python Implementation
The implementation includes methods for hashing, inserting, searching, and deleting items in the CBF, with considerations for uniform distribution and efficiency.

### 4. Analysis of Implementation

#### 4.1 Memory Size vs. False Positive Rate (FPR)
Memory size scales logarithmically with FPR, allowing efficient memory use based on desired accuracy.

#### 4.2 Memory Size vs. Number of Items
Memory size scales linearly with the number of items, maintaining efficiency as the dataset grows.

#### 4.3 FPR vs. Number of Hash Functions
The FPR decreases exponentially with the number of hash functions, optimizing accuracy.

#### 4.4 Access Time Scaling
Access time remains constant regardless of the number of items stored, highlighting the efficiency of CBFs in large-scale applications.
