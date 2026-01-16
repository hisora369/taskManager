# query_task.py
def query_tasks(task_list, status=None):
    """查询任务：status=None查全部，否则按状态筛选"""
    if not task_list:
        print("📄 暂无任务！")
        return

    print("===== 任务列表 =====")
    count = 0
    for task in task_list:
        if status is None or task["status"] == status:
            print(f"ID:{task['id']} | 名称：{task['name']} | 状态：{task['status']}")
            count += 1

    if count == 0:
        print(f"📄 无「{status}」状态的任务！")
    print("====================")