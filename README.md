## ローカルでセットアップ
```sh
# uv
curl -LsSf https://astral.sh/uv/install.sh
uv version
> uv 0.4.22

# task
sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d
task -v
> Task version: v3.39.0 (h1:Loe6ppP1x38Puv1M2wigp91bH/garCt0vLWkJsiTWNI=)

# taskのインストール後
task new # 仮想環境セットアップ
source .venv/bin/activate # 仮想環境に入る
task run # pythonスクリプトの実行
```

## dockerでセットアップ
```sh
# Taskがインストール済みなら
task docker:build
task docker:sh

# Taskが未インストールなら
docker compose build --no-cache \
        --build-arg UID=$(id -u) \
        --build-arg GID=$(id -g) \
        --build-arg USERNAME=$(whoami)

docker compose up -d
docker exec -it コンテナ名 sh
```

### メモ
```sh
# 仮想環境に入る
source .venv/bin/activate

# 仮想環境から抜ける
deactivate
```
