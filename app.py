import tkinter as tk
import math

# -----------------------------
# Window
# -----------------------------
root = tk.Tk()
root.title("Color3D")
root.geometry("1100x700")
root.configure(bg="#120b3d")

canvas = tk.Canvas(
    root,
    width=1100,
    height=700,
    bg="#120b3d",
    highlightthickness=0
)
canvas.pack(fill="both", expand=True)


# -----------------------------
# Gradient Background
# -----------------------------
def background():
    for i in range(70):
        color = f"#{20 + i // 4:02x}{10 + i // 5:02x}{70 + i * 2:02x}"
        canvas.create_rectangle(
            0, i * 10,
            1100, (i + 1) * 10,
            fill=color,
            outline=""
        )


# -----------------------------
# Navigation
# -----------------------------
def navigation():
    canvas.create_text(
        70, 55,
        text="◆ Color3D",
        fill="white",
        font=("Arial", 28, "bold"),
        anchor="w"
    )

    links = ["Home", "About", "Services", "Gallery", "Contact"]

    x = 430

    for link in links:
        canvas.create_text(
            x, 55,
            text=link,
            fill="white",
            font=("Arial", 15, "bold")
        )
        x += 105

    canvas.create_rectangle(
        930, 30,
        1045, 75,
        fill="#e843c6",
        outline=""
    )

    canvas.create_text(
        987, 52,
        text="Get Started",
        fill="white",
        font=("Arial", 12, "bold")
    )


# -----------------------------
# Hero Text
# -----------------------------
def hero_text():
    canvas.create_text(
        80, 190,
        text="Welcome to",
        fill="white",
        font=("Arial", 48, "bold"),
        anchor="w"
    )

    canvas.create_text(
        80, 250,
        text="Color3D",
        fill="#ff4fc3",
        font=("Arial", 62, "bold"),
        anchor="w"
    )

    canvas.create_text(
        80, 335,
        text="A colorful and interactive",
        fill="#ddddff",
        font=("Arial", 19),
        anchor="w"
    )

    canvas.create_text(
        80, 370,
        text="3D experience made with Python.",
        fill="#ddddff",
        font=("Arial", 19),
        anchor="w"
    )

    # Explore button
    canvas.create_rectangle(
        80, 420,
        230, 470,
        fill="#e83fbd",
        outline=""
    )

    canvas.create_text(
        155, 445,
        text="Explore More",
        fill="white",
        font=("Arial", 14, "bold")
    )

    # Learn button
    canvas.create_rectangle(
        250, 420,
        370, 470,
        outline="white",
        width=2
    )

    canvas.create_text(
        310, 445,
        text="Learn More",
        fill="white",
        font=("Arial", 14, "bold")
    )


# -----------------------------
# 3D Cube
# -----------------------------
angle = 0


def rotate_point(x, y, z, angle):
    """Rotate a 3D point around Y axis."""

    rad = math.radians(angle)

    new_x = x * math.cos(rad) - z * math.sin(rad)
    new_z = x * math.sin(rad) + z * math.cos(rad)

    return new_x, y, new_z


def project(x, y, z):
    """Convert 3D coordinates to screen coordinates."""

    scale = 1.0 + z / 800

    screen_x = 790 + x * scale
    screen_y = 350 + y * scale

    return screen_x, screen_y


def draw_cube():
    canvas.delete("cube")

    size = 130

    points = [
        (-size, -size, -size),
        (size, -size, -size),
        (size, size, -size),
        (-size, size, -size),

        (-size, -size, size),
        (size, -size, size),
        (size, size, size),
        (-size, size, size)
    ]

    rotated = []

    for x, y, z in points:
        rotated.append(
            rotate_point(x, y, z, angle)
        )

    projected = [
        project(x, y, z)
        for x, y, z in rotated
    ]

    faces = [
        ([0, 1, 2, 3], "#ff24b9"),
        ([4, 5, 6, 7], "#2865ff"),
        ([0, 4, 7, 3], "#8d35ff"),
        ([1, 5, 6, 2], "#00aaff"),
        ([0, 1, 5, 4], "#ff55d0"),
        ([3, 2, 6, 7], "#5d36e8")
    ]

    # Draw faces
    for face, color in faces:
        coords = []

        for index in face:
            coords.extend(projected[index])

        canvas.create_polygon(
            coords,
            fill=color,
            outline="#ffffff",
            width=2,
            tags="cube"
        )

    # Glow around cube
    canvas.create_oval(
        650, 230,
        930, 510,
        outline="#9d42ff",
        width=4,
        tags="cube"
    )

    # Continue animation
    global angle
    angle += 2

    root.after(30, draw_cube)


# -----------------------------
# Floating Balls
# -----------------------------
floating = 0


def draw_objects():
    global floating

    canvas.delete("objects")

    offset = math.sin(floating / 15) * 15

    # Yellow ball
    canvas.create_oval(
        930, 160 + offset,
        990, 220 + offset,
        fill="#ffb52e",
        outline="",
        tags="objects"
    )

    # Pink ball
    canvas.create_oval(
        600, 390 - offset,
        655, 445 - offset,
        fill="#ff36b8",
        outline="",
        tags="objects"
    )

    # Blue ball
    canvas.create_oval(
        950, 470 + offset,
        1005, 525 + offset,
        fill="#327dff",
        outline="",
        tags="objects"
    )

    floating += 1

    root.after(40, draw_objects)


# -----------------------------
# Feature Cards
# -----------------------------
def cards():

    data = [
        ("🚀", "Fast Performance", "Smooth and fast"),
        ("🎨", "Colorful Design", "Beautiful 3D colors"),
        ("🛡", "Secure & Reliable", "Simple and reliable")
    ]

    x_positions = [70, 400, 730]

    for i, (icon, title, description) in enumerate(data):

        x = x_positions[i]

        canvas.create_rectangle(
            x, 565,
            x + 290, 650,
            fill="#261b70",
            outline="#604bca",
            width=2
        )

        canvas.create_text(
            x + 35, 607,
            text=icon,
            fill="white",
            font=("Arial", 25)
        )

        canvas.create_text(
            x + 75, 590,
            text=title,
            fill="white",
            font=("Arial", 14, "bold"),
            anchor="w"
        )

        canvas.create_text(
            x + 75, 620,
            text=description,
            fill="#c8c8e8",
            font=("Arial", 11),
            anchor="w"
        )


# -----------------------------
# Start
# -----------------------------
background()
navigation()
hero_text()
cards()

draw_cube()
draw_objects()

root.mainloop()
