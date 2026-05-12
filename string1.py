#memory allocation and slicing

name="rajneesh Sahu"
print(name[0])
print(name[::-1])
print(name[:3])


print(name.lower())
print(name.upper())
print(name.swapcase())
print(name.title())

input=["ramsingh06@gmail.com","mohansingh07@gmail.com"]
mainresult = []
for res in input:
    res1 = res.split('@gmail.com')
    name = res1[0]
    first = name[0]
    last  = name[-1]
    stars = "*" * (len(name)-2)
    output = first+ stars+last+'@gmail.com'
    mainresult.append(output)
print(mainresult)

input = ["ramsingh06@gmail.com", "mohansingh07@gmail.com"]

output = [
    e.split("@")[0][0] + "*" * (len(e.split("@")[0]) - 2) + e.split("@")[0][-1] + "@" + e.split("@")[1]
    for e in input
]

print(output)


urls = [
    "http://example.com/user/192.168.1.10",
    "http://test.com/data/10.0.0.5"
]

ips = []
for url in urls:
    ip = url.split("/")[-1]   # last part after /
    ips.append(ip)

print(ips)

p = [url.split('/')[-1] for url in urls]
print(p)


newlist = []
key ="name"
value ="sham"

newlist.append(f'{key} = "{value}"')
print(newlist)