punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(s) :
    if s == '' :
        return s
    lst = []
    for char in  punctuation_chars :
        if lst == [] :
            s1 = s.replace(char,'')
            if s1 != s :
                lst.append(s1)
        else :
            s1 = lst[-1].replace(char,'')
            if s1 != lst[-1] :
                lst.append(s1)
    if lst == [] :
        return s
    return lst[-1]

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
def get_pos(s) :
    count = 0
    l_wrds = s.split()
    for i in range(len(l_wrds)) :
        l_wrds[i] = strip_punctuation( l_wrds[i] ).lower()
        if l_wrds[i] in positive_words :
            count += 1
    return count

def get_neg(s) :
    count = 0
    l_wrds = s.split()
    for i in range(len(l_wrds)) :
        l_wrds[i] = strip_punctuation( l_wrds[i] ).lower()
        if l_wrds[i] in negative_words :
            count += 1
    return count

with open( 'project_twitter_data.csv' , 'r' ) as gfile :
    lst_tweets = gfile.readlines()    
    lst_t = []
    
    for string in lst_tweets :
        s1 = string.strip()
        lst_3 = s1.split(',')
        lst_t.append(lst_3)
    del lst_t[0]    
        
    for string in lst_t :
        lst_w_t = string[0].split()
        for i in range(len(lst_w_t)) :
            lst_w_t[i] = strip_punctuation(lst_w_t[i]).lower()
        string[0] = ' '.join(lst_w_t)
        string[1] = int(string[1])
        string[2] = int(string[2])
        string.append(get_pos(string[0]))
        string.append(get_neg(string[0]))
        string.append(string[3]-string[4])
    
    myfile = open('resulting_data.csv' , 'w')
    myfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
    myfile.write('\n')
    for s in lst_t :
        string = str(s[1]) + ',' + str(s[2]) + ',' + str(s[3]) + ',' + str(s[4]) + ',' + str(s[5])
        myfile.write(string + '\n' )
         
    myfile.close()
