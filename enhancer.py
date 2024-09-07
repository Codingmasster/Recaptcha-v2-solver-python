# import OpenCV library
def solve_tesseract():

    # Step 1: Load the image using OpenCV
    image_path = "captcha.jpg"
    image = cv2.imread(image_path)

    # Step 2: Resize the image to enhance OCR accuracy
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Step 3: Create a mask to identify all non-black pixels
    lower_black = np.array([0, 0, 0], dtype=np.uint8)
    upper_black = np.array([50, 50, 50], dtype=np.uint8)

    # Create a mask for black pixels
    black_mask = cv2.inRange(image, lower_black, upper_black)

    # Step 4: Invert the mask to get non-black pixels and set them to white
    non_black_mask = cv2.bitwise_not(black_mask)
    image[non_black_mask > 0] = [255, 255, 255]

    # Step 5: Invert the colors so that the background is black and the text is white
    # inverted_image = cv2.bitwise_not(image)

    # Step 6: Convert the OpenCV image (numpy.ndarray) to a Pillow image for further processing
    pillow_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Step 7: Enhance contrast
    enhancer = ImageEnhance.Contrast(pillow_image)
    pillow_image = enhancer.enhance(2)

    # Step 8: Apply a slight Gaussian blur to reduce noise
    pillow_image = pillow_image.filter(ImageFilter.GaussianBlur(radius=2.15))

    # Step 10: Apply adaptive thresholding to create a clearer binary image
    deskewed_image_cv = cv2.cvtColor(np.array(pillow_image), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(deskewed_image_cv, cv2.COLOR_BGR2GRAY)
    thresholded_image = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2
    )

    # Step 11: Save the processed image
    processed_image_path = "processed_captcha.jpg"
    cv2.imwrite(processed_image_path, thresholded_image)

    # Step 12: Perform OCR with Tesseract
    image_path = "processed_captcha.jpg"
    digits = run_tesseract(image_path)
    print(f"ress {digits}")
    return digits

