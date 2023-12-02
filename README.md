# autoboot data starter
基于 [autoboot](https://github.com/yizzuide/autoboot) 框架的扩展，用于支持数据层接入。
<p>
  <a href="https://pypi.org/project/autoboot-data">
      <img src="https://img.shields.io/pypi/v/autoboot-data?color=%2334D058&label=pypi%20package" alt="Version">
  </a>
  <a href="https://pypi.org/project/autoboot-data">
        <img src="https://img.shields.io/pypi/pyversions/autoboot-data.svg?color=%2334D058" alt="Python">
    </a>
    <a href="https://pepy.tech/project/autoboot-data">
        <img src="https://static.pepy.tech/personalized-badge/autoboot-data?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads" alt="Downloads">
    </a>
    <a href="https://github.com/yizzuide/autoboot-data/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/yizzuide/autoboot-data" alt="License">
    </a>
</p>

## Quick Start

### Install
```sh
pip install autoboot-web
```

### Usage

#### 配置

* 启动配置文件`.env`
```ini
# 环境名称（默认值：dev，框架根据这个配置项来加载当前的环境配置）
ENV_NAME=dev

APPLICATION_NAME=data-runner
```

* 环境配置文件`.env.dev`
```ini
APPLICATION_NAME=data-runner-dev

REDIS_HOST=127.0.0.1
REDIS_PORT=6379
```

* 主配置文件`autoboot.yaml`
```yaml
autoboot:
  application:
    name: !env APPLICATION_NAME
    module: api

  data:
    redis:
      host: !env REDIS_HOST
      port: !env REDIS_PORT
```

#### 创建并启动容器
```py
from autoboot import AutoBoot, AutoBootConfig
from autoboot_data import redis

context = AutoBoot(AutoBootConfig(config_dir="."))
context.run()

r = redis.connection()
AutoBoot.logger.info(r.ping())
```

## Contributors
有问题可以在issues开话题讨论，如果你有新的想法，创建新的`feat`或`pref`分支并提交PR。

## License
[MIT License](https://github.com/yizzuide/autoboot/blob/main/LICENSE.txt)

## Citation
```bibtex
@article{yizzuide2023autobootData,
  author    = {yizzuide},
  title     = {autobootData: Data starter build with autoboot},
  year      = {2023},
}
```
