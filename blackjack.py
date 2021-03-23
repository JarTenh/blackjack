from modules.ui import UI

def main():
    ui = UI()
    ui.intro()
    ui.show_instructions()
    player_name = ui.ask_player_name()
    ui.start_session(player_name)

if __name__ == '__main__':
    main()
