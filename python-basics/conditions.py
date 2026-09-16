application_name = "TestLab"
environment_count = 5
status = "Ready"

print(f"Application: {application_name}")
print(f"Available environments: {environment_count}")
print(f"Status: {status}")

if environment_count > 0:
    print("Environments available")
else:
    print("No environments available")

if status == "Ready" and environment_count > 0:
    print("Application is ready for testing")