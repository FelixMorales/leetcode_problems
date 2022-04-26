def strStr(haystack: str, needle: str) -> int:
    len_needle = len(needle)
    len_haystack = len(haystack)

    result = -1

    if len_needle == 0:
        return 0

    if len(haystack.replace(needle, '')) == len_haystack:
        return -1

    for i in range(len_haystack):

        c = haystack[i]

        if c == needle[0] and i+len_needle <= len_haystack:
            subs_str = haystack[i:i+len_needle]

            if subs_str == needle:
                result = i
                break

    return result

r = strStr("a", "a")
print(r)
    