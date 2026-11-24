from dlt.sources.rest_api import rest_api_source


def get_pokeapi_source(api_config):
    return rest_api_source({
        "client": {
            "base_url": api_config["base_url"],
        },
        "resources": [
            {
                "name": "pokemon",
                "primary_key": "name",
                "write_disposition": "merge",
                "endpoint": {
                    "path": "pokemon",
                    "params": {
                        "limit": api_config["page_limit"],
                    },
                    "paginator": {
                        "type": "offset",
                        "limit": api_config["page_limit"],
                        "offset_param": "offset",
                        "limit_param": "limit",
                        "total_path": "count",
                        "maximum_offset": api_config["max_offset"],
                    },
                    "data_selector": "results",
                },
            },
        ],
    })
