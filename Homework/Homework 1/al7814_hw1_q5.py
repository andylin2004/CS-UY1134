def fibs(n):
    last = 1
    second_to_last = 1

    for i in range(n):
        if i == 0:
            yield last
        else:
            if i == 1:
                yield second_to_last
            else:
                yield last + second_to_last
                temp = last
                last = second_to_last
                second_to_last += temp

if __name__ == "__main__":
    print([x for x in fibs(8)])