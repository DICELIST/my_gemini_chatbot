import os  
from core import environment_checker, config_manager  
from core.api_client import GeminiClient  
from ui import console_chat, web_chat  
from core.utils import open_webpage  
import webbrowser  

DEPENDENCIES = ["google.generativeai", "flask"] # 使用 Flask  

def main():  
    """  
    主程序入口。  
    """  
    # 1. 环境检测  
    if not environment_checker.check_os():  
        print("不支持的操作系统。程序仅支持 Windows 10 或更高版本。")  
        return  

    if not environment_checker.check_dependencies(DEPENDENCIES):  
        # check_dependencies 内部会处理安装和退出逻辑.  
        return  

    environment_checker.print_environment_info(DEPENDENCIES)  

    # 2. API Key 验证  
    api_key = config_manager.get_api_key()  
    if not api_key:  
        api_key = config_manager.prompt_for_api_key()  
        if not api_key:  
            print("未提供 API Key。程序退出。")  
            return  

    gemini_client = GeminiClient(api_key)  
    latency = gemini_client.ping()  
    if latency is None:  
        print("API Key 无效。请检查你的 API Key。")  
        return  
    else:  
        print(f"API 链接质量：延迟 {latency:.2f} 秒")  

    # 3. 对话方式选择  
    while True:  
        print("\n请选择对话方式：")  
        print("1. 控制台对话")  
        print("2. 网页对话")  
        print("3. 修改 API Key")  
        print("4. 退出")  

        choice = input("请输入你的选择 (1-4): ")  

        if choice == "1":  
            console = console_chat.ConsoleChat(gemini_client)  
            console.start_chat()  
            break  # 返回主菜单  
        elif choice == "2":  
            web_chat.start_web_chat(gemini_client) # Flask  
            break  # 返回主菜单  

        elif choice == "3":  
            config_manager.prompt_for_api_key()  
            # 重新加载 API Key  
            api_key = config_manager.get_api_key()  
            if not api_key:  
              print("API Key 加载失败，请重新启动程序")  
              return  
            gemini_client = GeminiClient(api_key) # 更新 client  
            latency = gemini_client.ping()  
            if latency is None:  
              print("新的 API Key 仍然无效，请检查你的 API Key。")  
              return  
            else:  
              print(f"API 链接质量：延迟 {latency:.2f} 秒")  

        elif choice == "4":  
            print("程序退出。")  
            break  
        else:  
            print("无效的选择。请重新输入。")  

if __name__ == "__main__":  
    main()