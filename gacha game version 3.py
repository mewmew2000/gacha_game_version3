import random
import time

class_names = [
    "Мечник", 
    "Лучник", 
    "Двуручник", 
    "Копейщик", 
    "Маг", 
    "Бард", 
    "Антигерой", 
    "Клирик"
]

class_descriptions = [
    "Мастер клинка. Баланс скорости и защиты.",
    "Смерть издалека. Высокая точность, малая защита.",
    "Разрушитель. Огромный урон, но медлителен.",
    "Страж порядка. Держит дистанцию и пробивает броню.",
    "Повелитель стихий. Мощная магия, хрупкое тело.",
    "Душа компании. Поддерживает союзников и дезориентирует врагов.",
    "Тень правосудия. Использует запрещенные приемы.",
    "Служитель света. Исцеляет раны и карает нежить."
]

class_hp =      [100, 80,  120, 110, 70,  90,  95,  100]
class_damage =  [20,  25,  35,  22,  40,  15,  28,  18]
class_defense = [15,  8,   10,  18,  5,   10,  12,  14]

class_strong = [
    ["нежить", "гоблины"], 
    ["летучие", "быстрые"], 
    ["бронированные", "крупные"],
    ["бронированные", "крупные"],
    ["элементали", "роение"], 
    ["демоны", "нежить"], 
    ["демоны", "анти-магические"],
    ["нежить", "демоны"] 
]

class_weak = [
    ["драконы", "элементали"], 
    ["бронированные", "тролли"],
    ["быстрые", "летучие"], 
    ["быстрые", "роение"],
    ["анти-магические", "глухие"],
    ["механические", "глухие"],
    ["нежить", "священные"], 
    ["механические", "анти-магические"]
]

monster_names = [
    "Гоблин-вор", "Скелет-страж", "Летучая Мышь", "Рыцарь-предатель",
    "Огр-вышибала", "Огненный Элементаль", "Лесной Тролль", "Древний Энт",
    "Волк-оборотень", "Рой Пчёл", "Малый Демон", "Анти-Маг Голем",
    "Каменный Страж", "Механический Паук", "Молодой Дракон"
]

monster_types = [
    "гоблины", "нежить", "летучие", "бронированные",
    "крупные", "элементали", "тролли", "деревянные",
    "быстрые", "роение", "демоны", "анти-магические",
    "глухие", "механические", "драконы"
]

monster_health = [50, 60, 40, 80, 100, 90, 110, 95, 45, 55, 120, 130, 85, 75, 200]
monster_damage = [10, 12, 8, 18, 22, 20, 25, 21, 11, 13, 28, 30, 19, 17, 45]
monster_coins = [10, 15, 8, 25, 30, 35, 40, 45, 12, 20, 50, 55, 35, 40, 100]
monster_exp = [15, 20, 12, 30, 35, 40, 45, 50, 18, 25, 55, 60, 40, 45, 100]

location_names = [
    "Тихая Гавань",
    "Шепчущий Лес",
    "Проклятые Руины",
    "Пепельные Вершины",
    "Логово Дракона"
]

location_descriptions = [
    "Последнее безопасное место для беглецов. Здесь пахнет элем и каждую ночь проводяться весёлые танцы.",
    "Шёпот листвы напоминает вам о непонимании",
    "Камни шепчут имена павших героев. И ваших врагов.",
    "Воздух дрожит от жара. Смотрите не превратитесь в курочку кфс",
    "Даже драконоборцы бояться сюда соваться без дела"
]

location_monsters = [
    [0, 2, 8], 
    [0, 8, 9, 7],
    [1, 3, 13],
    [5, 4, 10],
    [14, 4, 10, 11] 
]

location_unlock_level = [1, 3, 5, 7, 9]

npc_merchant = {
    "name": "Торговец Вёльнир",
    "dialogue": [
        "Эй, ты! Выглядишь так, будто тебя только что выплюнули из ада. Покупаешь или просто любуешься?",
        "У меня есть всё: от ржавых гвоздей до мечей королей. Ну, почти всё. Королевскую печать я не продаю.",
        "Слушай, друг. Если увидишь стражу — беги. Если увидишь меня — покупай. Это единственное правило выживания."
    ]
}

npc_bard = {
    "name": "Бард Лукас",
    "dialogue": [
        "Ах, новенькое лицо! Я знаю все секреты. Например, что король носит парик. Шучу! ...Наполовину.",
        "Хочешь новость? Бесплатно? Говорят, в лесах видели тень с красными глазами. А ещё что пиво разбавлено. Обе новости страшны.",
        "Я пишу балладу о тебе. Пока что она называется 'Неизвестный Беглец с Усталым Лицом'. Звучит эпично, да?"
    ]
}

