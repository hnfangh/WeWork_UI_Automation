# Wework_UI_Auto

## page
        app.py 封装基本app的启动、暂停、重启、跳转main主页相关
        base_page 封装基础操作方法，findlocator、findslocator、clicklocater、黑名单处理机制
        main.py 封装APP的home页功能，负责具体跳转哪个首页的页签
        contactadd&memberinvite 分别为具体的业务功能的操作
        -- 待优化：测试用例数据封装、测试用例步骤封装、通用的断言封装

## testcase
        test_addcontanct.py 具体业务的用例，引用链式调用，组合page内的业务方法即可，case里包含断言