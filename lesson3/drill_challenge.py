"""
Author: Yarin Galmor
Description: Python Basics, Lesson 3, Drill Challenge
Flow Control, Loops and Functions.
"""

from PIL import Image, ImageDraw, ImageFont


def draw_image():
    width = 400
    height = 300
    color = (255, 255, 255)  # White

    with Image.new("RGB", (width, height), color) as image:
        draw = ImageDraw.Draw(image)

        # Draw a rectangle
        rectangle_coords = (100, 50, 300, 200)
        draw.rectangle(rectangle_coords, fill=(0, 255, 0), outline=(0, 0, 255))

        # Draw an ellipse
        ellipse_coords = (350, 100, 450, 200)
        draw.ellipse(ellipse_coords, fill=(255, 0, 0), outline=(0, 0, 0))

        # Save the image
        image.save("image.png")


def main():
    draw_image()


if __name__ == '__main__':
    main()

