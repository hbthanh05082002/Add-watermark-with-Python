import cv2

img_path = 'original_picture.jpg'
watermark_path = 'watermark.png'

img = cv2.imread(img_path)
watermark = cv2.imread(watermark_path)

img_scale = 20

new_img_width = int(img.shape[1] * img_scale/100)
new_img_height = int(img.shape[0] * img_scale/100)
new_img_dimension = (new_img_width, new_img_height)
resized_img = cv2.resize(img, new_img_dimension, interpolation=cv2.INTER_AREA)

watermark_scale = 50

new_watermark_width = int(watermark.shape[1] * watermark_scale/100)
new_watermark_height = int(watermark.shape[0] * watermark_scale/100)
new_watermark_demension = (new_watermark_width, new_watermark_height)
resized_watermark = cv2.resize(watermark, new_watermark_demension, interpolation=cv2.INTER_AREA)

height_img, width_img, _ = resized_img.shape
center_x = int(width_img/2)
center_y = int(height_img/2)

height_watermark, width_watermark, _ = resized_watermark.shape
top_y = center_y - int(height_watermark/2)
left_x = center_x - int(width_watermark/2)
bottom_y = top_y + height_watermark
right_x = left_x + width_watermark

roi = resized_img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(roi, 1, resized_watermark, 0.3, 0)
# cv2.imshow("Watermark Added", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
resized_img[top_y:bottom_y, left_x:right_x] = result

output_path = ''
output_filename = 'Watermarked_img.jpg'
cv2.imwrite(output_path + output_filename, resized_img)
cv2.imshow("Output", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
