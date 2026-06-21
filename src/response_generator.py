from prompt_templates import PROMPTS

def generate_prompt(template_name, data):
    if template_name not in PROMPTS:
        return "Invalid template selected."

    return PROMPTS[template_name].format(**data)