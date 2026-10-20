import streamlit as st

# 页面基础配置
st.set_page_config(
    page_title="VIP免费追剧神器",
    page_icon="🎬",
    layout="centered"
)

# ========== 接口完全照搬你原代码 ==========
# 主解析接口（你桌面版一直在用的、亲测可用的那个）
MAIN_API = "https://jiexi.789jiexi.net:4433/?url="
# 备用接口（你原代码里注释的两个，已修正拼写错误）
BACKUP_API_1 = "https://jx.xmflv.cc/?url="
BACKUP_API_2 = "https://jix.77flv.cc/?url="

# ========== 页面界面 ==========
st.title("🎬 VIP免费追剧神器")
st.caption("支持爱奇艺、腾讯视频、优酷等主流平台VIP视频解析播放")

# 视频链接输入框
video_url = st.text_input(
    label="输入视频网址",
    placeholder="粘贴视频播放页链接，例如：https://www.iqiyi.com/v_xxxxxx.html"
)

# 第一行按钮：清空 + 三个平台跳转
col_clear, col_iqy, col_tx, col_yk = st.columns(4)

with col_clear:
    if st.button("清空", use_container_width=True):
        st.rerun()

with col_iqy:
    st.link_button("爱奇艺", "https://www.iqiyi.com/", use_container_width=True)

with col_tx:
    st.link_button("腾讯视频", "https://v.qq.com/", use_container_width=True)

with col_yk:
    st.link_button("优酷视频", "https://www.youku.com/", use_container_width=True)

# 播放按钮
st.markdown("---")
play_col, _ = st.columns([1, 3])
with play_col:
    play_clicked = st.button("▶ 播放VIP视频", type="primary", use_container_width=True)

# ========== 播放逻辑和你原代码完全一致 ==========
if play_clicked:
    video_url = video_url.strip()
    
    if not video_url:
        st.error("⚠️ 请先输入视频播放页的网址")
    else:
        st.success("✅ 解析完成！点击下方按钮在新标签页播放")
        
        # 主接口播放
        st.link_button(
            "立即播放（主接口）", 
            MAIN_API + video_url, 
            type="primary", 
            use_container_width=True
        )
        
        # 备用接口展开栏
        with st.expander("🔧 主接口失效？点我尝试备用接口"):
            st.link_button("备用接口1", BACKUP_API_1 + video_url, use_container_width=True)
            st.link_button("备用接口2", BACKUP_API_2 + video_url, use_container_width=True)