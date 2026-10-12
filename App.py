import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. TẠO DATAFRAME BẢN GỐC CỦA BẠN
du_lieu = {
    'Họ và tên': [
        'Nguyễn Văn A', 'Trần Thị B', 'Lê Hoàng C', 'Phạm Minh D', 'Vũ Thu E',
        'Hoàng Văn F', 'Đỗ Thị G', 'Phan Văn H', 'Bùi Thị I', 'Ngô Minh K'
    ],
    'Điểm chuyên cần': [9.0, 8.5, 10.0, 9.5, 7.0, 8.0, 9.0, 8.5, 9.0, 8.0],
    'Điểm giữa kỳ': [7.5, 8.0, 6.5, 9.0, 7.0, 5.5, 8.5, 6.0, 4.5, 9.5],
    'Điểm cuối kỳ': [8.0, 7.5, 9.0, 8.5, 6.0, 5.0, 8.0, 7.0, 5.5, 9.0]
}

df_sinh_vien = pd.DataFrame(du_lieu)
df_sinh_vien.index = df_sinh_vien.index + 1  # Chỉ số bắt đầu từ 1

# Tính tổng kết (giữ nguyên chữ 'Tổng_kết' có dấu của bạn)
df_sinh_vien['Tổng_kết'] = (0.2 * df_sinh_vien['Điểm chuyên cần']) + \
                           (0.3 * df_sinh_vien['Điểm giữa kỳ']) + \
                           (0.5 * df_sinh_vien['Điểm cuối kỳ'])

# Xếp loại sinh viên (giữ nguyên chữ 'Xếp_loại' có dấu của bạn)
df_sinh_vien['Xếp_loại'] = pd.cut(
    df_sinh_vien['Tổng_kết'], 
    bins=[0, 5.0, 7.0, 8.5, 10], 
    labels=['Yếu', 'Trung bình', 'Khá', 'Giỏi']
)

# 2. HIỂN THỊ LÊN GIAO DIỆN WEB APP BẰNG STREAMLIT
st.title("🏆 QUẢN LÝ ĐIỂM SINH VIÊN")

st.subheader("📊 Bảng điểm chi tiết của lớp")
st.dataframe(df_sinh_vien)

st.subheader("📈 Thống kê lớp học")
diem_tb = df_sinh_vien['Tổng_kết'].mean()
st.write(f"**Điểm tổng kết trung bình của lớp:** {diem_tb:.2f}")

# Lọc thủ khoa và á khoa theo đúng logic bạn đã tự viết
sv_cao_nhat = df_sinh_vien[df_sinh_vien['Tổng_kết'] == df_sinh_vien['Tổng_kết'].max()]
sv_thap_nhat = df_sinh_vien[df_sinh_vien['Tổng_kết'] == df_sinh_vien['Tổng_kết'].min()]
so_sv_dat = df_sinh_vien[df_sinh_vien['Tổng_kết'] >= 5].shape[0]

st.write("**Sinh viên có điểm tổng kết cao nhất:**")
st.dataframe(sv_cao_nhat)

st.write("**Sinh viên có điểm tổng kết thấp nhất:**")
st.dataframe(sv_thap_nhat)

st.write(f"**Số sinh viên đạt (Tổng kết ≥ 5):** {so_sv_dat} sinh viên")

# Hộp chọn tra cứu danh sách xổ xuống
st.subheader("🔍 Tra cứu thông tin từng sinh viên")
danh_sach_ten = df_sinh_vien['Họ và tên'].tolist()
ten_duoc_chon = st.selectbox("Chọn một sinh viên để xem điểm:", danh_sach_ten)
sv_duoc_chon = df_sinh_vien[df_sinh_vien['Họ và tên'] == ten_duoc_chon]
st.table(sv_duoc_chon[['Điểm chuyên cần', 'Điểm giữa kỳ', 'Điểm cuối kỳ', 'Tổng_kết', 'Xếp_loại']])

# Phần vẽ đồ thị cột đứng
st.subheader("📊 Biểu đồ cột điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 5))
cac_cot = ax.bar(df_sinh_vien['Họ và tên'], df_sinh_vien['Tổng_kết'], color='royalblue', width=0.6)
ax.bar_label(cac_cot, padding=3, fmt='%.2f')
ax.set_ylim(0, 11)
plt.xticks(rotation=45)
st.pyplot(fig)

# ĐIỀN THÔNG TIN CỦA BẠN VÀO ĐÂY NHÉ
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Người tạo ứng dụng: NGUYỄN ĐỨC ANH - MSSV: SỐ CỦA BẠN</p>", unsafe_allow_html=True)
