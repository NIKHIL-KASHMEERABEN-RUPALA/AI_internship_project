import os

# Run Rasa server
os.system("rasa run --enable-api --cors '*' --debug")
