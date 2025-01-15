import pdfplumber
import os

# 文件路径
pdf_path = r"20.pdf"
output_dir = r"Images"

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 打开 PDF 文件
with pdfplumber.open(pdf_path) as pdf:
    # 遍历每一页
    for page_number, page in enumerate(pdf.pages, start=1):
        
        # 获取页面上的所有图像
        images = page.images
        print(f"Page {page_number} has {len(images)} images.")

        # # 遍历每个图像
        for img_index, image in enumerate(images):
            # 提取图像的位置信息
            x0 = image["x0"]
            y0 = image["y0"]
            x1 = image["x1"]
            y1 = image["y1"]
            width = x1 - x0
            height = y1 - y0

            # 提取图像
            img = page.within_bbox((x0, y0, x1, y1)).to_image()
            # img_path = os.path.join(
            #     output_dir, f"page_{page_number}_img_{img_index}.png"
            # )
            # img.save(img_path)

        #     # 创建图像信息字典
        #     image_info = {
        #         "page": page_number,
        #         "index": img_index,
        #         "bbox": [x0, y0, x1, y1],
        #         "width": width,
        #         "height": height,
        #         "path": img_path,
        #     }

        #     # 保存图像信息到单独的 JSON 文件
        #     json_path = os.path.join(
        #         output_dir, f"page_{page_number}_img_{img_index}.json"
        #     )
        #     with open(json_path, "w") as json_file:
        #         json.dump(image_info, json_file, indent=4)

        #     print(f"Saved image and JSON for page {page_number}, image {img_index}")

print("All images and JSON files have been saved.")