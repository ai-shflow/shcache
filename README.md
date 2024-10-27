# shcache

[![Actions Status](https://github.com/ai-shflow/shcache/workflows/ci/badge.svg?branch=main&event=push)](https://github.com/ai-shflow/shcache/actions?query=workflow%3Aci)
[![License](https://img.shields.io/github/license/ai-shflow/shcache.svg?color=brightgreen)](https://github.com/ai-shflow/shcache/blob/main/LICENSE)
[![Tag](https://img.shields.io/github/tag/ai-shflow/shcache.svg?color=brightgreen)](https://github.com/ai-shflow/shcache/tags)



## Introduction

*shcache* is gpt cache of *[ai-shflow](https://github.com/ai-shflow)* written in Python.



## Prerequisites

- Python >= 3.13.0



## Run

```bash
pip install -Ur requirements.txt
python cache.py --config-file="tests/data/config.yml" --listen-url="127.0.0.1:8080"
```



## Docker

```bash
docker build -f Dockerfile -t ai-shflow/shcache:latest .
docker run ai-shflow/shcache:latest ./shcache --config-file="config.yml" --listen-url="127.0.0.1:8080"
```



## Usage

```
usage: cache.py [-h] --config-file CONFIG_FILE --listen-url LISTEN_URL [-v]

gpt cache

options:
  -h, --help            show this help message and exit
  --config-file CONFIG_FILE
                        config file (.yml)
  --listen-url LISTEN_URL
                        listen url (host:port)
  -v, --version         show program's version number and exit
```



## Settings

*shcache* parameters can be set in the directory [config](https://github.com/ai-shflow/shcache/blob/main/shcache/config).

An example of configuration in [config.yml](https://github.com/ai-shflow/shcache/blob/main/shcache/config/config.yml):

```yaml
```



## License

Project License can be found [here](LICENSE).



## Reference

- [gptcache - modules](https://gptcache.readthedocs.io/en/latest/index.html#modules)

- [gptcache - server](https://github.com/zilliztech/GPTCache/tree/main/examples#How-to-use-GPTCache-server)



- [embedding generator - onnx.py](https://github.com/zilliztech/GPTCache/blob/main/gptcache/embedding/onnx.py)

- [embedding generator - paraphrase-albert-onnx](https://huggingface.co/GPTCache/paraphrase-albert-onnx/)



- [similarity evaluator - distance](https://github.com/zilliztech/GPTCache/blob/main/gptcache/similarity_evaluation/distance.py)



- [cache storage - sqlite3](https://docs.python.org/3/library/sqlite3.html)

- [vectore store - faiss](https://github.com/facebookresearch/faiss)
