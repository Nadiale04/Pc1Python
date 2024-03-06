nombre_archivo=input('Escriba el nombre de su archivo: ').lower()
extension_ingresada=nombre_archivo.split('.')[1]
extensiones={'gif':'image/gif',
             'jpg':'image/jpeg',
             'jpeg':'image/jpeg',
             'png':'image/png',
             'pdf':'application/pdf',
             'txt':'text/plain',
             'zip':'application/zip'}
if extension_ingresada in extensiones:
    print(extensiones[extension_ingresada])   
else:
    print('application/octet-stream.')