rare_characters = [
    {"name": "Кенджи", "class": "Лучник", "stars": 4, "desc": "Мастер лука из дальних земель"},
    {"name": "Фридрих Молот", "class": "Двуручник", "stars": 4, "desc": "Наемник с тяжелым молотом"},
    {"name": "Сакура", "class": "Маг", "stars": 4, "desc": "Восточная чародейка ветра"}
]

epic_characters = [
    {"name": "Астрид", "class": "Копейщик", "stars": 5, "desc": "Северная воительница, непробиваемая защита"},
    {"name": "Хироши Тень", "class": "Антигерой", "stars": 5, "desc": "Ниндзя, использующий запретные техники"}
]

legendary_characters = [
    {"name": "Бьёрн Светлый", "class": "Клирик", "stars": 6, "desc": "Легендарный целитель, может воскресить павших"},
    {"name": "Ингрид Железная", "class": "Двуручник", "stars": 6, "desc": "Рыцарша с двуручным мечом, разрубает горы"}
]

username = ""
class_index = 0
player_class = ""
player_max_hp = 0
player_hp = 0
player_base_damage = 0
player_defense = 0
player_coins = 0
player_level = 1
player_exp = 0
player_exp_to_next = 100
player_battles_won = 0
player_battles_fled = 0
unlocked_locations = []
current_location = 0
gacha_characters = []
active_character_index = -1

def init_game():
    global username, class_index, player_class, player_max_hp, player_hp
    global player_base_damage, player_defense, player_coins, player_level
    global player_exp, player_exp_to_next, unlocked_locations, current_location
    global gacha_characters, active_character_index

    print("=" * 60)
    print("Мир Драконов и мечей")
    print("=" * 60)
    print("\nВы просыпаетесь от холодного ветра, пробирающего до костей")
    print("Это лес. Голова раскалывается. Последнее, что вы помните —")
    print("крик короля: 'Измена!' и лязг кандалов.")
    print("\nВас обвинили в том, чего вы не совершали.")
    print("Король должен быть отравлен, трон шатается, на юге огнедышащий дракон разоряет города, а стража ищет вашу голову.")
    print("Единственный путь — вниз, в преступный мир, собирать союзников")
    print("и найти настоящего предателя, пока не стало слишком поздно.")
    print("\n'Добро пожаловать во тьму, путник. Надеюсь, ты выберешься живым'")
    print("=" * 60)

    username = input("\nВведите имя вашего беглеца: ").strip()
    if not username:
        username = "Безымянный Предатель"

    print(f"\n{'=' * 60}")
    print("⚔️  ВЫБЕРИТЕ СВОЙ КЛАСС")
    print(f"{'=' * 60}\n")

    for i in range(len(class_names)):
        print(f"{i+1}. {class_names[i]}")
        print(f"   {class_descriptions[i]}")
        print(f"   HP: {class_hp[i]} | Урон: {class_damage[i]} | Защита: {class_defense[i]}")
        print(f"   ✅ Сильно против: {', '.join(class_strong[i])}")
        print(f"   ❌ Слабо против: {', '.join(class_weak[i])}")
        print()

    while True:
        choice = input("Введите номер класса (1-8): ").strip()
        if choice in [str(x) for x in range(1, 9)]:
            class_index = int(choice) - 1
            break
        print("❌ Неверный ввод. Введите число от 1 до 8")

    player_class = class_names[class_index]
    player_max_hp = class_hp[class_index]
    player_hp = player_max_hp
    player_base_damage = class_damage[class_index]
    player_defense = class_defense[class_index]

    player_coins = 50
    player_level = 1
    player_exp = 0
    player_exp_to_next = 100
    player_battles_won = 0
    player_battles_fled = 0

    unlocked_locations = [0]
    current_location = 0

    gacha_characters = []
    active_character_index = -1

    print(f"\n✅ Приветствую, {username}.")
    print(f"Ваш класс: {player_class}")
    print(f"Стартовые монеты: {player_coins} (хватит только на плохой эль)")
    print(f"HP: {player_hp}/{player_max_hp}")

def get_class_modifier(c_idx, m_type):
    if m_type in class_strong[c_idx]:
        return 1.5
    elif m_type in class_weak[c_idx]:
        return 0.5
    else:
        return 1.0

