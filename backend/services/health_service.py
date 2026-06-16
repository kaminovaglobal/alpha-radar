def get_health():

    return {

        "api":"healthy",

        "database":"healthy",

        "redis":"healthy"
    }

@app.get("/health")
def health():

    return get_health()