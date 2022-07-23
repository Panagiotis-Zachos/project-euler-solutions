if __name__ == "__main__":
    for a in range(1000):
        for b in range(498):
            if a < b:
                c = (a**2 + b**2)**0.5
                if c.is_integer() and b < c:
                    c = int(c)
                    if a + b + c == 1000:
                        print(a * b * c)
                        exit()