def show_status():
    hp_bar = "█" * (player_hp // 5) + "░" * ((player_max_hp - player_hp) // 5)
    
    print(f"\n{'=' * 60}")
    print(f"👤 {username} ({player_class}) | Ур.{player_level} | 💰 {player_coins}")
    print(f"❤️  HP: [{hp_bar}] {player_hp}/{player_max_hp}")
    print(f"⚔️  Урон: {player_base_damage} | 🛡️  Защита: {player_defense}")
    print(f"📍 {location_names[current_location]}")
    
    if gacha_characters and active_character_index >= 0:
        ally = gacha_characters[active_character_index]
        stars = "⭐" * ally['stars']
        print(f"🤝 Активный союзник: {ally['name']} [{ally['class']}] {stars}")
    else:
        print(f"🤝 Союзников нет (используйте гачу)")
    
    print(f"{'=' * 60}")

def calculate_attack():
    roll = random.randint(1, 100)
    if roll <= 1: 
        return "КРИТИЧЕСКИЙ УДАР", 3.0, "1"
    elif roll <= 20:
        return "МОЩНЫЙ УДАР ОТЧАЯНИЯ", 2.0, "2-20"
    else:
        return "Обычный удар", 1.0, "50-100"

def interact_npc(npc_type):
    if npc_type == "merchant":
        npc = npc_merchant
    else:
        npc = npc_bard
    
    print(f"\n🗣️  {npc['name']}:")
    print(f"'{random.choice(npc['dialogue'])}'")

def battle():
    global player_hp, player_coins, player_exp, player_exp_to_next
    global player_level, player_max_hp, player_base_damage, player_battles_won, player_battles_fled
    
    available_monsters = location_monsters[current_location]
    monster_idx = random.choice(available_monsters)
    
    e_name = monster_names[monster_idx]
    e_type = monster_types[monster_idx]
    e_hp = monster_health[monster_idx]
    e_atk = monster_damage[monster_idx]
    e_coins = monster_coins[monster_idx]
    e_exp = monster_exp[monster_idx]
    
    print(f"\n{'=' * 60}")
    print(f"⚔️  АТАКА!")
    print(f"{'=' * 60}")
    print(f"Враг: {e_name} [{e_type}]")
    print(f"HP врага: {e_hp} | Атака: {e_atk}")
    print(f"Ваш класс: {player_class}")
    
    modifier = get_class_modifier(class_index, e_type)
    if modifier > 1.0:
        print(f"✨ Ваш класс идеален против этой твари! (+50% урона)")
    elif modifier < 1.0:
        print(f"⚠️  Ваш класс слаб против этого ужаса! (-50% урона)")
    
    ally_bonus = 0
    if gacha_characters and active_character_index >= 0:
        ally = gacha_characters[active_character_index]
        ally_bonus = ally['stars'] * 2 
        print(f"🤝 Союзник {ally['name']} помогает вам! (+{ally_bonus} урона)")
    
    print(f"\n1 - Атаковать")
    print(f"2 - Убежать (как трус)")
    
    action = input("\nВыбор (1-2): ").strip()
    
    if action == "2":
        print(f"\n🏃 Вы позорно сбежали от {e_name}!")
        player_battles_fled += 1
        return
    
    print(f"\n{'=' * 60}")
    print(f"⚔️  СМЕРТЕЛЬНАЯ СХВАТКА НАЧАЛАСЬ")
    print(f"{'=' * 60}\n")
    
    while e_hp > 0 and player_hp > 0:
        atype, mult, rng = calculate_attack()

        base_dmg = random.randint(10, 20) + player_base_damage // 2
        final_dmg = int((base_dmg + ally_bonus) * mult * modifier)
        
        print(f"⚔️  {atype} ({rng})")
        print(f"💥 Урон: {final_dmg}")
        
        e_hp -= final_dmg
        
        if e_hp <= 0:
            print(f"\n🎉 ПОБЕДА! {e_name} побеждён!")
            player_coins += e_coins
            player_exp += e_exp
            player_battles_won += 1
            print(f"✨ Награда: {e_coins} монет, {e_exp} опыта")
            
            if player_exp >= player_exp_to_next:
                player_level += 1
                player_exp -= player_exp_to_next
                player_exp_to_next = int(player_exp_to_next * 1.5)
                player_max_hp += 10
                player_hp = player_max_hp
                player_base_damage += 2
                
                for i in range(len(location_unlock_level)):
                    if player_level >= location_unlock_level[i] and i not in unlocked_locations:
                        unlocked_locations.append(i)
                        print(f"🔓 Открыто: {location_names[i]}!")
                
                print(f"🎊 УРОВЕНЬ {player_level}! HP: {player_max_hp}, Урон: {player_base_damage}")
            return

        m_dmg = max(1, random.randint(5, 15) - player_defense)
        player_hp -= m_dmg
        print(f"\n💥 {e_name} атакует! Урон: {m_dmg}")
        print(f"❤️  HP: {max(0, player_hp)}/{player_max_hp}")
        
        if player_hp <= 0:
            print(f"\n💀 ВЫ ПАЛИ... Но судьба еще не решена.")
            player_hp = 0
            return
        
        print(f"\nПродолжить атаку?")
        print(f"1 - Да")
        print(f"2 - Нет (сбежать)")
        print(f"3 - В меню")
        
        cont = input("\nВыбор (1-3): ").strip()
        if cont in ["2", "3"]:
            print(f"\n🏃 Вы оставили {e_name} недобитым.")
            player_battles_fled += 1
            return

def change_class_or_ally():
    global class_index, player_class, player_max_hp, player_hp
    global player_base_damage, player_defense, active_character_index
    
    if gacha_characters:
        print("\n⚠️  У вас есть призванные союзники.")
        print("1 - Сменить класс персонажа (сбросит статы!)")
        print("2 - Выбрать активного союзника")
        print("3 - Отмена")
        
        ch = input("Выбор (1-3): ").strip()
        if ch == "1":
            pass 
        elif ch == "2":
            show_gacha_inventory()
            return
        else:
            return
    
    print(f"\n{'=' * 60}")
    print("⚔️  СМЕНА КЛАССА")
    print(f"{'=' * 60}\n")
    
    for i in range(len(class_names)):
        print(f"{i+1}. {class_names[i]} - {class_descriptions[i]}")
        print(f"   HP: {class_hp[i]} | Урон: {class_damage[i]}")
    
    while True:
        c = input("Номер (1-8): ").strip()
        if c in [str(x) for x in range(1, 9)]:
            class_index = int(c) - 1
            player_class = class_names[class_index]
            player_max_hp = class_hp[class_index]
            player_hp = player_max_hp
            player_base_damage = class_damage[class_index]
            player_defense = class_defense[class_index]
            print(f"✅ Теперь вы: {player_class}")
            break
        print("❌ Ошибка")

def show_gacha_inventory():
    global active_character_index
    
    if not gacha_characters:
        print("\n❌ У вас нет призванных союзников!")
        return
    
    print(f"\n📦 Ваши союзники:")
    for i, char in enumerate(gacha_characters):
        stars = "⭐" * char['stars']
        active = " 📍 АКТИВНЫЙ" if i == active_character_index else ""
        print(f"{i+1}. {char['name']} ({char['class']}) {stars}{active}")
        print(f"   {char['desc']}")
    
    print(f"\nВыберите активного союзника (номер) или 0 для отмены:")
    try:
        choice = int(input("Выбор: ").strip())
        if choice == 0:
            return
        if 1 <= choice <= len(gacha_characters):
            active_character_index = choice - 1
            print(f"✅ Активный союзник: {gacha_characters[active_character_index]['name']}")
        else:
            print("❌ Неверный номер")
    except:
        print("❌ Ошибка ввода")

def change_location():
    global current_location
    print(f"\n{'=' * 60}")
    print("🗺️  КАРТА МИРА")
    print(f"{'=' * 60}\n")
    
    for i in range(len(location_names)):
        if i in unlocked_locations:
            cur = " 📍 ВЫ ЗДЕСЬ" if i == current_location else ""
            print(f"[{i+1}] {location_names[i]}{cur}")
            print(f"    {location_descriptions[i]}")
        else:
            print(f"[{i+1}] {location_names[i]} 🔒 (Уровень {location_unlock_level[i]})")
        print()
    
    while True:
        c = input("Куда отправимся? (номер): ").strip()
        try:
            idx = int(c) - 1
            if idx in unlocked_locations:
                current_location = idx
                print(f"✅ Вы прибыли в: {location_names[current_location]}")
                break
            else:
                print("❌ Дорога закрыта. Нужно стать сильнее.")
        except:
            print("❌ Неверно")

def show_stats():
    print(f"\n{'=' * 60}")
    print("📊 ДОСЬЕ БЕГЛЕЦА")
    print(f"{'=' * 60}")
    print(f"Имя: {username}")
    print(f"Класс: {player_class}")
    print(f"Уровень: {player_level}")
    print(f"Опыт: {player_exp}/{player_exp_to_next}")
    print(f"Монеты: {player_coins}")
    print(f"Побед: {player_battles_won}")
    print(f"Позорных побегов: {player_battles_fled}")
    print(f"Союзников: {len(gacha_characters)}")
    print(f"Открыто земель: {len(unlocked_locations)}/{len(location_names)}")

def gacha_system():
    global player_coins, gacha_characters, active_character_index
    
    cost = 100
    if player_coins < cost:
        print(f"❌ Нужно {cost} монет. У вас: {player_coins}. Ищите сокровища!")
        return
    
    player_coins -= cost
    print(f"\n🎲 Вы бросаете монету в древний колодец призыва...")
    time.sleep(1)
    print("💫 Свет заполняет пространство...")
    time.sleep(1)
    
    roll = random.randint(1, 100)
    new_char = None
    
    if roll > 50:
        junk = ["Старый носок", "Пустая бутылка", "Камень", "Лысая крыса"]
        item = random.choice(junk)
        print(f"⚪ Выпало: {item}... Это мусор. Попробуйте еще раз.")
        player_coins += 50
        print(f"💰 Вам вернули 50 монет из жалости.")
        return
        
    elif roll > 20:
        new_char = random.choice(rare_characters)
        print(f"🟢🟢🟢🟢 Выпал герой: {new_char['name']}!")
        print(f"⭐⭐⭐⭐ (4 звезды)")
        
    elif roll > 10:
        new_char = random.choice(epic_characters)
        print(f"🔵🔵🔵🔵🔵 Выпал герой: {new_char['name']}!")
        print(f"⭐⭐⭐⭐⭐ (5 звезд)")
        
    else:
        new_char = random.choice(legendary_characters)
        print(f"🟡🟡🟡🟡🟡🟡 ЛЕГЕНДА! {new_char['name']} присоединяется к вам!")
        print(f"⭐⭐⭐⭐⭐⭐ (6 ЗВЕЗД!)")
    
    if new_char:
        gacha_characters.append(new_char)
        if len(gacha_characters) == 1:
            active_character_index = 0
        print(f"\n📜 {new_char['desc']}")
    
    print(f"💰 Осталось монет: {player_coins}")

def fake_donate():
    print(f"\n{'=' * 60}")
    print("💳 КУПИТЬ ПРИМОГЕМЫ")
    print(f"{'=' * 60}")
    
    choice = input("\nВаш выбор (1-3): ").strip()
    
    if choice == "3":
        card = input("Введите номер карты (16 цифр): ").strip()
        if len(card) == 16 and card.isdigit():
            print(f"\nМы сохранили вашу карту {card[:4]}****{card[-4:]}.")
            print("Спасибо!")
        else:
            print("❌ Нужно ввести 16 цифр!")

def game_loop():
    while True:
        show_status()
        
        print(f"\n📋 МЕНЮ БЕГЛЕЦА:")
        print(f"1 - Исследовать локацию")
        print(f"2 - Поговорить с Торговцем Бормундом")
        print(f"3 - Послушать Барда Лютниуса")
        print(f"4 - Сменить класс / Выбрать союзника")
        print(f"5 - Призвать союзника (Гача, 100 монет)")
        print(f"6 - Статистика")
        print(f"7 - 💳 Поддержать проект (Донат-шутка)")
        print(f"8 - Выход")
        
        choice = input("\nВыбор (1-8): ").strip()
        
        if choice == "1":
            print(f"\n📍 {location_names[current_location]}")
            print(f"{location_descriptions[current_location]}")
            print(f"\n1 - Искать приключения (бой)")
            print(f"2 - Сменить локацию")
            print(f"3 - Назад")
            
            sub = input("\nВыбор (1-3): ").strip()
            if sub == "1":
                battle()
            elif sub == "2":
                change_location()
        
        elif choice == "2":
            interact_npc("merchant")
        
        elif choice == "3":
            interact_npc("bard")
        
        elif choice == "4":
            change_class_or_ally()
        
        elif choice == "5":
            gacha_system()
        
        elif choice == "6":
            show_stats()
        
        elif choice == "7":
            fake_donate()
        
        elif choice == "8":
            print(f"\n👋 Прощай, {username}. Пусть удача будет на вашей стороне.")
            print("И помните: король невиновен... наверное.")
            break
        
        else:
            print("❌ Неверная команда")

        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    init_game()
    game_loop()