import firebase_admin
from firebase_admin import firestore, credentials
from config import FIREBASE_CREDENTIALS
import json
from loguru import logger

class Firebase(object):

    def __init__(self, collection):
        cert = json.loads(FIREBASE_CREDENTIALS, strict=False)
        cred = credentials.Certificate(cert)
        firebase_admin.initialize_app(cred)
        self._db = firestore.client()
        self._collection = self._db.collection(collection)

    # get all docs
    def get_stream(self):
        return self._collection.stream()

    # get one doc
    def get(self, document):
        return self._collection.document(document).get().to_dict()

    def update(self, document, account: dict):
        try:
            self._collection.document(document).update(account)
            logger.info(f"update the doc {account['screen_name']}")
        except ValueError as e:
            logger.error(f"{account['screen_name']}: {e}")