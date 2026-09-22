def get_environment_count(environments_list):
    ready_environment = []
    for env in environments_list:
        if env["status"] == "Ready":
            ready_environment.append(env["name"])
    return ready_environment, len(ready_environment)


environments = [
    {
        "name": "DEV",
        "status": "Ready"
    },
    {
        "name": "TEST",
        "status": "Maintenance"
    },
    {
        "name": "UAT",
        "status": "Ready"
    }
]

count = get_environment_count(environments)
print(f"Amount of environments: {count}")