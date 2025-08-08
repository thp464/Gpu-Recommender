import streamlit as st

st.set_page_config(page_title="All About GPUs", page_icon="🎯")

st.title("All About GPUs")
st.write("Everything you need to know about Graphics Processing Units")

# GPU Basics
st.header("🖥️ What is a GPU?")
st.markdown("""
A **Graphics Processing Unit (GPU)** is a specialized processor designed to handle graphics rendering and parallel computations. 
Originally created for rendering images and video, modern GPUs are essential for:
- Gaming and entertainment
- Video editing and content creation
- AI and machine learning
- Cryptocurrency mining
- Scientific computing
""")

# VRAM Section
st.header("💾 What is VRAM?")
st.markdown("""
**Video Random Access Memory (VRAM)** is dedicated memory on your graphics card that stores:
- Textures and image data
- Frame buffers
- Shader programs
- 3D models and geometry

### VRAM Requirements by Resolution:
- **1080p Gaming**: 6-8 GB VRAM
- **1440p Gaming**: 8-12 GB VRAM  
- **4K Gaming**: 12+ GB VRAM
- **Content Creation**: 16+ GB VRAM recommended
""")

# FPS Section
st.header("⚡ What is FPS?")
st.markdown("""
**Frames Per Second (FPS)** measures how many images your GPU can render each second.

### Common FPS Targets:
- **30 FPS**: Minimum for playable gaming
- **60 FPS**: Smooth gaming experience
- **120+ FPS**: Competitive gaming, high refresh rate monitors
- **240+ FPS**: Professional esports

### Factors Affecting FPS:
- GPU performance
- Game settings (resolution, graphics quality)
- CPU performance
- Available VRAM
""")

# GPU Types
st.header("🏷️ Types of GPUs")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Gaming GPUs")
    st.markdown("""
    **NVIDIA GeForce Series:**
    - RTX 40 Series (RTX 4090, 4080, 4070)
    - RTX 30 Series (RTX 3080, 3070, 3060)
    
    **AMD Radeon Series:**
    - RX 7000 Series (RX 7900 XTX, 7800 XT)
    - RX 6000 Series (RX 6800 XT, 6700 XT)
    """)

with col2:
    st.subheader("Professional GPUs")
    st.markdown("""
    **NVIDIA Quadro/RTX A Series:**
    - For CAD, 3D modeling, rendering
    
    **AMD Radeon Pro:**
    - Professional workstation graphics
    
    **Features:**
    - ECC memory
    - Certified drivers
    - Optimized for professional software
    """)

# Performance Metrics
st.header("📊 Key Performance Metrics")
st.markdown("""
### When Choosing a GPU, Consider:

**1. Target Resolution**
- Higher resolution = more GPU power needed

**2. Game Types**
- AAA games require more power than indie games
- Ray tracing games need RTX/RDNA2+ GPUs

**3. Monitor Refresh Rate**
- 60Hz monitor: 60+ FPS target
- 144Hz monitor: 144+ FPS target

**4. Budget vs Performance**
- Entry level: GTX 1660 Super, RX 6500 XT
- Mid-range: RTX 4060, RX 7600
- High-end: RTX 4080, RX 7900 XTX
- Enthusiast: RTX 4090
""")

# Technologies
st.header("🔬 Modern GPU Technologies")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Ray Tracing")
    st.markdown("""
    Realistic lighting and reflections:
    - NVIDIA RTX series
    - AMD RDNA2+ (RX 6000/7000)
    - Significant performance impact
    """)
    
    st.subheader("DLSS/FSR")
    st.markdown("""
    AI upscaling for better performance:
    - **DLSS**: NVIDIA RTX cards only
    - **FSR**: Works on most modern GPUs
    - Improves FPS with minimal quality loss
    """)

with col2:
    st.subheader("VRAM Buffer")
    st.markdown("""
    How much VRAM you need:
    - **4GB**: 1080p low-medium settings
    - **8GB**: 1080p high, 1440p medium
    - **12GB+**: 1440p/4K high settings
    """)
    
    st.subheader("Power Consumption")
    st.markdown("""
    GPU power requirements:
    - **Entry**: 75-150W
    - **Mid-range**: 150-250W  
    - **High-end**: 250-350W
    - **Enthusiast**: 350-450W
    """)

# Buying Guide
st.header("🛒 GPU Buying Guide")
st.markdown("""
### Step-by-Step Guide:

1. **Determine Your Budget** 💰
   - Entry: $200-400
   - Mid-range: $400-700
   - High-end: $700-1200+

2. **Choose Your Target Resolution** 🎯
   - 1080p: RTX 4060, RX 7600
   - 1440p: RTX 4070, RX 7700 XT
   - 4K: RTX 4080+, RX 7900 XTX

3. **Check Your PSU** ⚡
   - Ensure adequate wattage
   - Required power connectors

4. **Consider Your CPU** 🖥️
   - Avoid CPU bottlenecks
   - Match GPU tier with CPU tier

5. **Future-Proofing** 🔮
   - VRAM amount for future games
   - Ray tracing support
   - DLSS/FSR compatibility
""")

# Tips
st.header("💡 Pro Tips")
st.info("""
**Money-Saving Tips:**
- Buy previous generation GPUs when new ones release
- Consider used GPUs from reputable sellers
- Look for bundle deals with games

**Performance Tips:**
- Update GPU drivers regularly
- Monitor GPU temperatures (keep under 80°C)
- Ensure adequate case ventilation
- Use MSI Afterburner for monitoring

**Future Considerations:**
- Games are requiring more VRAM over time
- Ray tracing is becoming standard
- 1440p is becoming the new 1080p
""")

st.success("💡 **Ready to find your perfect GPU?** Use our GPU Recommender tool to get personalized suggestions based on your needs and budget!")