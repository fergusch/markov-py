# markov-py
A simple Python script to build a Markov chain based on input text and generate text from the model.

## Usage
```Python
from markov import *

# Input should be an array of strings.
text = [
	"Lorem ipsum dolor sit amet, consectetur adipiscing elit",
	"Aliquam condimentum metus diam",
	"Duis volutpat orci sit amet elit finibus, sit amet porta leo egestas",
	"Praesent quam neque, faucibus vel mi quis, cursus sagittis nibh",
	"Aenean ultricies tempus neque, ac elementum felis semper eu",
	"Aenean et sapien ut purus blandit ultrices quis in mi",
	"Phasellus finibus massa risus, feugiat fermentum augue vehicula dictum"
]

# Build a model based on the text
model = build_model(text)

# Generate output using the model
print(' '.join(write_sentences(3, model, punctuate=True)))
```
Output:
```
Aenean ultricies tempus neque, faucibus vel mi. Lorem ipsum dolor sit amet elit. Aenean et sapien ut purus blandit ultrices quis in mi quis, cursus sagittis nibh.
```

More training data will produce more diverse output.

For more information about Markov chains, [see here](https://en.wikipedia.org/wiki/Markov_chain).

## License
This project is licensed under the GNU GPLv3 license. Please see the LICENSE file for more details.