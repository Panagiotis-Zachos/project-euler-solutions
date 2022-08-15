def alpha_value(name):
    val = 0
    for c in name:
        val += ord(c) - 64
    return val

if __name__ == "__main__":
    with open('./input_files/p022_names.txt', 'r') as f:
        names = sorted(f.read().replace('"', '').split(','))

        names_total = 0
        for i in range(len(names)):
            names_total += (i+1) * alpha_value(names[i])
        
        print(names_total)
