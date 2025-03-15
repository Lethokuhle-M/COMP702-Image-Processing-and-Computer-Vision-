import cv2
from PIL import Image
import numpy as np

def resize_to_fit_window(image):
    window_width = 800
    window_height = 600

    resized_image = cv2.resize(image, (window_width, window_height))
    return resized_image

def load_and_display_image(image_path, is_gif=False):
    if is_gif:
        image = Image.open(image_path)
        frames = image.n_frames
        
        while True:
            for frame_num in range(frames):
                image.seek(frame_num)
                frame = image.convert("RGB")  
                frame = np.array(frame) 
                
                frame_resized = resize_to_fit_window(frame)
                
                cv2.imshow('Loaded GIF Image', frame_resized)
                
                if cv2.waitKey(100) & 0xFF == ord('q'): 
                    cv2.destroyAllWindows()  
                    return
            
            if cv2.waitKey(100) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                return
                
    else:
        image = cv2.imread(image_path)
        if image is None:
            print("Error: Could not read the image.")
            return
        
        image_resized = resize_to_fit_window(image)
        
        cv2.imshow('Loaded Image', image_resized)
        
        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows() 

def main():
    print("Choose the type of image to open:")
    print("1. PNG")
    print("2. BMP")
    print("3. JPEG")
    print("4. GIF")
    num = int(input("Enter number: "))

    if num == 1:
        image_path = "Mario(png).png"
        is_gif = False
    elif num == 2:
        image_path = "Wolf(bmp).bmp"
        is_gif = False
    elif num == 3:
        image_path = "Space(jpeg).jpg"
        is_gif = False
    elif num == 4:
        image_path = "Wallpaper(gif).gif"
        is_gif = True

    load_and_display_image(image_path, is_gif)

if __name__ == "__main__":
    main()
