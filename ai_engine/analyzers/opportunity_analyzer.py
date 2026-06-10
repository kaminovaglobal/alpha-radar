from providers.openai_provider import ask


def analyze(opportunity):

    prompt = f"""
Analyze this Web3 opportunity.

Title:
{opportunity.title}

Category:
{opportunity.category}

Score:
{opportunity.score}

Explain:

1. Why it matters

2. Potential value

3. Risks

4. Recommended action
"""

    return ask(prompt)