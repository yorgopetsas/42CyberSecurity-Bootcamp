# All methods take a list or a numpy.ndarray as parameter

# We are assuming that all inputs have a correct format, i.e. a list or array of numeric type
# or empty list or array. You don’t have to protect your functions against input errors.

class TinyStatistician:


    @staticmethod
    def mean(x):
        ''' computes the mean of a given non-empty list or array x, using a for-loop '''
        # The method returns the mean as a float, otherwise None if x is an empty list or
        # array. Given a vector x of dimension m × 1, the mathematical formula of its mean is:
        # Example: The sum of all values is 47 and there are 10 values. Therefore, the mean is 47 ÷ 10 = 4.7 goals per game.
        # if isinstance(list, list)
        nn = 0
        ii = 1
        result = 0
        for i, n in enumerate(x):
            nn = nn + n
        ii = ii + i
        result = nn / ii
        return float(result)
    

    @staticmethod
    def median(x):
        #  computes the median of a given non-empty list or array x. The method
        # returns the median as a float, otherwise None if x is an empty list or array.
        x = sorted(x)
        y = len(x)
        if y % 2 != 0:
            inx = y / 2
            result = x[int(inx)]
            return result
        else:
            inx = int(y / 2) - 1
            inx2 = int(y / 2)
            nn = x[inx]
            nn2 = x[inx2]
            result = (nn + nn2) / 2
            return result


    @staticmethod
    def quartiles(x):
        # computes the 1 st and 3rd quartiles of a given non-empty array x. 
        # The method returns the quartile as a float, otherwise None if x is an empty list or array.
        x = sorted(x)
        y = len(x)
        if y % 4 != 0:
            inx = y / 4
            result = x[int(inx)]
            return result
        else:
            inx = int(y / 2) - 1
            inx2 = int(y / 2)
            nn = x[inx]
            nn2 = x[inx2]
            result = (nn + nn2) / 2
            return result


    @staticmethod
    def var(x):
        # computes the variance of a given non-empty list or array x, using a forloop. 
        # The method returns the variance as a float, otherwise None if x is an empty
        # list or array. Given a vector x of dimension m × 1, the mathematical formula of itsvariance is:
        mean = sum(x) / len(x)
        res = sum((i - mean) ** 2 for i in x) / len(x)
        return res

    
    @staticmethod
    def std(x):
        # computes the standard deviation of a given non-empty list or array x,
        # using a for-loop. The method returns the standard deviation as a float, otherwise
        # None if x is an empty list or array. Given a vector x of dimension m × 1, the
        # mathematical formula of its standard deviation is:
        return TinyStatistician.var(x) ** 0.5


if __name__ == "__main__":
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    b = [4, 8, 11, 18, 22, 23, 30, 32]

    # Yorgo Tests
    # test = tstat.mean(a)
    # print(test)
    # test = tstat.median(a)
    # print(test)
    # test = tstat.median(b[:-1])
    # print(test)
    # test = tstat.median(b)
    # print(test)

    tests = [[tstat.mean(a),            82.4],
                [tstat.mean(b),            18.5],
                [tstat.median(a),          42.0],
                [tstat.median(b[:-1]),     18],
                [tstat.median(b),          20],
                # [tstat.quartile(a, 25),    10.0],
                # [tstat.quartile(a, 75),    59.0],
                [tstat.var(a),             12279.439999999999],
                [tstat.std(a),             110.81263465868862]
            ]

    for i, ele in enumerate(tests):
        color = "✅" if (ele[0] == ele[1]) else "🚨"
        print("[%d] %s - %f. Expected: %f" %(i, color, ele[0], ele[1]))