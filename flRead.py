def fl_txt(fl_file: str):
  try:
    fl = open(fl_file, "r")
    fl_text = open(fl_file.replace('fl', 'txt'), "w")
    fl_text.write(fl.read())
    fl_text.close()
    return '<200>'
  except:
    return '<404>'


def fl_markdown(fl_file: str):
  try:
    fl = open(fl_file, "r")
    fl_text = open(fl_file.replace('fl', 'md'), "w")
    fl_text.write(fl.read())
    fl_text.close()
    return '<200>'
  except:
    return '<404>'

def fl_cf(fl_file: str, new_file: str):
  try:
    fl = open(fl_file, "r")
    fl_text = open(new_file.replace('.', '.cf.'), "w")
    fl_text.write(fl.read())
    fl_text.close()
    return '<200>'
  except:
    return '<404>'