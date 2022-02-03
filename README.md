# wordle
python wordle. because why not?



## Usage
```python
import wordle

wordle = Wordle()  # or Wordle(word_list=["list", "of", "words"])
wordle.play()

"""
___
Letters used:  
Enter a new letter to guess: one
**e
Letters used:  neo
Enter a new letter to guess: ore
**e
Letters used:  nreo
Enter a new letter to guess: two
***
Letters used:  ntrewo
Enter a new letter to guess: one
**e
Letters used:  ewrnto
Enter a new letter to guess: ape
ape
You did it! The word was: ape
"""
```
