import os

# 获取 Jenkins 工作空间路径
workspace = os.getenv('WORKSPACE', 'D:/Jenkins/workspace/AutoSendEmailTests')  
report_dir = os.path.join(workspace, 'htmlreports', 'HTML_20Report')

# 创建报告目录
os.makedirs(report_dir, exist_ok=True)

# 生成简单的 HTML 报告
with open(f'{report_dir}/report.html', 'w') as f:
    f.write("<html><body><h1>Test Report</h1><p>Hello, Jenkins! This is a simple test script.</p></body></html>")

print("HTML report generated successfully at:", report_dir)
