import { chromium } from 'playwright';
const base=process.env.DEVFORGE_URL||'http://127.0.0.1:5173';
let browser; try { browser=await chromium.launch({headless:true}); } catch (error) { console.warn(`browser smoke skipped: ${error.message.split("`n")[0]}`); process.exit(0); }
const page=await browser.newPage({viewport:{width:1440,height:900}});
const failures=[]; const expect=async (ok,msg)=>{if(!ok) failures.push(msg)};
console.log('goto'); await page.goto(base); console.log('home'); await expect(await page.locator('text=DevForge').count()>0,'главная не открылась');
await page.getByRole('button',{name:'Web Lab'}).click(); console.log('weblab'); await expect(await page.locator('text=WEB LAB').count()>0,'Web Lab не открылся');
await page.getByRole('button',{name:'Счётчик кликов'}).click(); await page.getByRole('button',{name:'JAVASCRIPT'}).click(); console.log('js'); console.log('monaco'); await expect(await page.locator('.monaco-editor, .editor-fallback').count()>0,'редактор не отображён');
const editor=page.locator('.editor-fallback').first(); if(await editor.count()) await editor.fill('console.log(\"smoke\")');
await page.getByRole('button',{name:'▶ Запустить'}).click(); console.log('run'); await expect(await page.locator('iframe').count()>0,'iframe preview missing');
await page.getByRole('button',{name:'Проверить задание'}).click(); console.log('check');
console.log('projects'); await page.getByRole('button',{name:'Проекты'}).click({force:true}); console.log('projects-open'); await expect(await page.locator('text=МОИ ПРОЕКТЫ').count()>0,'projects screen missing'); console.log('project-list'); for(const name of ['Персональная веб-страница','Адаптивный многостраничный сайт','Менеджер задач','Приложение с API','Итоговое веб-приложение']){await page.getByRole('button',{name}).click({force:true}); await expect(await page.locator('text=Техническое задание').count()>0,'project workspace missing');} await page.getByRole('button',{name:'Моё обучение'}).click(); await expect(await page.locator('text=Учебная аналитика').count()>0,'progress screen missing'); await page.setViewportSize({width:390,height:844}); await expect(await page.locator('.stats-grid').count()>0,'mobile layout отсутствует');
console.log('closing'); await browser.close(); if(failures.length){console.error(failures.join('\n'));process.exit(1)} console.log('browser smoke passed');

