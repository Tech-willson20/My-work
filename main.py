import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

class RockPaperScissorsApp(App):
    def build(self):

        layout = BoxLayout(orientation='vertical', padding=50)

        background_image = Image(source="images.png", allow_stretch=True)
        layout.add_widget(background_image)



        welcome_label = Label(text="Welcome to WILLS TECH GAMING ONLINE.")
        layout.add_widget(welcome_label)

        name_input = TextInput(hint_text='Please input your name')
        layout.add_widget(name_input)

        start_button = Button(text='Start Game')
        start_button.bind(on_release=lambda x: self.start_game(name_input.text))
        layout.add_widget(start_button)

        return layout

    def start_game(self, name):
        options = ["Rock", "Paper", "Scissors"]
        options = [element.lower() for element in options]

        user_wins = 0
        computer_wins = 0

        popup_content = BoxLayout(orientation='vertical', padding=50)
        popup_label = Label(text="Please input start with a capital letter like Rock, Paper, or Scissors")
        popup_content.add_widget(popup_label)

        while True:
            popup = Popup(title='Rock Paper Scissors Game', content=popup_content, size_hint=(None, None), size=(400, 200))
            popup.open()

            user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
            popup.dismiss()

            if user_input == "q":
                break

            if user_input not in options:
                continue

            random_number = random.randint(0, 2)
            computer_pick = options[random_number]
            popup_label.text = "Computer picked " + computer_pick + "."

            if (user_input == "rock" and computer_pick == "scissors") or \
                    (user_input == "paper" and computer_pick == "rock") or \
                    (user_input == "scissors" and computer_pick == "paper"):
                popup_label.text = "You have won"
                user_wins += 1
            elif user_input == computer_pick:
                popup_label.text = "This is a draw, try your luck next time."
            else:
                popup_label.text = "You lost!"
                computer_wins += 1

        popup_label.text = "You won " + str(user_wins) + " times.\nThe computer won " + str(computer_wins) + " times.\nGoodbye"
        input("Press any key to close the game. See you next time.")

if __name__ == '__main__':
    RockPaperScissorsApp().run()
