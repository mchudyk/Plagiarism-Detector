def window(text, num):
    """
    Converts text into the windows of num words
    
    Parameters
    ----------
    text: list of strings
        list of words used to construct windows
    num: int
        number of words in a window

    Returns
    ----------
    concat_windows: list of strings
        list of concatenated words with " " between them
    """
    
    windows = []
    
    for i in range(len(text)-num+1):
        windows.append(text[i:i+num])
        
    concat_windows = []
    for window in windows:
        concat_windows.append(' '.join(window))
        
    return concat_windows


def detect_plagiarism(text1, text2, fpr):
    """
    Checks for plagiarism between two texts using CBFs
    
    Parameters
    ----------
    text1: list of strings
        list of windows with which we are comparing 
    text2: list of strings
        list of windows that we are comparing
    fpr: float
        false positive rate

    Returns
    ----------
    float
        plagiarism detection score
    """
    
    CBF = CountingBloomFilter(fpr, len(text1))
    
    for window in text1:
        CBF.insert(window)
      
    counter = 0
    total = 0
    for window in text2:
        total += 1
        if CBF.search(window):
            counter += 1
    
    return counter/total



#creating windows for each of the versions
window_1 = window(version_1, 3)
window_2 = window(version_2, 3)
window_3 = window(version_3, 3)



print(f"CBFS: the plagiarism detection score for the 2nd version based on the 1st version = {round(detect_plagiarism(window_1, window_2, 0.0001)*100, 2)}%.")
print(f"CBFS: the plagiarism detection score for the 3nd version based on the 1st version = {round(detect_plagiarism(window_1, window_3, 0.0001)*100, 2)}%.")
print(f"CBFS: the plagiarism detection score for the 3nd version based on the 2nd version = {round(detect_plagiarism(window_2, window_3, 0.0001)*100, 2)}%.")