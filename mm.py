import random
import string

def generate_wordlist(file_path, count, min_length, max_length):
    chars = string.ascii_letters + string.digits + string.punctuation

    try:
        with open(file_path, "w") as file:
            for _ in range(count):
                password_length = random.randint(min_length, max_length)
                password = ''.join(random.choices(chars, k=password_length))
                file.write(password + "\n")

        print(f"[+] Wordlist created successfully at: {file_path}")

    except Exception as e:
        print(f"[!] Error: {e}")

# إعدادات
file_path = "/storage/emulated/0/Download/nn/"  # مسار حفظ القائمة
count = 10000  # عدد كلمات المرور
man_length = 6  # الطول الأدنى لكلمة المرور
max_length = 12  # الطول الأقصى لكلمة المرور

# استدعاء الدالة
generate_wordlist(file_path, count, min_length, max_length)