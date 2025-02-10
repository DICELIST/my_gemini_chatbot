import os  

CONFIG_FILE = "config.txt"  
API_KEY_KEY = "GEMINI_API_KEY"  

def get_api_key():  
    """  
    从配置文件中安全地获取 Gemini API Key。  

    Returns:  
        str: API Key。如果未找到，则返回 None。  
    """  
    if not os.path.exists(CONFIG_FILE):  
        return None  

    try:  
        with open(CONFIG_FILE, "r") as f:  
            for line in f:  
                key, value = line.strip().split("=", 1)  
                if key == API_KEY_KEY:  
                    return value  
    except Exception as e:  
        print(f"读取配置文件时出错: {e}")  
        return None  

    return None  

def set_api_key(api_key):  
    """  
    安全地设置 Gemini API Key 到配置文件。  

    Args:  
        api_key: 要设置的 API Key。  
    """  
    try:  
        with open(CONFIG_FILE, "w") as f:  
            f.write(f"{API_KEY_KEY}={api_key}\n")  
        print("API Key 已成功保存。")  
    except Exception as e:  
        print(f"写入配置文件时出错: {e}")  

def prompt_for_api_key():  
  """提示用户输入API Key, 并进行保存."""  
  api_key = input("请输入你的 Gemini API Key: ")  
  set_api_key(api_key)  
  return api_key