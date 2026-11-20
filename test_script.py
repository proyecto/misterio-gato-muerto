import re

# Let's verify we can cleanly parse characters block in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "const characters = {"
end_marker = "const roundTitles = {"

idx_start = content.find(start_marker)
idx_end = content.find(end_marker)

print(f"Start: {idx_start}, End: {idx_end}")
assert idx_start != -1 and idx_end != -1
print("Markers found successfully!")
