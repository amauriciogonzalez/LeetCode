class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        taskSet = {}
        queue = []
        time = 0
        for task in tasks:
            taskSet[task] = taskSet.get(task, 0) + 1
        tasks = [-1 * task for task in taskSet.values()]
        heapq.heapify(tasks)
        while tasks or queue:
            time += 1
            if tasks:
                num = heapq.heappop(tasks) + 1
                if num:
                    queue.append([num, time + n])
            else:
                time = queue[0][1]
            if queue and time == queue[0][1]:
                heapq.heappush(tasks, queue.pop(0)[0])  
        return time


            