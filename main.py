# python3

def parallel_processing(n, m, data):
    output = []
    threads = [0]*n
    time = 0
    times = [0]*n
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    for i in range(m):
        for thi in range(n):
            if threads[thi] == 0:
                output.append([thi,time])
                threads[thi] += data[i]
                break
        if 0 not in threads:
            time += min(threads)
            threads = [x - min(threads) for x in threads]

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    nm = input().split()
    n,m = int(nm[0]), int(nm[1])

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i in result:
        print(*i, sep=" ")


if __name__ == "__main__":
    main()
