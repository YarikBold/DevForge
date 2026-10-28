import {test} from 'node:test';import assert from 'node:assert/strict';import {runCpp} from './runners.ts';
test('C++ runner compiles and executes real program',async()=>{const r=await runCpp('#include <iostream>\nint main(){int x;std::cin>>x;std::cout<<x*2;}','21');assert.equal(r.phase,'run');assert.equal(r.stdout,'42');assert.equal(r.timedOut,false)});
test('C++ runner reports compile errors',async()=>{const r=await runCpp('int main(){ this is invalid; }','');assert.equal(r.phase,'compile');assert.notEqual(r.code,0);assert.ok(r.stderr.length>0)});
test('C++ runner terminates infinite loop',async()=>{const r=await runCpp('int main(){while(true){} }','');assert.equal(r.phase,'run');assert.equal(r.timedOut,true)});
