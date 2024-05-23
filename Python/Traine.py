import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class JavaTrainerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Java Programming Trainer")
        self.create_gradient_background()
        self.create_widgets()

    def create_gradient_background(self):
        # Создание градиентного изображения
        width = 1920
        height = 1080
        image = Image.new("RGB", (width, height), "#FFFFFF")
        for i in range(height):
            r = int(255 * (i / height))
            g = int(128 * (i / height))
            b = int(255 * (i / height))
            for j in range(width):
                image.putpixel((j, i), (r, g, b))
        self.bg_image = ImageTk.PhotoImage(image)

    def create_widgets(self):
        # Меню
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file_menu = tk.Menu(menu)
        menu.add_cascade(label="Главная", menu=file_menu)
        file_menu.add_command(label="Главная", command=self.show_main)
        file_menu.add_command(label="Уроки", command=self.show_lessons)
        file_menu.add_command(label="Упражнения", command=self.show_exercises)
        file_menu.add_command(label="Прогресс", command=self.show_progress)
        file_menu.add_command(label="Профиль", command=self.show_profile)
        file_menu.add_command(label="Выход", command=self.root.quit)

        # Создаем рамку
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Устанавливаем градиентный фон для рамки
        self.canvas = tk.Canvas(self.main_frame, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)

        # Отображаем главную страницу
        self.show_main()

    def show_main(self):
        # Просто для примера: кнопки и другие виджеты
        start_lesson_button = tk.Button(self.main_frame, text="Начать новый урок", command=self.start_lesson, bg="#4CAF50", fg="white", padx=10, pady=5)
        start_lesson_button.place(relx=0.1, rely=0.05, anchor="center")

        start_exercise_button = tk.Button(self.main_frame, text="Начать новое упражнение", command=self.start_exercise, bg="#4CAF50", fg="white", padx=10, pady=5)
        start_exercise_button.place(relx=0.32, rely=0.05, anchor="center")

        recent_activities_label = tk.Label(self.main_frame, text="Последние завершенные задания:", font=("Helvetica", 14), bg="#4CAF50", fg="white", padx=10, pady=5)
        recent_activities_label.place(relx=0.5, rely=0.2, anchor="center")

        recent_activities_list = tk.Listbox(self.main_frame, width=60, height=10, bg="#333333", fg="#FFFFFF")
        recent_activities_list.insert(1, "Урок 1: Введение в Java")
        recent_activities_list.insert(2, "Упражнение 1: Hello World")
        recent_activities_list.insert(3, "Упражнение 2: Основы")
        recent_activities_list.insert(4, "Упражнение 3: Операторы, выражения")
        recent_activities_list.insert(5, "Упражнение 4: Условный оператор if, ветвления")
        recent_activities_list.insert(6, "Упражнение 5: Условный оператор if, продолжение")
        recent_activities_list.place(relx=0.5, rely=0.4, anchor="center")

        contacts_button = tk.Button(self.main_frame, text="Контакты", command=self.show_contacts, bg="#2196F3", fg="white", padx=10, pady=5)
        contacts_button.place(relx=0.2, rely=0.9, anchor="center")

        support_button = tk.Button(self.main_frame, text="Поддержка", command=self.show_support, bg="#2196F3", fg="white", padx=10, pady=5)
        support_button.place(relx=0.5, rely=0.9, anchor="center")

        privacy_button = tk.Button(self.main_frame, text="Политика конфиденциальности", command=self.show_privacy, bg="#2196F3", fg="white", padx=10, pady=5)
        privacy_button.place(relx=0.8, rely=0.9, anchor="center")

    def start_lesson(self):
        messagebox.showinfo("Начать новый урок", "Функция запуска нового урока.")

    def start_exercise(self):
        messagebox.showinfo("Начать новое упражнение", "Функция запуска нового упражнения.")

    def show_lessons(self):
        messagebox.showinfo("Уроки", "Отображение уроков.")

    def show_exercises(self):
        messagebox.showinfo("Упражнения", "Отображение упражнений.")

    def show_progress(self):
        messagebox.showinfo("Прогресс", "Отображение прогресса.")

    def show_profile(self):
        messagebox.showinfo("Профиль", "Отображение профиля пользователя.")

    def show_contacts(self):
        messagebox.showinfo("Контакты", "Контактная информация.")

    def show_support(self):
        messagebox.showinfo("Поддержка", "Информация о поддержке.")

    def show_privacy(self):
        messagebox.showinfo("Политика конфиденциальности", "Информация о политике конфиденциальности.")

if __name__ == "__main__":
    root = tk.Tk()
    app = JavaTrainerApp(root)
    root.mainloop()