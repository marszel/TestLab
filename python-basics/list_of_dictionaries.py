environments = [
    {"name": "DEV",
     "status": "Ready"
     },
    {"name": "TEST",
     "status": "Maintenance"
     },
    {"name": "UAT",
     "status": "Ready"
     }
]

print(environments[0], environments[1], environments[2])
print(environments[0]["name"])
print(environments[1]["name"])
print(environments[2]["name"])

for environment in environments:
    print(f'{environment["name"]} from loop')

for environment in environments:
    print(f'{environment["name"]} - {environment["status"]}')

for environment in environments:
    if environment["status"] == "Ready":
            print(f'{environment["name"]} - {environment["status"]}')
