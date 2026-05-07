import subprocess

from google.auth.exceptions import DefaultCredentialsError
from google.cloud import datastore
from google.oauth2.credentials import Credentials

PROJECT_ID = "projet-cloud-494614"


def create_client():
    try:
        return datastore.Client(project=PROJECT_ID)
    except DefaultCredentialsError:
        token = subprocess.check_output(
            ["gcloud", "auth", "print-access-token"], text=True
        ).strip()
        return datastore.Client(project=PROJECT_ID, credentials=Credentials(token))


client = create_client()

def delete_kind(kind):
    query = client.query(kind=kind)
    query.keys_only()
    keys = [entity.key for entity in query.fetch()]

    for i in range(0, len(keys), 400):
        client.delete_multi(keys[i : i + 400])

    return len(keys)


posts_count = delete_kind("Post")
users_count = delete_kind("User")

print(f"{posts_count} posts supprimés.")
print(f"{users_count} users supprimés.")
