def one():
    biggest_sum = -1
    list_of_all_cals = []
    with open('input/01.txt', 'r') as f:
        lines = f.readlines()
        tmp_sum = 0
        for line in lines:
            if line != "\n":
                tmp_sum += int(line)
                # print(int(line))
            else:
                # print(tmp_sum)
                if tmp_sum >= biggest_sum:
                    biggest_sum = tmp_sum
                tmp_sum = 0

    print(tmp_sum)
    print(biggest_sum)


def two():
    biggest_sum = -1
    list_of_all_cals = []
    with open('input/01.txt', 'r') as f:
        lines = f.readlines()
        tmp_sum = 0
        for line in lines:
            if line != "\n":
                tmp_sum += int(line)
                # print(int(line))
            else:
                list_of_all_cals.append(tmp_sum)
                # print(tmp_sum)
                if tmp_sum >= biggest_sum:
                    biggest_sum = tmp_sum
                tmp_sum = 0

    list_of_all_cals.sort(reverse=True)

    end_result = list_of_all_cals[0] + \
        list_of_all_cals[1] + list_of_all_cals[2]
    print(end_result)


two()
