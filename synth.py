from pyo import *
import tkinter as tk

# Start server
s = Server().boot()
s.start()

# Note map
note_map = {
    'a': 261.63, 'w': 277.18, 's': 293.66, 'e': 311.13, 'd': 329.63,
    'f': 349.23, 't': 369.99, 'g': 392.00, 'y': 415.30, 'h': 440.00,
    'u': 466.16, 'j': 493.88, 'k': 523.25
}

# Settings
volume = 0.4
attack = 0.01
decay = 0.1
sustain = 0.7
release = 0.3

# Track playing notes
active_notes = {}

# Tkinter GUI
root = tk.Tk()
root.title("Polyphonic Synth")

# NOTE: These voices are entirely independent per key
def key_press(event):
    char = event.char.lower()
    if char in note_map and char not in active_notes:
        freq = note_map[char]
        amp = Fader(fadein=attack, fadeout=release, dur=2, mul=volume).play()
        osc = Sine(freq=freq, mul=amp)
        pan = Pan(osc, outs=2, pan=0.5).out()
        active_notes[char] = (amp, osc, pan)

def key_release(event):
    char = event.char.lower()
    if char in active_notes:
        amp, osc, pan = active_notes[char]
        amp.stop()
        del active_notes[char]

# Bind keys
root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)

tk.Label(root, text="Focus this window and use A–K, W–U to play").pack()

# Run GUI
root.mainloop()
s.stop()
