# Design Decisions

I renamed the functions and variables to make their purposes easier to understand, changing "do_math_stuff" to "scale_numbers" and "do_string_stuff" to "format_words", while using names such as numbers and words to describe the input data, helping another developer understand the program without having to interpret generic names.

I replaced the number loop with a list comprehension because the calculation only requires one simple condition, and used join with a generator expression to format and combine the words with spaces, making the code more concise and avoiding the need to remove a trailing space, although a regular loop could be easier to follow if the processing became more complicated.

I added docstrings to explain each function's purpose, parameters, and return value where applicable, along with short comments where extra explanation was helpful, making the program easier to understand and maintain, and ran both versions to confirm that the changes preserved the expected output for the provided sample data.
