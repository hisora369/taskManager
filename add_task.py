# add_task.py
def add_task(task_list, task_name):
    """新增任务，包含空值校验"""
    if not task_name.strip():
        print("❌ 任务名称不能为空！")
        return task_list
    # 自动生成任务ID（基于列表长度）
    task_id = len(task_list) + 1
    task_list.append({"id": task_id, "name": task_name, "status": "未完成"})
    print(f"✅ 任务「{task_name}」新增成功（ID：{task_id}）")
    return task_list