def separate_str(str_to_separate, delim):
    separated_str = []

    temp = str_to_separate.partition(delim)
    while 1:
        if len(temp[0]) != 0:
            separated_str.append(temp[0])
            if len(temp[2]) == 0:
                return separated_str
        else:
            return separated_str
        temp = temp[2].partition(delim)
    return separated_str


if __name__ == "__main__":
    separated_str = separate_str("test_toto_hello", "_")
    print(separated_str)
