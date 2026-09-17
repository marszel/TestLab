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

ready_count = 0
maintenance_count = 0
ready_environments = []

for environment in environments:
    if environment["status"] == "Ready":
        ready_count += 1
        ready_environments.append(environment["name"])
    elif environment["status"] == "Maintenance":
        maintenance_count += 1

print(f"Ready: {ready_count}\n"
      f"Maintenance: {maintenance_count}\n")

for environment in ready_environments:
      print(f"Ready environments: {environment}")