import time
import transcolors
import cv2
import os

SCALE_FACTOR = 0.1

def convert_ascii(pixel, r=True):
    chars = "  .:-=+*#%@"
    brightness = pixel / 255.0
    chars_index = int((len(chars) - 1) * brightness)
    return chars[chars_index]

def get_winsize():
    rows, columns = os.popen("stty size", "r").read().split()
    return int(rows), int(columns)

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

def main():
    capture = cv2.VideoCapture(1)

    while True:
        # os.system("clear")
        (ret, frame) = capture.read()
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        finalFrame = cv2.resize(frame, (0, 0), fx=SCALE_FACTOR+0.08, fy=SCALE_FACTOR)
        finalGrayFrame = cv2.resize(grayFrame, (0, 0), fx=SCALE_FACTOR+0.08, fy=SCALE_FACTOR)

        finalFrame = cv2.flip(finalFrame, 1)
        finalGrayFrame = cv2.flip(finalGrayFrame, 1)

        finalResult = ""

        finalResult += "\n" * 100

        row_int = 0
        for row in finalFrame:
            line_int = 0

            for pixel in row:
                color_escaped = transcolors.get_color_escape(pixel[2], pixel[1], pixel[0])
                finalResult += f"""{color_escaped}{convert_ascii(finalGrayFrame[row_int][line_int])}\033[0m"""
                line_int += 1

            finalResult += "\n"
            row_int += 1

        print(finalResult)
        if cv2.waitKey(1) == 27:
            break

        time.sleep(0.02)

if __name__ == "__main__":
    main()
