import imgkit
# url = "https://devlabel.globex.vn/itemsStation/label/printlabel?hawb=LEXST0010316431VN"
# url = "https://devlabel.globex.vn//itemsOrderExpress/label/printbill?orderNumber=GB00000224225"
url = "https://devlabel.globex.vn//itemsOrderExpress/label/printbill?orderNumber=GB00000224225,GB00000224232,GB00000224218,GB00000224201,GB00000224195,GB00000224188,GB00000224171,GB00000224164,GB00000224157,GB00000224140"
path_wkhtmltoimgge = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe'
config = imgkit.config(wkhtmltoimage=path_wkhtmltoimgge, xvfb='/opt/bin/xvfb-run')
imgkit.from_url(url, 'a.jpg', config=config)