import json,urllib.request,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
course=json.loads((ROOT/'src/course.json').read_text(encoding='utf-8'))
lessons=[]; page=1
while True:
    req=urllib.request.Request(f'https://stepik.org/api/lessons?course=58852&page={page}',headers={'User-Agent':'DevForge curriculum research/1.0'})
    try:
        with urllib.request.urlopen(req,timeout=30) as response: data=json.load(response)
    except Exception as exc:
        lessons.append({'page':page,'status':'unavailable','error':str(exc)}); break
    for item in data.get('lessons',[]):
        lessons.append({'id':item.get('id'),'title':item.get('title'),'url':item.get('canonical_url'),'unit_ids':item.get('units'),'step_count':len(item.get('steps') or []),'first_step_id':(item.get('steps') or [None])[0],'status':'metadata-only'})
    if not data.get('meta',{}).get('has_next'): break
    page+=1; time.sleep(.1)
items=[]
for topic in course.get('topics',[]):
    for lesson in topic.get('lessons',[]):
        text=' '.join(str(lesson.get(k,'')) for k in ('title','statement','starterCode','solution','hint','solutionExplanation')); tests=lesson.get('tests') or []; issues=[]
        generic=['обычный валидный набор данных','пустой или граничный набор данных','корректный результат по контракту','предсказуемый результат без исключения','Сначала зафиксируйте контракт']
        if any(x in text or any(x in str(t) for t in tests) for x in generic): issues.append('шаблонные формулировки/тесты')
        if not tests or any(not t.get('input') or not t.get('expected') for t in tests): issues.append('неполные тестовые данные')
        if lesson.get('type') in {'pytest','match','choice','predict_output','traceback','refactor','hidden_tests'}: issues.append('тип требует отдельного интерфейса/runner')
        if topic.get('number',0)<=3 and lesson.get('difficulty')=='hard': issues.append('сложность слишком рано')
        status='KEEP' if not issues else ('MOVE' if 'сложность слишком рано' in issues and len(issues)==1 else ('UNSUPPORTED' if 'тип требует отдельного интерфейса/runner' in issues and len(issues)==1 else 'REWORK'))
        items.append({'id':lesson.get('id'),'topic':topic.get('title'),'title':lesson.get('title'),'status':status,'issues':issues,'type':lesson.get('type'),'difficulty':lesson.get('difficulty'),'tests':len(tests)})
counts={s:sum(x['status']==s for x in items) for s in ['KEEP','REWORK','MOVE','REPLACE','UNSUPPORTED']}
out=ROOT/'docs/research'; out.mkdir(parents=True,exist_ok=True)
lines=['# Аудит 250 Python-заданий','',f'Проверено заданий: {len(items)}. Источник: `src/course.json` и прикреплённый список ID.','', '## Сводка','', '| Статус | Количество |','|---|---:|']+[f'| {k} | {v} |' for k,v in counts.items()]+['','## Правила аудита','','- `KEEP`: конкретное условие, проверяемые данные и поддерживаемый тип задания.','- `REWORK`: идея полезна, но есть шаблонные тесты, неполный контракт или несоответствие условия.','- `MOVE`: требуется переставить по уровню сложности.','- `REPLACE`: смысл задания нужно заменить новым.','- `UNSUPPORTED`: нужен отдельный тип интерфейса или runner.','','## Все задания','','| ID | Тема | Тип | Сложность | Статус | Проблемы |','|---|---|---|---|---|---|']
for x in items: lines.append(f"| `{x['id']}` | {x['topic']} | `{x['type']}` | `{x['difficulty']}` | **{x['status']}** | {'; '.join(x['issues']) or 'не обнаружено'} |")
(out/'python-250-audit.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
(out/'stepik-58852-raw-metadata.json').write_text(json.dumps(lessons,ensure_ascii=False,indent=2),encoding='utf-8')
(out/'stepik-58852-lesson-coverage.md').write_text('\n'.join(['# Stepik 58852: покрытие открытого API','',f'Получено уроков: {len(lessons)}.','', '| Поле | Значение |','|---|---:|',f'| Уроки с метаданными | {sum(x.get("status")=="metadata-only" for x in lessons)} |',f'| Уроки с первым шагом | {sum(bool(x.get("first_step_id")) for x in lessons)} |',f'| Недоступные записи/ошибки | {sum(x.get("status")=="unavailable" for x in lessons)} |','', 'API: `https://stepik.org/api/lessons?course=58852&page=N`. Сохраняются только публичные метаданные и step IDs.'])+'\n',encoding='utf-8')
(out/'stepik-58852-methodology.md').write_text('''# Методические выводы по Stepik 58852\n\nПодтверждено открытой страницей курса: обучение начинается с базового ввода/вывода, затем идут условия, типы данных, циклы, строки, списки, функции и мини-проект. Уроки содержат теорию и практику; задачи идут с ростом сложности и проверяются автоматически. Указаны тестовые, табличные, сопоставляющие и программные упражнения.\n\nДля DevForge полезно перенять последовательность от простого к сложному, единый формат урока, несколько типов упражнений, автоматическую проверку, баллы, контрольные точки и мини-проект. Это методические рекомендации DevForge, а не копирование содержания Stepik.\n\nИсточник: https://stepik.org/course/58852/promo (открыт 2026-10-29).\n''',encoding='utf-8')
(out/'python-curriculum-comparison.md').write_text('''# Сравнение программ\n\n| Область | Stepik 58852 | DevForge после аудита | Решение |\n|---|---|---|---|\n| Начало | Ввод-вывод и структурное программирование | 25-темный junior-путь | Публиковать отдельный Basics-путь перед API и ООП |\n| Практика | Автоматическая проверка и несколько типов упражнений | JSON-каталог, часть типов пока требует отдельного интерфейса | Реализовать code runner, quiz, match и debug отдельно |\n| Теория | Текстовые конспекты перед практикой | Теория и термины хранятся в курсе | Расширить построчный разбор и эксперименты |\n| Контроль | Задачи с ростом сложности и мини-проект | Контрольные описаны в JSON | Превратить контрольные в исполняемые наборы |\n\nВыводы, зависящие от Stepik, основаны на открытой странице курса; предложения по DevForge являются собственной архитектурной рекомендацией.\n''',encoding='utf-8')
print(json.dumps({'lessons':len(lessons),'audit':len(items),'counts':counts},ensure_ascii=False))

