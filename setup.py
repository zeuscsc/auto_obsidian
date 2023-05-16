from setuptools import setup, find_packages

setup(
    name = 'AutoObsidian',
    version = '0.1.0',
    url = '',
    description = '',
    packages = find_packages(),
    install_requires = [
        "openai",
        "python-dotenv",
        "sentence-transformers",
        "spacy",
        "opencv-python",
        "yt-dlp",
        "openai-whisper"
    ]
)