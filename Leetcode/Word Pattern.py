def wordPattern(pattern, s):
        
    s = s.split()

    if len(pattern) != len(s):
        return False
    
    dict_ = {}
    
    for i in range(len(pattern)):
        if pattern[i] in dict_:
            if dict_[pattern[i]] != s[i]:
                return False
        elif s[i] in dict_.values():
            return False
        else:
            dict_[pattern[i]] = s[i]
            
    return True

print(wordPattern("abba", "dog dog dog dog"))
