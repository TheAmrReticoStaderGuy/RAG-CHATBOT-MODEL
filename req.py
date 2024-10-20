import subprocess
import sys

def install_package(package_name):
    """Install a package using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

def main():
    # List of packages to install
    packages = [
        'langchain',
        'streamlit',
        'langchain_community',
        'huggingface_hub',  # Specify exact version to avoid conflicts
        'tiktoken',
        'chromadb',
        'PyPDF2',
        'pypdf',
        'sentence_transformers',
        'FlagEmbedding',
        'torch',  # Correct installation of torch
    ]

    for package in packages:
        try:
            print(f"Installing {package}...")
            install_package(package)
            print(f"Successfully installed {package}\n")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {package}: {e}")

if __name__ == "__main__":
    main()

# pip install -U langchain-huggingface