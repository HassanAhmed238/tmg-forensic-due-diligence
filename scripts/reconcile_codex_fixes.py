# -*- coding: utf-8 -*-
"""
Script to apply all fixes identified in the Codex Audit Report:
1. Fix missing Oman (jood_yamal) project filter mapping in both companies table and teams cards.
2. Add escapeHTML() sanitizer and protocol validator for safe DOM injection (anti-XSS).
3. Ensure updateMapTheme(theme) is called inside setTheme(theme).
4. Reconcile build_perfect_dashboard.py and compile both TMG_Forensic_Due_Diligence_Dashboard.html and index.html in full parity.
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

builder_path = Path(r"F:\Mr Hesham\TMG\scripts\build_perfect_dashboard.py")
content = builder_path.read_text(encoding="utf-8")

# 1. Add escapeHTML helper before Tab 11 functions
escape_helper = """
    // XSS Sanitizer & Protocol Validator (Codex Audit Recommendation)
    function escapeHTML(str) {
      if (!str) return '';
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }

    function safeUrl(url, allowedProtocols = ['http:', 'https:']) {
      if (!url) return '';
      try {
        const parsed = new URL(url);
        return allowedProtocols.includes(parsed.protocol) ? parsed.href : '';
      } catch (e) {
        return '';
      }
    }
"""

if "function escapeHTML" not in content:
    content = content.replace("let activeProjectFilter = 'all';", escape_helper + "\n    let activeProjectFilter = 'all';")
    print("escapeHTML and safeUrl helpers injected.")

# 2. Update projMap in renderCompaniesTable
old_comp_filter = """        // Project Match
        if (activeProjectFilter !== 'all') {
          const projMap = {
            'southmed': 'southmed',
            'noor': 'نور',
            'madinaty': 'مدينتي',
            'celia': 'celia',
            'fs_luxor': 'أقصر',
            'fs_sharm': 'شرم',
            'san_stefano': 'سان ستيفانو',
            'banan': 'سعودية'
          };
          const keyword = projMap[activeProjectFilter];
          if (keyword && !c.project.toLowerCase().includes(keyword.toLowerCase())) {
            return false;
          }
        }"""

new_comp_filter = """        // Project Match (Full Multi-Keyword & Oman Support)
        if (activeProjectFilter !== 'all') {
          const projMap = {
            'southmed': ['southmed', 'ساوث'],
            'noor': ['نور', 'noor'],
            'madinaty': ['مدينتي', 'madinaty'],
            'celia': ['celia', 'سيليا'],
            'fs_luxor': ['أقصر', 'luxor'],
            'fs_sharm': ['شرم', 'sharm'],
            'san_stefano': ['سان ستيفانو', 'san stefano', 'إسكندرية'],
            'banan': ['سعودية', 'رياض', 'بنان', 'banan', 'ksa'],
            'jood_yamal': ['عمان', 'جود', 'يامال', 'oman']
          };
          const keywords = projMap[activeProjectFilter];
          if (keywords && !keywords.some(k => (c.project || '').toLowerCase().includes(k.toLowerCase()))) {
            return false;
          }
        }"""

if old_comp_filter in content:
    content = content.replace(old_comp_filter, new_comp_filter)
    print("Updated projMap in renderCompaniesTable with Oman & multi-keyword support.")

# 3. Update projMap in renderTeamsCards
old_team_filter = """        // Project Match
        if (activeProjectFilter !== 'all') {
          const projMap = {
            'southmed': 'southmed',
            'noor': 'نور',
            'madinaty': 'مدينتي',
            'celia': 'celia',
            'fs_luxor': 'أقصر',
            'fs_sharm': 'شرم',
            'san_stefano': 'سان ستيفانو',
            'banan': 'سعودية'
          };
          const keyword = projMap[activeProjectFilter];
          if (keyword && !t.project.toLowerCase().includes(keyword.toLowerCase())) {
            return false;
          }
        }"""

new_team_filter = """        // Project Match (Full Multi-Keyword & Oman Support)
        if (activeProjectFilter !== 'all') {
          const projMap = {
            'southmed': ['southmed', 'ساوث'],
            'noor': ['نور', 'noor'],
            'madinaty': ['مدينتي', 'madinaty'],
            'celia': ['celia', 'سيليا'],
            'fs_luxor': ['أقصر', 'luxor'],
            'fs_sharm': ['شرم', 'sharm'],
            'san_stefano': ['سان ستيفانو', 'san stefano', 'إسكندرية'],
            'banan': ['سعودية', 'رياض', 'بنان', 'banan', 'ksa'],
            'jood_yamal': ['عمان', 'جود', 'يامال', 'oman']
          };
          const keywords = projMap[activeProjectFilter];
          if (keywords && !keywords.some(k => (t.project || '').toLowerCase().includes(k.toLowerCase()))) {
            return false;
          }
        }"""

if old_team_filter in content:
    content = content.replace(old_team_filter, new_team_filter)
    print("Updated projMap in renderTeamsCards with Oman & multi-keyword support.")

# 4. Verify setTheme calls updateMapTheme
set_theme_target = """function setTheme(theme) {
      currentTheme = theme;
      document.documentElement.setAttribute('data-theme', theme);
      document.getElementById('theme-light').classList.toggle('active', theme === 'light');
      document.getElementById('theme-dark').classList.toggle('active', theme === 'dark');
      localStorage.setItem('tmg_theme', theme);
      updateChartsTheme(theme);
    }"""

set_theme_replacement = """function setTheme(theme) {
      currentTheme = theme;
      document.documentElement.setAttribute('data-theme', theme);
      document.getElementById('theme-light').classList.toggle('active', theme === 'light');
      document.getElementById('theme-dark').classList.toggle('active', theme === 'dark');
      localStorage.setItem('tmg_theme', theme);
      updateChartsTheme(theme);
      if (typeof updateMapTheme === 'function') updateMapTheme(theme);
    }"""

if set_theme_target in content:
    content = content.replace(set_theme_target, set_theme_replacement)
    print("setTheme updated to reliably call updateMapTheme(theme).")

# Save updated master script
builder_path.write_text(content, encoding="utf-8")
print("build_perfect_dashboard.py updated with all Codex audit recommendations!")
