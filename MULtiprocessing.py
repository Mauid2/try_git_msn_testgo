import multiprocessing
import time

def copy_numbers(task_id, start_index, end_index, Kang):
    print("Task[%s] start" % task_id)
    for i in range(start_index, end_index):
        Kang.append(i)
    print("Task[%s] end" % task_id)

def main():

    time_0 = time.time()
    Kang = multiprocessing.Manager().list()  # 使用multiprocessing.Manager().list()来创建共享列表
    num_numbers = 300000
    num_processes = multiprocessing.cpu_count()

    # 计算每个进程需要处理的数字范围
    numbers_per_process = num_numbers // num_processes
    processes = []

    for i in range(num_processes):
        start_index = i * numbers_per_process
        end_index = (i + 1) * numbers_per_process if i != num_processes - 1 else num_numbers
        p = multiprocessing.Process(target=copy_numbers, args=(i, start_index, end_index, Kang))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    Kang = list(Kang)  # 将共享列表转换为普通列表
    print("所有数字复制完成，列表长度:", len(Kang))
    print("总共用时:", time.time() - time_0, "秒")
if __name__ == "__main__":
    main()
