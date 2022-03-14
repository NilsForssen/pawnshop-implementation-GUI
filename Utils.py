import os
import sys
from PIL import Image
import SoundQueue


def getResourcePath(relative_path):
    """
    Get pyinstaller resource
    """

    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)


def fetchImage(color, imgpath):
    """Fetch image from disk"""
    img = Image.open(imgpath)
    pixels = img.load()
    fullGreen = 255
    r, g, b = color
    for x in range(img.height):
        for y in range(img.width):
            _, greenVal, _, alpha = pixels[x, y]
            if greenVal:
                ratio = greenVal / fullGreen
                pixels[x, y] = (round(r * ratio), round(g * ratio), round(b * ratio), alpha)
    return img


def squeek(move):
    queue = SoundQueue.SoundQueue()
    if move[0].islower() or "P" in move:
        queue.addSound("sound/pawn.mp3")
    elif "N" in move:
        queue.addSound("sound/knight.mp3")
    elif "K" in move:
        queue.addSound("sound/king.mp3")
    elif "B" in move:
        queue.addSound("sound/bishop.mp3")
    elif "R" in move:
        queue.addSound("sound/rook.mp3")
    elif "Q" in move:
        queue.addSound("sound/queen.mp3")
    elif "O-O" in move or "O-O-O" in move:
        queue.addSound("sound/castling.mp3")

    if "x" in move:
        queue.addSound("sound/capture.mp3")
    if "=" in move:
        queue.addSound("sound/promote.mp3")
    if "+" in move:
        queue.addSound("sound/check.mp3")
    if "#" in move:
        queue.addSound("sound/checkmate.mp3")
