# image_utilities

Image utilities using CLI.

## Requirements

- `img2pdf`

```sh
pip install -r requirements.txt
```

## Usage

### Convert images to pdf

[src/images_to_pdf.py](src/images_to_pdf.py)

Convert images in each directory to pdf.

#### Parameters

- `-i`, `--input_dir`

  - **required parameter.**
  - input directory.
  - type: str

- `-o`, `--output_dir`

  - **required parameter.**
  - output directory.
  - type: str

- `-e`, `--extensions`

  - **optional parameter.**
  - **default parameter is `jpg` and `png`.**
  - extension types for filtering.
  - type: str | tuple(str)

- `-f`, `--force_write`

  - **optional parameter.**
  - **default parameter is `False`.**
  - force to write pdf file.
  - type: boolean

#### Note

- This command will recursively watch the input directory, and convert the **files in each directory** to pdf.

- `-e`, `--extensions` can pass multiple extension. But you have to pass a list, with no space between comma.
- Also the extensions is **case sensitive**.
  - e.g. `-e "jpg,jpeg,png"`

#### Example

```bash
python src/images_to_pdf.py convert -i "path/to/input" -o "path/to/output" -f
```

---

### Rename images to sequential number

[src/rename_to_sequential.py](src/rename_to_sequential.py)

Rename images in each directory to sequential number.

#### Parameters

- `-t`, `--target_dir`

  - **required parameter.**
  - target directory.
  - type: str

- `-d`, `--digit`

  - **optional parameter.**
  - **default parameter is 4.**
  - digit for sequential number.
  - type: int

- `-e`, `--extensions`

  - **optional parameter.**
  - **default parameter is `jpg` and `png`.**
  - extension types to rename.
  - type: str | tuple(str)

#### Note

- This command will recursively watch the target directory, and rename the **files in each directory** to sequential number.

- `-e`, `--extensions` can pass multiple extension. But you have to pass a list, with no space between comma.
- Also the extensions is **case sensitive**.
  - e.g. `-e "jpg,jpeg,png"`

#### Example

```bash
python src/rename_to_sequential.py rename -t "path/to/target"
```
