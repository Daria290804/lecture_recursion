import matplotlib.pyplot as plt


# flood_fill.py

def flood_fill(image, x, y):
    """Perform flood fill algorithm."""
    rows = len(image)
    cols = len(image[0])

    # Check if pixel is out of image bounds
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return image

    # Check if pixel is background or already filled
    if image[x][y] == 0 or image[x][y] == 2:
        return image

    # Change pixel value to filled
    image[x][y] = 2

    # Recursively call flood_fill for 4 neighboring pixels
    flood_fill(image, x + 1, y)  # Down
    flood_fill(image, x - 1, y)  # Up
    flood_fill(image, x, y + 1)  # Right
    flood_fill(image, x, y - 1)  # Left

    return image


def main():
    # Example image (2D array)
    image = [
        [1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1],
        [0, 0, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 0, 1, 0, 1]
    ]

    # Starting seed coordinates (0-based index)
    x = 0
    y = 0

    # Perform flood fill
    result = flood_fill(image, x, y)

    # Print result
    for row in result:
        print(row)


if __name__ == "__main__":
    main()
