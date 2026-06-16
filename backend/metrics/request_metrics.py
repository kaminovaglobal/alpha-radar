from prometheus_client import Counter

REQUEST_COUNT = Counter(
    "requests_total",
    "Total Requests"
)

from prometheus_client import generate_latest

@app.get("/metrics")
def metrics():

    return generate_latest()