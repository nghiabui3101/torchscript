import torch
import torchvision

model = torch.load('my_model.pth')
# Tải một mô hình nơ ron đã huấn luyện từ một tệp lưu trữ
# mô hình được lưu trong tệp có tên my_model.pth(tên tập nào thì lưu tệp đó)

model.eval()
#Đặt mô hình ở chế độ đánh giá để ngừng sử dụng các lớp như dropout

example = torch.rand(1, 3, 224, 224)
# một tensor ngẫu nhiên có kích thước tương thích với mô hình, có thể chỉnh lại nếu lệch kĩhs thước của tensor

traced_script_module = torch.jit.trace(model, example)
#Sử dụng hàm torch.jit.trace để chuyển đổi mô hình sang một đối tượng torchscript, đồng thời cung cấp một đầu vào mẫu cho mô hình

traced_script_module.save("traced_model.pt")
# Lưu đối tượng torchscript một tệp có tên: traced_model.pt