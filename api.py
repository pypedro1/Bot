import requests
import json
import blaze_double as g
import telebot
import time

class bot:
    def __init__(self):
        self.name = 'Blaze Double'
        self.token_bot = '6665098953:AAEOnpkgR11McGLgm507krPlcKjVgKu10F8'
        self.user_id = '-1001915782988'
        self.link = 'http://api.mxvinvest.com:63000/blaze-double'
        self.chave = 'blaze_double'
        self.result = None
        self.now = None
        self.check_now = None
        self.now_time = 0
        self.message_ids = 0
        self.entrada_atual = 0
        self.message_delete = False
        self.win_results = 0
        self.loss_results = 0
        self.empate_results = 0
        self.max_hate = 0
        self.win_hate = 0
        self.win_semgale = 0
        self.win_gale1 = 0
        self.win_gale2 = 0
        self.empate_semgale = 0
        self.empate_gale1 = 0
        self.empate_gale2 = 0
        self.analisar = 0
        self.bot = telebot.TeleBot(token=self.token_bot, parse_mode='MARKDOWN')
        g.utils.get_data(self)

    def requets_game(self):
        time.sleep(1)
        url = requests.get(self.link)
        data = json.loads(url.content)
        results = data["results"]
        print (results)
        return results

    def rum(self):
        check_results = []
        while True:
            main_results = self.requets_game()

            if main_results != check_results:
                print(main_results)
                check_results = main_results
                g.utils.delet(self)
                g.utils.estrategy(self, main_results)


try:
    objeto = bot()
    objeto.rum()
except:
    pass
