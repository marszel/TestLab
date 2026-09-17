environment = {
    "name": "DEV",
    "status": "Ready",
    "users": 5
}

print(environment)

print(environment["name"])
print(environment["status"])
print(environment["users"])

environment2 = {
    "name": "Test",
    "status": "Maintenance",
    "users": 2
}

print(environment, environment2)