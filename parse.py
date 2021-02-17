import glob, pickle

folder = "spool"
# folder = "queue/archive"
sct = "Senior computer team <scteam.lists.tjhsst.edu>"

for fname in sorted(glob.glob(f"{folder}/*.pck")):
    with open(fname, "rb") as f:
        email = pickle.load(f)
        headers = dict(email._headers)
        if headers.get("List-Id", None) == sct:
            print(headers["Date"], headers["Subject"], headers["X-MailFrom"])
            print(fname)
            # print(email._payload)

