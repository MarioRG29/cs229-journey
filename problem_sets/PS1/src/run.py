from pathlib import Path
import argparse

from p01b_logreg_solution import main as p01b
from p01e_gda import main as p01e
from p02cde_posonly import main as p02
from p03d_poisson import main as p03
from p05b_lwr import main as p05b
from p05c_tau import main as p05c

# Rutas ancladas al propio script
BASE_DIR = Path(__file__).parent.resolve()
DATA_DIR = (BASE_DIR / ".." / "data").resolve()
OUT_DIR = (BASE_DIR / "output").resolve()
OUT_DIR.mkdir(parents=True, exist_ok=True)  # crea 'output/'


def p(path):  # helper para convertir Path a str
    return str(path)


parser = argparse.ArgumentParser()
parser.add_argument(
    "p_num",
    nargs="?",
    type=int,
    default=0,
    help="Problem number to run, 0 for all problems.",
)
args = parser.parse_args()

# Problem 1
if args.p_num in (0, 1):
    p01b(
        train_path=p(DATA_DIR / "ds1_train.csv"),
        eval_path=p(DATA_DIR / "ds1_valid.csv"),
        pred_path=p(OUT_DIR / "p01b_pred_1.txt"),
    )

    p01b(
        train_path=p(DATA_DIR / "ds2_train.csv"),
        eval_path=p(DATA_DIR / "ds2_valid.csv"),
        pred_path=p(OUT_DIR / "p01b_pred_2.txt"),
    )

    p01e(
        train_path=p(DATA_DIR / "ds1_train.csv"),
        eval_path=p(DATA_DIR / "ds1_valid.csv"),
        pred_path=p(OUT_DIR / "p01e_pred_1.txt"),
    )

    p01e(
        train_path=p(DATA_DIR / "ds2_train.csv"),
        eval_path=p(DATA_DIR / "ds2_valid.csv"),
        pred_path=p(OUT_DIR / "p01e_pred_2.txt"),
    )

# Problem 2
if args.p_num in (0, 2):
    p02(
        train_path=p(DATA_DIR / "ds3_train.csv"),
        valid_path=p(DATA_DIR / "ds3_valid.csv"),
        test_path=p(DATA_DIR / "ds3_test.csv"),
        pred_path=p(OUT_DIR / "p02X_pred.txt"),
    )

# Problem 3
if args.p_num in (0, 3):
    p03(
        lr=1e-7,
        train_path=p(DATA_DIR / "ds4_train.csv"),
        eval_path=p(DATA_DIR / "ds4_valid.csv"),
        pred_path=p(OUT_DIR / "p03d_pred.txt"),
    )

# Problem 5
if args.p_num in (0, 5):
    p05b(
        tau=5e-1,
        train_path=p(DATA_DIR / "ds5_train.csv"),
        eval_path=p(DATA_DIR / "ds5_valid.csv"),
    )

    p05c(
        tau_values=[3e-2, 5e-2, 1e-1, 5e-1, 1e0, 1e1],
        train_path=p(DATA_DIR / "ds5_train.csv"),
        valid_path=p(DATA_DIR / "ds5_valid.csv"),
        test_path=p(DATA_DIR / "ds5_test.csv"),
        pred_path=p(OUT_DIR / "p05c_pred.txt"),
    )
