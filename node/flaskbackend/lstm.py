import torch
import torch.nn as nn
import pickle

# Load vocabulary
def load_vocab(file_path):
    with open(file_path, 'rb') as f:
        vocab = pickle.load(f)
    return vocab

vocab = load_vocab('vocab.pkl')

# LSTM Model
class LSTMClassifier(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, output_dim):
        super(LSTMClassifier, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, text):
        embedded = self.embedding(text)
        lstm_out, _ = self.lstm(embedded)
        out = self.fc(lstm_out[:, -1, :])
        return out

# Load the trained model
def load_model(path, vocab_size):
    model = LSTMClassifier(vocab_size=vocab_size, embed_dim=100, hidden_dim=128, output_dim=2)
    model.load_state_dict(torch.load(path))
    model.eval()
    return model

model = load_model('lstm_model.pth', len(vocab))

# Dummy tokenizer (same as used in training)
def tokenizer(text):
    return text.split()

# Preprocess and predict function
def predict(title, vocab):
    tokenized = tokenizer(title)
    indexed = torch.tensor([vocab[word] for word in tokenized], dtype=torch.long).unsqueeze(0)
    with torch.no_grad():
        output = model(indexed)
        _, predicted = torch.max(output, dim=1)
    return 'Real' if predicted.item() == 1 else 'Fake'


