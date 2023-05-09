import sys

def align_sequences(sequence1, sequence2):


    # Initialize the alignment table
    rows = len(sequence1) + 1
    cols = len(sequence2) + 1
    table = [[0] * cols for _ in range(rows)]

    # Fill the first row and column with gap costs
    for i in range(1, rows):
        table[i][0] = table[i-1][0] + gap_cost
    for j in range(1, cols):
        table[0][j] = table[0][j-1] + gap_cost

    # Perform the alignment
    for i in range(1, rows):
        for j in range(1, cols):
            if sequence1[i-1] == sequence2[j-1]:
                cost = match_cost
            else:
                cost = mismatch_cost
            table[i][j] = max(table[i-1][j-1] + cost, table[i-1][j] + gap_cost, table[i][j-1] + gap_cost)

    # Traceback to find the aligned sequences
    aligned_seq1 = ""
    aligned_seq2 = ""
    i, j = rows - 1, cols - 1
    while i > 0 and j > 0:
        if sequence1[i-1] == sequence2[j-1]:
            cost = match_cost
        else:
            cost = mismatch_cost
        if table[i][j] == table[i-1][j-1] + cost:
            aligned_seq1 = sequence1[i-1] + aligned_seq1
            aligned_seq2 = sequence2[j-1] + aligned_seq2
            i -= 1
            j -= 1
        elif table[i][j] == table[i-1][j] + gap_cost:
            aligned_seq1 = sequence1[i-1] + aligned_seq1
            aligned_seq2 = '-' + aligned_seq2
            i -= 1
        else:
            aligned_seq1 = '-' + aligned_seq1
            aligned_seq2 = sequence2[j-1] + aligned_seq2
            j -= 1

    while i > 0:
        aligned_seq1 = sequence1[i-1] + aligned_seq1
        aligned_seq2 = '-' + aligned_seq2
        i -= 1
    while j > 0:
        aligned_seq1 = '-' + aligned_seq1
        aligned_seq2 = sequence2[j-1] + aligned_seq2
        j -= 1

    return table[rows-1][cols-1], aligned_seq1, aligned_seq2

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the input file name as a command-line argument.")
        sys.exit(1)

    filename = sys.argv[1]

    print(sys.argv)

    with open(filename, "r") as file:
        s1 = file.readline().strip()
        s2 = file.readline().strip()
    if len(sys.argv) > 4:
        gap_cost = int(sys.argv[2])
        match_cost = int(sys.argv[3])
        mismatch_cost = int(sys.argv[4])
    else:
        gap_cost = -1
        match_cost = 1
        mismatch_cost = 0

    score, aligned_s1, aligned_s2 = align_sequences(s1, s2)

    print(f"High score: {score}")
    print(f"Sequence1:\t{aligned_s1}")
    print(f"Sequence1:\t{aligned_s2}")