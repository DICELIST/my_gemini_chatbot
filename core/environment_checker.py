import platform  
import importlib  
import subprocess  

def check_os():  
    """  
    检查操作系统是否为 Windows 10 或更高版本。  

    Returns:  
        bool: 如果是 Windows 10 或更高版本，则返回 True，否则返回 False。  
    """  
    os_name = platform.system()  
    if os_name == "Windows":  
        os_version = platform.release()  
        try:  
            version_number = int(os_version.split('.')[0])  # 获取主版本号  
            if version_number >= 10:  
                return True  
            else:  
                return False  
        except ValueError:  
            print("无法解析 Windows 版本。") # 无法解析则按失败处理  
            return False  
    else:  
        return False  

def check_dependencies(dependencies):  
    """  
    检查是否安装了所需的依赖包。  

    Args:  
        dependencies: 一个包含所需依赖包名称的列表。  

    Returns:  
        bool: 如果所有依赖包都已安装，则返回 True，否则返回 False。  
    """  
    missing_dependencies = []  
    for dependency in dependencies:  
        try:  
            importlib.import_module(dependency)  
        except ImportError:  
            missing_dependencies.append(dependency)  

    if missing_dependencies:  
        print(f"缺少以下依赖包: {', '.join(missing_dependencies)}")  
        answer = input("是否安装这些依赖包？ (y/n): ")  
        if answer.lower() == 'y':  
            try:  
                subprocess.check_call(["pip", "install", *missing_dependencies])  
                print("依赖包已成功安装。请重新启动程序。")  
                return False # 安装完毕，需要重启  
            except subprocess.CalledProcessError as e:  
                print(f"安装依赖包时出错: {e}")  
                return False  
        else:  
            print("程序退出。")  
            return False  
    return True  

def get_package_version(package_name):  
    """  
    获取已安装的 Python 包的版本。  

    Args:  
        package_name: 包的名称。  

    Returns:  
        str: 包的版本。如果未安装，则返回 "未安装"。  
    """  
    try:  
        module = importlib.import_module(package_name)  
        return module.__version__  
    except ImportError:  
        return "未安装"  

def print_environment_info(dependencies):  
    """  
    打印当前环境信息，如操作系统版本和已安装的依赖包版本。  
    """  
    os_version = platform.system() + " " + platform.release()  
    print(f"当前环境：{os_version}")  

    for dependency in dependencies:  
        version = get_package_version(dependency)  
        print(f"{dependency} 版本：{version}")