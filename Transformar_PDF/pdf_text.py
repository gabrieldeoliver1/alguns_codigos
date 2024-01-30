from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
# Para abrir um PDF localmente
from io import open
# Para abrir um PDF online
from urllib.request import urlopen

def lerPDF(arquivoPDF):
    #
    recursos = PDFResourceManager()
    buffer = StringIO()
    layoutParams = LAParams()
    dispositivo = TextConverter(recursos, buffer, laparams=layoutParams)

    process_pdf(recursos, dispositivo, arquivoPDF)
    dispositivo.close()

    conteudo = buffer.getvalue()
    buffer.close()
    return conteudo

# Arquivo PDF online
#arquivoPDF = urlopen("https://s3.novatec.com.br/sumarios/sumario-9788575226926.pdf")
# Arquivo PDF local (Abrindo modo leitura e binário)
#arquivoPDF = open("sumario-9788575226926.pdf", "rb")
arquivoPDF = open("Aula03_ArquivosPDF.pdf", "rb")

stringSaida = lerPDF(arquivoPDF)
print(stringSaida)
arquivoPDF.close()

# PDFResourceManager Usado para armazenar recursos compartilhados como fontes e imagens

