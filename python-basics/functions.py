def show_application_status(application, status):
    print(f"Application name: {application}")
    print(f"Application status: {status}")
    if status == "Ready":
        print("Application is ready for testing")
    else:
        print("Application is not ready for testing")

show_application_status("Word","Ready")
show_application_status("LibreOfice", "Maintenance")


