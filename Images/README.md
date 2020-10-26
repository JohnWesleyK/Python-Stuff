# Images-with-python
Images with python using pilow library.
First install pillow library using pip install
```bash
pip install pillow
```
This is how you load the images onto a vriable 
```python
from PIL import Image
img = Image.open('example.jpg')
```
you can see the size of the image
```python
#(width, height)
img.size 
```
you can see the filename with this
```python
img.filename 
```
specific description
```python
img.format_description
```
you can see the image
```python
img.show() 
```

## Cropping
```python
img.crop((x, y, width, height))
# x,w in same direction
# y,h in same direction
crop = mac.crop((0,0,100,100))
crop.show()
```

## Copying images
```python
img.paste(im=img_name, box=(x,y))
```

## Re-sizing Images
```python
img.resize(new_width, new_height)
```

## Color Transparency
RGBA - Red, Green, Blue, Alpha

### Re-Setting Alpha:
0 <= number <= 255
```python
img.putalpha(number)
img1.paste(im=img2, box=(0, 0), mask=img2)
```

## Saving Images
```python
img.save("Path")
```

