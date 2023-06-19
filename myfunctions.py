def get_img_to_Tensor(file_location, resized_resolution=None, rgb2gray=None):
    img = Image.open(file_location)

    tf_transforms = []

    if rgb2gray:
        tf_transforms.append(F.Grayscale())

    if resized_resolution is not None:
        tf_transforms.append(F.Resize(resized_resolution))

    tf_transforms.append(F.ToTensor())

    tf = F.Compose(tf_transforms)

    img_tensor = tf(img)
    #returns tensor of [Channel, Height, Width]
    return img_tensor