using System;
using Telegram.Bot;
using Telegram.Bot.Args;
using Telegram.Bot.Types.Enums;
using Telegram.Bot.Types.ReplyMarkups;

namespace tgBot
{
    internal class Program
    {   
        static TelegramBotClient Bot;
        public static void Main(string[] args)
        {
            Bot = new TelegramBotClient("1643274368:AAEpax0UseXw_mqGU-C31WfkpWGy12m9z7Y");
            
            Bot.OnMessage += BotOnOnMessageReceived;
            Bot.OnCallbackQuery += BotOnCallbackQueryReceived;
            
            var me = Bot.GetMeAsync().Result;
            
            Console.WriteLine(me.FirstName);
            Bot.StartReceiving();
            Console.ReadLine();
            Bot.StopReceiving();
        }

        private static void BotOnCallbackQueryReceived(object sender, CallbackQueryEventArgs e)
        {
            throw new NotImplementedException();
        }

        private static async void BotOnOnMessageReceived(object sender, MessageEventArgs e)
        {
            var message = e.Message;
            if(message == null || message.Type != MessageType.Text)
                return;
            string name = $"{message.From.FirstName} {message.From.LastName}"; 
            Console.WriteLine($"{name} отправил сообщение: '{message.Text}'");
            switch (message.Text)
            {
                case "/start":
                    string text = 
                        @"список команд:
/start - запуск бота
/aboutme - обо мне
/wholoveme - узнать кто тебя любит)";
                    await Bot.SendTextMessageAsync(message.From.Id, text);   
                    break;  
                case "/aboutme":
                    string msg = $"Привет, {name}. Это Нурсултан! Мне 23 года. Я говнокодер)";
                        /* var inlinekeyboard = new InlineKeyboardMarkup(new[]
                    {
                        new[]
                        {
                            InlineKeyboardButton.WithUrl("VK", "https://instagram.com/iamkabulov")
                        },
                        new[]
                        {
                            InlineKeyboardButton.WithCallbackData("Пункт 1")
                        }
                    });
                    await Bot.SendTextMessageAsync(message.From.Id, "Выберите пункт", 
                        replyMarkup: inlinekeyboard);*/
                    await Bot.SendTextMessageAsync(message.From.Id, msg);
                    break;
                case "/wholoveme":
                    string love = "Нурсултан любит тебя ";
                    await Bot.SendTextMessageAsync(message.From.Id, love);
                    break;
            }
            {
                
            }
        }
    }
}