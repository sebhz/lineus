#!/usr/bin/env python3
""" Calibration of the low position of Lineus """
import drawing_engine

de = drawing_engine.LineUsDrawEngine()
input("Press enter")
de.lower_stylus()
input("Fix pen, then press enter.")
de.reset_position()
