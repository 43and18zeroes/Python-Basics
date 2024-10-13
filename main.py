def render_template(**template_vars):
    # Simulierte Templating-Engine
    template = "Hello, {name}! Your age is {age}."
    print(template.format(**template_vars))

render_template(name="Alice", age=25)