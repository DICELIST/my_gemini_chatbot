class ConsoleChat:  
    def __init__(self, gemini_client):  
        """  
        初始化 ConsoleChat。  

        Args:  
            gemini_client: Gemini API 客户端。  
        """  
        self.gemini_client = gemini_client  

    def start_chat(self):  
        """  
        启动控制台对话。  
        """  
        print("欢迎使用 Gemini 控制台对话！")  
        while True:  
            prompt = input("你：")  
            if prompt.lower() == "exit":  
                break  
            response = self.gemini_client.generate_content(prompt)  
            if response:  
                print("Gemini：", response)  
            else:  
                print("出错，请重试。")