def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print("move "+str(n) + " from " + source + " to " + destination)
        return

    tower_of_hanoi(n - 1, source, destination, helper)
    print("move "+str(n) + " from "+ source + " to " + destination + "hiii")
    tower_of_hanoi(n-1, helper, source, destination)


print(tower_of_hanoi(3, "source","helper","destination"))