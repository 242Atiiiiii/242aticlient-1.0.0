import zipfile
import os

with zipfile.ZipFile("../242aticlient-1.0.0.jar", "w", zipfile.ZIP_DEFLATED) as jar:
    for root, dirs, files in os.walk("."):
        for file in files:
            full_path = os.path.join(root, file)
            arcname = os.path.relpath(full_path, ".")
            jar.write(full_path, arcname)