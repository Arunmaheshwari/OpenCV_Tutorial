import cv2

# img = cv2.imread("My_Image.jpg")
# # img = cv2.resize(img, (1280,700))    # width, height
# print(img)

# cv2.imshow("original", img)
# cv2.waitKey()
# cv2.destroyAllWindows()


# black and white image

# img1 = cv2.imread("My_Image.jpg", 0)    # parameter values = 1, -1, 0
# # img = cv2.resize(img, (1280,700))    # width, height
# print(img)

# cv2.imshow("Gray Scale image", img1)
# cv2.waitKey()
# cv2.destroyAllWindows()


# For saving the image


# img = cv2.imread("My_Image.jpg")
# # img = cv2.resize(img, (1280,700))    # width, height
# print(img)

# cv2.imshow("original", img)

# k = cv2.waitKey(0)
# if k == ord("s"):
#     cv2.imwrite(img)
# else:
#     cv2.destroyAllWindows()


# Flip function

img = cv2.imread("My_Image.jpg")
# img = cv2.resize(img, (1280,700))    # width, height
img = cv2.flip(img, -1)    # parameter values 1, 1, -0
print(img)

cv2.imshow("original", img)
cv2.waitKey()
cv2.destroyAllWindows()