def log_event(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

log_event(message="Eintritt ins System", user="admin", timestamp="2023-11-23 14:32:15")