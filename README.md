# Gemini Chatbot  

这是一个使用 Google Gemini API 构建的聊天机器人项目，支持控制台和网页两种对话方式。  

## 环境要求  

*   Windows 10 或更高版本  
*   Python 3.7+  

## 依赖  

*   `google-generativeai`  
*   `flask` 或 `streamlit`  

## 安装  

1.  克隆此仓库。  
2.  创建并激活虚拟环境 (推荐):  
    ```bash  
    python -m venv venv  
    venv\Scripts\activate  # Windows  
    source venv/bin/activate # macOS/Linux  
    ```  
3.  安装依赖:  
    ```bash  
    pip install -r requirements.txt  
    ```  

## 配置  

1.  获取 Google Gemini API Key。  
2.  首次运行程序时，程序会提示你输入 API Key，它将被安全地保存在 `config.txt` 文件中。  

## 运行  

运行 `main.py`：  

```bash  
python main.py