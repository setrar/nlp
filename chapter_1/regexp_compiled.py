import re

r = r"[^a-z]*([y]o|[h']?ello|ok|hey|(good[ ])?(morn[gin']{0,3}|"\
       r"afternoon|even[gin']{0,3}))[\s,;:]{1,3}([a-z]{1,20})"

re_greeting = re.compile(r, flags=re.IGNORECASE)

re_greeting.match('Hello Rosa')
re_greeting.match('Hello Rosa').groups()
re_greeting.match("Good Manning Rosa")
re_greeting.match('Good evening Rosa Parks').groups()
re_greeting.match("Good Morn'n Rosa")
re_greeting.match("yo Rosa")
