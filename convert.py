import csv
import json

def csv_to_jsonl(csv_path, jsonl_path):
    """Convert a CSV file to JSONL format.
    
    Args:
        csv_path (str): Path to input CSV file
        jsonl_path (str): Path to output JSONL file
    """
    import pandas as pd
    df = pd.read_csv(csv_path)
    df.to_json(jsonl_path, orient='records', lines=True)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: python convert.py input.csv output.jsonl")
        sys.exit(1)
    
    csv_path = sys.argv[1]
    jsonl_path = sys.argv[2]
    csv_to_jsonl(csv_path, jsonl_path)
