import cv2 as cv
import numpy as np

imagem = cv.imread('fofo.jpeg')
largura = imagem.shape[0] #x da img
altura = imagem.shape[1] #y da img

tx = float(input('\n\t\tTranslação em x: '))
ty = float(input('\t\tTranslação em y: '))

Matriz_B = np.zeros_like(imagem) # criar matriz vazia p/ adicionar os novos pontos

for i in range(largura):
    for j in range(altura):
        x = i + tx
        y = j + ty
        if 0 <= x < altura and 0 <= y < largura:
            Matriz_B[int(x),int(y)] = imagem[i,j]

cv.imshow('',  Matriz_B)
cv.waitKey(0)