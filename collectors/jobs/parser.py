def detect_remote(location):

    location = location.lower()

    if "remote" in location:
        return True

    return False

def classify_job(title):

    title = title.lower()

    if "security" in title:
        return "SECURITY"

    if "devrel" in title:
        return "DEVREL"

    if "community" in title:
        return "COMMUNITY"

    if "growth" in title:
        return "GROWTH"

    return "GENERAL"