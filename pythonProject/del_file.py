import os


def delete_kfc_files(directory):
    # 遍历目录中的所有文件
    cnt = 0
    for filename in os.listdir(directory):
        # 检查文件名是否以 'kfc' 开头（不区分大小写）
        if filename.lower().startswith('kfc_'):
            file_path = os.path.join(directory, filename)
            try:
                os.remove(file_path)
                cnt += 1
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
    print(f'本次一共删除了{format(str(cnt))}个文件\n')


if __name__ == '__main__':
    folder_path = input("请输入要遍历的文件夹路径: ")
    delete_kfc_files(folder_path)
    print("完成删除操作！")
