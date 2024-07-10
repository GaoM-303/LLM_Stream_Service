import requests
from settings import parse_arguments


def chat(query, history, prompt):
    if not prompt:
        prompt = ""
    if not history:
        history = []
    history = history[-args.max_his:]

    if query:
        res = requests.post(args.address + "chat", json={"query": query, "prompt": prompt, "history": history}).json()
        return res["response"]


if __name__ == '__main__':
    args = parse_arguments()
    history = [("Hi there!", "Hi, what can I help you?")]
    prompt = "You are a helpful assistant."
    text = "Do you know chinese kongfu?"

    gen = chat(text, history, prompt)
    print(gen)