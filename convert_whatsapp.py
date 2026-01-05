import re
from pathlib import Path
from datetime import datetime

input_file = "input.txt"
output_file = "output.txt"

# محارف RTL الخفية في واتساب العربي
RTL_CHARS = "\u200e\u200f\u202a\u202b\u202c"

def clean_rtl(text):
    for ch in RTL_CHARS:
        text = text.replace(ch, "")
    return text.strip()

text = Path(input_file).read_text(encoding="utf-8", errors="ignore")

output = []
current = None

# Regex السطر الأساسي (عربي واتساب)
line_pattern = re.compile(
    r"""
    ^\s*
    (\d{1,2})/(\d{1,2})/(\d{4})
    \s*[،,]\s*
    (\d{1,2}:\d{2}:\d{2})
    \s*(AM|PM)
    \s*-\s*
    (.+)
    """,
    re.VERBOSE
)

# Regex استخراج اسم الملف من <المُرفق: ...>
attachment_pattern = re.compile(
    r"<المُرفق:\s*([^>]+)>"
)

for raw_line in text.splitlines():
    line = clean_rtl(raw_line)

    m = line_pattern.match(line)
    if m:
        if current:
            output.append(current)

        day, month, year, time, ampm, rest = m.groups()
        year = year[-2:]

        # تحويل الوقت إلى 24 ساعة مع الثواني
        dt = datetime.strptime(f"{time} {ampm}", "%H:%M:%S %p")
        time_24 = dt.strftime("%H:%M:%S")

        # 🔹 هل السطر يحتوي على مرفق؟
        att = attachment_pattern.search(rest)
        if att:
            filename = att.group(1)
            current = (
                f"[{day.zfill(2)}.{month.zfill(2)}.{year}, {time_24}] "
                f"{rest.split(':', 1)[0]}: <attached: {filename}>"
            )
        else:
            # رسالة عادية (نتركها كما هي أو يمكنك توحيدها لاحقًا)
            current = (
                f"[{day.zfill(2)}.{month.zfill(2)}.{year}, {time_24}] "
                f"{rest}"
            )

    else:
        if current:
            current += "\n" + line

if current:
    output.append(current)

Path(output_file).write_text("\n".join(output), encoding="utf-8")

print("✅ تم التحويل بنجاح")
print(f"📄 الملف الناتج: {output_file}")
