def delete_task(task_list, task_id):
    """删除指定ID的任务，删除后自动修复ID断层"""
    for idx, task in enumerate(task_list):
        if task["id"] == task_id:
            del task_list[idx]
            print(f"✅ 任务ID{task_id}已删除！")
            # 重新分配ID，避免断层
            for i in range(idx, len(task_list)):
                task_list[i]["id"] = i + 1
            return task_list

    print(f"❌ 未找到ID为{task_id}的任务")
    return task_list


