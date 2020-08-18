
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
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

def strip_punctuation(wstr):
    for i in punctuation_chars:
        wstr = wstr.replace('%s' % i, '')
    return wstr

def get_neg(scndstr):
    thrdstr = strip_punctuation(scndstr).split()
    count = 0
    for i in thrdstr:
        lowerc = i.lower()
        if lowerc in negative_words:
            count += 1
    return count

def get_pos(scndstr):
    thrdstr = strip_punctuation(scndstr).split()
    count = 0
    for i in thrdstr:
        lowerc = i.lower()
        if lowerc in positive_words:
            count += 1
    return count

    
with open("resulting_data.csv", 'w') as wrfile:
    fname= open("project_twitter_data.csv", 'r')
    lines = fname.readlines()
    hdr= 'Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n'
    write = wrfile.write(hdr)
    for line in lines[1:]:
        rtct = 0
        rect = 0
        posct = 0
        negct = 0
        scr = 0
        datas = line.split(",")
        rtct = int(datas[1])
        rect = int(datas[2].replace("\n",""))
        posct = get_pos(datas[0])
        negct = get_neg(datas[0])
        scr = posct - negct
        res = str(rtct) + "," + str(rect) + "," + str(posct) + "," + str(negct) + "," + str(scr)+"\n"
        write = wrfile.write(res)
