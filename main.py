import PyPDF2     #importa biblioteca pra manipular pdfs
import os         #manipula arquivos do PC

merger = PyPDF2.PdfMerger()   #atribui a ferramenta da biblioteca PyPDF2 que mescla arquivos PDF à variavel merger

listaArquivos = os.listdir('automacoes/PDFMerger/arquivos')   #lista os conteudos do diretorio arquivos
listaArquivos.sort()   #organiza eles 
print(listaArquivos)   #mostra os conteudos

for arquivo in listaArquivos:      #para cada arquivo na pasta, ele roda o bloco uma vez.
      if '.pdf' in arquivo:        #verifica se os arquivos da pasta são do tipo PDF
            merger.append(f'automacoes/PDFMerger/arquivos/{arquivo}')       #se for do tipo PDF, incrementa o texto à variavel merger

merger.write('automacoes/PDFMerger/arquivos/PDF Final.pdf')    #salva tudo e cria o PDF final com todo texto dos outros PDFs