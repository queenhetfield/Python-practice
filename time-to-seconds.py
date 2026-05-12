""" Function to convert hours and mnutes into seconds.
Two alternate implementations: with single and double inputs.
"""
def to_seconds(hours, mins):
    mts = int(mins) * 60 #minutes to seconds
    hts = int(hours) * 3600 #hours to seconds

    return mts + hts

#single in input:
"""if __name__ == "__main__":
    hours, mins = input('Please enter hours and minutes (separated by space)\n').split()
    result = to_seconds(hours, mins)
    print(f'Total number of seconds:{result}')"""

#double inputs:
if __name__ == "__main__":
    hours = input('Please enter number of hours\n')
    mins = input('Please enter number of minutes\n')
    result = to_seconds(hours, mins)
    print(f'Total number of seconds:{result}')
    