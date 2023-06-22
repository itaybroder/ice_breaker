import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f"Bearer kD0gOr6PGzQOJ5-hK5t8hw"}

    if linkedin_profile_url == "https://www.linkedin.com/in/roy-ohana/":
        response = requests.get(
            "https://gist.githubusercontent.com/itaybroder/9b85e4e1d5ab5ec05af3e28a2e5bcf8a/raw/e0ac325dc7f939ea56c0a547fd2eca86b06d5a8b/roy_ohana.json"
        )
    else:
        response = requests.get(
            api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
        )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
