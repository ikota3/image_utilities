# image_utilities

Image utilities using CLI.

## Requirements

- `img2pdf`

```sh
pip install -r requirements.txt
```

## Usage

### Convert images to pdf

#### Parameters

- `-i`, `--input_dir`
  - **required parameter.**
  - input directory.
- `-o`, `--output_dir`
  - **required parameter.**
  - output directory.
- `-e`, `--extensions`
  - **optional parameter.**
  - **default paramter is `jpg` and `png`**
  - extension type for filtering.
- `-f`, `--force_write`
  - **optional parameter.**
  - **default paramter is `False`**
  - force to write pdf file.

#### Note

- This command will recursively watch the input directory, and convert the **images in each directory** to pdf.

- `-e`, `--extensions` can pass multiple extension. But you have to pass a list, with no space between comma.
- Also the extensions is **case sensitive**.
  - e.g. `-e "jpg,jpeg,png"`

#### Example

```sh
python src/images_to_pdf.py convert -i "path/to/input" -o "path/to/output" -f
```

### Rename images to sequential number

#### Parameters

- `-t`, `--target_dir`

  - **required parameter.**
  - target directory.

- `-d`, `--digit`

  - **optional parameter.**
  - digit for sequential number.

- `-e`, `--extensions`
  - extension type to rename.

#### Note

TODO

#### Example

TODO
