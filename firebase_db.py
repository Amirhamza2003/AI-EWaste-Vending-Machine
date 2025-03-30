import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("firebase_key.json")  # Ensure this file is in .gitignore
firebase_admin.initialize_app(cred)
db = firestore.client()

# Store e-waste data
def save_user_data(user_id, item, reward_points):
    doc_ref = db.collection("e-waste").document(user_id)
    doc_ref.set({"item": item, "reward": reward_points})
    return "Data Saved!"
