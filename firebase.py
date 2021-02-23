import firebase_admin
from firebase_admin import firestore, credentials
from config import FIREBASE_CREDENTIALS
import json

class Firebase(object):

    def __init__(self):
        cert = json.loads(FIREBASE_CREDENTIALS, strict=False)
        cred = credentials.Certificate(cert)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def get(self, collection, document):
        self.db.collection(collection).document(document).get().to_dict()

    def set(self, collection, document, account):
        self.db.collection(collection).document(document).set(account)

if __name__ == '__main__':
    nonno = {
        "filter_word": "西野七瀬",
        "last_seen_id": "1363847281406070784",
        "screen_name": "nonno_staff"
    }
    f = Firebase()
    print(f.set("Twitter", "nonno", nonno))
