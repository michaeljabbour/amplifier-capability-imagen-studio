"""Luminance semantics, independent of the conversion implementation."""

import importlib.util
from pathlib import Path

import pytest
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "ascii_tone_converter", ROOT / "skills/imagen-studio/scripts/asciiart.py"
)
CONVERTER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CONVERTER)


@pytest.mark.parametrize(
    "invert,detailed,dark,light",
    [(False, False, "@", " "), (True, False, " ", "@"), (False, True, "$", " ")],
)
def test_extreme_source_tones_match_the_documented_ramp(tmp_path, invert, detailed, dark, light):
    source = tmp_path / "fictional-tones.png"
    image = Image.new("RGB", (32, 16))
    image.putdata([(0, 0, 0) if x < 16 else (255, 255, 255) for _ in range(16) for x in range(32)])
    image.save(source)
    lines, _ = CONVERTER.to_ascii(
        str(source), cols=16, contrast=1.0, gamma=1.0, invert=invert, detailed=detailed
    )
    assert len(lines) == 4
    assert all(len(line) == 16 for line in lines)
    assert all(line[0] == dark and line[-1] == light for line in lines)
