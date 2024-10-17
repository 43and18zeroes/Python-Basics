def raise_custom_exception(**kwargs):
    raise Exception(f"Custom Exception: {kwargs}")

raise_custom_exception(error_code=404, message="Not Found")