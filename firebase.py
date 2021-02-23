import firebase_admin
from firebase_admin import firestore, credentials
from config import FIREBASE_CREDENTIALS
import json

class Firebase(object):

    def __init__(self):
        cert = json.loads(FIREBASE_CREDENTIALS, strict=False)
        cred = credentials.Certificate(cert)
        app = firebase_admin.initialize_app(cred)
        self.db = firestore.client(app)

if __name__ == '__main__':
    f = Firebase()
    print(f.db.collection("Twitter").document("nanase").get().to_dict())
    print(f.db.collection("Twitter").document("nanase").get().to_dict())
    print(f.db.collection("Twitter").document("nanase").get().to_dict())
