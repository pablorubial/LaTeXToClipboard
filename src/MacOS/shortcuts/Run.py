from pix2text import Pix2Text, merge_line_texts
import os
 
img_fp = os.path.expandvars("/opt/Pix2text-Mac/shortcuts/images/test.png")
p2t = Pix2Text.from_config()
outs = p2t.recognize_text_formula(img_fp, return_text=True)
print(outs)