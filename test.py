parms = {
    "1" : "111",
    "2" : "sigma",
    "skibidi" : "ligma"
}

url = "https:/aaa.com/s?"

for key, val in parms.items():
    url += f"&{key}={val}"

print(url)