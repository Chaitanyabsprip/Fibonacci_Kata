from fibonacci import Fibonacci

if __name__ == '__main__':
    for value in Fibonacci.series(int(input("Enter a number: "))):
        print(value)
