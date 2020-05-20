#! python

def concept(value):
    note = float(value)
    if note > 10:
        return 'Invalid note!'
    elif note >= 9.1:
        return 'A'
    elif note >= 8.1:
        return 'A-'
    elif note >= 7.1:
        return 'B'
    elif note >= 6.1:
        return 'B-'
    elif note >= 5.1:
        return 'C'
    elif note >= 4.1:
        return 'C-'
    elif note >= 3.1:
        return 'D'
    elif note >= 2.1:
        return 'D-'
    elif note >= 1.1:
        return 'E'
    else:
        return 'E-'


if __name__ == "__main__":
    note = input('Entry note: ')
    concept = concept(note)
    print(f'The concept is: %s' % (concept))
