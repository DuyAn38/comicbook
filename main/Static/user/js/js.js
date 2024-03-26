document.getElementById("userInfoForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Ngăn chặn việc gửi form mặc định
  
    // Lấy giá trị từ các trường input
    var fullName = document.getElementById("fullName").value;
    var email = document.getElementById("email").value;
    var phone = document.getElementById("phone").value;
  
    // In thông tin người dùng ra console (có thể thay thế bằng các hành động khác như gửi dữ liệu đến máy chủ)
    console.log("Họ và tên: " + fullName);
    console.log("Email: " + email);
    console.log("Số điện thoại: " + phone);
  
    // Reset form sau khi gửi thành công
    document.getElementById("userInfoForm").reset();
  });
  