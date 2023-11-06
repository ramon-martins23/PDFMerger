import PyPDF2  
import os      
from tkinter.filedialog import askdirectory

merger = PyPDF2.PdfMerger()

caminho = askdirectory(title = 'Selecione uma pasta')
listaArquivos = os.listdir(caminho)
listaArquivos.sort()
print(listaArquivos)

for arquivo in listaArquivos:  
      if '.pdf' in arquivo:     
            merger.append(f'{caminho}/{arquivo}')   

merger.write(f'{caminho}/PDF Final.pdf') 