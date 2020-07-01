'''
Substring with Concatenation of All Words
'''

from collections import Counter
def brutalfind(words, s):
    '''
    暴力解法，遍历长度为len_words * len_word的子串，进行匹配
    '''
    len_word = len(words[0])
    len_ss = len(words) * len_word
    vocab = Counter(words)
    pos = []
    for i in range(len(s)):
        ss = s[i:i+len_ss]
        if ss[:len_word] not in vocab:
            continue
        ss_tokenized = [ss[j:j+len_word] for j in range(0,len_ss,len_word)]
        vocab_ss = Counter(ss_tokenized)
        if vocab_ss == vocab:
            pos.append(i)
    print(pos)
    return pos


if __name__ == "__main__":
    words1 = ['foo','bar']
    words2 = ["word","good","best","word"]
    s1 = "barfoothefoobarman"
    s2 = "wordgoodgoodgoodbestword"
    brutalfind(words2, s2)
