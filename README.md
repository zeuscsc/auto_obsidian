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
~~~shell Unix
export OPENAI_API_KEY=your openai key
export TECKY_API_KEY=your tecky key
# Example
export OPENAI_API_KEY=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
export TECKY_API_KEY=12a34567-bc89-1011-12de-1234567x1234
~~~

~~~shell Windows
$ENV:TECKY_API_KEY="your openai key"
$ENV:OPENAI_API_KEY="your tecky key"
# Example
export OPENAI_API_KEY="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"
export TECKY_API_KEY="12a34567-bc89-1011-12de-1234567x1234"
~~~
## Usage
~~~shell
python auto_obsidian
~~~