from machine import Pin
import time

# 7-segment display pin configuration
segments = [13,12,14,27,26,25,33]  # A, B, C, D, E, F, G
digits = [21,19,18,5]  # Digit control pins
#         D4,D3,D2,D1
# Initialize pins
for pin in segments:
    Pin(pin, Pin.OUT)

for pin in digits:
    Pin(pin, Pin.OUT)


def light_number(num):
    # Turn off all segments
    for pin in segments:
        Pin(pin).value(0)  # Turn off (assuming common cathode)

    # Light up the appropriate segments for the number
    if num == 0:
        Pin(segments[0]).value(1)
        Pin(segments[1]).value(1)
        Pin(segments[2]).value(1)
        Pin(segments[3]).value(1)
        Pin(segments[4]).value(1)
        Pin(segments[5]).value(1)
    elif num == 1:
        Pin(segments[1]).value(1)
        Pin(segments[2]).value(1)
    elif num == 2:
        Pin(segments[0]).value(1)
        Pin(segments[1]).value(1)
        Pin(segments[3]).value(1)
        Pin(segments[4]).value(1)
        Pin(segments[6]).value(1)
    elif num == 3:
        Pin(segments[0]).value(1)
        Pin(segments[1]).value(1)
        Pin(segments[2]).value(1)
        Pin(segments[3]).value(1)
        Pin(segments[6]).value(1)
    elif num == 4:
        Pin(segments[1]).value(1)
        Pin(segments[2]).value(1)
        Pin(segments[5]).value(1)
        Pin(segments[6]).value(1)
    elif num == 5:
        Pin(segments[0]).value(1)
        Pin(segments[2]).value(1)
        Pin(segments[3]).value(1)
        Pin(segments[5]).value(1)
        Pin(segments[6]).value(1)
    elif num == 6:
        Pin(segments[0]).value(1)
        Pin(segments[2]).value(1)
        Pin(segments[3]).value(1)
        Pin(segments[4]).value(1)
        Pin(segments[5]).value(1)
        Pin(segments[6]).value(1)
    elif num == 7:
        Pin(segments[0]).value(1)
        Pin(segments[1]).value(1)
        Pin(segments[2]).value(1)
    elif num == 8:
        for pin in segments:
            Pin(pin).value(1)  # All segments on
    elif num == 9:
        Pin(segments[0]).value(1)
        Pin(segments[1]).value(1)
        Pin(segments[2]).value(1)
        Pin(segments[3]).value(1)
        Pin(segments[5]).value(1)
        Pin(segments[6]).value(1)


def display_number(number):
    for i in range(4):
        digit = number % 10
        number //= 10

        # Activate the corresponding digit
        for j in range(4):
            Pin(digits[j]).value(1 if j != i else 0)

        light_number(digit)
        time.sleep(0.005)  # Refresh rate for the display


# Keep the program running
while True:
    for number in range(10000):
        display_number(number)
    # = 17*100+30  # Display 17:30 #17*100=1700;1700+30 = 1730
    #display_number(heure)    
    #display_number(5791)