# filename: perplexity_image.py

from PIL import Image, ImageDraw, ImageFont

# define dimensions of the image
W = 800
H = 600

# create a new image with white background
img = Image.new(mode='RGB', size=(W, H), color=(255, 255, 255))

# initialize ImageDraw
draw = ImageDraw.Draw(img)

# load the font
font = ImageFont.load_default()

# define the messages
msg_product = "Perplexity has released 2 products this year!"
msg_traffic = "Direct traffic percentage: 76.87%"

# calculate width and height of the messages
w_product, h_product = draw.textsize(msg_product, font=font)
w_traffic, h_traffic = draw.textsize(msg_traffic, font=font)

# calculate positions
xy_product = ((W - w_product) / 2, H / 3 - h_product / 2)
xy_traffic = ((W - w_traffic) / 2, 2 * H / 3 - h_traffic / 2)

# add text to image
draw.text(xy_product, msg_product, fill="black", font=font)
draw.text(xy_traffic, msg_traffic, fill="black", font=font)

# path to save image
image_path = "perplexity_image.png"
img.save(image_path)

# print path of saved image
print(f"Image saved to: {image_path}")