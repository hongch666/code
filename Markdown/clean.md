# Ubuntu清理空间
1. 使用apt-get清理
```sh
sudo apt-get clean
sudo apt-get autoremove
sudo apt-get autoclean
```
2. 清理系统缓存
```sh
sudo rm -rf /var/cache/apt/archives/*
sudo rm -rf /var/cache/apt/archives/partial/*
```
3. 清理/tmp目录
```sh
sudo rm -rf /tmp/*
```
4. 清理用户的缓存目录
```sh
rm -rf ~/.cache/*
```
5. 使用journalctl清理系统日志
```sh
sudo journalctl --vacuum-time=0.2weeks
```