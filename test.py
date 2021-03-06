import time

duration1 = 0.0
duration2 = 0.0

answer = 'n'

for i in range(10000):
    # answer = str(input("Do you want to start over? y/n ")).lower()
    start_time = time.time()
    if answer == "y" or answer == "n":
        if answer == "n":
            # print("k. bye!")
            pass
        elif answer == "y":
            # print('end')
            pass
    else:
        # print("That's not a valid answer")
        pass
    end_time = time.time()
    duration1 += end_time - start_time

    # answer = str(input("Do you want to start over? y/n ")).lower()
    start_time = time.time()
    if answer == "y" or answer == "n":
        if answer == "n":
            # print("k. bye!")
            pass
        elif answer == "y":
            # print('end')
            pass
    else:
        # print("That's not a valid answer")
        pass
    end_time = time.time()
    duration2 = end_time - start_time


print(duration1)
print(duration2)