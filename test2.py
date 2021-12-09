# from pyhtml2pdf import converter
# import os
# url = "https://devlabel.globex.vn/itemsStation/label/printlabel?hawb=LEXST0010316695VN,LEXST0010318256VN"
# path = os.path.abspath('a.html')
# # converter.convert(f'file:///{path}', "a.pdf")
# converter.convert(url, "a.pdf")







# ------------------------------------------------------------------------------
import pdfkit
# url = "https://devlabel.globex.vn/itemsStation/label/printlabel?hawb=LEXST0010316695VN,LEXST0010318256VN"
url="https://devlabel.globex.vn/itemsOrderExpress/label/printbill?orderNumber=GB00000224225"
path_wkhtmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
pdfkit.from_url(url, "a.pdf", configuration=config)
