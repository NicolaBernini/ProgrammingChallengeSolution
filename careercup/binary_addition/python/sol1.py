

def check_binary(a):
  if not (a=='0' or a=='1'): raise RuntimeError(f"Symbcl {a} not supported")


def get_val(a, idx, default='0'):
  if idx >= len(a): return default
  return a[len(a)-1-idx]


def sum(a,b,c):
  check_binary(a)
  check_binary(b)
  check_binary(c)
  # LUT 
  if a=='0' and b=='0' and c=='0': return '0','0'
  if a=='0' and b=='0' and c=='1': return '1','0'
  if a=='0' and b=='1' and c=='0': return '1','0'
  if a=='0' and b=='1' and c=='1': return '0','1'
  if a=='1' and b=='0' and c=='0': return '1','0'
  if a=='1' and b=='0' and c=='1': return '0','1'
  if a=='1' and b=='1' and c=='0': return '0','1'
  if a=='1' and b=='1' and c=='1': return '1','1'


def solve(a,b):
  res = ''
  carry = '0'
  for i in range(max(len(a), len(b))):
    temp, carry = sum(a=get_val(a,i), b=get_val(b,i), c=carry)
    res = temp+res
  return carry+res


####### USAGE #######

assert(solve('101101', '111101')=='1101010')


