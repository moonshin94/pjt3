from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from tensorflow.keras.utils import to_categorical
import pandas as pd

data = pd.read_csv("Paasta_Notice_Preprocess.csv")
print(data)
t = Tokenizer()
for text in data["Content"]:
    t.fit_on_texts([text])
    vocab_size = len(t.word_index) + 1

    print("단어 집합의 크기: %d" % vocab_size)

    print(t.word_index)

    sequences = list()
    for line in text.split("\n"):
        encoded = t.texts_to_sequences([line])[0]
        for i in range(1, len(encoded)):
            sequence = encoded[:i+1]
            sequences.append(sequence)

    print("학습에 사용할 샘플의 개수: %d" % len(sequences))

    print("sequence")

    max_len = max(len(l) for l in sequences)

    print('샘플의 최대 길이: {}'.format(max_len))

    sequences = pad_sequences(sequences, maxlen=max_len, padding="pre")

    print(sequences)

    sequences = np.array(sequences)

X = sequences[:, :-1]
y = sequences[:, -1]

print(X)
print(y)
y = to_categorical(y, num_classes=vocab_size)
print(y)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, SimpleRNN

model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=max_len-1))
model.add(SimpleRNN(32))
model.add(Dense(vocab_size, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=200, verbose=2)

def sentence_generation(model, t, current_word, n):
    init_word = current_word
    sentence = ''
    for _ in range(n):
        encoded = t.texts_to_sequences([current_word])[0]
        encoded = pad_sequences([encoded], maxlen=5, padding='pre')
        #result = model.predict_classes(encoded, verbose=0)
        result = np.argmax(model.predict(encoded), axis = -1)
        for word, index in t.word_index.items():
            if index == result:
                break
        current_word = current_word + ' ' + word
        sentence = sentence + ' ' + word
    sentence = init_word + sentence
    return sentence

print(sentence_generation(model, t, '장애', 5))