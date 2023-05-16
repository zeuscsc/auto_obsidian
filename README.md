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
## Set Environment Variables
~~~shell
set OPENAI_API_KEY={your openai key}
set TECKY_API_KEY={your tecky key}
~~~
## Usage
~~~shell
python auto_obsidian
~~~