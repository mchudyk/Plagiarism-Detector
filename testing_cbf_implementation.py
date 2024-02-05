def memory_with_fpr (num_item):
    """
    Finds the scaling growth of memory size with FPR

    Parameters
    ----------
    num_item: int
        number of items in the set

    Returns
    ----------
    None
    """
    
    fprs = [x * 0.01 for x in range(1, 100)]
    memory_size = []
    
    for fpr in fprs:
        CBF = CountingBloomFilter(fpr, num_item)
        memory_size.append(CBF.memory_size)
    
    plt.plot(fprs, memory_size)
    plt.title(f"The memory size scaling with FPR for {num_item} items.")
    plt.xlabel("False positive rate.")
    plt.ylabel("Memory size.")
    plt.show()
    
    #calculating the theoretical answer only for one of the tests
    if num_item == 10000:
        print(f"The experimental result for fpr = 0.2 is {memory_size[19]}")
        print(f"The expected result for fpr = 0.4 is {memory_size[19]*(1/math.log2(0.2)+1)}")
        print(f"The actual result for fpr = 0.4 is {memory_size[39]}.")
        theor = memory_size[19]*(1/math.log2(0.2)+1)
        exper = memory_size[39]
        print(f"The precision of the theoretical answer is {round((1 - abs(theor-exper)/theor)*100,1)}%.")

memory_with_fpr(100)
memory_with_fpr(1000)
memory_with_fpr(10000)



def memory_with_num_item (fpr):
    """
    Finds the scaling growth of memory size with the number of items

    Parameters
    ----------
    fpr: float
        false positive rate

    Returns
    ----------
    None
    """
    
    num_items = range(1,1000)
    memory_size = []
    
    for num_item in num_items:
        CBF = CountingBloomFilter(fpr, num_item)
        memory_size.append(CBF.memory_size)
    
    plt.plot(num_items, memory_size)
    plt.title(f"The memory size scaling with num_item for the false positive rate of {fpr}.")
    plt.xlabel("Number of items.")
    plt.ylabel("Memory size.")
    plt.show()
    
    #calculating the theoretical answer only for one of the tests
    if fpr == 0.02:
        print(f"The experimental result for num_item = 200 is {memory_size[199]}")
        print(f"The expected result for num_item = 400 is {memory_size[199]*2}")
        print(f"The actual result for fpr = 0.4 is {memory_size[399]}.")
        theor = memory_size[199]*2
        exper = memory_size[399]
        print(f"The precision of the theoretical answer is {round(((1 - abs(theor-exper)/theor)*100),1)}%.")

memory_with_num_item(0.0001)
memory_with_num_item(0.02)
memory_with_num_item(0.9)


def fpr_with_hash():
    """
    Finds the scaling growth of false positive rate with the number of hash functions (from 1 to 14)

    Parameters
    ----------
    None

    Returns
    ----------
    None
    """
    
    fprs = []
    num_hash = []
    
    for k in range(1, 15):
        num_item = random.randint(1, 10000)
        CBF = CountingBloomFilter(2**(-1*k), num_item)
        num_hash.append(CBF.num_hashfn)
        fprs.append(CBF.fpr)
        
    plt.plot(num_hash, fprs)
    plt.title(f"The fpr scaling with number of hash functions used.")
    plt.xlabel("Number of hash functions.")
    plt.ylabel("False positive rate.")
    plt.show()
        
    print(f"The experimental result for num_hash = 5 is {fprs[4]}")
    print(f"The expected result for num_hash = 10 is {fprs[4]**2}")
    print(f"The actual result for fpr = 0.4 is {fprs[9]}.")
    theor = fprs[4]**2
    exper = fprs[9]
    print(f"The precision of the theoretical answer is {round(((1 - abs(theor-exper)/theor)*100),1)}%.")

    
fpr_with_hash()