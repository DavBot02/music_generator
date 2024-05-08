from sounddevice import play, wait
from numpy import random, linspace, sin, pi

from music_declarations import FREQUENCY_NOTE, INDEX_NOTE, TRANSITION_MATRIX


def play_tone(frequency, duration, sample_rate, amplitude):
    interval = linspace(0, duration, int(
        sample_rate * duration), False)  # time
    tone = amplitude * sin(2 * pi * frequency * interval)  # resulting wave

    play(tone, sample_rate)
    wait()


def generate_melody(starting_note, iterations):
    current_note = starting_note
    resulting_melody = []
    for iteration in range(iterations):
        resulting_melody.append(current_note)
        current_note = random.choice(len(TRANSITION_MATRIX),
                                     p=TRANSITION_MATRIX[current_note])
    return resulting_melody


def main():
    print('Generating a melody...')
    sequence = generate_melody(0, 20)

    print('Playing the melody...')
    for note in sequence:
        play_tone(FREQUENCY_NOTE[INDEX_NOTE[note]], 0.5, 44000, 0.7)


if __name__ == '__main__':
    main()
