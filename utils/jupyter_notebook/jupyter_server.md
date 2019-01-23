There are the ways to connect to the server's jupyter notebook

# first Way

```python
import os
from IPython.lib import passwd

c.NotebookApp.ip = '*'
c.NotebookApp.port = int(os.getenv('PORT', 8888))
c.NotebookApp.open_browser = False

# sets a password if PASSWORD is set in the environment
if 'PASSWORD' in os.environ:
  password = os.environ['PASSWORD']
  if password:
    c.NotebookApp.password = passwd(password)
  else:
    c.NotebookApp.password = ''
    c.NotebookApp.token = ''
  del os.environ['PASSWORD']
```
OR

```python
c = get_config()
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
```

Or 

open python and type
```python
from notebook.auth import passwd
passwd()
```

In terminal
jupyter notebook --generate-config

In .jupyter/jupyter_notebook_config.py

```python
c.NotebookApp.ip = '*'
#设置可访问的ip为任意。
c.NotebookApp.open_browser = False
#设置默认不打开浏览器
c.NotebookApp.password = '第1步生成的密文'
 
c.NotebookApp.port = 6666
c.NotebookApp.notebook_dir = '/your/file/saved/path/'

作者：minningl
链接：https://www.jianshu.com/p/08f276d48669
來源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
```
for more details: https://www.jianshu.com/p/08f276d48669?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation


# second way
remote host: user@remote_host$ jupyter notebook --no-browser --port=8889
local host : ssh -N -L localhost:8888:localhost:8889 user@remote_host