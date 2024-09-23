import os


def read_config(config_path):
    # Here, we assume that the configuration is stored in a file,
    # such as a JSON or YAML file.
    import json

    with open(config_path, 'r') as f:
        config = json.load(f)
    return config


def format_response_times(json_data):
    for key, value in json_data.items():
        if 'pct2ResTime' in value and value['pct2ResTime'] > 1000:
            value['pct2ResTime'] = f"{value['pct2ResTime'] / 1000:.1f} seconds"
        else:
            value['pct2ResTime'] = f"{value['pct2ResTime']} ms"
    return json_data
