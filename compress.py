import os
import glob
import urllib.request
from urllib.parse import urlparse
from ok.feature.FeatureSet import compress_copy_x_anylabeling

def get_exe():
    folder = "xanylabeling"
    url = "https://github.com/CVHub520/X-AnyLabeling/releases/download/v4.0.0-beta.2/X-AnyLabeling-v4.0.0-beta.2-CPU.exe"

    filename = os.path.basename(urlparse(url).path)
    
    def find_local_exe():
        return glob.glob(os.path.join(folder, "*AnyLabeling*.exe"))

    exes = find_local_exe()
    
    if not exes:
        os.makedirs(folder, exist_ok=True)
        save_path = os.path.join(folder, filename)
        
        print(f"Downloading X-AnyLabeling to {folder} ...")
        try:
            urllib.request.urlretrieve(url, save_path)
        except Exception as e:
            raise RuntimeError(f"Download failed: {e}. Please manually put AnyLabeling.exe into '{folder}/'")

        exes = find_local_exe()

        if not exes:
            raise FileNotFoundError(f"Could not find *AnyLabeling*.exe in '{folder}' even after download.")

    print(f"Using EXE: {exes[0]}")
    return exes[0]

use_exe = get_exe()
compress_copy_x_anylabeling('xanylabeling/project_dir', 'assets', generate_label_enmu='src.Labels', use_exe=use_exe)
