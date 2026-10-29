import json,urllib.request
from concurrent.futures import ThreadPoolExecutor,as_completed
from pathlib import Path
root=Path(__file__).resolve().parents[1]; path=root/'docs/research/stepik-58852-raw-metadata.json'; lessons=json.loads(path.read_text(encoding='utf-8'))
def fetch(item):
 sid=item.get('first_step_id')
 if not sid: return item
 try:
  req=urllib.request.Request(f'https://stepik.org/api/steps/{sid}',headers={'User-Agent':'DevForge curriculum research/1.0'})
  with urllib.request.urlopen(req,timeout=30) as r: d=json.load(r)
  st=(d.get('steps') or [{}])[0]; item['first_step']={'id':sid,'position':st.get('position'),'block_name':st.get('block',{}).get('name'),'has_text':bool(st.get('block',{}).get('text')),'instruction_type':st.get('instruction_type'),'accessible':True}
 except Exception as exc: item['first_step']={'id':sid,'accessible':False,'error':str(exc)}
 return item
with ThreadPoolExecutor(max_workers=6) as pool: lessons=list(pool.map(fetch,lessons))
path.write_text(json.dumps(lessons,ensure_ascii=False,indent=2),encoding='utf-8')
accessible=sum(bool(x.get('first_step',{}).get('accessible')) for x in lessons); text=sum(bool(x.get('first_step',{}).get('has_text')) for x in lessons)
(root/'docs/research/stepik-58852-lesson-coverage.md').write_text('\n'.join(['# Stepik 58852: покрытие открытого API','',f'Получено уроков: {len(lessons)}.','', '| Поле | Значение |','|---|---:|',f'| Уроки с метаданными | {len(lessons)} |',f'| Первые шаги успешно открыты | {accessible} |',f'| Первые шаги с текстовым блоком | {text} |',f'| Ошибки/недоступные шаги | {len(lessons)-accessible} |','', 'Проверены публичные endpoints уроков и первых шагов. Полные тексты и решения Stepik не сохраняются в репозитории; в JSON остаются только структурные признаки доступа.'])+'\n',encoding='utf-8')
print({'lessons':len(lessons),'steps_accessible':accessible,'text_blocks':text})
