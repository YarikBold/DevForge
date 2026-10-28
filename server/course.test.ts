import {test} from 'node:test';import assert from 'node:assert/strict';import {pythonCourse,exercises} from '../src/content.ts';
test('published Python lessons contain beginner theory and three hints',()=>{const lessons=pythonCourse.flatMap(m=>m.lessons);assert.ok(lessons.length>=5);for(const l of lessons){assert.equal(l.stage,'published');assert.ok(l.goal.length>10&&l.theory.length>80);assert.equal(l.hints.length,3);assert.ok(l.example&&l.solution&&l.errors.length>0&&l.understanding.length>0)}});

test('Python practice catalog expanded beyond starter set',()=>{const py=exercises.filter((x:any)=>x.language==='python');assert.ok(py.length>=70);assert.equal(new Set(py.map((x:any)=>x.id)).size,py.length);assert.ok(py.some((x:any)=>x.category==='control'))});
