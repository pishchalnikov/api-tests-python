from os import environ


staging = {
    "host": environ.get("STAGING_API_HOST", "jsonplaceholder.typicode.com"),
    "port": environ.get("STAGING_API_PORT", 80)
}
