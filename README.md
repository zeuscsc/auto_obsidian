## Install
Clone repo with submodules:
~~~shell
git clone https://github.com/zeuscsc/auto_obsidian.git --recurse-submodules
git submodule update --init --recursive
~~~
Torch 2.0 with conda
~~~shell
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
~~~
Install requirements
~~~shell
pip install -r requirements.txt
~~~
## For ImportError: cannot import name 'COMMON_SAFE_ASCII_CHARACTERS' from 'charset_normalizer.constant'
~~~shell
conda install -c conda-forge charset-normalizer
~~~
## Usage
First export your youtube links from Toby as json file,put it on root directory and name it articles_indexes.json then run:
~~~shell
python yt2txt.py
~~~
This will downlaod all the videos and convert them to json files.
Then run:
~~~shell
python obsidian_notes_generator.py
~~~