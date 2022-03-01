import qrcode
import uuid
path = "static/qrcode/" + str(uuid.uuid4()) + ".png"
# ids=int(1)
# print(ids)
img = qrcode.make("1")
img.save(path)
