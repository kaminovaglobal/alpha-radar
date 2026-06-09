from models import Job

jobs = [

    Job(
        title="Security Researcher",
        company="Monad",
        location="Remote",
        remote=True,
        url="https://example.com",
        category="SECURITY"
    ),

    Job(
        title="DevRel Engineer",
        company="Arbitrum",
        location="Remote",
        remote=True,
        url="https://example.com",
        category="DEVREL"
    )
]

for job in jobs:

    print(job.title)