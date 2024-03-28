import subprocess


def text_to_phonemes(text, language='fr', amplitude=20, speed=150, output_file='phonemes_fr.txt'):
    # Command to generate phoneme data using espeak-ng, including amplitude and speed adjustments
    command = ['espeak-ng', '-v', language, '--ipa', '-a', str(amplitude), '-s', str(speed), text]

    # Open the output file
    with open(output_file, 'w') as file:
        # Call espeak-ng and redirect the output to the file
        subprocess.run(command, stdout=file)


# Example usage
text = "Bonjour, ceci est un test."
text_to_phonemes(text)
