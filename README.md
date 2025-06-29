<h1 align="center">  AdSnap Studio</h1>
<p align="center"> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/Requests-20232A?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white"> <img src="https://img.shields.io/badge/Pillow-3670A0?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/Bria%20AI-8C52FF?style=for-the-badge"> </p>

<h4 align="center">A powerful Streamlit app for generating professional product ads using Bria AI's advanced image generation and manipulation APIs.</h4>

## 🌟 Features

- 🖼️ Generate HD product images from text prompts
- 🎯 Remove backgrounds with custom colors
- 🌅 Add realistic shadows
- 🏠 Create lifestyle shots with text or reference images
- ✨ AI-powered prompt enhancement
- 📝 Optional CTA text overlay
- 🎮 Intuitive UI controls
- 💾 Easy image download

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/adanSiqueira/adsnap-studio.git
cd adsnap-studio
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory:
```bash
BRIA_API_KEY=your_api_key_here
```

4. Run the app:
```bash
streamlit run app.py
```
---

## 📺 Project Demonstration

![Demonstration](adSnap.gif)

---

## 💡 Usage

1. Enter a product description or upload an image
2. Configure generation options in the sidebar:
   - Enhance prompt with AI
   - Remove background
   - Add shadows
   - Generate lifestyle shots
3. Adjust advanced settings like background color and shadow intensity
4. Click "Generate Ad" to create your images
5. Download the results

## 🔧 Configuration

The app supports various configuration options through the UI:

- **Prompt Enhancement**: Improve your text prompts with AI
- **Background Removal**: Remove backgrounds with custom colors
- **Shadow Effects**: Add realistic shadows with adjustable intensity
- **Lifestyle Shots**: Place products in context using text or reference images
- **CTA Text**: Add optional call-to-action text overlays

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
