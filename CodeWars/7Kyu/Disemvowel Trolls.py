def disemvowel(string_):
    for c in "aeiouAEIOU":
        string_ = string_.replace(c,'')
    return string_
