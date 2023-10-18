import PyPDF2  
import os      

merger = PyPDF2.PdfMerger()

listaArquivos = os.listdir('automacoes/PDFMerger/arquivos')
listaArquivos.sort()
print(listaArquivos)

for arquivo in listaArquivos:  
      if '.pdf' in arquivo:     
            merger.append(f'automacoes/PDFMerger/arquivos/{arquivo}')   

merger.write('automacoes/PDFMerger/arquivos/PDF Final.pdf') 