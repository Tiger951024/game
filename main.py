import random
import xml.etree.ElementTree as ET

def load_settings():
    tree = ET.parse('settings.xml')
    root = tree.getroot()
    x1 = int(root.find('x1').text)
    x2 = int(root.find('x2').text)
    n = int(root.find('n').text)
    return x1, x2, n

def save_settings(x1, x2, n):
    root = ET.Element("settings")
    ET.SubElement(root, "x1").text = str(x1)
    ET.SubElement(root, "x2").text = str(x2)
    ET.SubElement(root, "n").text = str(n)
    tree = ET.ElementTree(root)
    tree.write('settings.xml')

def game():
    x1, x2, n = load_settings()
    target_number = random.randint(x1, x2)
    
    for _ in range(n):
        guess = int(input("請輸入你的猜測: "))
        if guess == target_number:
            print("恭喜你，猜對了！")
            break
        elif guess < target_number:
            print("太低了，再試一次。")
        else:
            print("太高了，再試一次。")

if __name__ == "__main__":
    game()