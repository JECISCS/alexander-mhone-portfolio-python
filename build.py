from pathlib import Path


ROOT = Path(__file__).resolve().parent
CV_DIRECTORY = ROOT / "data" / "mycv"
PUBLIC_DIRECTORY = ROOT / "public"
PUBLIC_CV = PUBLIC_DIRECTORY / "cv.pdf"


def main() -> None:
    if not CV_DIRECTORY.is_dir():
        raise SystemExit(f"CV directory does not exist: {CV_DIRECTORY}")

    candidates = sorted(
        (path for path in CV_DIRECTORY.iterdir() if path.is_file() and path.suffix.lower() == ".pdf"),
        key=lambda path: path.name.casefold(),
    )
    if len(candidates) != 1:
        names = ", ".join(path.name for path in candidates) or "none"
        raise SystemExit(
            f"Expected exactly one PDF in {CV_DIRECTORY}; found {len(candidates)}: {names}. "
            "Replace the existing CV instead of keeping multiple versions."
        )

    cv_data = candidates[0].read_bytes()
    if not cv_data.startswith(b"%PDF-"):
        raise SystemExit(f"The CV file is not a valid PDF: {candidates[0].name}")

    PUBLIC_DIRECTORY.mkdir(parents=True, exist_ok=True)
    PUBLIC_CV.write_bytes(cv_data)
    print(f"Published {candidates[0].name} as public/{PUBLIC_CV.name}")


if __name__ == "__main__":
    main()
