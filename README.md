# Gemini Chatbot - 基于 Google Gemini API 的智能聊天机器人  

这是一个使用 Google Gemini API 构建的聊天机器人项目，提供控制台和网页两种交互方式，旨在提供流畅且智能的对话体验。  

## 项目特性  

*   **双模式支持:**  提供控制台和网页两种交互方式，满足不同场景的需求。  
*   **Google Gemini API 驱动:**  基于 Google Gemini API 的强大能力，提供高质量的自然语言处理能力。  
*   **简洁易用:**  代码结构清晰，易于理解和定制。  
*   **安全配置:**  API Key 安全存储，避免敏感信息泄露。  
*   **可扩展性:**  易于扩展新的功能和特性。  

## 环境要求  

*   Windows 10 或更高版本 (或其他支持 Python 的操作系统)  
*   Python 3.7+  

## 依赖  

本项目使用以下 Python 包：  

*   `google-generativeai`: 用于访问 Google Gemini API。  
*   `flask`: (如果使用网页版) 用于构建 Web 应用。  
*   `streamlit`: (备选方案，如果使用 Streamlit 构建网页版) 用于快速构建 Web 应用。  

可以使用 `pip install -r requirements.txt` 命令安装所有依赖。  

## 安装步骤  

1.  **克隆仓库:**  

    ```bash  
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git  
    cd YOUR_REPOSITORY_NAME  
    ```  

    *   请将 `YOUR_USERNAME` 替换为你的 GitHub 用户名，并将 `YOUR_REPOSITORY_NAME` 替换为你的仓库名称。  

2.  **创建并激活虚拟环境 (推荐):**  

    ```bash  
    python -m venv venv  
    venv\Scripts\activate  # Windows  
    source venv/bin/activate # macOS/Linux  
    ```  

    使用虚拟环境可以隔离项目依赖，避免与其他 Python 项目的依赖冲突。  

3.  **安装依赖:**  

    ```bash  
    pip install -r requirements.txt  
    ```  

    这会自动安装 `requirements.txt` 文件中列出的所有依赖包。  

## 配置 API Key  

1.  **获取 Google Gemini API Key:** 前往 [Google AI Studio](https://makersuite.google.com/app/apikey) 获取你的 API Key。  
2.  **运行项目:** 首次运行程序时 (例如，运行 `main.py`)，程序会提示你输入 API Key。 输入后，API Key 将被安全地保存在 `config.txt` 文件中。  请确保将 `config.txt` 文件添加到 `.gitignore` 文件中，以防止将 API Key 提交到代码仓库。  

    *   **注意:** 强烈建议使用环境变量来存储 API Key，而不是直接存储在 `config.txt` 文件中。  有关如何使用环境变量，请参阅文档或示例代码。  例如，可以使用 `os.environ.get("GEMINI_API_KEY")` 来获取环境变量。  

## 运行  

*   **控制台版本:**  

    ```bash  
    python main.py  
    ```  

    运行 `main.py` 将启动控制台版本的聊天机器人。  

*   **网页版本 (使用 Flask):**  

    1.  确保你已经安装了 `flask`。  
    2.  运行 Flask 应用 (具体运行方式取决于你的 Flask 应用代码，通常会有一个 `app.py` 或类似的入口文件)。  

*   **网页版本 (使用 Streamlit):**  

    1.  确保你已经安装了 `streamlit`。  
    2.  运行 Streamlit 应用：  

        ```bash  
        streamlit run your_streamlit_app.py  
        ```  

        *   将 `your_streamlit_app.py` 替换为你的 Streamlit 应用的文件名。  

##  .gitignore 文件 (重要!)  

为了保护你的 API Key，请确保你的项目根目录下有一个 `.gitignore` 文件，并且包含了以下内容：
