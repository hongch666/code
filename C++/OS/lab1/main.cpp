#include <iostream>
#include <queue>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <thread>
#include <unistd.h> // For usleep
#include <atomic>

using namespace std;

const int MAX_PID = 100;
const int MAX_PRIORITY = 50;

struct PCB {
    int pid;
    string status;
    int priority;
    int life;
};

vector<bool> pid_array(MAX_PID + 1, true);
vector<queue<PCB>> ready_queues(MAX_PRIORITY);
vector<PCB> process_list;

atomic<bool> running(true);  // 使用原子变量来标记程序是否在运行

int generate_pid() {
    int pid = rand() % MAX_PID + 1;
    while (!pid_array[pid]) {
        pid = rand() % MAX_PID + 1;
    }
    pid_array[pid] = false;
    return pid;
}

void create_process() {
    int pid = generate_pid();
    int priority = rand() % MAX_PRIORITY;
    int life = rand() % 5 + 1;
    PCB new_pcb = {pid, "ready", priority, life};
    ready_queues[priority].push(new_pcb);
    process_list.push_back(new_pcb);
}

void display_processes() {
    for (const auto& process : process_list) {
        cout << "PID: " << process.pid 
             << ", Status: " << process.status 
             << ", Priority: " << process.priority 
             << ", Life: " << process.life << endl;
    }
}

void schedule_process() {
    while (running) {
        int highest_priority = -1;
        for (int i = MAX_PRIORITY - 1; i >= 0; --i) {
            if (!ready_queues[i].empty()) {
                highest_priority = i;
                break;
            }
        }
        
        if (highest_priority == -1) {
            cout << "No process to schedule." << endl;
            usleep(1000000); // Sleep for 1 second
            continue;
        }

        PCB process = ready_queues[highest_priority].front();
        ready_queues[highest_priority].pop();
        process.status = "run";

        cout << "Running process PID: " << process.pid 
             << ", Priority: " << process.priority 
             << ", Life: " << process.life << endl;

        usleep(1000000); // Simulate process running for 1 second

        process.priority = max(0, process.priority / 2);
        process.life -= 1;

        if (process.life > 0) {
            process.status = "ready";
            ready_queues[process.priority].push(process);
        } else {
            cout << "Process PID: " << process.pid << " completed." << endl;
            pid_array[process.pid] = true;
            process_list.erase(remove_if(process_list.begin(), process_list.end(), 
                                        [process](const PCB& p) { return p.pid == process.pid; }), 
                               process_list.end());
        }

        display_processes();
    }
}

void dynamic_process_creation() {
    while (running) {
        char c;
        cin >> c;
        if (c == 'f') {
            create_process();
        } else if (c == 'q') {
            running = false;  // 设置退出标志
            break;
        }
    }
}

int main() {
    srand(time(0));
    thread creation_thread(dynamic_process_creation);
    schedule_process();
    creation_thread.join();
    return 0;
}
