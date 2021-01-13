# image_utilities

Image utilities using CLI.

## TODO

Add color to logger.

## Requirements

- `fire`

- `img2pdf`

- `alive-progress`

```sh
pip install -r requirements.txt
```

## Usage

### Convert images to pdf

[src/convert_to_pdf.py](src/convert_to_pdf.py)

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
  - **default parameter is `jpg`.**
  - extension types for filtering.
  - type: str | tuple(str)

- `-f`, `--force_write`

  - **optional parameter.**
  - **default parameter is `False`.**
  - force to write pdf file.
  - type: bool

- `-y`, `--yes`

  - **optional parameter.**
  - **default parameter is `False`.**
  - execute without asking.
  - type: bool

#### Notes

- This command will recursively watch the input directory, and convert the **files in each directory** to pdf.

- `-e`, `--extensions` can pass multiple extension. But you have to pass a list, with no space between comma.

  - e.g. `-e "jpg,jpeg,png"`

- Extensions is **case sensitive**.

- The sorting method is human sorting.

  - e.g.

    ```python
    l = ["01.jpg", "02.jpg", "003.jpg"]
    # Not in the right order
    print(sorted(l)) # ["003.jpg", "01.jpg", "02.jpg"]

    # :)
    print(human_sort(l)) # ["01.jpg", "02.jpg", "003.jpg"]
    ```

#### Example

```bash
python src/convert_to_pdf.py convert -i "path/to/input" -o "path/to/output" -f
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
  - **default parameter is `jpg`.**
  - extension types to rename.
  - type: str | tuple(str)

- `-y`, `--yes`

  - **optional parameter.**
  - **default parameter is `False`.**
  - execute without asking.
  - type: bool

#### Notes

- This command will recursively watch the target directory, and rename the **files in each directory** to sequential number.

- `-e`, `--extensions` can pass multiple extension. But you have to pass a list, with no space between comma.

  - e.g. `-e "jpg,jpeg,png"`

- Extensions is **case sensitive**.

- The sorting method is human sorting.

#### Example

```bash
python src/rename_to_sequential.py rename -t "path/to/target"
```

---

### Swap first and second image

[src/swap_image.py](src/swap_image.py)

Swap first and second image in each directory.

#### Parameters

- `-t`, `--target_dir`

  - **required parameter.**
  - target directory.
  - type: str

- `-e`, `--extension`

  - **optional parameter.**
  - **default parameter is `jpg`.**
  - extension types to swap.
  - type: str

- `-y`, `--yes`

  - **optional parameter.**
  - **default parameter is `False`.**
  - execute without asking.
  - type: bool

#### Notes

- This command will recursively watch the target directory, and swap the first and second image **in each directory**.

- `-e`, `--extension` can only pass one extension.

- Extension is **case sensitive**.

- The sorting method is human sorting.

#### Example

```bash
python src/swap_image.py swap -t "path/to/target"
```
