with open('Website-UKM-ASC/index.html', 'r', encoding='utf-8') as f:
    c = f.read()
old = '<span class="mono" id="wibClock">Waktu Lokal --:-- WIB</span>'
new = '<span class="footer-clock-badge"><span class="footer-clock-dot"></span><span id="wibClock">Waktu Lokal --:--:-- WIB · Malang</span></span>'
assert old in c, "old span not found"
c = c.replace(old, new)
with open('Website-UKM-ASC/index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Replaced footer clock markup!')
