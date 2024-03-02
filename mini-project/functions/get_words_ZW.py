def get_words(row):
    w = ''
    for s in row:  # For each string for each line
        if s.lower() == 'i' or s.lower() == 'a':
            w += s.lower()
        else:
            for e in s:    # For each element in a string in lower cases
                # An element is number or letter
                if e.isalpha() and e.isascii():
                    w += e.lower()
                elif e == "'" or e == "-" or e == " ":
                    w += e.lower()
                else:
                    e = " "
                    w += e
    lst = w.split()     # A list containing full_text
    return lst
