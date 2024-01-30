from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import XMLConverter
from pdfminer.layout import LAParams
from io import StringIO
from urllib.request import urlopen

def lerPDF(arquivo):
    recursos = PDFResourceManager()
    buffer = StringIO()
    layoutParams = LAParams()
    disp = XMLConverter(recursos, buffer, laparams=layoutParams)

    process_pdf(recursos, disp, arquivo)
    disp.close()

    conteudo = buffer.getvalue()
    buffer.close()
    return conteudo

arquivoPDF = urlopen("https://s3.novatec.com.br/sumarios/sumario-9788575226926.pdf")
saida = lerPDF(arquivoPDF)
print(saida)
arquivoPDF.close()