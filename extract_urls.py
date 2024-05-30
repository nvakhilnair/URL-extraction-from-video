import cv2
import re
import pytesseract


class ExtractUrls:
    """
    A class to extract URLs from a video using OCR.

    Attributes:
        video_path (str): The path to the video file.
        extracted_urls (list): A list to store the extracted URLs.
        sec (float): Current time position in the video.
        frame_rate (float): Frame rate to skip while extracting text from video frames.
        success_flag (bool): Flag to indicate successful extraction of text from a frame.
        raw_text (str): The raw text extracted from the video frame.
    """

    def __init__(self, video_path) -> None:
        """
        Initializes the ExtractUrls object.

        Args:
            video_path (str): The path to the video file.
        """
        self.video_path = video_path
        self.extracted_urls = []
        self.sec = 0
        self.frame_rate = 5
        self.success_flag = False
        self.start()

    def start(self):
        """
        Initiates the process of extracting URLs from the video frames.
        """
        self.extract_text_from_frame()
        while self.success_flag:
            self.sec += self.frame_rate
            self.sec = round(self.sec, 2)
            self.extract_text_from_frame()
        self.extracted_urls = set(self.extracted_urls)
        if self.extracted_urls:
            print(self.extracted_urls)
        else:
            print("Unable to extract URLs from the text")

    def extract_text_from_frame(self):
        """
        Extracts text from the video frame using OCR.
        """
        vidcap = cv2.VideoCapture(self.video_path)
        vidcap.set(cv2.CAP_PROP_POS_MSEC, self.sec * 1000)
        has_frames, image = vidcap.read()
        if has_frames:
            self.success_flag = True
            self.raw_text = pytesseract.image_to_string(image)
            if self.raw_text:
                self.get_extract_urls_from_raw_text()
            else:
                print("Unable to extract text from the video")
        else:
            self.success_flag = False

    def get_extract_urls_from_raw_text(self):
        """
        Extracts URLs from the raw text using regular expressions.
        """
        lines = self.raw_text.splitlines()  # Split text into lines
        # Iterate through each line
        for line in lines:
            line = line.strip()  # Remove leading and trailing spaces
            if line:  # Check if line is not empty after stripping spaces
                # Search for URLs in the line
                url_matches = re.findall(
                    r"(?P<url>https?://[^\s]+)|(www?\.[^\s]+)", line
                )
                # Extract URLs from the matches
                for match in url_matches:
                    self.extracted_urls.append(match[0] if match[0] else match[1])


if __name__ == "__main__":
    video_path = input('Enter the video file path: ')
    obj = ExtractUrls(video_path=video_path)
