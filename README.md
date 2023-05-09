# Study_projecy_Alignment
Sequence alignment program: Aligns two sequences using dynamic programming. Computes optimal score and aligned sequences. Handles optional costs. Essential for bioinformatics and genetic analysis.

# Sequence Alignment Program

[![Git Emotion](https://img.shields.io/badge/Git%20Emotion-%F0%9F%94%A5-ff69b4)](https://git-emotion.openai.com/)

The Sequence Alignment Program is a Python script that performs pairwise sequence alignment using a dynamic programming algorithm. It takes two input sequences and computes their optimal alignment score along with the aligned sequences.

## Features

- Efficient sequence alignment algorithm
- Customizable gap, match, and mismatch costs
- Support for reading sequences from a file
- Outputs alignment score and aligned sequences

## Usage

1. Clone the repository: `git clone https://github.com/your/repo.git`
2. Navigate to the project directory: `cd sequence-alignment`
3. Run the script: `python alignment.py input_file.txt [gap_cost] [match_cost] [mismatch_cost]`

   - `input_file.txt`: File containing the input sequences
   - `gap_cost` (optional): Cost for introducing a gap (default: -1)
   - `match_cost` (optional): Cost for matching characters (default: 1)
   - `mismatch_cost` (optional): Cost for mismatching characters (default: 0)

4. View the alignment score and aligned sequences in the terminal.

## Examples

```shell
python alignment.py sequences.txt -2 2 -1
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to use Git Emotion to express your excitement about this project! 😄