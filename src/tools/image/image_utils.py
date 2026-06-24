from __future__ import annotations
from typing import Iterable, Tuple
from PIL import Image


def resize_image(input_path: str, output_path: str, width: int, height: int) -> None:
    if width <= 0 or height <= 0:
        raise ValueError("width and height must be positive integers")
    with Image.open(input_path) as im:
        resized = im.resize((width, height), Image.LANCZOS)
        resized.save(output_path)


def rotate_image(input_path: str, output_path: str, degrees: int) -> None:
    with Image.open(input_path) as im:
        rotated = im.rotate(degrees, expand=True)
        rotated.save(output_path)


def flip_image(input_path: str, output_path: str, horizontal: bool = True) -> None:
    with Image.open(input_path) as im:
        if horizontal:
            flipped = im.transpose(Image.FLIP_LEFT_RIGHT)
        else:
            flipped = im.transpose(Image.FLIP_TOP_BOTTOM)
        flipped.save(output_path)


def png_to_ico(input_path: str, output_path: str, sizes: Iterable[Tuple[int, int]] = ((256, 256),)) -> None:
    with Image.open(input_path) as im:
        im.save(output_path, format="ICO", sizes=list(sizes))
