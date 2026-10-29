import json
from pathlib import Path
p=Path('src/course.json'); d=json.loads(p.read_text(encoding='utf-8'))
for t in d['topics'][:3]:
 for l in t['lessons']:
  if l['id']=='python-io-ops-02': l['solution']='total_minutes = 135\nhours = total_minutes // 60\nminutes = total_minutes % 60\nprint(f"{hours} ч {minutes} мин")'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
