    img_maked = make_pixel(img, SIZE)
    cv2.imshow(f'{SIZE, img_maked.shape}', img_maked)
    cv2.waitKey(0)