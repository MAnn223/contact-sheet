from PIL import Image
from PIL import ImageEnhance
from PIL import ImageDraw
from PIL import ImageFont

# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

# build a list of 9 images which have different brightnesses
enhancer=ImageEnhance.Brightness(image)
r = 20
b = 100
g = 50
images=[]
pixeldata = image.load() 
####################################
txt = Image.new('RGB', image.size, (230,0,0))
fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 75)
d = ImageDraw.Draw(txt)
d.text((10,350), 'channel 0 intensity 0.1', font=fnt, fill=(255,255,255))
images.append(Image.blend(image, txt, 0.5))

txt = Image.new('RGB', image.size, (128,0,0))
fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 75)
d = ImageDraw.Draw(txt)
d.text((10,350), 'channel 0 intensity 0.5', font=fnt, fill=(255,255,255))
images.append(Image.blend(image, txt, 0.5))

txt = Image.new('RGB', image.size, (26,0,0))
fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 75)
d = ImageDraw.Draw(txt)
d.text((10,350), 'channel 0 intensity 0.9', font=fnt, fill=(255,255,255))
images.append(Image.blend(image, txt, 0.5))
####################################
txt = Image.new('RGB', image.size, (0,230,0))
fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 75)
d = ImageDraw.Draw(txt)
d.text((10,350), 'channel 1 intensity 0.1', font=fnt, fill=(255,255,255))
images.append(Image.blend(image, txt, 0.5))

txt = Image.new('RGB', image.size, (0,128,0))
fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 75)
d = ImageDraw.Draw(txt)
d.text((10,350), 'channel 1 intensity 0.5', font=fnt, fill=(255,255,255))
images.append(Image.blend(image, txt, 0.5))

txt = Image.new('RGB', image.size, (0,26,0))
fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 75)
d = ImageDraw.Draw(txt)
d.text((10,350), 'channel 1 intensity 0.9', font=fnt, fill=(255,255,255))
images.append(Image.blend(image, txt, 0.5))
####################################
txt = Image.new('RGB', image.size, (0,0,230))
fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 75)
d = ImageDraw.Draw(txt)
d.text((10,350), 'channel 2 intensity 0.1', font=fnt, fill=(255,255,255))
images.append(Image.blend(image, txt, 0.5))

txt = Image.new('RGB', image.size, (0,0,128))
fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 75)
d = ImageDraw.Draw(txt)
d.text((10,350), 'channel 2 intensity 0.5', font=fnt, fill=(255,255,255))
images.append(Image.blend(image, txt, 0.5))

txt = Image.new('RGB', image.size, (0,0,26))
fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 75)
d = ImageDraw.Draw(txt)
d.text((10,350), 'channel 2 intensity 0.9', font=fnt, fill=(255,255,255))
images.append(Image.blend(image, txt, 0.5))
# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)
