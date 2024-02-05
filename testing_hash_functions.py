#setting quasirandom values
num_item = 5000
fpr = 0.1

CBF = CountingBloomFilter(fpr, num_item)


def generate_input(num):
    """
    Generates random quasiwords, so that each of the characters has the same
    probability of being A-Z and a-z. 
    
    Parameters:
    -----------
    num_item: int
        number of words that should be produced
    
    """
    
    words = []
    for i in range(num):
        word = ""
        word_length = random.randint(1,10)
        for j in range(word_length):
            #generating uppercase and lowercase letters
            word += chr(random.choice(list(range(65, 91)) + list(range(97, 123))))
        if word in words:
            i -= 1
        else:
            words.append(word)   

    return words


#generating two lists of the same size
items1 = generate_input(num_item//2)
items2 = generate_input(num_item//2)


for item in items1:
    CBF.insert(item)

    
indices = CBF.counters
y_values = indices



#plotting histogram showing the frequency values of indices
plt.hist(y_values, bins = 50)
plt.title("Hash values distribution.")
plt.xlabel("Number of times.")
plt.ylabel("The number of the indices.")
plt.show()   


#sampling from uniform distribution
new_y_values = [0]*len(y_values)
for i in range(len(items1)):
    for j in range(CBF.num_hashfn):
        new_y_values[random.randint(0, len(new_y_values)-1)] += 1
        
        
#plotting the histogram for the uniform distribution
plt.hist(new_y_values, bins = 50)
plt.title("Sampling from uniform distribution.")
plt.xlabel("Number of times.")
plt.ylabel("The number of the indices.")
plt.show()          
    
    
    
#calculating mistakenly found words and proving that there are no false negatives
mistakenly_found = 0

for word in items1:
    if not CBF.search(word):
        raise KeyError(f"The word {word} was not found in the set.")

for word in items2:
    if word in items1:
        continue
    if CBF.search(word):
         mistakenly_found += 1
            
print(f"There are {mistakenly_found} mistakenly found words.")
       
    
    
#Deleting elements and showing that the resulted distribution has only zeros. 
for item in items1:
     CBF.delete(item)


indices = CBF.counters
y_values = indices


plt.hist(y_values, bins = 50)
plt.title("Hash values distribution.")
plt.xlabel("Number of times.")
plt.ylabel("The number of the indices.")
plt.show()
print(f"The maximum value of indices = {max(CBF.counters)}.")





url_version_1 = 'https://bit.ly/39MurYb'
url_version_2 = 'https://bit.ly/3we1QCp'
url_version_3 = 'https://bit.ly/3vUecRn'
url_version_0 = 'https://gist.githubusercontent.com/raquelhr/78f66877813825dc344efefdc684a5d6/raw/361a40e4cd22cb6025e1fb2baca3bf7e166b2ec6/'

from requests import get

def get_txt_into_list_of_words(url):
    '''
    Cleans the text data
    Input
    ----------
    url : string
        The URL for the txt file.
        
    Returns
    -------
    data_just_words_lower_case: list
        List of "cleaned-up" words sorted by the order they appear in the original file.
    '''
    bad_chars = [';', ',', '.', '?', '!', '_', '[', ']', '(', ')', '*']
    data = get(url).text
    data = ''.join(c for c in data if c not in bad_chars)
    data_without_newlines = ''.join(c if (c not in ['\n', '\r', '\t']) else " " for c in data)
    data_just_words = [word for word in data_without_newlines.split(" ") if word != ""]
    data_just_words_lower_case = [word.lower() for word in data_just_words]
    return data_just_words_lower_case

version_1 = get_txt_into_list_of_words(url_version_1)
version_2 = get_txt_into_list_of_words(url_version_2)
version_3 = get_txt_into_list_of_words(url_version_3)
version0 = get_txt_into_list_of_words(url)




#Note: it takes a while to run the following code cells

import time

def time_with_num_item(text, fpr):
    """
    Finds the scaling growth of the access time to hashed values with the number of items stored

    Parameters
    ----------
    text: list of strings
        list of words that is collected in CBF data structure
    fpr: float
        false positive rate

    Returns
    ----------
    None
    """
    
    total_words = len(text)
    num_items = []
    times = []
    
    for i in range(1, 101):
        #taking only a fraction of words
        num_words = int(i/100*total_words)
        num_items.append(num_words)
        CBF = CountingBloomFilter(fpr, num_words)
        
        for i in range(num_words):
            CBF.insert(text[i])
        
        
        start = time.time()
        #searching for words for 100000 times
        for k in range(100000):
            index = random.randint(0, num_words-1)
            k = CBF.search(text[index])
        end = time.time()
        times.append(end-start)
        
    plt.plot(num_items, times)
    plt.title(f"The access time to hashed values scaling with the number of items stored for fpr = {fpr}.")
    plt.xlabel("Number of words.")
    plt.ylabel("Access time.")
    plt.show()
    
    #calculating the theoretical answer and comparing with the experimental
    print(f"The experimental result for num_items = 36,000 is {times[39]}")
    print(f"The expected result for num_items = 72000 is {times[39]}")
    print(f"The actual result for num_items = 72000 is {times[79]}.")
    theor = times[39]
    exper = times[79]
    print(f"The precision of the theoretical answer is {round(((1 - abs(theor-exper)/theor)*100),1)}%.")


version0 = get_txt_into_list_of_words(url)
version0 = version[:90000] #1/10 of words to decrease the running time