import os, shutil

dict_extensions = { 
    'document_extensions' : ('.pdf', '.docx', '.wordx', '.txt'),
    'app_extensions' : ('.exe', '.apk'),
    'image_extensions' : ('.jpeg', '.png', '.jpg', '.raw'),
    'media_extensions' : ('.mp4','.mp3','.mkv',)
}

folderpath = input('enter folder path: ')


def file_finder(folder_path, file_extensions):
    # files = []
    # for file in os.listdir(folder_path):
    #     for extension in file_extensions:
    #         if file.endswith(extension):
    #             files.append(file)
    # return files    

    return[file for file in os.listdir(folder_path) for extension in file_extensions if file.endswith(extension)]

# print(file_finder(folderpath, document_extensions))

for ext_type, ext_tuple in dict_extensions.items():
    folder_name = ext_type.split('_')[0] + ' files'
    folder_path = os.path.join(folderpath, folder_name)
    os.mkdir(folder_path)
    for item in file_finder(folderpath, ext_tuple):
        item_path = os.path.join(folderpath, item)
        item_new_path = os.path.join(folder_path, item)
        shutil.move(item_path,item_new_path)


    # print('calling file finder...')
    # print(file_finder(folderpath,ext_tuple))



