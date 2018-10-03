def run_problem(n=1000, multiple_set={3, 5}):
    return sum(
        num
        for num in range(1000)
        if any(
            num % x == 0
            for x in multiple_set
        )
    )

if __name__ == '__main__':
    print(run_problem(n=1000, multiple_set={3,5}))
