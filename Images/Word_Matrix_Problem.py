from PIL import Image

# load both the given images
word_matrix = Image.open("word_matrix.png")
mask = Image.open("mask.png")

# convert both the images into same size
matrix_x,matrix_y=word_matrix.size
mask = mask.resize((matrix_x,matrix_y))

# make mask a bit transparent
mask.putalpha(100)

# put transparent-ish mask on the matrix
word_matrix.paste(im=mask, box=(0, 0), mask=mask)
word_matrix.show()

# save it as a new image
word_matrix.save('Word_Matrix_Solution.png')