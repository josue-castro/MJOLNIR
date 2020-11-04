# Import os library to determine CWD.
import os

# Path to service account credentials.
serv_path = os.getcwd() + \
    "/handler/dao/config/white-smile-272204-firebase-adminsdk-spbxn-39a2631978.json"

# Firebase RTBD config information required by Firebase Admin SDK.
rtdb_config = {
    "databaseURL": "https://white-smile-272204.firebaseio.com/",
}
