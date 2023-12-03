import emoji
import get_input


text = get_input.get_input("Input: ")
print("Output:", emoji.emojize(text, language="alias"))
