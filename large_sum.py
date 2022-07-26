if __name__ == "__main__":

    with open(".\input_files\large_sum.txt") as f_in:
        numbers = f_in.read().split()
        l_sum = 0

        for num in numbers:
            l_sum += int(num[:10])

        print(round(l_sum/100))
