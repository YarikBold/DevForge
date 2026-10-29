import json,io,contextlib
from pathlib import Path
c=json.loads(Path('src/course.json').read_text(encoding='utf-8')); checked=0; failed=[]
for topic in c['topics'][:3]:
 for lesson in topic['lessons']:
  if lesson.get('type') not in {'write_program','debug','hidden_tests'} or lesson.get('runtime')!='stdout': continue
  for case in lesson.get('tests',[])[:2]:
   lines=iter(str(case.get('input','')).splitlines()); ns={'input':lambda:next(lines)}; out=io.StringIO(); checked+=1
   try:
    with contextlib.redirect_stdout(out): exec(lesson['solution'],ns)
    if out.getvalue().strip()!=str(case.get('expected','')).strip(): failed.append(lesson['id'])
   except Exception as exc: failed.append(f"{lesson['id']}: {type(exc).__name__}")
print({'checked':checked,'failed':len(failed),'details':failed})
raise SystemExit(1 if failed else 0)

