import os


def del_file(path):
    cnt = 0
    for file in os.listdir(path):
        if file.lower().endswith('.json'):
            try:
                os.remove(os.path.join(path, file))
                cnt += 1
                print(f'file of {format(file)}  deleted successfully!')
            except Exception as e:
                print(f"Something went wrong {file} : {e}")
    print(f'deleted {cnt} files')


if __name__ == '__main__':
    try:
        file_path = input('请输入所要删除的文件路径')
        del_file(file_path)
        print('删除操作完成')
    except Exception as e:
        print(e)