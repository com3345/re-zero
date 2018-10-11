
系统任务（System Task）用于实现在workflow里流程控制、多线程等，用于安排和控制工作任务（Worker Task）执行。根据指定任务的`type`属性为以下其中一个的固定值，来实现不同的功能。

# DYNAMIC

## 参数:


<table class="docutils">
<thead>
<tr>
<th>参数名称</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr>
<td>dynamicTaskNameParam</td>
<td>指定这个参数为ABC，则下一个任务被执行的任务的类型就是在本dynamic任务的inputParameters里ABC。类似于本身不执行实际内容，用于根据输入分发任务的任务</td>
</tr>
</tbody>
</table>

## 例子

    {
      "name": "user_task",
      "taskReferenceName": "t1",
      "inputParameters": {
        "files": "${workflow.input.files}",
        "taskToExecute": "${workflow.input.user_supplied_task}"
      },
      "type": "DYNAMIC",
      "dynamicTaskNameParam": "taskToExecute"
    }

    {
        "name": "user_task_1",
        ...
    }

    {
        "name": "user_task_2",
        ...
    }

如果上面这个workflow的input里面的user_supplied_task值为**user_task_2**并赋值给了`taskToExecute`这个"临时变量"，且`dynamicTaskNameParam`也指向了这个"临时变量"，那么其实`dynamicTaskNameParam`的值就是被赋值为了**user_task_2**, 因此执行完这个DYNAMIC类型的任务**user_task**后，并不是按照顺序执行**user_task_1**而是执行**user_task_2**。

# DECISION

Decision的系统任务相当于`case...swith`的分支判断语句。该类型的任务有三个参数：

## 参数

<table class="docutils">
<thead>
<tr>
<th>name</th>
<th>description</th>
</tr>
</thead>
<tbody>
<tr>
<td>caseValueParam</td>
<td>任务input里面将做为判断分支的那个值</td>
</tr>
<tr>
<td>decisionCases</td>
<td>根据 <code>caseValueParam</code> 的值的不同被决定执行的任务们</td>
</tr>
<tr>
<td>defaultCase</td>
<td>如果传进来的值没有在<code>decisionCases</code>里面找到，就会执行的默认任务，类似于switch...case...default里面的default</td>
</tr>
</tbody>
</table>

## 例子

    {
      "name": "decide_task",
      "taskReferenceName": "decide1",
      "inputParameters": {
        "case_value_param": "${workflow.input.movieType}"
      },
      "type": "DECISION",
      "caseValueParam": "case_value_param",
      "decisionCases": {
        "Show": [
          {
            "name": "setup_episodes",
            "taskReferenceName": "se1",
            "inputParameters": {
              "movieId": "${workflow.input.movieId}"
            },
            "type": "SIMPLE"
          },
          {
            "name": "generate_episode_artwork",
            "taskReferenceName": "ga",
            "inputParameters": {
              "movieId": "${workflow.input.movieId}"
            },
            "type": "SIMPLE"
          }
        ],
        "Movie": [
          {
            "name": "setup_movie",
            "taskReferenceName": "sm",
            "inputParameters": {
              "movieId": "${workflow.input.movieId}"
            },
            "type": "SIMPLE"
          },
          {
            "name": "generate_movie_artwork",
            "taskReferenceName": "gma",
            "inputParameters": {
              "movieId": "${workflow.input.movieId}"
            },
            "type": "SIMPLE"
          }
        ]
      }
    }


# FORK

Fork任务用于安排并行的任务集

## 参数

<table class="docutils">
<thead>
<tr>
<th>name</th>
<th>description</th>
</tr>
</thead>
<tbody>
<tr>
<td>forkTasks</td>
<td>嵌套的任务列表。每一个子列表都会被并行执行，但是同一个子列表中的任务都是以顺序执行的</td>
</tr>
</tbody>
</table>

## 例子

    {
      "forkTasks": [
        [
          {
            "name": "task11",
            "taskReferenceName": "t11"
          },
          {
            "name": "task12",
            "taskReferenceName": "t12"
          }
        ],
        [
          {
            "name": "task21",
            "taskReferenceName": "t21"
          },
          {
            "name": "task22",
            "taskReferenceName": "t22"
          }
        ]
      ]
    }

**task11**和**task12**按先后顺序执行，但同**task21**和**task22**同时开始执行。

# FORK_JOIN_DYNAMIC

