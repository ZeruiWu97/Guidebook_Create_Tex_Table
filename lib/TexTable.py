import pandas as pd
from pathlib import Path
import traceback

BASE_OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

def df_to_tex_table(
    df: pd.DataFrame,
    caption: str = "Table",
    filename: str = "table.tex",
    subfolder: str = None,
    use_booktabs: bool = False,
) -> str:
    """
    Save a pandas DataFrame as a Tex table.

    Parameters
    ----------
    df: pd.DataFrame
        Data frame.
    caption: str, optional
        Caption for the TeX table.
    filename: str, optional
        Name of the .tex file to save.
    subfolder: str, optional
        Subfolder inside output/.
    use_booktabs: bool, optional
        If False, replace rules with \\hline for classic table style.
    Returns
    -------
    str
        Path to the saved .tex file.
    """
    output_dir = BASE_OUTPUT_DIR if subfolder is None else BASE_OUTPUT_DIR / subfolder
    output_dir.mkdir(parents=True, exist_ok=True)

    tex_path = output_dir / filename
    log_path = tex_path.with_suffix(".log")

    try:
        tabular = df.to_latex(
            index=False,
            escape=False,
            longtable=False,
            multicolumn=True,
            multicolumn_format="c",
            column_format="l" + "c" * (df.shape[1] - 1),
        )

        if not use_booktabs:
            tabular = (
                tabular.replace("\\toprule", "\\hline\\hline")
                       .replace("\\midrule", "\\hline")
                       .replace("\\bottomrule", "\\hline\\hline")
            )

        table = (
            "\\begin{table}[htbp]\n"
            "\\centering\n"
            f"\\caption{{{caption}}}\n"
            "\\vspace{0.5em}\n"
            f"{tabular}\n"
            "\\end{table}\n"
        )

        with open(tex_path, "w") as f:
            f.write(table)

        with open(log_path, "w") as f:
            f.write("Table saved successfully\n")
            f.write(f"File: {tex_path}\n")
            f.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")
            f.write(f"Columns: {', '.join(df.columns)}\n")
            f.write(f"Caption: {caption}\n")

    except Exception as e:
        with open(log_path, "w") as f:
            f.write("Table generation failed\n")
            f.write(str(e) + "\n")
            f.write(traceback.format_exc())
        return None

    return str(tex_path)


