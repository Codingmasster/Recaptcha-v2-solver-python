def run_tesseract(image_path, lang="eng", psm=7, oem=3):
    # Define the command with the given parameters
    command = [
        "tesseract",
        image_path,
        "stdout",  # Print the result to the terminal
        "--psm",
        str(psm),
        "--oem",
        str(oem),
        "-l",
        lang,
    ]

    # Execute the command and capture the output
    try:
        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        if result.returncode == 0:
            print("OCR Output:\n")
            print(result.stdout)
            return result.stdout  # Print the OCR result
        else:
            print(f"Error: {result.stderr}")
    except FileNotFoundError:
        print("Tesseract is not installed or not found in PATH.")


# Example usage



