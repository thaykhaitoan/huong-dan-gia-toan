import streamlit as st
import google.generativeai as genai
from PIL import Image

# Cấu hình API từ hệ thống bảo mật của Streamlit
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Trợ lý Toán học của Thầy", layout="wide")
st.title("🎓 Trợ lý Giải toán Đa phương thức")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📥 Nhập dữ liệu")
    uploaded_file = st.file_uploader("Tải ảnh đề bài:", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Ảnh đã tải lên", use_container_width=True)
    user_query = st.text_area("Yêu cầu thêm:", placeholder="Ví dụ: Giải chi tiết câu 1...")

with col2:
    st.subheader("💡 Lời giải từ AI")
    if st.button("Bắt đầu giải"):
        with st.spinner("Đang xử lý..."):
            try:
                # Chuẩn bị nội dung gửi đi
                content = ["Bạn là giáo viên Toán chuyên nghiệp. Hãy giải bài toán này chi tiết bằng định dạng LaTeX."]
                if uploaded_file:
                    content.append(image)
                if user_query:
                    content.append(user_query)
                
                response = model.generate_content(content)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Lỗi: {e}")