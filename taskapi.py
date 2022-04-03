'''
创建 TaskService 对象。 此对象允许您在指定的文件夹中创建任务。
获取任务文件夹并创建任务。 使用 TaskService. GetFolder 方法获取存储任务的文件夹，使用 TaskService 方法创建表示任务的 TaskDefinition 对象。
使用 TaskDefinition 对象定义有关任务的信息。 使用 设置 TaskDefinition属性来定义设置，这些设置确定任务计划程序服务执行任务的方式，并使用 RegistrationInfo属性来定义描述任务的信息。
使用 TaskDefinition 属性创建登录触发器。 此属性提供对 TriggerCollection 对象的访问。 使用 TriggerCollection 方法 (指定要创建启动触发器) 创建的触发器类型。 创建触发器时，设置触发器的 StartBoundary 和 EndBoundary 属性以激活和停用该触发器。 还可以为启动触发器的 " 延迟 " 属性指定一个值。
使用 TaskDefinition 属性为要执行的任务创建操作。 此属性提供对 ActionCollection 对象的访问。 使用 ActionCollection 方法来指定要创建的操作的类型。 此示例使用 ExecAction 对象，该对象表示启动可执行文件的操作。
使用 RegisterTaskDefinition 方法注册任务。 TaskFolder 使用本地服务帐户将任务注册为运行任务所用的安全上下文。

'''
import win32com.client
import argparse


def regtask(patha):
    TriggerTypeBoot=8
    ActionTypeExecutable=0
    #创建 taskservice对象
    taskserver = win32com.client.Dispatch("Schedule.Service")
    taskserver.Connect()
    #创建获取要在其中创建任务定义的文件夹。Get a folder to create a task definition in.
    folder=taskserver.GetFolder("\\")
#flags参数为0，因为它不受支持。 暂时8懂什么意思
    taskdefinition=taskserver.NewTask(0)

    #  Define information about the task.
    #权限维持的描述和设置的作者
    # Set the registration info for the task by
    # creating the RegistrationInfo object.
    regInfo = taskdefinition.RegistrationInfo
    regInfo.Description="TTask will execute"
    regInfo.Author="Administrator"
    # Set the task setting info for the Task Scheduler by
    # creating a TaskSettings object.
    settings=taskdefinition.Settings
    settings.StartWhenAvailable = True


    # 创建一个每日触发器。请注意，开始边界
    # 指定一天中任务开始的时间和
    # 间隔指定任务运行的天数

    #' Create a boot trigger.
    triggers = taskdefinition.Triggers
    trigger=triggers.Create(TriggerTypeBoot)

    # 定义触发器何时激活的触发器变量
    # '以及任务运行的时间。格式
    # “这次是YYYY - MM - DDTHH: MM:SS
    startTime = "2020-05-02T10:49:02"
    endTime = "2025-05-02T10:52:02"
    print("startTime :" , startTime)
    print("startTime :", endTime)
    trigger.StartBoundary = startTime
    trigger.EndBoundary = endTime
    trigger.ExecutionTimeLimit = "PT5M"   # ' Five minutes
    trigger.Id = "BootTriggerId"
    #trigger.delay = "PT5S" #系统启动后多久运行
    trigger.Delay="PT30S"
    #' 30 Seconds
#     '''
# Create the action for the task to execute.
# Add an action to the task. The action executes notepad.
#     '''
    Action =taskdefinition.Actions.Create( ActionTypeExecutable )
    Action.Path = patha # 相当于改为C:\\Users\\Administrator\\Desktop\\1.jpg
    createOrUpdateTask=6
    folder.RegisterTaskDefinition( "Test Boot Trigger", taskdefinition, createOrUpdateTask, "Local Service",None,5)
    print("计划任务创建完成")

def parse_args():
    """
    :return:进行参数的解析
    """
    description = "you should add those parameter"                   # 步骤二
    parser = argparse.ArgumentParser(description=description)        # 这些参数都有默认值，当调用parser.print_help()或者运行程序时由于参数不正确(此时python解释器其实也是调用了pring_help()方法)时，
                                                                     # 会打印这些描述信息，一般只需要传递description参数，如上。
    help = "The path of address"
    parser.add_argument('--addresses',help = help)                   # 步骤三，后面的help是我的描述
    args = parser.parse_args()                                       # 步骤四
    return args

if __name__ == '__main__':
    args = parse_args()
    print(args.addresses)
    regtask(args.addresses)




