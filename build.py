import os
from sys import stderr
from PIL import Image

images = sorted(os.listdir("./images"))

frames: list[int] = []

for filename in images:
    im = Image.open("./images/" + filename)
    width, height = im.size

    frame = []

    for y in range(height):
        row = 0

        for x in range(width):
            values: tuple[int, int, int] = im.getpixel((x, y))  # pyright: ignore

            v = round((values[0] + values[1] + values[2]) / 765)
            is_on = min(1, max(0, v))  # 765 = 3*255

            row *= 2
            row += is_on

        frame.append(row)

    frames.extend(frame)
    print("finished " + filename, file=stderr)

print(len(frames))
print(len(images) * height)  # pyright: ignore

array_contents = "export const data = ["

for frame in frames:
    array_contents += str(frame) + ","

array_contents += "];\n"


def create_demo_image(frame_id: int):
    offset_i = frame_id * height

    im = Image.new("RGB", (width, height))

    for y in range(height):
        row = frames[offset_i + y]

        for x in range(width - 1, -1, -1):
            im.putpixel((x, y), (255, 255, 255) if row % 2 == 1 else (0, 0, 0))
            row //= 2

    im.show()


create_demo_image(72)

with open("./src/data.ts", "w") as f:
    f.write(array_contents)
