#!/usr/bin/env python3

from sys import argv, stdout
from math import pow, sqrt

class   BadArgumentError(Exception):
    def __init__(self, message, errors = "BadArgumentError"):
        super().__init__(message)
        self.errors = errors

class   Poll():
    """ Definition of Poll classe """

    def __init__(self, pSize, sSize,  p):
        """ Initialise Poll's instance and check little errors """
        if pSize < 0 or sSize < 0:
            raise BadArgumentError("You must pass a probability between 0 and 100")
        if 0 < p > 100:
            raise BadArgumentError("You must pass a probability between 0 and 100")
        self.pSize = pSize
        self.sSize = sSize
        self.probability = p

    def computeValue(self):
        """ Calculate all printable value required by printValue method """
        self.variance = (((self.probability * (100 - self.probability)) / 10000)
            / self.sSize) * ((self.pSize - self.sSize) / (self.pSize - 1))
        self.confidence95 = (1.96 * sqrt(self.variance) * 2) / 2 * 100
        self.confidence99 = (2.58 * sqrt(self.variance) * 2) / 2 * 100

    def printValue(self):
        """ Print all computed value into the tab """
        print("population size:\t\t{}".format(self.pSize))
        print("sample size:\t\t\t{}".format(self.sSize))
        print("voting intentions:\t\t{:.2f}%".format(self.probability))
        print("variance:\t\t\t{:.6f}".format(self.variance))
        print("95% confidence interval:\t[{:.2f}% ; {:.2f}%]"
              .format(self.probability - self.confidence95,
                      self.probability + self.confidence95))
        print("99% confidence interval:\t[{:.2f}% ; {:.2f}%]"
              .format(self.probability - self.confidence99,
                      self.probability + self.confidence99))

def     manHelp():
    """ This function will print the help """
    print("USAGE\n\t./209poll pSize sSize p\n\nDESCRIPTION\n\tpSize\tsize of the "
          "population\n\tsSize\tsize of the sample (supposed to be representative)"
          "\n\tp\tpercentage of voting intentions for a specific candidate")

# Do not put more information in this function, it's must be clearer as possible
def     main():
    """ Main function who perform program's core action like arguments resolution """
    if len(argv) == 2:
        if argv[1] == "-h":
            manHelp()
            exit(0)
    if len(argv) is not 4:
        raise BadArgumentError("You must pass 3 valid arguments")
    obj = Poll(int(argv[1]), int(argv[2]), float(argv[3]))
    obj.computeValue()
    obj.printValue()

if __name__ == "__main__":
    try:
        main()
    except BaseException as error:
        stdout.write(str(type(error).__name__) + ": {}\n".format(error))
        exit(84)
