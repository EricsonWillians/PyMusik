#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pymusik.py
#  
#  Copyright 2017 Ericson Willians (Rederick Deathwill) <EricsonWRP@ERICSONWRP-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import pygame.midi
import sys
from time import sleep
from random import randint

# Instruments

ACOUSTIC_GRANDPIANO = 0
BRIGHT_ACOUSTIC_PIANO = 1
ELECTRIC_GRAND_PIANO = 2
HONKY_TONK_PIANO = 3
ELECTRIC_PIANO = 4
ELECTRIC_PIANO2 = 5
HARPSICHORD = 6
CLAVI = 7
CELESTA = 8
GLOCKENSPIEL = 9
MUSIC_BOX = 10
VIBRAPHONE = 11
MARIMBA = 12
XYLOPHONE = 13
TUBULAR_BELLS = 14
DULCIMER = 15
DRAWBAR_ORGAN = 16
PERCUSSIVE_ORGAN = 17
ROCK_ORGAN = 18
CHURCH_ORGAN = 19
REED_ORGAN = 20
ACCORDION = 21
HARMONICA = 22
TANGO_ACCORDION = 23
ACOUSTIC_GUITAR_NYLON = 24
ACOUSTIC_GUITAR_STEEL = 25
ELECTRIC_GUITAR_JAZZ = 26
ELECTRIC_GUITAR_CLEAN = 27
ELECTRIC_GUITAR_MUTED = 28
OVERDRIVEN_GUITAR = 29
DISTORTION_GUITAR = 30
GUITAR_HARMONICS = 31
ACOUSTIC_BASS = 32
ELECTRIC_BASS_FINGER = 33
ELECTRIC_BASS_PICK = 34
FRETLESS_BASS = 35
SLAP_BASS1 = 36
SLAP_BASS2 = 37
SYNTH_BASS1 = 38
SYNTH_BASS2 = 39
VIOLIN = 40
VIOLA = 41
CELLO = 42
CONTRABASS = 43
TREMOLO_STRINGS = 44
PIZZICATO_STRINGS = 45
ORCHESTRAL_HARP = 46
TIMPANI = 47
STRING_ENSEMBLE1 = 48
STRING_ENSEMBLE2 = 49
SYNTHSTRINGS1 = 50
SYNTHSTRINGS2 = 51
CHOIR_AAHS = 52
VOICE_OOHS = 53
SYNTH_VOICE = 54
ORCHESTRA_HIT = 55
TRUMPET = 56
TROMBONE = 57
TUBA = 58
MUTED_TRUMPET = 59
FRENCH_HORN = 60
BRASS_SECTION = 61
SYNTHBRASS1 = 62
SYNTHBRASS2 = 63
SOPRANO_SAX = 64
ALTO_SAX = 65
TENOR_SAX = 66
BARITONE_SAX = 67
OBOE = 68
ENGLISH_HORN = 69
BASSOON = 70
CLARINET = 71
PICCOLO = 72
FLUTE = 73
RECORDER = 74
PAN_FLUTE = 75
BLOWN_BOTTLE = 76
SHAKUHACHI = 77
WHISTLE = 78
OCARINA = 79
LEAD_SQUARE = 80
LEAD_SAWTOOTH = 81
LEAD_CALLIOPE = 82
LEAD_CHIFF = 83
LEAD_CHARANG = 84
LEAD_VOICE = 85
LEAD_FIFTHS = 86
LEAD_BASS = 87
PAD1_NEW_AGE = 88
PAD2_WARM = 89
PAD3_POLYSYNTH = 90
PAD4_CHOIR = 91
PAD5_BOWED = 92
PAD6_METALLIC = 93
PAD7_HALO = 94
PAD8_SWEEP = 95
FX1_RAIN = 96
FX2_SOUNDTRACK = 97
FX3_CRYSTAL = 98
FX4_ATMOSPHERE = 99
FX5_BRIGHTNESS = 100
FX6_GOBLINS = 101
FX7_ECHOES = 102
FX8_SCIFI = 103
SITAR = 104
BANJO = 105
SHAMISEN = 106
KOTO = 107
KALIMBA = 108
BAG_PIPE = 109
FIDDLE = 110
SHANAI = 111
TINKLE_BELL = 112
AGOGO = 113
STEEL_DRUMS = 114
WOODBLOCK = 115
TAIKO_DRUM = 116
MELODIC_TOM = 117
SYNTH_DRUM = 118
REVERSE_CYMBAL = 119
GUITAR_FRET_NOISE = 120
BREATH_NOISE = 121
SEASHORE = 122
BIRD_TWEET = 123
TELEPHONE_RING = 124
HELICOPTER = 125
APPLAUSE = 126
GUNSHOT = 127

# Lengths

WHOLE = 1
SEMIBREVE = 1
HALF = 2
MINIM = 2
QUARTER = 4
CROTCHET = 4
EIGHTH = 8
QUAVER = 8
SIXTEENTH = 16
SEMIQUAVER = 16
THIRTY_SECOND = 32
DEMISEMIQUAVER = 32

# Octave positions

C = 0
C_SHARP = 1
D = 2
D_SHARP = 3
E = 4
F = 5
F_SHARP = 6
G = 7
G_SHARP = 8
A = 9
A_SHARP = 10
B = 11

class Note:
	
	def __init__(self, octave, pos, length=2):
		if octave < 0 or octave > 10:
			raise Exception("Invalid octave. There are only 11 octaves (From 0 to 10).")
		else:
			self.octave = octave
		if pos < 0 or pos > 11:
			raise Exception("Invalid octave position. There are only 12 positions (From 0 to 11).")
		else:
			self.pos = pos
		if length not in (1, 2, 4, 8, 16, 32):
			raise Exception("Invalid note length. Valid note length values are 1, 2, 4, 8, 16 and 32.")
		else:
			self.length = length
		
class Chord:
	
	def __init__(self, *notes):
		self.notes = notes
		
class Music:
	
	def __init__(self, elements):
		self.elements = elements
		
class Player:
	
	def __init__(self, instrument, music):
		self.instrument = instrument
		self.music = music
		pygame.midi.init()
		print("Pygame MIDI initiated.")
		self.out = pygame.midi.Output(0)
		self.out.set_instrument(self.instrument)
	
	def find_pitch(self, octave, pos):
		return (12 * octave) + pos
	
	def check_duration(self, note):
		if note.length == 1:
			sleep(4)
		elif note.length == 2:
			sleep(2)
		elif note.length == 4:
			sleep(1)
		elif note.length == 8:
			sleep(0.5)
		elif note.length  == 16:
			sleep(0.25)
		elif note.length  == 32:
			sleep(0.25 / 2)
	
	def play(self, loop=False):
		print("Playing the music.")
		print(self.music.elements)
		for e in self.music.elements:
			vel = randint(100, 127) # Simulating a human playing with random velocity.
			if isinstance(e, Note):
				self.out.note_on(self.find_pitch(e.octave, e.pos), vel)
				self.check_duration(e)
				self.out.note_off(self.find_pitch(e.octave, e.pos), vel)
			elif isinstance(e, Chord):
				chord_size = len(e.notes)
				for note in e.notes:
					vel = randint(100, 127)
					self.out.note_on(self.find_pitch(note.octave, note.pos), vel)
				self.check_duration(e.notes[0])
				self.out.note_off(self.find_pitch(note.octave, note.pos), vel)
		print("PyMusik finished playing the music object.")
		sleep(2)
		pygame.midi.quit()
