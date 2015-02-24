"""
До цього ми писали тести за допомогою `assert`, а зараз
напишемо тести по-дорослому.

Попередні інструкції:
1. Створити папку для цієї вправи і перейти в неї
2. Покласти цей файл в неї
4. Створити в папці віртуальне середовище
   ```
   pyvenv-3.4 venv
   ```
5. Активувати Python з середовища
   ```
   . venv/bin/activate
   ```
6. Встановити nose – пакет, який виконує тести
   ```
   pip install nose
   ```
7. Перезавантажити середовище
   ```
   deactivate
   . venv/bin/activate
   ```
7. Виконати тести і переконатися, що вони фейляться.
   ```
   nosetests .
   ```
8. Зробити так, щоб тести не фейлились
9. ...
10. PROFIT


Свого роду, тести документують і задають специфікацію
коду, який ми маємо написати. Потрібно їх прочитати, зрозуміти
і закодувати те, що вони від нас очікують.

Тут треба створити файл instruments.py і визначити в ньому
3 класи: Instrument, Guitar, Ukulele.

При цьому нехай Guitar наслідується з Instrument, а Ukulele
з Guitar

"""

from .instruments import Instrument, Guitar, Ukulele

# Instrument – будь-який музичний інструмент
# Guitar – гітара
# Ukulele – укулеле (маленька Гавайська гітарка)


class TestInstrument:

    def test_should_be_creatable(self):
        instrument = Instrument(name='my favourite guitar')

    def test_should_be_playable(self):
        guitar = Instrument(name='my favourite guitar')
        assert guitar.play() == 'Playing on my favourite guitar'

        drum = Instrument(name='my favourite drum')
        assert drum.play() == 'Playing on my favourite drum'

    def test_should_be_stringifiable(self):
        instrument = Instrument(name='my favourite guitar')
        assert str(instrument) == 'Instrument: my favourite guitar'


class TestGuitar:

    def test_should_be_creatable(self):
        guitar = Guitar(name='my favourite guitar', strings=6)

    def test_should_be_playable(self):
        acoustic_guitar = Guitar(name='my acoustic guitar', strings=6)
        assert acoustic_guitar.play() == 'Playing on my acoustic guitar'

        electric_guitar = Guitar(name='my electric guitar', strings=6)
        assert electric_guitar.play() == 'Playing on my electric guitar'

    def test_should_not_be_able_to_play_with_no_strings(self):
        guitar = Guitar(name='my favourite guitar', strings=0)
        assert guitar.play() == 'Can not play, no strings :('

    def test_should_unfortunately_break_strings(self):
        # Щоразу, коли ми граємо на гітарі, імовірність порвати струну
        # має бути 1%.
        #
        # Підказка: можна використати функцію random.randint

        guitar = Guitar(name='my acoustic guitar', strings=6)

        # Зіграємо дуже багато пісень
        n = 100000

        for song in range(n):
            guitar.play()

        # З великою імовірністю хоча б одна струна порветься
        assert guitar.strings < 6

        # Але не може бути від’ємна кількість струн
        assert guitar.strings >= 0

    def test_should_be_stringifiable(self):
        guitar = Guitar(name='my favourite guitar', strings=12)
        assert str(guitar) == 'Instrument: my favourite guitar'


class TestUkulele:

    def test_should_be_creatable(self):
        uke = Ukulele(name='my favourite uke')

    def test_should_be_playable(self):
        uke = Ukulele(name='my soprano uke')
        assert uke.play() == 'Playing on my soprano uke'

        uke1 = Ukulele(name='my concert uke')
        assert uke1.play() == 'Playing on my concert uke'

    def test_should_have_4_strings(self):
        uke = Ukulele(name='my soprano uke')
        assert uke.strings == 4

    def test_should_be_stringifiable(self):
        uke = Ukulele(name='my favourite uke')
        assert str(uke) == 'Instrument: my favourite uke'
