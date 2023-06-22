from langchain.serpapi import SerpAPIWrapper
def get_profile_url(text:str) -> str:
    """Searches for Linkedin profile Page."""
    search = SerpAPIWrapper(serpapi_api_key="404034def03e122b382f45f1a613c9e60f9eb638bee60099c30aae1cac770257")
    res = search.run(f"{text}")
    return res


