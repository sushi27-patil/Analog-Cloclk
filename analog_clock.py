
import tkinter as tk
import math
import time

# Main window
root = tk.Tk()
root.title("Luxury Analog Clock")
root.geometry("460x520")
root.configure(bg="#080808")
root.resizable(False, False)

# Clock canvas
canvas = tk.Canvas(
    root,
    width=440,
    height=440,
    bg="#080808",
    highlightthickness=0
)
canvas.pack(pady=10)

CX, CY = 220, 210
RADIUS = 175

# Premium colors
BLACK = "#101010"
GOLD = "#FFD700"
LIGHT_GOLD = "#FFF0A0"
WHITE = "#FFFFFF"
RED = "#FF3030"


def draw_clock():
    canvas.delete("all")

    # Black clock face and golden borders
    canvas.create_oval(
        CX - RADIUS, CY - RADIUS,
        CX + RADIUS, CY + RADIUS,
        fill=BLACK, outline=GOLD, width=5
    )

    canvas.create_oval(
        CX - RADIUS + 8, CY - RADIUS + 8,
        CX + RADIUS - 8, CY + RADIUS - 8,
        outline="#806500", width=2
    )

    # Stylish Roman numerals
    roman = [
        "XII", "I", "II", "III", "IV", "V",
        "VI", "VII", "VIII", "IX", "X", "XI"
    ]

    for i, number in enumerate(roman):
        angle = math.radians(i * 30 - 90)

        x = CX + 137 * math.cos(angle)
        y = CY + 137 * math.sin(angle)

        canvas.create_text(
            x, y,
            text=number,
            font=("Georgia", 16, "bold"),
            fill=LIGHT_GOLD
        )

    # Minute markers
    for i in range(60):
        angle = math.radians(i * 6 - 90)

        outer = RADIUS - 17
        inner = outer - (13 if i % 5 == 0 else 5)

        x1 = CX + inner * math.cos(angle)
        y1 = CY + inner * math.sin(angle)
        x2 = CX + outer * math.cos(angle)
        y2 = CY + outer * math.sin(angle)

        canvas.create_line(
            x1, y1, x2, y2,
            fill=GOLD if i % 5 == 0 else "#777777",
            width=2 if i % 5 == 0 else 1
        )

    # Current time
    now = time.localtime()
    h = now.tm_hour % 12
    m = now.tm_min
    s = now.tm_sec

    # Calculate hand angles
    hour_angle = math.radians(h * 30 + m * 0.5 - 90)
    minute_angle = math.radians(m * 6 + s * 0.1 - 90)
    second_angle = math.radians(s * 6 - 90)

    # Helper to draw clock hands
    def hand(angle, length, color, width):
        x = CX + length * math.cos(angle)
        y = CY + length * math.sin(angle)

        canvas.create_line(
            CX, CY, x, y,
            fill=color,
            width=width,
            capstyle=tk.ROUND
        )

    # Hour, minute and second hands
    hand(hour_angle, 82, GOLD, 8)
    hand(minute_angle, 115, WHITE, 5)
    hand(second_angle, 137, RED, 2)

    # Center jewel
    canvas.create_oval(
        CX - 8, CY - 8,
        CX + 8, CY + 8,
        fill=GOLD, outline=WHITE, width=1
    )

    # Digital time
    digital = time.strftime("%I:%M:%S %p")

    canvas.create_text(
        CX, 410,
        text=digital,
        font=("Georgia", 19, "bold"),
        fill=GOLD
    )

    # Update every second
    root.after(1000, draw_clock)


draw_clock()
root.mainloop()
