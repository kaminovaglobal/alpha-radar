from providers.openai_provider import ask


def detect_narrative(text):

    prompt = f"""
Analyze this content.

{text}

Identify:

1. Narrative

2. Trend strength

3. Growth potential

4. Key projects
"""

    return ask(prompt)