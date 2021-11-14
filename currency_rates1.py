

from requests import get, utils
# user_value ='AUD'
# user_value.upper()

def get_response(url, currencie):
      response = get(url)
      encodings = utils.get_encoding_from_headers(response.headers)
      content = response.content.decode(encoding = encodings)
      currencies = content.split('</Valute>',)
      if currencie.upper() in content:
            for element in currencies:
                  if currencie in element:
          # print(element)
                        idx_2 = element.rindex('<Value>')
                        idx = element.rindex('</Value>')
                        my_cur = float((element[idx_2:idx]).strip('<Value>').replace(',', '.'))
                        print(f'Курс {currencie} сегодня {my_cur:.2f} рублей')
      else:
            print(None)


get_response('http://www.cbr.ru/scripts/XML_daily.asp', 'EUR')