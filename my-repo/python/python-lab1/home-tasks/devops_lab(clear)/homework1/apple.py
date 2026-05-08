"""
Grocery assistant.
Note, it may be only 0-30 apples.
If other quantity is required, the answer is "Столько нет"
"""


def main():
    """Add "яблоко" word."""
    n = int(input("Сколько яблок Вам нужно?\n"))
    if n == 0:
        print("Пожалуйста,", n, "яблок")


if __name__ == "__main__":
    print("Grocery assistant")  # color this caption
    main()
