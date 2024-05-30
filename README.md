# URL Extraction from Video

## Project Description

This project provides a Python class `ExtractUrls` that extracts URLs from video frames using Optical Character Recognition (OCR). The program reads a video file, processes each frame to extract text, and then uses regular expressions to find and collect URLs from the extracted text. This can be particularly useful for videos containing embedded URLs that you need to gather.

## Requirements

- Python 3.6 or higher
- OpenCV
- pytesseract
- Tesseract-OCR engine

## Installation

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/your-username/url-extraction-from-video.git
    cd url-extraction-from-video
    ```

2. **Install Required Libraries:**
    ```sh
    pip install opencv-python pytesseract
    ```

3. **Install Tesseract-OCR:**
    - **Ubuntu:**
        ```sh
        sudo apt update
        sudo apt install tesseract-ocr
        ```
    - **Windows:**
        Download and install the Tesseract installer from [this link](https://github.com/UB-Mannheim/tesseract/wiki).

    - **MacOS:**
        ```sh
        brew install tesseract
        ```

## Usage

1. **Prepare your Video File:**
    Ensure that the video file from which you want to extract URLs is available and note its path.

2. **Run the Script:**
    Execute the script and provide the path to the video file when prompted:
    ```sh
    python extract_urls.py
    ```

    You will be prompted to enter the video file path:
    ```sh
    Enter the video file path: /path/to/your/video.mp4
    ```

3. **Output:**
    The script will process the video, extract URLs, and print them. If no URLs are found, it will notify you.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Code Explanation

Here's a brief explanation of the main components of the code:

### ExtractUrls Class

- **Attributes:**
  - `video_path`: The path to the video file.
  - `extracted_urls`: A list to store the extracted URLs.
  - `sec`: Current time position in the video.
  - `frame_rate`: Frame rate to skip while extracting text from video frames.
  - `success_flag`: Flag to indicate successful extraction of text from a frame.
  - `raw_text`: The raw text extracted from the video frame.

- **Methods:**
  - `__init__(self, video_path)`: Initializes the `ExtractUrls` object with the given video path and starts the extraction process.
  - `start(self)`: Initiates the extraction process, iterating through frames and extracting text.
  - `extract_text_from_frame(self)`: Extracts text from the current video frame using OCR.
  - `get_extract_urls_from_raw_text(self)`: Uses regular expressions to find URLs in the extracted text.

### Example Usage

Here's an example of how to use the `ExtractUrls` class in your script:

```python
if __name__ == "__main__":
    video_path = input('Enter the video file path: ')
    obj = ExtractUrls(video_path=video_path)
