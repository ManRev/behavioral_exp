def fill_CRN_html(path, out_path, url_images, title, source, CRN_type):
    # Read in the file
    with open(path, 'r') as file :
        filedata_null = file.read()
    # Replace the target string
    filedata = filedata_null
    filedata = filedata.replace('URL_image_auto1', url_images[0])
    filedata = filedata.replace('URL_image_auto2', url_images[1])
    filedata = filedata.replace('URL_image_auto3', url_images[2])
    filedata = filedata.replace('URL_image_auto4', url_images[3])
    filedata = filedata.replace('Title_auto1', title[0])
    filedata = filedata.replace('Title_auto2', title[1])
    filedata = filedata.replace('Title_auto3', title[2])
    filedata = filedata.replace('Title_auto4', title[3])
    filedata = filedata.replace('Source_auto1', source[0])
    filedata = filedata.replace('Source_auto2', source[1])
    filedata = filedata.replace('Source_auto3', source[2])
    filedata = filedata.replace('Source_auto4', source[3])
    filedata = filedata.replace('CRN_type_auto', CRN_type)
    # Write the file out again
    with open(out_path, 'w') as file:
        file.write(filedata)
