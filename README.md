# llm_utils

A package of utility functions needed across llm projects. There are 4 modules in this package:

1. **general** - containing general utility functions
   * **shrink(```text```)** - shrinks a string by removing whitespace and repeated '.' characters
   * **print_wrapped(```text```, ```width=80```)** - takes a large block of text and wraps it to the specified width
   * **get_path_to_model(```model_name```)** - returns the path to a model in the saved_models directory
   * **find_models_dir(dir=os.path.abspath('.'))** - starting from the directory specified, recursively searches up the directory tree for the **saved_models** directory and returns its absolute path
2. **extractors** - functions for extracting data from files
   * **pdfminer_extract_text(```pdf_path```)** - extracts text from pdf using pdfminer
3. **chunkers** - functions for chunking data
   * **split_using_create_documents(```text```)** - splits ```text``` into smaller Documents using the create_documents function
   * **split_using_split_text(text)** - splits ```text``` into smaller chunks using the split_text function
4. **summarizers** - functions for summarizing data. Currently uses a local version of ```facebook/bart-large-cnn``` as the model and tokenizer.
   * **summarize_text(```text```)** - takes a block of text and returns a summary of it.
   * **summarize_pdf(```pdf_file```)** - takes a pdf file and returns a summary of it.
   * **summarize_chunks(```chunks```, ```model_path```, ```tokenizer_path```)** - takes a list of chunks and returns a summary.
   * **summarize_pdf_doc(```pdf_file```)** - takes a pdf and returns a summary.

## Installation

```shell
% pip install git+https://github.com/jerichoBob/bob-pyutils.git
```

which installs the package ```llm_utils```.

## Usage

```python
import llm_utils.general as ut

print(ut.shrink("123....................................455"))
```
which produces:

```
123.455
```

## License

Apache 2.0 License

Copyright (c) 2023 jerichoBob-llc

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction

