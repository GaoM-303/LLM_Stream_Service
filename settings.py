import argparse


def parse_arguments():
    # api
    parser = argparse.ArgumentParser(description='Stream API Service for Meta-Llama-3')
    parser.add_argument('--ckpts', '-c', help='Model path', default="./ckpts/Meta-Llama-3-8B-Instruct")
    parser.add_argument('--host', '-H', help='Host to listen', default='0.0.0.0')
    parser.add_argument('--port', '-P', help='Port of this service', default=8800)
    # app
    parser.add_argument('--address', '-A', help='Service address', default="http://127.0.0.1:8800/")
    parser.add_argument('--max_his', '-M', help='Max number of llm\'s history', default=5)
    args = parser.parse_args()
    return args