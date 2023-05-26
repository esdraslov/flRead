
def fl_txt(fl_file: str):
  try:
    fl = open(fl_file, "r")
    fl_text = open(fl_file.replace('fl', 'txt'), "w")
    fl_text.write(fl.read())
    fl_text.close()
    return '<200>'
  except:
    return '<404>'