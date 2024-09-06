import os
import requests

def main():
    image_folder = 'images'
    output_folder = 'output'

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all image files in the image folder
    image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)

        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': open(image_path, 'rb')},
            data={'size': 'auto'},
            headers={'X-Api-Key': 'INSERT_YOUR_API_KEY_HERE'},
        )
        if response.status_code == requests.codes.ok:
            output_path = os.path.join(output_folder, f'no-bg-{image_file}')
            with open(output_path, 'wb') as out:
                out.write(response.content)
        else:
            print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    main()