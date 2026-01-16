# update_task.py
def update_task_status(task_list, task_id, new_status):
    """修改任务状态，仅支持「未完成/已完成/暂停」"""
    valid_status = ["未完成", "已完成", "暂停"]
    if new_status not in valid_status:
        print(f"❌ 状态仅支持：{valid_status}")
        return task_list

    # 查找并修改任务
    for task in task_list:
        if task["id"] == task_id:
            task["status"] = new_status
            print(f"✅ 任务ID{task_id}状态已更新为：{new_status}")
            return task_list

    print(f"❌ 未找到ID为{task_id}的任务")
    return task_list

