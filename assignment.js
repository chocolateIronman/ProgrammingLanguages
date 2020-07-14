class ArithmeticTaskRunner {
    constructor() {
        this.tasks = [];
    }

    addNegationTask() {
        this.tasks[this.tasks.length] = function(x) {
            return x * -1;
        }
    }

    addAdditionTask(y) {
        this.tasks[this.tasks.length] = function(x) {
            return x + y;
        }
    }

    addMultiplicationTask(y) {
        this.tasks[this.tasks.length] = function(x) {
            return x * y;
        }
    }

    get taskCount() {
        return this.tasks.length;
    }

    execute(startValue) {
        if (!startValue) {
            startValue = 0;
        }

        for (var i = 0; i < this.tasks.length; i++) {
            startValue = this.tasks[i](startValue);
        }

        return startValue;
    }
}

taskRunner = new ArithmeticTaskRunner();
taskRunner.addAdditionTask(10);
taskRunner.addNegationTask();
taskRunner.addMultiplicationTask(0.5);

console.log(taskRunner.execute());
console.log(taskRunner.execute(10));
console.log(taskRunner.taskCount);