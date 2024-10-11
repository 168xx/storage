import os  
import subprocess  
import shutil  
  
# GitHub repository details  
PRIVATE_REPO_OWNER = "168xx"  
PRIVATE_REPO_NAME = "cj"  
PRIVATE_REPO_BRANCH = "main"  # Replace with your branch name  
TOKEN = os.getenv("GITHUB_TOKEN")  
IP_FOLDER = "IP"  
TARGET_FILE = "live.txt"  
  
def clone_and_sparse_checkout(owner, repo, branch, token, target_file):  
    repo_url = f"https://{token}:x-oauth-basic@github.com/{owner}/{repo}.git"  
    repo_folder = repo.replace('/', '_')  # Avoid issues with special characters in repo name  
    sparse_checkout_config = f".git/info/sparse-checkout"  
  
    # Clone the repository with --no-checkout to avoid fetching all files  
    command = [  
        "git", "clone", "--no-checkout", repo_url, repo_folder  
    ]  
    subprocess.run(command, check=True)  
  
    # Enable sparse-checkout  
    with open(os.path.join(repo_folder, sparse_checkout_config), 'w') as f:  
        f.write(f"/{target_file}\n")  
  
    # Checkout the specified branch and sparse-checkout the file  
    command = [  
        "git", "-C", repo_folder, "checkout", branch  
    ]  
    subprocess.run(command, check=True)  
  
    # Verify that the file exists  
    if not os.path.exists(os.path.join(repo_folder, target_file)):  
        raise FileNotFoundError(f"The file {target_file} does not exist in the repository {repo}")  
  
def copy_file(source_file, destination_folder):  
    if not os.path.exists(destination_folder):  
        os.makedirs(destination_folder)  
      
    shutil.copy(source_file, destination_folder)  
  
def main():  
    repo_folder = PRIVATE_REPO_NAME.replace('/', '_')  
    target_path = os.path.join(repo_folder, TARGET_FILE)  
    clone_and_sparse_checkout(PRIVATE_REPO_OWNER, PRIVATE_REPO_NAME, PRIVATE_REPO_BRANCH, TOKEN, TARGET_FILE)  
    copy_file(target_path, IP_FOLDER)  
    # Remove the cloned repo folder after copying the file  
    shutil.rmtree(repo_folder)  
  
if __name__ == "__main__":  
    main()