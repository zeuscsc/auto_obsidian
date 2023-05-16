from setuptools import setup, find_packages

setup(
    name = 'AutoObsidian',
    version = '0.1.0',
    url = 'https://github.com/zeuscsc/auto_obsidian.git',
    description = 'Auto Generate Obsidian from your Exported Toby History',
    packages = find_packages(),
    py_modules=["auto_obsidian"],
    author="ZeusChiu",
    include_package_data=True,
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