code = [
  'code = [',
  'for line in code:',
  "  print ' %r,' % line",
  'print code[0]',
  'for line in code:',
  "  print ' %r,' % line",
  'print code[-1]',
  'for line in code[3:-1]:',
  '  print line',
  ']',
]
print code[0]
for line in code[0:]:
  print '  %r,' % line
print code[-1]
for line in code[3:-1]:
  print line
