import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def mostrar_secao():
    # Carregue a imagem usando matplotlib.image
    imagem = mpimg.imread(os.path.join('..', 'secao.png'))

    # Exiba a imagem
    plt.imshow(imagem)

    # Personalize a exibição, se desejar
    plt.axis('off')  # Desabilita os eixos

    # Mostra a imagem na janela
    plt.show()
