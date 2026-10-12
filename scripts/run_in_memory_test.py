import sys
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

test_runner_js = """
const fs = require('fs');
const html = fs.readFileSync('F:/Mr Hesham/TMG/TMG_Forensic_Due_Diligence_Dashboard.html', 'utf8');

// Find script containing tmgFinData
const sIdx = html.indexOf('const tmgFinData = {');
const scriptStart = html.lastIndexOf('<script', sIdx);
const scriptContentStart = html.indexOf('>', scriptStart) + 1;
const scriptEnd = html.indexOf('</script>', sIdx);

const codeToEval = html.substring(scriptContentStart, scriptEnd);

const domStore = {};
function getOrCreate(id) {
  if (!domStore[id]) {
    domStore[id] = {
      id: id,
      innerHTML: '',
      textContent: '',
      value: '50000000',
      style: {},
      classList: {
        toggle: function(cls, state) {},
        add: function(cls) {},
        remove: function(cls) {}
      },
      getContext: function() { return {}; }
    };
  }
  return domStore[id];
}

global.document = {
  documentElement: { setAttribute: () => {}, getAttribute: () => 'ar' },
  getElementById: (id) => getOrCreate(id),
  querySelectorAll: (selector) => [],
  querySelector: (selector) => null,
  addEventListener: () => {}
};
global.window = { addEventListener: () => {} };
global.localStorage = { getItem: () => 'ar', setItem: () => {} };
global.currentLang = 'ar';
global.currentTheme = 'light';
global.Chart = function() { return { destroy: () => {} }; };

eval(codeToEval);

console.log("Testing setFinView('is-bs')...");
setFinView('is-bs');
console.log("IS&BS tbody rows count:", domStore['fin-fs-tbody'].innerHTML.split('<tr').length - 1);

console.log("Testing setFinView('sources-uses')...");
setFinView('sources-uses');
console.log("Sources&Uses tbody rows count:", domStore['fin-su-tbody'].innerHTML.split('<tr').length - 1);

console.log("Testing setFinView('common-size')...");
setFinView('common-size');
console.log("CommonSize tbody rows count:", domStore['fin-cs-tbody'].innerHTML.split('<tr').length - 1);

console.log("Testing setFinView('cfo-ratios')...");
setFinView('cfo-ratios');
console.log("CFO Ratios tbody rows count:", domStore['fin-rt-tbody'].innerHTML.split('<tr').length - 1);

console.log("Testing updateSimCalculations()...");
getOrCreate('sim-input-val').value = '60000000';
getOrCreate('sim-input-mep').value = '70';
getOrCreate('sim-input-days').value = '180';
getOrCreate('sim-input-fx').value = '20';
updateSimCalculations();
console.log("Sim Frozen Capital:", domStore['res-sim-frozen'].textContent);
console.log("Sim Verdict:", domStore['res-sim-verdict-title'].textContent);

console.log("Testing Unit Slicer conversions...");
setFinUnit('thousands');
console.log("Thousands Unit test complete.");
setFinUnit('usd');
console.log("USD Unit test complete.");
setFinUnit('billions');
console.log("Billions Unit test complete.");

console.log("Testing Language switch to English...");
currentLang = 'en';
updateFinancialLanguage();
console.log("English translation update complete.");

console.log("ALL IN-MEMORY RUNTIME CHECKS PASSED WITH FLYING COLORS!");
"""

with open("scripts/test_runtime.js", "w", encoding="utf-8") as tf:
    tf.write(test_runner_js)

res = subprocess.run(["node", "scripts/test_runtime.js"], capture_output=True, text=True, encoding="utf-8")
print(res.stdout)
if res.stderr:
    print("STDERR:\n", res.stderr)
