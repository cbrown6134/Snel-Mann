def get_file_name(num):
    zeros = ""

    if num < 10:
        zeros = "00000"
    elif num >= 10 and num <= 99:
        zeros = "0000"
    elif num >= 100 and num <= 999:
        zeros = "000"
    elif num >= 1000 and num <= 9999:
        zeros = "00"
    elif num >= 10000 and num <= 99999:
        zeros = "0"

    return "file_" + zeros + str(num) + ".txt"

def mean(counts):
    total = 0

    for i in counts:
        total += i

    d = total / len(counts)

    return d

def chi_square(counts):
    expected = mean(counts)
    
    X = 0

    for n in counts:
        X += ((n - expected) ** 2) / expected

    return X

for i in range(18000):
    file_name = get_file_name(i)
    with open('text_files/' + file_name, 'r') as f:
        contents = f.read()

        counts = [0] * 127

        for c in contents:
            n = ord(c)
            counts[n] += 1

        counts = counts[32:]
        x = chi_square(counts)

        if x > 140:
            print(file_name)
            print(x)


