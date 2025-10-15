Dự án: Thuật toán Tìm kiếm Nhị phân (Binary Search) – Mở rộng cho AlgoVault

🧠 Mô tả dự án
Dự án AlgoVault là một thư viện mã nguồn mở tổng hợp các thuật toán lập trình viết bằng nhiều ngôn ngữ khác nhau như Python, Java, C++, giúp sinh viên và lập trình viên dễ dàng học tập, chia sẻ và đóng góp.  

Trong phần đóng góp của tôi, tôi đã bổ sung một thuật toán Tìm kiếm Nhị phân (Binary Search) bằng ngôn ngữ Python, nhằm mở rộng kho thuật toán Python của dự án.  
Thuật toán này giúp tìm vị trí của một phần tử trong danh sách đã sắp xếp nhanh chóng và hiệu quả (độ phức tạp O(log n)).

⚙️ Công nghệ sử dụng
- Ngôn ngữ: Python 3  
- Công cụ: GitHub, Visual Studio Code  
- Môi trường: Mã nguồn mở (Open Source Repository)  
- Cấu trúc lưu trữ: `algorithms/python/binary_search.py`

💎 Phân tích nội dung đóng góp
📄 File: `binary_search.py`
Đây là trung tâm của phần đóng góp, chứa toàn bộ logic xử lý tìm kiếm nhị phân.  
Mã nguồn được viết rõ ràng, có chú thích và ví dụ minh họa để người học dễ hiểu và tái sử dụng.

Chức năng chính:
1. Tìm kiếm phần tử:  
   - Đầu vào: Danh sách `arr` (đã sắp xếp) và giá trị cần tìm `target`.  
   - Đầu ra: Trả về chỉ số (index) của phần tử nếu tìm thấy, hoặc `-1` nếu không tồn tại.  

2. Ví dụ minh họa:
   ```python
   arr = [1, 3, 5, 7, 9]
   print(binary_search(arr, 7))  # 👉 Kết quả: 3
