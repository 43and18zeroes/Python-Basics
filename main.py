def configure_app(**config):
    for key, value in config.items():
        print(f"Setting {key} to {value}")

configure_app(debug=True, host="localhost", port=5000)