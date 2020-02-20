"""
    FROID main module.
"""
import random, sqlite3, string, sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


CLEVERBOT_URL = 'https://www.cleverbot.com'
NAME = 'Froid'
DB = 'froid.sqlite3'
GREETINGS = (
    f'Hello, my name is { NAME }.',
    'How do you do?',
    'What is your name?'
)
SCHEMA = 'froid.sql'
LEGALLETTERS = string.ascii_letters + "ąćęłńóśżź"
LEGALCHARS = LEGALLETTERS + "!?'., "
SENSECHARS = ('.', '?', '!')
WORD_MAX_LEN = 16
WORD_MIN_LEN = 2


def connect_db():
    """
        Connect to database.
    """
    with sqlite3.connect(DB) as con:
        return con


def create_tables(schema_url):
    """
        Open schema file and create tables.
    """
    with open(schema_url) as file:
        con = connect_db()
        cur = con.cursor()
        try:
            cur.executescript(file.read())
        except sqlite3.OperationalError: # Tables already exist.
            pass


def associate_sentence_word(sent_id, word_id):
    """
        Create sentence-word association.
    """
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute('INSERT INTO sent_word VALUES (?,?)', (sent_id, word_id))
        con.commit()
    except sqlite3.IntegrityError: # sentence-word pair is not unique.
        pass


def get_word_sentences(word_id):
    """
        Return all sentences associated with given word id.
    """
    sentences = set()
    con = connect_db()
    cur = con.cursor()
    cur.execute('SELECT sent_id FROM sent_word WHERE word_id=?', (word_id, ))
    for sentence_id in cur.fetchall():
        cur.execute('SELECT text FROM sent WHERE id=?', (sentence_id[0], ))
        sentences.add(cur.fetchone()[0])
    return sentences


def handle_stimulus(stimulus):
    """
        Handle incoming stimulus.
    """
    sentences = []

    sentence = stimulus if stimulus else '?'
    sentence = strip_doubles(stimulus)
    sentence = sentence.replace('  ', ' ')
    sentence = sentence.split(' ') if ' ' in sentence else [sentence]

    for word in sentence:
        word = strip_nonletters(word[:WORD_MAX_LEN].lower())
        if len(sentence) >= 2 and (WORD_MIN_LEN <= len(word) <= WORD_MAX_LEN):
            sentence_id = save_sentence(' '.join(sentence))
            word_id = save_word(word)
            associate_sentence_word(sentence_id, word_id)
            sentences.extend(get_word_sentences(word_id))

    sentence = ' '.join(sentence)
    sentences.append(get_random_sentence())
    sentences = list(set(sentences))

    for item in sentences:
        if item.lower() == sentence.lower():
            sentences.remove(item)

    return random.choice(sentences) if sentences else random.choice(GREETINGS)


def save_sentence(sentence):
    """
        Save sentence and return row id.
    """
    con = connect_db()
    cur = con.cursor()
    row_id = None
    try:
        cur.execute('INSERT INTO sent VALUES (NULL,?)', (sentence, ))
        con.commit()
        row_id = cur.lastrowid
    except sqlite3.IntegrityError:
        cur.execute('SELECT id FROM sent WHERE text=?', (sentence, ))
        row_id = cur.fetchone()[0]
    return row_id


def save_word(word):
    """
        Save word and return row id.
    """
    con = connect_db()
    cur = con.cursor()
    row_id = None
    try:
        cur.execute('INSERT INTO word VALUES (NULL, ?)', (word, ))
        con.commit()
        row_id = cur.lastrowid
    except sqlite3.IntegrityError:
        cur.execute('SELECT id FROM word WHERE text=?', (word, ))
        row_id = cur.fetchone()[0]
    return row_id


def get_random_greeting():
    """
        Return random greeting message.
    """
    return random.choice(GREETINGS)


def get_random_sentence():
    """
        Get all sentences from database and return random sentence.
        If no sentences exist yet, return random greeting.
    """
    sentences = []
    con = connect_db()
    cur = con.cursor()

    cur.execute('SELECT text FROM sent')
    sentences = [sentence[0] for sentence in cur.fetchall()]

    return random.choice(sentences) if sentences else random.choice(GREETINGS)


def strip_doubles(_str):
    """
        Strip recurring non-letter characters.
    """
    _str = _str if _str else '?'
    new = ''

    for i, char in enumerate(_str):
        if _str[i-1] not in LEGALLETTERS \
        and char not in LEGALLETTERS \
        and char not in ' ':
            continue
        new += char

    return new


def strip_nonletters(_str):
    """
        Strip all non letter characters.
    """
    new = ''

    for char in _str:
        new += char if char in LEGALLETTERS else ''

    return new


def run_selenium():
    """
        Connect to Cleverbot with Selenium browser.
    """
    try:
        driver = webdriver.Firefox()

        driver.get(CLEVERBOT_URL)
        stimulus_input = driver.find_element_by_class_name('stimulus')
        stimulus_input.send_keys(get_random_greeting())
        stimulus_input.send_keys(Keys.ENTER)

        for i in range(100):
            time.sleep(random.randrange(10, 15))
            response = driver.find_element_by_id('line1')
            response = response.find_element_by_class_name('bot').text
            print('\nCLEVER>', response)
            response = handle_stimulus(response)
            stimulus_input.send_keys(response)
            stimulus_input.send_keys(Keys.ENTER)
            print('FROID>', response)
    finally:
        driver.quit()


def run_froid():
    """
        Run console conversation.
    """
    for i in range(100):
        stimulus = str(input('ME> '))
        response = handle_stimulus(stimulus)
        print(f'FROID> { response }\n')


if __name__ == '__main__':

    ARGS = {
        'runfroid': run_froid,
        'runselenium': run_selenium
    }

    create_tables(SCHEMA)

    ARGS[sys.argv[1]]()
