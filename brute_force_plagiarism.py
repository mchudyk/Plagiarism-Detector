def brute_force_plagiarism(text1, text2, num):
    """
    Checks for plagiarism between two texts using brute force algorithm
    
    Parameters
    ----------
    text1: list of strings
        list of windows with which we are comparing 
    text2: list of strings
        list of windows that we are comparing
    num: int
        number of words that form a window

    Returns
    ----------
    float
        plagiarism detection score
    """
    
    counter = 0
    
    for ind_word1 in range(len(text1)):
        word1 = text1[ind_word1]
        
        for ind_word2 in range(len(text2)):
            word2 = text2[ind_word2]
            
            if word1 == word2:
                
                text1_next = ind_word1+1
                text2_next = ind_word2+1
                same = 1
                
                while text1_next < len(text1) and text2_next < len(text2) and same < num and text1[text1_next] == text2[text2_next]:
                    text1_next = text1_next+1
                    text2_next = text2_next+1
                    same += 1
                    
                if same == num:
                    counter += 1
                    break

    return counter/len(text2)
        


print(f"CBFS: the plagiarism detection score for the 2nd version based on the 1st version = {round(detect_plagiarism(window_1, window_2, 0.0001)*100, 2)}%.")
print(f"CBFS: the plagiarism detection score for the 3nd version based on the 1st version = {round(detect_plagiarism(window_1, window_3, 0.0001)*100, 2)}%.")
print(f"CBFS: the plagiarism detection score for the 3nd version based on the 2nd version = {round(detect_plagiarism(window_2, window_3, 0.0001)*100, 2)}%.")
print('\n')
print(f"Brute Force: the plagiarism detection score for the 2nd version based on the 1st version = {round(brute_force_plagiarism(version_1, version_2, 3)*100, 2)}%.")
print(f"Brute Force: the plagiarism detection score for the 3nd version based on the 1st version = {round(brute_force_plagiarism(version_1, version_3, 3)*100, 2)}%.")
print(f"Brute Force: the plagiarism detection score for the 3nd version based on the 2nd version = {round(brute_force_plagiarism(version_2, version_3, 3)*100, 2)}%.")