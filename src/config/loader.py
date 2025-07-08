"""参数配置--- # 读取 YAML/JSON 配置文件"""
import yaml


def load_yaml_config(path: str) -> dict:
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    return data


import json


def load_json_config(path: str) -> dict:
    with open(path, 'r') as f:
        data = json.load(f)
    return data

