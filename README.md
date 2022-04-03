计划任务-权限维持

钓鱼🎣之后终于不用求别人了<img width="119" alt="image" src="https://user-images.githubusercontent.com/88639842/161436292-109daa96-1a00-4ac9-808d-63c2eaddc8bb.png">


使用python，通过调用Windows-api建立计划任务。

```python
创建 TaskService 对象。 此对象允许您在指定的文件夹中创建任务。

获取任务文件夹并创建任务。 使用 TaskService. GetFolder 方法获取存储任务的文件夹，使用 TaskService 方法创建表示任务的 TaskDefinition 对象。

使用 TaskDefinition 对象定义有关任务的信息。 使用 设置 TaskDefinition属性来定义设置，这些设置确定任务计划程序服务执行任务的方式，并使用 RegistrationInfo属性来定义描述任务的信息。

使用 TaskDefinition 属性创建登录触发器。 此属性提供对 TriggerCollection 对象的访问。 使用 TriggerCollection 方法 (指定要创建启动触发器) 创建的触发器类型。 创建触发器时，设置触发器的 StartBoundary 和 EndBoundary 属性以激活和停用该触发器。 还可以为启动触发器的 " 延迟 " 属性指定一个值。

使用 TaskDefinition 属性为要执行的任务创建操作。 此属性提供对 ActionCollection 对象的访问。 使用 ActionCollection 方法来指定要创建的操作的类型。 此示例使用 ExecAction 对象，该对象表示启动可执行文件的操作。

使用 RegisterTaskDefinition 方法注册任务。 TaskFolder 使用本地服务帐户将任务注册为运行任务所用的安全上下文。
```



**Register (create) the task.**

C++

```c++
hr = pRootFolder->RegisterTaskDefinition(
            _bstr_t( wszTaskName ),
            pTask,
            TASK_CREATE_OR_UPDATE, 
            _variant_t(L"Local Service"), 
            varPassword, 
            TASK_LOGON_SERVICE_ACCOUNT,
            _variant_t(L""),
            &pRegisteredTask);
```

python

```python
Folder.RegisterTaskDefinition( "Test Boot Trigger", taskdefinition, createOrUpdateTask, "Local Service",None,5)
```



**how to use**

```
pyinstaller -F -w tackcom.py
tackcom.exe --addresses C:\xxxxxxxx\xxx.exe
重启生效
```
![image](https://user-images.githubusercontent.com/88639842/161434981-efa023b1-bd32-4ca3-9fd4-838adabfe0fd.png)

**效果**
<img width="1410" alt="image" src="https://user-images.githubusercontent.com/88639842/161434990-d40803fb-98c2-4cf5-8964-25c7bf1d83f7.png">


![image](https://user-images.githubusercontent.com/88639842/161435571-29ceb83e-a375-413b-b8d0-5b631507c1c5.png)


**缺点**


1.大有8M
2.需要管理员权限
3.使用过程可能有bug暂时懒的修。

<img width="120" alt="image" src="https://user-images.githubusercontent.com/88639842/161435269-b5b11f52-db44-417c-90cd-e24e448caac2.png">


**参考资料**


https://docs.microsoft.com/zh-cn/windows/win32/taskschd/taskservice-getfolder


https://docs.microsoft.com/zh-cn/windows/win32/taskschd/daily-trigger-example--scripting-


