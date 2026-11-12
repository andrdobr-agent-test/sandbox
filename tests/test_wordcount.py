import io

from wordcount import Counts, count, main


def test_count_empty() -> None:
    assert count("") == Counts(lines=0, words=0)


def test_count_text() -> None:
    assert count("one two\nthree\n") == Counts(lines=2, words=3)


def test_main_reads_file(tmp_path, capsys) -> None:
    path = tmp_path / "f.txt"
    path.write_text("a b c\nd\n", encoding="utf-8")
    assert main([str(path)]) == 0
    assert capsys.readouterr().out == "2 lines, 4 words\n"


def test_main_reads_stdin(capsys) -> None:
    assert main([], stdin=io.StringIO("x y")) == 0
    assert capsys.readouterr().out == "1 lines, 2 words\n"
