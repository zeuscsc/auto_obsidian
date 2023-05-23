# Auto Obsidian
I love watching youtube tutorials about new technology and algorithms. More and more content creator are creating tutorials about new technologies and algorithms. Now the newly created videos are uploaded much faster than the speed I could watch. It is hard to keep up with all of them. That's why I would like to try using Ai to help me to keep up with the latest technologies.
Auto Obsidian is a tool that helps you to keep up with the latest technologies and tools. It is a tool that helps you to learn new technologies and tools by summarizing notes, creating links between notes and creating chapters' urls for youtube with marked timed urls tutorials from your exported toby collections (JSON).
## Features
- [x] Summarize notes from videos
- [x] Create links between notes
- [x] Create chapters for youtube tutorials with marked timed urls
- [ ] Group notes by classes
- [ ] Self train LLM without GPT (Able to be totally Free of Charge finally)
## Quick Usage
~~~shell
pip install git+https://github.com/zeuscsc/auto_obsidian.git
python auto_obsidian
~~~

## Install
Clone repo with submodules:
~~~shell
git clone https://github.com/zeuscsc/auto_obsidian.git
~~~
Torch 2.0 with conda for wisperer
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
Unix:
~~~shell Unix
export OPENAI_API_KEY="your openai key"
export TECKY_API_KEY="your tecky key" (Optional)
# Example
export OPENAI_API_KEY=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
export TECKY_API_KEY=12a34567-bc89-1011-12de-1234567x1234
~~~
Windows:
~~~shell Windows
$ENV:OPENAI_API_KEY="your tecky key"
$ENV:TECKY_API_KEY="your openai key" (Optional)
# Example
$ENV:OPENAI_API_KEY="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"
$ENV:TECKY_API_KEY="12a34567-bc89-1011-12de-1234567x1234"
~~~
## Usage
~~~shell
python main.py
~~~
