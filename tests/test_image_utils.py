from PIL import Image
from src.tools.image.image_utils import resize_image, rotate_image, flip_image, png_to_ico


def _make_image(path):
    img = Image.new("RGBA", (100, 100), (255, 0, 0, 255))
    img.save(path)


def test_resize_image(tmp_path):
    src = tmp_path / "src.png"
    dst = tmp_path / "dst.png"
    _make_image(src)
    resize_image(str(src), str(dst), 50, 50)
    with Image.open(dst) as im:
        assert im.size == (50, 50)


def test_rotate_image(tmp_path):
    src = tmp_path / "src.png"
    dst = tmp_path / "rot.png"
    _make_image(src)
    rotate_image(str(src), str(dst), 45)
    assert dst.exists()


def test_flip_image(tmp_path):
    src = tmp_path / "src.png"
    dst = tmp_path / "flip.png"
    _make_image(src)
    flip_image(str(src), str(dst), horizontal=True)
    assert dst.exists()


def test_png_to_ico(tmp_path):
    src = tmp_path / "src.png"
    dst = tmp_path / "out.ico"
    _make_image(src)
    png_to_ico(str(src), str(dst))
    assert dst.exists()
