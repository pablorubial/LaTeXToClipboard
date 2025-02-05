from pix2text import Pix2Text, merge_line_texts
import os
 
img_fp = os.path.expandvars("$HOME/software/LaTeXTOClipboard/images/test.jpg")
p2t = Pix2Text.from_config()
outs = p2t.recognize_text_formula(img_fp, resized_shape=768, return_text=True)
print(outs)