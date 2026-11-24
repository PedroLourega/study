from dlt.sources.rest_api import rest_api_source


def get_github_source(api_config):
    return rest_api_source({
        "client": {
            "base_url": api_config["base_url"],
        },
        "resources": [
            {
                "name": "repositorios_python",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "path": "orgs/python/repos",
                    "params": {
                        "per_page": api_config["per_page"],
                    },
                    "paginator": {
                        "type": "page_number",
                        "base_page": 1,
                        "page_param": "page",
                        "total_path": None,
                        "maximum_page": api_config["max_pages"],
                    },
                    "data_selector": "$",
                },
            },
        ],
    })
