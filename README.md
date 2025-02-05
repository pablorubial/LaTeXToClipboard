# LaTeXToClipboard

This script automates the process of capturing a screenshot, extracting LaTeX-formatted text from it, and copying the result to the clipboard. It offers an open-source alternative to proprietary tools like Mathpix Snip.

![Demo](./media/out.gif)

# Prerequesites

**gnome-screenshot** for capturing screenshots. In case of not have it installed:
  ```bash
  sudo apt-get install gnome-screenshot
  ```
**xclip** for clipboard management. In case of not have it installed:
```bash
sudo apt-get install xclip
```
**awk** for extract content using regular exppressions from log files. In case of not have it installed:
```bash
sudo apt-get install gawk
```

# Setup

Clone this repository and locate it in place confortable to the user. In my case I have it in:
```bash
mkdir $HOME/software
cd $HOME/software
git clone https://github.com/pablorubial/LaTeXToClipboard.git
```
Go inside the repo folder and create a python virtual environment inside of it:
```bash
cd LaTeXToClipboard
python3 -m venv .myvenv
```
Activate the virtual environment:
```bash
source .myvenv/bin/activate
```

Install the packages from the requirements file:
```bash
pip install -r requirements.txt
```

With this setup, we can run the `Run.py` file, that basically takes an image from `"$HOME/software/LaTeXTOClipboard/images/` and after apply the DeepLearning algorithm of pix2text, the output is print into the screen. Now, let us take advantage of this library and automatize the process of:

1. Take an screenshot of the desired formula that we are interested in get its LaTeX expression.
2. Send that image to the `images` folder od this repository.
3. Run the `Run.py` file and save the output to a temporal file.
4. Extract the content between $$ symbols that contains the LaTeX expression.
5. Copy the expression into the clipboard.

All this stuff can be put in a `.sh` inside a folder called `shortcuts` that is inside to the `software` folder automatasing the process. So first generate the mentioned folder:

```bash
mkdir $HOME/software/shortcuts
cd $HOME/software/shortcuts
```

then create the following `.sh` file called `latex_clipboard.sh`, for example and put the following content inside:

```sh
#!/bin/bash
# Take the screenshot and send it to $HOME/software/LaTeXTOClipboard/images/
gnome-screenshot -a -f $HOME/software/LaTeXToClipboard/images/test.jpg

# Process the image using pix2text and save the output in a temporal file
source $HOME/software/LaTeXToClipboard/.myenv/bin/activate
python3 $HOME/software/LaTeXToClipboard/src/Run.py |& tee /tmp/python_output.log
deactivate

# Extract all content between $$ and $$ and copy it to the clipboard
awk '/\$\$/ {flag=!flag; next} flag' /tmp/python_output.log | xclip -selection clipboard
```

and give to this file permissions to be executed:
```bash
chmod +x $HOME/software/shortcuts/latex_clipboard.sh
```

Once the `.sh` file is executable, we can create a linux custom shortcut that basically when it is executed, executes the `.sh` file. In my case I associated the `.sh` file to the 'Ctrl' + 'Alt' + 'p' keyboard combination. This can be done as follows:

![Demo](./media/shortcut.png)