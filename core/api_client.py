import google.generativeai as genai  
import time  

class GeminiClient:  
    def __init__(self, api_key):  
        """  
        初始化 GeminiClient。  

        Args:  
            api_key: Gemini API 密钥。  
        """  
        genai.configure(api_key=api_key)  
        self.model = genai.GenerativeModel('gemini-pro') # 使用 gemini-pro 模型  

    def ping(self):  
        """  
        验证 API 密钥的有效性，并返回延迟时间。  

        Returns:  
            float: API 延迟时间（秒）。如果密钥无效，则返回 None。  
        """  
        try:  
            start_time = time.time()  
            response = self.model.generate_content("ping")  # 使用简单的请求  
            end_time = time.time()  
            latency = end_time - start_time  
            print(f"Ping response: {response.text}") # 打印 ping 的结果  
            return latency  
        except Exception as e:  
            print(f"API Key 验证失败: {e}")  
            return None  

    def generate_content(self, prompt):  
        """  
        向 Gemini API 发送提示并获取生成的内容。  

        Args:  
            prompt: 用户提示。  

        Returns:  
            str: 生成的文本内容。  
        """  
        try:  
            response = self.model.generate_content(prompt)  
            return response.text  
        except Exception as e:  
            print(f"生成内容时出错: {e}")  
            return None