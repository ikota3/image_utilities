import os
import fire


def ImageRenamer(object):
    def __init__(
            self,
            target_dir: str,
            digit: int = 4,
            extensions: (str) = None
    ):
        self.target_dir: str = target_dir
        self.digit: int = digit
        if not extensions:
            extensions = ('jpg', 'png')

    def _input_is_valid(self) -> bool:
        # TODO
        pass

    def rename(self):
        if not os.path.isdir(self.target_dir):
            print('[ERROR] You must type a valid directory for target directory.')
            return

        for current_dir, dirs, files in os.walk(self.target_dir):
            for filename in sorted(files):
                # TODO
                pass


if __name__ == '__main__':
    fire.Fire(ImageRenamer)
