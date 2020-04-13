# Qnap-auto-power-off
Qnap nas auto power off script.威联通Nas配合非管理UPS自动关机脚本
博客地址：https://www.jianshu.com/p/e0beeeff3138

1. 将文件都放在第一块硬盘的software目录下，修改修改`auto_power_off.py`文件中`routerAddress`为你的路由地址
2. 给`start_check_power.sh`添加运行权限
3. 设置定时任务，编辑`/etc/config/crontab`添加以下规则：
```
*/2 * * * * /usr/local/bin/python /share/CACHEDEV1_DATA/software/auto_power_off_deamon.py
```
4. 执行`crontab /etc/config/crontab && /etc/init.d/crond.sh restart`重启crontab
5. Enjoy!
