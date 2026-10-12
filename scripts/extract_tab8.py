with open('scripts/generate_powerbi_ceo_dashboard.py', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="tab-sentiment"')
end_pos = text.find('</div>\n      </div>\n\n      <!-- ==========================================================================\n           TAB 9:', pos)
print("pos:", pos, "end_pos:", end_pos)
chunk = text[pos:end_pos+13]
print("Chunk length:", len(chunk))
with open('scripts/tab8_chunk.txt', 'w', encoding='utf-8') as f:
    f.write(chunk)
print("Saved chunk to tab8_chunk.txt")
