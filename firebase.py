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
        self.collection = None

    def set_collection(self, collection):
        self.collection = self.db.collection(collection)

    def get(self, document):
        return self.collection.document(document).get().to_dict()

    def update(self, document, account: dict):
        self.collection.document(document).update(account)