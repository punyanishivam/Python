def longestPalindrome(s):

    l = r = 0
    dict_ = index = {}
    max_ = ""
    odd = False
    
    while r < len(s):
        if s[r] in dict_:
            if odd and (dict_[s[r]] + 1) % 2 == 0:
                dict_[s[r]] = dict_[s[r]] + 1
            else:
                if r - l > len(max_):
                    max_ = s[l:r]
                l += 1
                dict_[s[l]] = dict_[s[l]] - 1
        else:
            dict_[s[r]] = 1
            
        r += 1
    
    return max_

print(longestPalindrome("cbbd"))