除了并行进行的任务是根据该任务的输入决定的这一点以外，FORK_JOIN_DYNAMIC任务类型类似于FORK任务类型。通俗的说，FORK是先写好并行执行的task的，FORK_JOIN_DYNAMIC是根据输入来决定并行执行的task。

## 参数

<table class="docutils">
<thead>
<tr>
<th>name</th>
<th>description</th>
</tr>
</thead>
<tbody>
<tr>
<td>dynamicForkTasksParam</td>
<td>指定为本任务input中某个值，该值包含了需要并行执行的任务列表</td>
</tr>
<tr>
<td>dynamicForkTasksInputParamName</td>
<td>为这些并行任务指定InputParameters的json</td>
</tr>
</tbody>
</table>

## 例子

    {
      "inputParameters": {
         "dynamicTasks": "${taskA.output.dynamicTasksJSON}",
         "dynamicTasksInput": "${taskA.output.dynamicTasksInputJSON}"
      }
      "type": "FORK_JOIN_DYNAMIC",
      "dynamicForkTasksParam": "dynamicTasks",
      "dynamicForkTasksInputParamName": "dynamicTasksInput"
    }

如果这个**taskA**的output是如下这些的话

    {
      "dynamicTasksInputJSON": {
        "forkedTask1": {
          "width": 100,
          "height": 100,
          "params": {
            "recipe": "jpg"
          }
        },
        "forkedTask2": {
          "width": 200,
          "height": 200,
          "params": {
            "recipe": "jpg"
          }
        }
      },
      "dynamicTasksJSON": [
        {
          "name": "encode_task",
          "taskReferenceName": "forkedTask1",
          "type": "SIMPLE"
        },
        {
          "name": "encode_task",
          "taskReferenceName": "forkedTask2",
          "type": "SIMPLE"
        }
      ]
    }

那么接下来并行执行的就会是`forkedTask1`和`forkedTask2`, 且各自对应的参数为`dynamicTasksInputJSON`指定的参数。

<div class="admonition warning">
<p class="admonition-title">FORK_JOIN_DYNAMIC和JOIN</p>
<p><strong>FORK_JOIN_DYNAMIC后面必须跟一个JOIN</strong></p>
<p>workflow只要定义了一个FORK_JOIN_DYNAMIC任务，那么后面就得紧跟一个JOIN任务.  但是由于FORK_JOIN_DYNAMIC的动态特性，不需要给后面的JOIN任务添加joinOn参数（见下一节），JOIN任务会等待所有并行任务完成后结束.</p>
<p>不像上面提到的FORK任务，并行执行的fork的其中一个分支下可以有多个顺序执行的任务，FORK_JOIN_DYNAMIC只能在每个FORK分支下执行一个任务，也就是不能在上面的例子中实现forkerdTask1-1, forkerdtask1-2这样在一个fork下塞入多个任务。但也有间接方法，那就是把放在fork里的任务类型改成SUB_WORKFLOW，以实现更复杂的执行流程。</p>
</div>

# JOIN

JOIN任务用于等待一个或多个fork分支下的任务完成。

## 参数

<table class="docutils">
<thead>
<tr>
<th>name</th>
<th>description</th>
</tr>
</thead>
<tbody>
<tr>
<td>joinOn</td>
<td>需要等待完成的任务名的列表</td>
</tr>
</tbody>
</table>

## 例子

    {
        "joinOn": ["taskRef1", "taskRef3"]
    }

## JOIN任务的output

JOIN任务的output是个json，键是任务名，值是相应任务的output。

# SUB_WORKFLOW

SUB_WORKFLOW允许把workflow嵌套进另一个workflow，就是说workflow的每一任务都可以设置为workflow。

## 参数

<table class="docutils">
<thead>
<tr>
<th>name</th>
<th>description</th>
</tr>
</thead>
<tbody>
<tr>
<td>subWorkflowParam</td>
<td>包含一系列任务的子workflow名，用JOIN去等待它的完成</td>
</tr>
</tbody>
</table>

## 例子

    {
      "name": "sub_workflow_task",
      "taskReferenceName": "sub1",
      "inputParameters": {
        "requestId": "${workflow.input.requestId}",
        "file": "${encode.output.location}"
      },
      "type": "SUB_WORKFLOW",
      "subWorkflowParam": {
        "name": "deployment_workflow",
        "version": 1
      }
    }

