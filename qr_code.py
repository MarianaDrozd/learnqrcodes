"""
before usage type "pip install pillow qrcode" in your terminal
"""
import qrcode

data = input("Please input/paste your data(link): ")
filename = input("How do we name your file?")
f_name = f"{filename}.png"

if __name__ == "__main__":
    img = qrcode.make(data)
    img.save(f_name)
