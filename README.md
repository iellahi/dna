# DNA

A Python project that that takes a DNA sequence and compares it to a list of individuals in either large.csv or small.csv to determine who the DNA most likely belongs to.

Command line usage: python dna.py databases/[file].csv sequences/[n].text
(where file is either large or small, and n is a number 1 through 20)

The program outputs the name of the individual the sequence matches to if there is a match, or that there is no match if not.

The script can also be used with your own data.

### Sample Usage:

python dna.py databases/large.csv sequences/5.txt

Lavender

python dna.py databases/small.csv sequences/15.txt

No match.
