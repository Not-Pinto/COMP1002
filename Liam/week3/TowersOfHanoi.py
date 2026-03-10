def input_checker(message, min_output, max_output):
    output = None
    while output is None:
        print(message)
        try:
            output = int(input("Please eneter an int: "))
            if max_output is None:
                if output < min_output:
                    print("Please enter an int in range:")
                    output = None
            elif output < min_output or output > max_output:
                 print("Please enter an int in range:")
                 output = None
        except ValueError:
            print("Please only input integers")
    return output


def move_disk(n, src, dest, level, moves):
    indent = "    "
    print(indent * (level - 1) + "Recursion Level:", level)
    print(indent * (level - 1) + "Moving Disk", n, "from Source", src, "to Destination", dest)
    print(indent * (level - 1) + "n=" + str(n), "src=" + str(src), "dest=" + str(dest))
    print()
    return moves + 1


def towers(n, src, dest, level=1, moves=0):
    if n == 1:
        moves = move_disk(n, src, dest, level, moves)
    else:
        tmp = 6 - src - dest
        moves = towers(n - 1, src, tmp, level + 1, moves)
        moves = move_disk(n, src, dest, level, moves)
        moves = towers(n - 1, tmp, dest, level + 1, moves)
    return moves


def main():
    dest = None
    print()
    n = input_checker("Enter a number of disks, (pos int only)", 1, None)
    print()
    src = input_checker("Where will the disks start from (1-3)", 1, 3)
    print()
    while dest is None:
        dest = input_checker("What is the destination for the disks (1-3)", 1, 3)
        if dest == src: 
            print("Destination cannot be starting point")
            dest = None
    print()
    try:
        moves = towers(n, src, dest)
        print("There are", moves, "moves for this problem")
    except RecursionError as err:
        print("Recursion depth exceeded (n too large). Error:", err)


main()