def half_pyramid(n: int, char: str) -> None:
    for i in range(1, n+1):
        print(char * i)

def pyramid(n: int, char: str) -> None:
    for i in range(1, n+1):
        print(" " * (n - i) + char * (2 * i - 1))

if __name__ == "__main__":
    n = int(input("Enter the number of rows for the half pyramid: "))
    char = input("Enter the character to use for the pyramid: ")
    half_pyramid(n, char)
    pyramid(n, char)