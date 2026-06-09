def colored_briks(li_ri_list: list[tuple]) -> list[tuple]:
    colored = []

    for row, (li, ri) in enumerate(li_ri_list, start=1):
        for col in range(li, ri):
            colored.append((row, col))

    return colored

def find_Neighbor_bricks(brick: tuple) -> list[tuple]:
    row, col = brick
    neighbors = []

    neighbors.append((row - 1, col))  
    neighbors.append((row + 1, col))  
    neighbors.append((row, col - 1))  
    neighbors.append((row, col + 1)) 

    return neighbors

def cal_colored_bricks_invironment(colored_bricks: list[tuple]) -> int:
    count = 0
    invironment = len(colored_bricks) * 4

    for brick in colored_bricks:
        neighbors = find_Neighbor_bricks(brick)
        for neighbor in neighbors:
            if neighbor in colored_bricks:
                count += 1

    return invironment - count

def main():
    n = int(input())
    li_ri_list = [] 
    for _ in range(n):
        li, ri = map(int, input().split())
        li_ri_list.append((li, ri))
    colored_bricks = colored_briks(li_ri_list)
    result = cal_colored_bricks_invironment(colored_bricks)
    print(result)


main()