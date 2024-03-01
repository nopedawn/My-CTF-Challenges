from datetime import datetime

boundary = "00000000000046efa505ffb39b09"

ts = int(boundary[18:-2] + boundary[12:-10], 16) / 1000000

dt = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print(dt)

# flag = datetime.fromtimestamp(ts).strftime('%d/%m/%Y-%H:%M:%S')
# print(f'TechnoFairCTF{{{flag}}}')