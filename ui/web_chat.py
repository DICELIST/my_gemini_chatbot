from flask import Flask, render_template, request  
from core.api_client import GeminiClient  

app = Flask(__name__)  

class WebChat:  
    def __init__(self, gemini_client):  
        """  
        初始化 WebChat。  

        Args:  
            gemini_client: Gemini API 客户端。  
        """  
        self.gemini_client = gemini_client  

@app.route("/")  
def index():  
    """  
    渲染主页，包含聊天界面。  
    """  
    return render_template("index.html")  # 渲染一个名为 index.html 的模板  

@app.route("/get_response", methods=["POST"])  
def get_response():  
    """  
    接收用户输入，调用 Gemini API，并返回响应。  
    """  
    user_input = request.form["user_input"]  
    response = app.web_chat.gemini_client.generate_content(user_input)  
    return response  # 返回 Gemini API 的响应  

def start_web_chat(gemini_client):  
  """  
  启动 Flask Web Chat 应用  
  """  
  app.web_chat = WebChat(gemini_client) # 将 WebChat 实例保存到 app 上  
  app.run(debug=False) # 生产环境不应该开启 debug 模式  

# 需要创建 templates/index.html 文件，内容如下：  
# templates/index.html  
'''  
<!DOCTYPE html>  
<html>  
<head>  
    <title>Gemini Chat</title>  
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>  
    <script>  
        $(document).ready(function() {  
            $("#send_button").click(function() {  
                var user_input = $("#user_input").val();  
                $.ajax({  
                    type: "POST",  
                    url: "/get_response",  
                    data: { user_input: user_input },  
                    success: function(response) {  
                        $("#chat_area").append("<p><b>You:</b> " + user_input + "</p>");  
                        $("#chat_area").append("<p><b>Gemini:</b> " + response + "</p>");  
                        $("#user_input").val(""); // Clear input field  
                    }  
                });  
            });  
        });  
    </script>  
</head>  
<body>  
    <h1>Gemini Chat</h1>  
    <div id="chat_area">  
        </div>  
    <input type="text" id="user_input" placeholder="Type your message here">  
    <button id="send_button">Send</button>  
</body>  
</html>  
'''