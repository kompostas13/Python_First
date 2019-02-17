def sumIntervals(input):
    interval = set()
    if len(input) > 0:
        for data in input:
            if len(data) == 2 and data[0] < data[1]:
                for i in range(data[0], data[1]):
                    interval.add(i)
            else:
                return 1
        return len(interval)
    else:
        return 0


sumIntervals([[1,2], [6, 10], [11, 15]])
