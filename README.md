## Text-to-Image Web App

Dự án này triển khai một ứng dụng web đơn giản cho phép người dùng nhập **prompt (văn bản)** và sinh ra **hình ảnh** bằng cách gọi API từ **Hugging Face**.  
Ứng dụng gồm 2 phần chính:

- **Backend**: Python (FastAPI/Flask) gọi API Hugging Face để xử lý prompt và trả về ảnh.
- **Frontend**: ReactJS để hiển thị giao diện web cho người dùng.
- **Triển khai**: Docker + Docker Compose để chạy toàn bộ hệ thống.

---

### Cấu trúc thư mục:
- **backend/** # Backend service
- **my-app/** # Frontend React app
- docker-compose.yml # Quản lý backend + frontend
- environment.yml # Cấu hình môi trường (API key Hugging Face, port, …)

### Cài đặt và chạy dự án:
- Clone dự án:  
  git clone https://github.com/thutranhsodo/text-to-image.git  
  cd project
- Đăng nhập vào HuggingFace và tạo một token với đầy đủ quyền truy cập Read và Write.
- Thêm vào file environment.yml:  
  API_KEY=your_huggingface_api_key
- Chạy với Docker Compose:  
  docker-compose up --build
- Backend sẽ chạy ở: http://localhost:8000  
  Frontend sẽ chạy ở: http://localhost:3000
