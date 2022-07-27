
if __name__ == "__main__":

    with open('.\input_files\maximum_path_sum_2.txt') as f:
        num_triangle = [list(map(int, x.split())) for x in f.read().split('\n')]

        for i in range(len(num_triangle)-1,0,-1):
            for j in range(len(num_triangle[i])-1):
                num_triangle[i-1][j] += max(num_triangle[i][j:j+2])

        print(num_triangle[0])