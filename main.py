import qrcode

# Defininfo o que estará no qr_code
url = str(input('Informe o item que estará no QrCode: '))

# Criando objeto do qr_code
qr_code = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr_code.add_data(url)
qr_code.make(fit=True)

# Gerando imagem do qr_code
imagem = qr_code.make_image(fill='black', back_color='white')
imagem.show()
