import csv
import sys
import array


def main():

    # Exit if complete argument not entered
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # Open files
    database = open(sys.argv[1], "r")
    sequence = open(sys.argv[2], "r")

    # Read through sequence for STR
    seq = sequence.read()
    seq[0:len(seq)]

    # Check if small.csv chosen or large.csv, make changes accordingly
    if sys.argv[1] == 'databases/small.csv':
        strVal = ['AGATC', 'AATG', 'TATC']
        strNum = [0, 0, 0]
        seqLen = len(seq)
        colNum = 4
    elif sys.argv[1] == 'databases/large.csv':
        strVal = ['AGATC', 'TTTTTTCT', 'AATG', 'TCTAG', 'GATA', 'TATC', 'GAAA', 'TCTG']
        strNum = [0, 0, 0, 0, 0, 0, 0, 0]
        seqLen = len(seq)
        colNum = 9
    else:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # Count strNum for each strVal
    fastComp(seq, seqLen, strVal, strNum)

    # Read into table - 2d array of rows and columns
    table = list(csv.reader(database))
    rowNum = len(table)
    row = 1
    same = True

    # Check if strNums match anyone in table
    row = 1
    # Iterate over every row
    while row != rowNum:
        same = True
        col = 1
        # Iterate over every column in said row
        while col != colNum:
            # Compare csv str values with str nums, if any dont match, set same to false
            if int(table[row][col]) != strNum[col - 1]:
                same = False
            col += 1
        # Print name if str values are same
        if same is True:
            print(table[row][0])
            break
        row += 1
    # If match not found
    if same is False:
        print("No match.")

    # Close files
    database.close()
    sequence.close()


def fastComp(seq, seqLen, strVal, strNum):
    # For every str value, go through sequence
    strNumLen = len(strNum)
    for i in range(strNumLen):
        strLen = len(strVal[i])
        tmpNum = 0
        reset = False
        x = 0
        # Iterate over length of sequence
        while x < seqLen:
            # If seq values same as strVal, 
            if seq[x: x + strLen] == strVal[i]:
                tmpNum += 1
                x += strLen
            # If tmpNum greater than previous one, update previous one
            if tmpNum > strNum[i]:
                strNum[i] = tmpNum
            # If it is not same, reset tmpNum
            if seq[x: x + strLen] != strVal[i]:
                tmpNum = 0
                x += 1


if __name__ == '__main__':
    main()