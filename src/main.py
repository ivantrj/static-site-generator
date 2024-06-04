
import shutil
import os

from copystatic import copy_files_recursive


dir_path_static = "./static"
dir_path_public = "./public"

def copy_files():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
      shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

def main():

  copy_files()



main()