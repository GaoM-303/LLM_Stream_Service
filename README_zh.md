# LLM Stream Service
## 只需要Python基础就能轻松部署


![](https://img.shields.io/badge/license-MIT-blue) [![](https://img.shields.io/badge/Engilsh-0000FF)](README.md) [![](https://img.shields.io/badge/中文-FF0000)](README_zh.md)

完全基于Python的大语言模型（LLM）**流式API**和**网页**。

本项目包含：
1. Flask API: 真正实现LLM的流式生成和后端流式响应；
2. Gradio APP: 快速、简单的LLM前端界面。
3. Request: 快速、简单的后端请求。

## Quick Start

以Llama3的部署为例：

1. 参考[Llama3 download](https://github.com/meta-llama/llama3?tab=readme-ov-file#download)下载Meta-Llama-3-8B-Instruct模型, 或者[huggingface](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) / [modelscope](https://modelscope.cn/models/LLM-Research/Meta-Llama-3-8B-Instruct/summary)（国内推荐modelscope）。
2. 参考[Llama3 quick-start](https://github.com/meta-llama/llama3?tab=readme-ov-file#quick-start)安装Llama3的依赖。

开始我们的项目：

1. 安装本项目所需依赖：

    ```bash
    pip install flask gradio transformers
    ```

2. [可选] 修改`settings.py`中的设置。

3. 运行Flask服务:

   ```bash
   python llm_service.py --host 0.0.0.0 --port 8800 --ckpts /Meta-Llama-3-8B-Instruct
   ```

4. 运行Gradio前端界面:

   ```bash
   python llm_app.py --address http://127.0.0.1:80/
   ```


6. 服务调用：

   ```bash
   python llm_request.py --address http://127.0.0.1:80/
   ```

# 心路历程

- 项目最初采用的流式输出方案是transformers官方自带的TextIteratorStreamer，然而生成速度还是很慢。调研后发现TextIteratorStreamer实际上是将"print-ready text"转换为流式结构，也就是需要LLM首先生成整段文本，再进行转换，这不是我想要的，我想要LLM每生成一个token就yield给我。
- 随后我发现了LowinLi的项目（感谢其付诸的努力），真正地实现了预训练模型的流式输出。当我迫不及待地使用到Llama3模型上时，报错了。debug后发现是因为Llama3有两个eos_token，循环过程中生成了负数的id。于是我在该项目的基础上进行了修正，并清理了冗余，使之适配了Llama3，并更容易阅读和理解。
# 鸣谢🙇

- https://github.com/meta-llama/llama3
- https://github.com/TylunasLi/ChatGLM-web-stream-demo
- https://github.com/LowinLi/transformers-stream-generator

