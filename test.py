import flRead as fr

res = fr.fl_txt('file-test.fl')

print(res)

res = fr.fl_markdown('markdown-file.fl')

print(res)

res = fr.fl_cf('file-test.fl', 'fill.fl')

print(res)