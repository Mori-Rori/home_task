
 def get_mask_card_number(card_number):
     #удаляем ненужные пробелы в номере
     card_number = card_number.replace(" ", ' ')
     #проверяем длину номера
     if len(card_number) != 16:
         raise ValueError

     #создаем маску
     masked_number = card_number[:6] + " " + card_number[6:8] + "** ****" + card_number[-4]

     return masked_number



 def get_mask_account(account_number):
     # Удаляем лишние пробелы, если они есть
     account_number = account_number.replace(" ", "")

     # Проверяем длину номера счета
     if len(account_number) < 4:
         raise ValueError("Номер счета должен содержать не менее 4 цифр.")

     # Создаем маску
     masked_number = "**" + account_number[-4:]

     return masked_number