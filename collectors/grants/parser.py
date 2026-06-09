def classify_grant(title):

    title = title.lower()

    if "security" in title:
        return "SECURITY"

    if "research" in title:
        return "RESEARCH"

    if "developer" in title:
        return "DEVELOPER"

    if "ai" in title:
        return "AI"

    return "GENERAL"