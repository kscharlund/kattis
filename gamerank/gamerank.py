import sys

promotion = [10000,                         # Legend
             5, 5, 5, 5, 5, 5, 5, 5, 5, 5,  # 1-10
             4, 4, 4, 4, 4,                 # 11-15
             3, 3, 3, 3, 3,                 # 16-20
             2, 2, 2, 2, 2,]                # 21-25


def main():
    games = sys.stdin.readline().strip()
    rank = 25
    stars = 0
    won = 0
    for game in games:
        if game == 'W':
            won += 1
            stars += 1
            if rank >= 6 and won >= 3:
                stars += 1
            if stars > promotion[rank]:
                stars -= promotion[rank]
                rank -= 1
                if rank == 0:
                    break
        else:
            # game == 'L'
            won = 0
            if rank <= 20:
                stars -= 1
                if stars < 0:
                    if rank < 20:
                        rank += 1
                        stars += promotion[rank]
                    else:
                        # rank == 20
                        stars = 0
    print(rank if rank else 'Legend')


main()
