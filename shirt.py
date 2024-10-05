import sys
import csv
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    extensions = [".jpg",".jpeg",".png"]

    if not valid_file(input_file,extensions):
        sys.exit("Not a JPEG or PNG file")
    if not valid_file(output_file,extensions):
        sys.exit("Not a JPEG or PNG file")

    if not matching_extensions(input_file, output_file):
        sys.exit("Input and output files must have the same extension")

    try:
        overlay_shirt(input_file, output_file)
    except FileNotFoundError:
        sys.exit(f"Could not find file: {input_file}")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")


def valid_file(filename, extensions):
    return any(filename.lower().endswith(ext) for ext in extensions)

def matching_extensions(file1, file2):
    return file1.split('.')[-1].lower() == file2.split('.')[-1].lower()

def overlay_shirt(input_file, output_file):
    input_image = Image.open(input_file)
    shirt_image = Image.open("shirt.png")
    resized_image = ImageOps.fit(input_image, shirt_image.size)
    resized_image.paste(shirt_image, mask=shirt_image)
    resized_image.save(output_file)
    print(f"Image saved as {output_file}")

if __name__ == "__main__":
    main()
