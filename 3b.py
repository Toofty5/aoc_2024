import re

test = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

with open("3_input.txt", 'r') as f:
    raw_input = ''.join([line.strip() for line in f.readlines()])

done = re.findall(r'do\(\).*?don\'t\(\)', raw_input)
print('\n\n\n'.join(done))

pairs = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', ''.join(done))
pairs = [ (int(a), int(b)) for (a,b) in pairs]

print(sum( [ (a*b) for a,b in pairs] ))
