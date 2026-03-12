import streamlit as st
import random
import time

st.set_page_config(
    page_title="AzaPlay",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 AzaPlay — Mini Apps & Games")
st.write("Бул жерде пайдалуу программалар жана кичине оюндар бар")

with st.sidebar:
    menu = st.radio(
        "Menu",
        [
            'Anketa',
            'Polindrom',
            'Calculator',
            'Tak san jana jup san',
            'Anagramma',
            'Koboituu tablisa',
            'Timer',
            'Sozdu ozgortuu',
            'Sozdun tamgalary',
            'Mini-Igry'
        ]
    )

# ---------------- ANKETA ----------------

if menu == 'Anketa':

    st.image("https://cdn-icons-png.flaticon.com/512/747/747376.png", width=120)

    st.title('Anketa')

    st.text_input('Atyndy jaz')

    age = st.number_input('Jashyndy jaz', value=0, min_value=0, max_value=100)

    st.number_input('Salmagyndy jaz', value=0.00, min_value=0.00, max_value=300.00)

    if st.button('Registrasiya'):

        if age > 18:

            st.success('Iigiluktuu')

        else:

            st.error('Доступ жок')

# ---------------- POLINDROM ----------------

elif menu == 'Polindrom':

    st.image("https://cdn-icons-png.flaticon.com/512/2991/2991148.png", width=120)

    st.title('Polindrom tabuu')

    name = st.text_input('Soz jaz: ').lower()

    if st.button('Teksheruu'):

        if name == name[::-1]:

            st.success('Polindrom')

        else:

            st.error('Polindrom emes')

# ---------------- CALCULATOR ----------------

elif menu == 'Calculator':

    st.image("https://cdn-icons-png.flaticon.com/512/2920/2920277.png", width=120)

    st.title('Calculator')

    number1 = st.number_input('1-san jaz: ')

    amal = st.selectbox('Aмалды танда', ['+', '-', '*', '/'])

    number2 = st.number_input('2-San jaz: ')

    if st.button('Chygaruu'):

        if amal == '+':

            st.success(number1 + number2)

        elif amal == '-':

            st.success(number1 - number2)

        elif amal == '*':

            st.success(number1 * number2)

        elif amal == '/':

            if number2 == 0:

                st.error("0го бөлүүгө болбойт")

            else:

                st.success(number1 / number2)

# ---------------- TAK JUP ----------------

elif menu == 'Tak san jana jup san':

    st.image("https://cdn-icons-png.flaticon.com/512/992/992651.png", width=120)

    st.title('Tak san jana jup san')

    number = st.number_input('San jaz', value=0, step=1)

    if st.button('Teksheruu'):

        if number % 2 == 0:

            st.success(f'{number} - Jup san')

        else:

            st.success(f'{number} - Tak san')

# ---------------- ANAGRAMMA ----------------

elif menu == 'Anagramma':

    st.image("https://cdn-icons-png.flaticon.com/512/1970/1970062.png", width=120)

    st.title('Anagramma')

    word1 = st.text_input('1-soz jaz: ').lower()

    word2 = st.text_input('2-soz jaz: ').lower()

    if st.button('Teksheruu'):

        if sorted(word1) == sorted(word2):

            st.success('Anagramma')

        else:

            st.error('Anagramma emes')

# ---------------- TABLE ----------------

elif menu == 'Koboituu tablisa':

    st.image("https://cdn-icons-png.flaticon.com/512/3038/3038015.png", width=120)

    st.title('Koboituu tablisa')

    number = st.number_input('San jaz', min_value=1, max_value=10, step=1)

    if st.button('Chygaruu'):

        for i in range(1, 11):

            st.info(f'{number} x {i} = {number*i}')

# ---------------- TIMER ----------------

elif menu == 'Timer':

    st.image("https://cdn-icons-png.flaticon.com/512/2088/2088617.png", width=120)

    st.title('Timer')

    seconds = st.number_input('Ubakytty jaz', min_value=1, max_value=3600, step=1)

    if st.button('Timerdi bashto'):

        timer_display = st.empty()

        for i in range(seconds, -1, -1):

            timer_display.markdown(f'### {i}')

            time.sleep(1)

        timer_display.markdown('💥 Таймер бутту')

# ---------------- WORD CHANGE ----------------
elif menu == 'Sozdu ozgortuu':

    st.image("https://cdn-icons-png.flaticon.com/512/1828/1828919.png", width=120)

    st.title('Sozdu ozgortuu')

    word = st.text_input('Soz jaz:')

    if st.button('Chygaruu'):

        if word:

            st.write(word.upper())

            st.write(word.lower())

            st.write(f"Tamgalar sany: {len(word)}")

        else:

            st.error("Soz jazynyz")

# ---------------- LETTER COUNT ----------------

elif menu == 'Sozdun tamgalary':

    st.image("https://cdn-icons-png.flaticon.com/512/3595/3595455.png", width=120)

    st.title('Sozdun tamgalary')

    word = st.text_input('Soz jaz:').lower()

    if st.button('Teksheruu'):

        vowels = "aeiouy"

        consonants = "bcdfghjklmnpqrstvwxz"

        word_vowels = sum(1 for letter in word if letter in vowels)

        word_consonants = sum(1 for letter in word if letter in consonants)

        st.write(f"Үндүү тамгалар: {word_vowels}")

        st.write(f"Үнсүз тамгалар: {word_consonants}")

        st.write(f"Бардык тамгалар: {len(word)}")

# ---------------- MINI GAMES ----------------

elif menu == 'Mini-Igry':

    st.image("https://cdn-icons-png.flaticon.com/512/686/686589.png", width=120)

    st.title("Mini-Igry")

    game_choice = st.selectbox("Оюнду танда", ["Угадай число"])

    if game_choice == "Угадай число":

        secret = random.randint(1, 10)

        guess = st.number_input("1ден 10го чейин сан тап", min_value=1, max_value=10)

        if st.button("Текшерүү"):

            if guess == secret:

                st.success("🎉 Туура таптың!")

            else:

                st.error(f"Туура эмес. Сан {secret} болчу")
