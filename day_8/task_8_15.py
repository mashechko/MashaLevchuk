# 15. Дан объект {a: 'aaa', b: 'bbb'}. Преобразуйте его в JSON.
import json
with open('task_15.data', 'w') as f:
    json.dump({'a': 'aaa', 'b': 'bbb'}, f)