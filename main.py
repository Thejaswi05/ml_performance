import os
import json
from ml_performance.model_inference import refine_summary
from ml_performance.utils.utils import format_response_times
from ml_performance.utils.utils import read_config


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, '..', '..', 'config', 'config.json')
    config = read_config(config_path)
    base_dir = config['BASE_DIR']
    json_path = os.path.join(base_dir, 'statistics.json')

    with open(json_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    formatted_json_data = format_response_times(json_data)
    refined_summary = refine_summary(formatted_json_data)
    refined_summary_str = refined_summary if isinstance(refined_summary, str) else refined_summary.get('text', '')

    output_file_path = os.path.join(base_dir, 'refined_summary.txt')
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(refined_summary_str)

    print("The summary has been saved to 'refined_summary.txt'.")


if __name__ == "__main__":
    main()
