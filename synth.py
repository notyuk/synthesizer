from pyo import *
import tkinter as tk

# --- Audio Setup ---
s = Server().boot()
s.start()

# Default values
freq = Sig(440)
amp = Sig(0.5)

# Envelope (ADSR)
env = Adsr(attack=0.01, decay=0.1, sustain=0.7, release=0.3, mul=amp)
osc = Sine(freq=freq, mul=env)
pan = Pan(osc, outs=2, pan=0.5).out()

# --- GUI Setup ---
root = tk.Tk()
root.title("Python Synth GUI")

# --- Functions ---
def play_note():
    env.play()

def release_note():
    env.stop()

def update_attack(val):
    env.attack = float(val)

def update_decay(val):
    env.decay = float(val)

def update_sustain(val):
    env.sustain = float(val)

def update_release(val):
    env.release = float(val)

def update_freq(val):
    freq.value = float(val)

def update_volume(val):
    amp.value = float(val)
    env.mul = amp

# --- Sliders ---
tk.Label(root, text="Frequency (Hz)").pack()
tk.Scale(root, from_=100, to=1000, resolution=1, orient=tk.HORIZONTAL, command=update_freq).pack()

tk.Label(root, text="Volume").pack()
tk.Scale(root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, command=update_volume).pack()

tk.Label(root, text="Attack").pack()
tk.Scale(root, from_=0.001, to=1, resolution=0.01, orient=tk.HORIZONTAL, command=update_attack).pack()

tk.Label(root, text="Decay").pack()
tk.Scale(root, from_=0.001, to=1, resolution=0.01, orient=tk.HORIZONTAL, command=update_decay).pack()

tk.Label(root, text="Sustain").pack()
tk.Scale(root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, command=update_sustain).pack()

tk.Label(root, text="Release").pack()
tk.Scale(root, from_=0.001, to=2, resolution=0.01, orient=tk.HORIZONTAL, command=update_release).pack()

# --- Buttons ---
tk.Button(root, text="Play Note", command=play_note).pack()
tk.Button(root, text="Release Note", command=release_note).pack()

root.mainloop()
s.stop()
