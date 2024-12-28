import random


class RandomPickWithWeight:

    def __init__(self, weights):
        # Write your code here
        # The weights array, consisting of integers, is passed to the constructor
        self.running_sums = []
        running_sum = 0

        for w in weights:
            running_sum += w
            self.running_sums.append(running_sum)

        self.total_sum = running_sum


    def pick_index(self):
        target = random.randint(1, self.total_sum)
        low = 0
        high = len(self.running_sums)

        while low < high:
            mid = (low + high) // 2
            if target > self.running_sums[mid]:
                low = mid + 1
            else:
                high = mid
        
        return low

# Driver code
def main():
    counter = 900

    weights = [[1, 2, 3, 4, 5],
                [1, 12, 23, 34, 45, 56, 67, 78, 89, 90],
                [10, 20, 30, 40, 50],
                [1, 10, 23, 32, 41, 56, 62, 75, 87, 90],
                [12, 20, 35, 42, 55],
                [10, 10, 10, 10, 10],
                [10, 10, 20, 20, 20, 30],
                [1, 2, 3],
                [10, 20, 30, 40],
                [5, 10, 15, 20, 25, 30]]

    dict = {}
    for i in range(len(weights)):
        print(i + 1, ".\tList of weights: ", weights[i], ", pick_index() called ", counter, " times", "\n", sep="")
        [dict.setdefault(l, 0) for l in range(len(weights[i]))]
        sol = RandomPickWithWeight(weights[i])
        for j in range(counter):
            index = sol.pick_index()
            dict[index] += 1
        print("-"*105)
        print("\t{:<10}{:<5}{:<10}{:<5}{:<15}{:<5}{:<20}{:<5}{:<15}".format( \
            "Indexes", "|", "Weights", "|", "Occurences", "|", "Actual Frequency", "|", "Expected Frequency"))
        print("-"*105)
        for key, value in dict.items():

            print("\t{:<10}{:<5}{:<10}{:<5}{:<15}{:<5}{:<20}{:<5}{:<15}".format(key, "|", weights[i][key], "|", value, "|", \
                str(round((value/counter)*100, 2)) + "%", "|", str(round(weights[i][key]/sum(weights[i])*100, 2))+"%"))
        dict = {}
        print("\n", "-"*105, "\n", sep="")


if __name__ == '__main__':
    main()
