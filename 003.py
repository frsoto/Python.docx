from __future__ import annotations
import fnmatch
from pathlib import Path
import re
import zipfile

class ZipReplace:
    def __init__(
        self,
        archive: Path, # objeto de la clase Path
        pattern: str,
        find: str,
        replace: str
    ) -> None:
        self.archive_path = archive # objeto de la clase Path. tiene metodo rename
        self.pattern = pattern # filename pattern to match
        self.find = find
        self.replace = replace

    def find_and_replace(self) -> None:
        input_path, output_path = self.make_backup()
        with zipfile.ZipFile(output_path, "w") as output:
            with zipfile.ZipFile(input_path) as input:
                self.copy_and_transform(input, output)


    def make_backup(self) -> tuple[Path, Path]:
        """ The make_backup() method will use the pathlib module to rename the old ZIP
        file so it's obviously the backup copy, untouched.
        sample.zip pasa a ser sample.zip.old"""
        input_path = self.archive_path.with_suffix(f"{self.archive_path.suffix}.old") # sample.zip.old
        output_path = self.archive_path # sample.zip
        self.archive_path.rename(input_path) #
        return input_path, output_path #


sample_zip = Path("sample.zip") # creo objeto de la clase Path
zr = ZipReplace(sample_zip, "*.md", "xyzzy", "xxxxx")



#
#
# %%


# # %%

#
# # %%


# zr.make_backup()
#
# # %%
#     def copy_and_transform(
#             self, input: zipfile.ZipFile, output: zipfile.ZipFile
#     ) -> None:
#         for item in input.infolist():
#             extracted = Path(input.extract(item))
#
#     if (not item.is_dir()
#             and fnmatch.fnmatch(item.filename, self.pattern)):
#         print(f"Transform {item}")
#     input_text = extracted.read_text()
#     output_text = re.sub(self.find, self.replace, input_text)
#     extracted.write_text(output_text)
#     else:
#     print(f"Ignore {item}")
#     output.write(extracted, item.filename)
#     extracted.unlink()
#     for parent in extracted.parents:
#         if parent == Path.cwd():
#             break
#     parent.rmdir()
#
# # %%
#
# if __name__ == "__main__":
#     sample_zip = Path("sample.zip")
#     zr = ZipReplace(sample_zip, "*.md", "xyzzy", "plover's egg")
#     zr.find_and_replace()
#

