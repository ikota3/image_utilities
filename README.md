# images_to_pdf

Convert images to pdf with CLI.

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
  - **default paramter is `jpg`**
  - image extension type.
- `-f`, `--force_write`
  - **optional parameter.**
  - **default paramter is `False`**
  - force to write pdf file.

#### Note

- This command will recursively watch the input directory, and convert the **images in each directory** to pdf.

- `-e`, `--extensions` can pass multiple extension. But you have to pass a list, with no space between comma.

  - e.g. `-e jpg,png`

#### Example

```sh
python src/images_to_pdf.py convert -i "path/to/input" -o "path/to/output" -e jpg,png -f
```
