from urllib import request 
request.urlopen("spam://spam.com")

"""
$ python materials/chapter10_aux/traceback.py 
Traceback (most recent call last):
  File "materials/chapter10_aux/traceback.py", line 2, in <module>
    request.urlopen("spam://spam.com")
  File "/home/shinseitaro/miniconda3/lib/python3.8/urllib/request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "/home/shinseitaro/miniconda3/lib/python3.8/urllib/request.py", line 525, in open
    response = self._open(req, data)
  File "/home/shinseitaro/miniconda3/lib/python3.8/urllib/request.py", line 547, in _open
    return self._call_chain(self.handle_open, 'unknown',
  File "/home/shinseitaro/miniconda3/lib/python3.8/urllib/request.py", line 502, in _call_chain
    result = func(*args)
  File "/home/shinseitaro/miniconda3/lib/python3.8/urllib/request.py", line 1421, in unknown_open
    raise URLError('unknown url type: %s' % type)
urllib.error.URLError: <urlopen error unknown url type: spam>
"""