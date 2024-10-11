import os  
import shutil  
  
def copy_files(src_dir, dest_dir):  
    if not os.path.exists(dest_dir):  
        os.makedirs(dest_dir)  
      
    for root, dirs, files in os.walk(src_dir):  
        for file in files:  
            if file.endswith('.txt') or file.endswith('.m3u'):  
                src_file = os.path.join(root, file)  
                dest_file = os.path.join(dest_dir, file)  
                shutil.copy2(src_file, dest_file)  
  
if __name__ == "__main__":  
    import sys  
      
    if len(sys.argv) != 3:  
        print("Usage: python3 copy_files.py <source_directory> <destination_directory>")  
        sys.exit(1)  
      
    src_directory = sys.argv[1]  
    dest_directory = sys.argv[2]  
      
    copy_files(src_directory, dest_directory)