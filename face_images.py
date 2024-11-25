"""Script Principal"""
from Utils.functions import face_encoding, face_compare

daenerys_001 = face_encoding('./Images/Daenerys_001.jpg')
# daenerys_002 = image_encoding('./Images/Daenerys_002.jpg')
# daenerys_003 = image_encoding('./Images/Daenerys_003.jpg')
# margaery_001 = image_encoding('./Images/Margaery_001.jpg')
# emilia_001 = image_encoding('./Images/Emilia_Clarke_001.jpeg')

# face_compare(daenerys_001, daenerys_002)
# face_compare(daenerys_001, daenerys_003)
# face_compare(daenerys_001, margaery_001)
# face_compare(daenerys_001, emilia_001)

daenerys_jon = face_encoding('./Images/Daenerys_Jon_001.jpg')

for i, encoding in enumerate(daenerys_jon):
    if face_compare(daenerys_001[0], daenerys_jon[i]):
        print(f'El rostro {i} es de Daenerys')
    else:
        print(f'El rostro {i} no es de Daenerys')
