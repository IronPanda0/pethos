

# 用户模块

## 后台登录

### 管理员登录

|   参数   |  中文  | 是否必须 |  类型  | 备注 |
| :------: | :----: | :------: | :----: | :--: |
| username | 用户名 |    是    | string |      |
| password |  密码  |    是    | string |      |

- 接口URL：`/mlogin`
- 请求方式：`POST`
- 参数说明：

- 返回参数(成功)

```json
{
    "code": 200,
    "data":
        {
            "token": "令牌",
            "userId": "管理员在数据库中的Id"
        }
    ,
    "msg": "登录成功~~"
}
```

- 返回参数(失败)

```json
{
    "code": -1,
    "data": [
        {}
    ],
    "msg": "(根据后端判断而定)"
}
```

### 管理员添加

|   参数   |  中文  | 是否必须 |  类型  | 备注 |
| :------: | :----: | :------: | :----: | :--: |
| username | 用户名 |    是    | string |      |
| password |  密码  |    是    | string |      |
| checkpwd |重复密码 |	是    | string |      |

- 接口URL：`/mregister`
- 请求方式：`POST`
- 参数说明：

- 返回参数(成功)

```json
{
    "code": 200,
    "data": 
        {}
    ,
    "msg": "注册成功~~"
}
```

- 返回参数(失败)

```json
{
    "code": -1,
    "data": 
        {}
    ,
    "msg": "(根据后端判断而定)"
}
```

### 获取管理员列表

|   参数   |  中文  | 是否必须 |  类型  | 备注 |
| :------: | :----: | :------: | :----: | :--: |
| userId | 当前用户Id |    是    | int |      |
| token |  令牌  	|    是    | string |      |
| page 	| 页数 		|	是    | int |      |
| per_page| 每页数据量|	是    | int |      |

- 接口URL：`/manager/list`
- 请求方式：`POST`
- 参数说明：

- 返回参数(成功)

```json
{
    "code": 200,
    "data": 
        [
        	{
        		"userId":1,
        		"userName":"小明",
        		"password":"123456",
        		"gender":1,
        		"age":20,
        		"mail":"1@c.cc"
        	}
        ,
        	{
        		// 以此类推
        	}
        ]
    ,
    "msg": "注册成功~~"
}
```

- 返回参数(失败)

```json
{
    "code": -1,
    "data": 
        {}
    ,
    "msg": "(根据后端判断而定)"
}
```


## 用户角色管理

### 添加角色

- 接口URL：`/userRole/add`
- 请求方式：`POST`
- 参数说明：

|   参数   |   中文   | 是否必须 |  类型  |       备注       | 案例 |
| :------: | :------: | :------: | :----: | :--------------: | :--: |
| userName | 用户名称 |    是    | string |                  |      |
|   role   |   角色   |    是    | string | 前台，医助，医师 |      |
| content  |   内容   |    是    | string |                  |      |
|   duty   |   责任   |    是    | string |                  |      |
| process  |   流程   |    是    | string |                  |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "content": "干活",
            "duty": "什么的干活啦啦啦",
            "process": "流程3,2，1",
            "role": "前台",
            "userName": "小王"
        }
    ],
    "msg": "添加成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "该用户已有此角色，请换一个试试"
}
```

### 删除角色

- 接口URL：`/userRole/delete`
- 请求方式：`POST`
- 参数说明：

|    参数    |    中文    | 是否必须 |  类型  | 备注 | 案例 |
| :--------: | :--------: | :------: | :----: | :--: | :--: |
| userRoleID | 用户角色ID |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "duty": "什么的干活啦啦啦",
            "process": "流程3,2，1",
            "role": "医助",
            "userName": "小王"
        }
    ],
    "msg": "删除成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "目前没有该角色，请再次确认"
}
```

### 更新角色

- 接口URL：`/userRole/update`
- 请求方式：`POST`
- 参数说明：

|    参数    |    中文    | 是否必须 |  类型  |       备注       | 案例 |
| :--------: | :--------: | :------: | :----: | :--------------: | :--: |
|  userName  |  用户名称  |    是    | string |                  |      |
|    role    |    角色    |    是    | string | 前台，医助，医师 |      |
|  content   |    内容    |    是    | string |                  |      |
|    duty    |    责任    |    是    | string |                  |      |
|  process   |    流程    |    是    | string |                  |      |
| userRoleId | 用户角色ID |    是    | string |                  |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "content": "干活",
            "duty": "什么的干活啦啦啦",
            "process": "流程3,2，1",
            "role": "医助",
            "userName": "小王"
        }
    ],
    "msg": "用户角色修改成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "该用户已有此角色，请换一个试试"
}
```

### 分页返回用户角色关系

- 接口URL：`/userRole/list`
- 请求方式：`POST`
- 参数说明：

|   参数   |    中文    | 是否必须 |  类型  |            备注            | 案例 |
| :------: | :--------: | :------: | :----: | :------------------------: | :--: |
|   page   |    页数    |    否    |  int   |       不传默认第1页        |      |
| per_page | 每页数据量 |    否    |  int   |        不传默认10条        |      |
| userName |  用户名称  |    否    | string | 不传默认返回全部用户的角色 |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "content": "干活",
            "duty": "什么的干活",
            "process": "流程1，2，3",
            "role": "医师",
            "userName": "小王",
            "userRoleId": 1
        },
        {
            "content": "干活",
            "duty": "什么的干活",
            "process": "流程1，2，3",
            "role": "医助",
            "userName": "小王",
            "userRoleId": 2
        },
        {
            "content": "干活",
            "duty": "什么的干活",
            "process": "流程1，2，3",
            "role": "前台",
            "userName": "小王",
            "userRoleId": 3
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有角色"
}
```

# 测试模块

## 试卷类

### 添加试卷

- 接口URL：`/paper/add`
- 请求方式：`POST`
- 参数说明：

|    参数     |     中文     | 是否必须 |  类型  | 备注 |        案例        |
| :---------: | :----------: | :------: | :----: | :--: | :----------------: |
|  paperName  |   试卷名称   |    是    | string |      | 期末考试狂犬病试卷 |
| diseaseName |   相关病种   |    是    | string |      |       狂犬病       |
|   IdList    | 试题ID的list |    是    | int[]  |      |      [1,3,4]       |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "diseaseName": "狂犬病",
            "num": 3,
            "paperName": "期中考试",
            "sum": 20
        }
    ],
    "msg": "添加成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "目前有该试卷，请重试"
}
```

### 删除试卷

- 接口URL：`/paper/delete`
- 请求方式：`POST`
- 参数说明：

|  参数   |  中文  | 是否必须 |  类型  | 备注 | 案例 |
| :-----: | :----: | :------: | :----: | :--: | :--: |
| paperId | 试卷Id |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "diseaseName": "狂犬病",
            "num": 3,
            "paperId": 46,
            "paperName": "入学考试试卷",
            "sum": 30
        }
    ],
    "msg": "删除成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "目前没有该试卷，请重新确认"
}
```

### 更新试卷

- 接口URL：`/paper/update`
- 请求方式：`POST`
- 参数说明：

|    参数     |   中文   | 是否必须 |  类型  | 备注 |        案例        |
| :---------: | :------: | :------: | :----: | :--: | :----------------: |
|   paperId   |  试卷ID  |    是    | string |      |                    |
|  paperName  | 试卷名称 |    是    | string |      | 期末考试狂犬病试卷 |
| diseaseName | 相关病种 |    是    | string |      |       狂犬病       |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "diseaseName": "狂犬病",
            "paperId": "47",
            "paperName": "入学考试试卷修改"
        }
    ],
    "msg": "修改试卷成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "相同试卷名已经存在，请换一个再试试。"
}
```

### 分页返回试卷

- 接口URL：`/paper/list`
- 请求方式：`POST`
- 参数说明：

|   参数   |    中文    | 是否必须 | 类型 |     备注      | 案例 |
| :------: | :--------: | :------: | :--: | :-----------: | :--: |
|   page   |    页数    |    否    | int  | 传空默认第1页 |      |
| per_page | 每页数据量 |    否    | int  | 传空默认10条  |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "diseaseName": "狂犬病",
            "num": 2,
            "paperId": 1,
            "paperName": "期末考试狂犬病试卷",
            "sum": 10
        },
        {
            "diseaseName": "狂犬病",
            "num": null,
            "paperId": 2,
            "paperName": "入学考试狂犬病试卷",
            "sum": 95
        },
        {
            "diseaseName": "狂犬病",
            "num": 3,
            "paperId": 47,
            "paperName": "入学考试试卷修改",
            "sum": 30
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有试卷"
}
```

### 分页返回模糊查询试卷

- 接口URL：`/paper/fuzzy`
- 请求方式：`POST`
- 参数说明：

|   参数    |    中文    | 是否必须 |  类型  |     备注      |  案例  |
| :-------: | :--------: | :------: | :----: | :-----------: | :----: |
|   page    |    页数    |    否    |  int   | 传空默认第1页 |        |
| per_page  | 每页数据量 |    否    |  int   | 传空默认10条  |        |
| paperName |  试卷名称  |    是    | string |               | 狂犬病 |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "diseaseName": "狂犬病",
            "num": 2,
            "paperId": 1,
            "paperName": "期末考试狂犬病试卷",
            "sum": 10
        },
        {
            "diseaseName": "狂犬病",
            "num": null,
            "paperId": 2,
            "paperName": "入学考试狂犬病试卷",
            "sum": 95
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有试卷"
}
```

## 考试管理

### 添加考试

- 接口URL：`/test/add`
- 请求方式：`POST`
- 参数说明：

|    参数     |   中文   | 是否必须 |  类型  | 备注 |        案例         |
| :---------: | :------: | :------: | :----: | :--: | :-----------------: |
|  testName   | 考试名称 |    是    | string |      |      期末考试       |
| diseaseName | 相关病种 |    是    | string |      |       狂犬病        |
|   paperId   |  试卷ID  |    是    | string |      |                     |
|  beginTime  | 考试时间 |    是    | string |      | 2021-04-01 10:00:00 |
|   endTime   | 结束时间 |    是    | string |      | 2021-04-01 12:00:00 |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "beginTime": "Mon, 01 Mar 2021 08:00:00 GMT",
            "diseaseName": "狂犬病",
            "endTime": "Mon, 01 Mar 2021 10:00:00 GMT",
            "paperName": "期中考试狂犬病试卷",
            "testName": "期中考试"
        }
    ],
    "msg": "添加成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "相同考试已存在，请再换一个试试"
}
```

### 更新考试

- 接口URL：`/paper/update`
- 请求方式：`POST`
- 参数说明：

|    参数     |   中文   | 是否必须 |  类型  | 备注 |        案例         |
| :---------: | :------: | :------: | :----: | :--: | :-----------------: |
|   testId    |  考试ID  |    是    | string |      |                     |
|  testName   | 考试名称 |    是    | string |      |      期末考试       |
| diseaseName | 相关病种 |    是    | string |      |       狂犬病        |
|  paperName  | 试卷名称 |    是    | string |      |                     |
|  beginTime  | 考试时间 |    是    | string |      | 2021-04-01 10:00:00 |
|   endTime   | 结束时间 |    是    | string |      | 2021-04-01 12:00:00 |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "beginTime": "Thu, 01 Apr 2021 10:00:00 GMT",
            "diseaseName": "狂犬病",
            "endTime": "Thu, 01 Apr 2021 12:00:00 GMT",
            "papName": "期中考试修改",
            "paperName": "入学考试考试试卷",
            "testId": "6"
        }
    ],
    "msg": "修改试卷成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "相同试卷名已经存在，请换一个再试试。"
}
```

### 删除考试

- 接口URL：`/test/delete`
- 请求方式：`POST`
- 参数说明：

|  参数  |  中文  | 是否必须 |  类型  | 备注 | 案例 |
| :----: | :----: | :------: | :----: | :--: | :--: |
| testId | 考试Id |    否    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "beginTime": "Thu, 01 Apr 2021 10:00:00 GMT",
            "diseaseName": "狂犬病",
            "endTime": "Thu, 01 Apr 2021 12:00:00 GMT",
            "paperName": "入学考试试卷修改",
            "testId": 5,
            "testName": "期中考试"
        }
    ],
    "msg": "删除成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "目前没有该考试，请再次确认"
}
```

### 分页返回考试

- 接口URL：`/test/list`
- 请求方式：`POST`
- 参数说明：

|    参数     |    中文    | 是否必须 |  类型  |         备注          | 案例 |
| :---------: | :--------: | :------: | :----: | :-------------------: | :--: |
|    page     |    页数    |    否    |  int   |     传空默认第1页     |      |
|  per_page   | 每页数据量 |    否    |  int   |     传空默认10条      |      |
| diseaseName |  病种名称  |    否    | string | 传all默认返回全部考试 |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "beginTime": "Mon, 01 Mar 2021 08:00:00 GMT",
            "diseaseName": "狂犬病",
            "endTime": "Mon, 01 Mar 2021 10:00:00 GMT",
            "paperName": "期末考试狂犬病试卷",
            "testId": 1,
            "testName": "期末考试"
        },
        {
            "beginTime": "Mon, 01 Mar 2021 08:00:00 GMT",
            "diseaseName": "狂犬病",
            "endTime": "Mon, 01 Mar 2021 10:00:00 GMT",
            "paperName": "入学考试狂犬病试卷",
            "testId": 2,
            "testName": "入学考试"
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有考试"
}
```

### 查询考试

- 接口URL：`/test/search`
- 请求方式：`POST`
- 参数说明：

|   参数   |   中文   | 是否必须 |  类型  | 备注 |   案例   |
| :------: | :------: | :------: | :----: | :--: | :------: |
| testName | 考试名称 |    是    | string |      | 期中考试 |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "beginTime": "Mon, 01 Mar 2021 08:00:00 GMT",
            "diseaseName": "狂犬病",
            "endTime": "Mon, 01 Mar 2021 10:00:00 GMT",
            "paperName": "期中考试狂犬病试卷",
            "testId": 1,
            "testName": "期中考试"
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有这场考试"
}
```

### 分页返回模糊查询考试

- 接口URL：`/test/fuzzy`
- 请求方式：`POST`
- 参数说明：

|   参数   |    中文    | 是否必须 |  类型  |     备注      | 案例 |
| :------: | :--------: | :------: | :----: | :-----------: | :--: |
|   page   |    页数    |    否    |  int   | 传空默认第1页 |      |
| per_page | 每页数据量 |    否    |  int   | 传空默认10条  |      |
| testName |  考试名称  |    是    | string |               |  期  |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "beginTime": "Mon, 01 Mar 2021 08:00:00 GMT",
            "diseaseName": "狂犬病",
            "endTime": "Mon, 01 Mar 2021 10:00:00 GMT",
            "paperName": "期末考试狂犬病试卷",
            "testId": 1,
            "testName": "期末考试"
        },
        {
            "beginTime": "Thu, 01 Apr 2021 10:00:00 GMT",
            "diseaseName": "狂犬病",
            "endTime": "Thu, 01 Apr 2021 12:00:00 GMT",
            "paperName": "入学考试考试试卷",
            "testId": 6,
            "testName": "期中考试修改"
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有考试"
}
```

## 试题管理

### 添加试题

- 接口URL：`/question/add`
- 请求方式：`POST`
- 参数说明：

|     参数     |   中文   | 是否必须 |  类型  | 备注 |     案例     |
| :----------: | :------: | :------: | :----: | :--: | :----------: |
| questionInfo |   题干   |    是    | string |      | 题干题干题干 |
| diseaseName  | 相关疾病 |    是    | string |      |    狂犬病    |
|    answer    |   答案   |    是    |  int   |      |      1       |
|   choiceA    |  选项A   |    是    | string |      |     选项     |
|   choiceB    |  选项B   |    是    | string |      |     选项     |
|   choiceC    |  选项C   |    是    | string |      |     选项     |
|   choiceD    |  选项D   |    是    | string |      |     选项     |
|    score     |   分值   |    是    |  int   |      |      10      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "answer": "2",
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "传染病",
            "questionId": 21,
            "questionInfo": "传染病传染病传染病",
            "score": "5"
        }
    ],
    "msg": "添加成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "已有相同题干，请重试"
}
```

### 删除试题

- 接口URL：`/question/delete`
- 请求方式：`POST`
- 参数说明：

|    参数    |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :--------: | :------: | :------: | :----: | :--: | :--: |
| questionId | 用户名称 |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "answer": 2,
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "传染病",
            "questionId": 21,
            "questionInfo": "传染病传染病传染病修改后",
            "score": 5
        }
    ],
    "msg": "删除成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "目前没有该题目，请重新确认"
}
```

### 更新试题

- 接口URL：`/question/update`
- 请求方式：`POST`
- 参数说明：
- 参数说明：

|     参数     |   中文   | 是否必须 |  类型  | 备注 |     案例     |
| :----------: | :------: | :------: | :----: | :--: | :----------: |
|  questionId  |  试题ID  |    是    | string |      |              |
| questionInfo |   题干   |    是    | string |      | 题干题干题干 |
| diseaseName  | 相关疾病 |    是    | string |      |    狂犬病    |
|    answer    |   答案   |    是    |  int   |      |      1       |
|   choiceA    |  选项A   |    是    | string |      |     选项     |
|   choiceB    |  选项B   |    是    | string |      |     选项     |
|   choiceC    |  选项C   |    是    | string |      |     选项     |
|   choiceD    |  选项D   |    是    | string |      |     选项     |
|    score     |   分值   |    是    |  int   |      |      10      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "answer": "2",
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "传染病",
            "questionId": "21",
            "questionInfo": "传染病传染病传染病修改后",
            "score": "5"
        }
    ],
    "msg": "修改问题成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "相同药品名已经存在，请换一个再试试。"
}
```

### 分页返回试题

- 接口URL：`/question/list`
- 请求方式：`POST`
- 参数说明：

|    参数     |    中文    | 是否必须 |  类型  |        备注         | 案例 |
| :---------: | :--------: | :------: | :----: | :-----------------: | :--: |
|    page     |    页数    |    否    |  int   |    传空默认第1页    |      |
|  per_page   | 每页数据量 |    否    |  int   |    传空默认10条     |      |
| diseaseName |  病种名称  |    否    | string | 传“all”返回全部试题 |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "answer": 1,
            "choiceA": "选A",
            "choiceB": "选B",
            "choiceC": "选C",
            "choiceD": "选D",
            "diseaseName": "狂犬病",
            "questionId": 1,
            "questionInfo": "题目1",
            "score": 5
        },
        {
            "answer": 1,
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "狂犬病",
            "questionId": 3,
            "questionInfo": "题干题干",
            "score": 5
        },
        {
            "answer": 1,
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "狂犬病",
            "questionId": 4,
            "questionInfo": "题干题干题干",
            "score": 10
        },
        {
            "answer": 1,
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "狂犬病",
            "questionId": 5,
            "questionInfo": "题干题干题干题干",
            "score": 10
        },
        {
            "answer": 1,
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "狂犬病",
            "questionId": 6,
            "questionInfo": "题干题干题干题干题干",
            "score": 10
        },
        {
            "answer": 1,
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "狂犬病",
            "questionId": 8,
            "questionInfo": "凑数生成试卷1",
            "score": 5
        },
        {
            "answer": 1,
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "狂犬病",
            "questionId": 9,
            "questionInfo": "凑数2",
            "score": 10
        },
        {
            "answer": 1,
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "狂犬病",
            "questionId": 10,
            "questionInfo": "凑数3",
            "score": 10
        },
        {
            "answer": 1,
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "狂犬病",
            "questionId": 11,
            "questionInfo": "凑数4",
            "score": 10
        },
        {
            "answer": 1,
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "狂犬病",
            "questionId": 12,
            "questionInfo": "凑数5",
            "score": 10
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有试题"
}
```

### 分页返回模糊查询题干

- 接口URL：`/question/fuzzy`
- 请求方式：`POST`
- 参数说明：

|     参数     |    中文    | 是否必须 |  类型  |     备注      | 案例 |
| :----------: | :--------: | :------: | :----: | :-----------: | :--: |
|     page     |    页数    |    否    |  int   | 传空默认第1页 |      |
|   per_page   | 每页数据量 |    否    |  int   | 传空默认10条  |      |
| questionInfo |  题目题干  |    是    | string |               | 题干 |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "answer": 1,
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "狂犬病",
            "questionId": 3,
            "questionInfo": "题干题干",
            "score": 5
        },
        {
            "answer": 1,
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "狂犬病",
            "questionId": 4,
            "questionInfo": "题干题干题干",
            "score": 10
        },
        {
            "answer": 1,
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "狂犬病",
            "questionId": 5,
            "questionInfo": "题干题干题干题干",
            "score": 10
        },
        {
            "answer": 1,
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "狂犬病",
            "questionId": 6,
            "questionInfo": "题干题干题干题干题干",
            "score": 10
        },
        {
            "answer": 1,
            "choiceA": "选项",
            "choiceB": " 选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "感染病",
            "questionId": 7,
            "questionInfo": "感染病题干",
            "score": 5
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有试题"
}
```

# 病例模块

## 分类管理

### 添加分类

- 接口URL：`/category/add`
- 请求方式：`POST`
- 参数说明：

|     参数     |   中文   | 是否必须 | 类型   | 备注 | 案例  |
| :----------: | :------: | -------- | ------ | ---- | ----- |
| categoryName | 分类名称 | 是       | string |      | 分类1 |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "categoryName": "分类1"
        }
    ],
    "msg": "添加成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "相同分类已存在，请再换一个试试"
}
```

### 删除分类

- 接口URL：`/category/delete`
- 请求方式：`POST`
- 参数说明：

|    参数    |  中文  | 是否必须 |  类型  | 备注 | 案例 |
| :--------: | :----: | :------: | :----: | :--: | :--: |
| categoryId | 分类ID |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": {},
    "msg": "删除成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "目前该分类还有病种，请确认后删除"
}
```

### 返回全部分类

- 接口URL：`/category/list`
- 请求方式：`POST`
- 参数说明：

| 参数 | 中文 | 是否必须 | 类型 | 备注 | 案例 |
| :--: | :--: | :------: | :--: | :--: | :--: |
|  无  |      |          |      |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "categoryID": 16,
            "categoryName": "分类9"
        },
        {
            "categoryID": 17,
            "categoryName": "分类10"
        },
        {
            "categoryID": 18,
            "categoryName": "分类1"
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（分类表为空）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有分类"
}
```

### 更新分类

- 接口URL：`/category/update`
- 请求方式：`POST`
- 参数说明：

|     参数     |   中文   | 是否必须 |  类型  | 备注 |  案例  |
| :----------: | :------: | :------: | :----: | :--: | :----: |
|  categoryId  |  分类ID  |    是    | string |      |   1    |
| categoryName | 分类名称 |    是    | string |      | 传染病 |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "categoryID": 1,
            "categoryName": "传染病修改"
        }
    ],
    "msg": "修改成功"
}
```

- 返回参数（分类表为空）

```json
{
    "code": -1,
    "data": {},
    "msg": "分类已经存在，请换一个再试试。"
}
```

## 病种管理

### 添加病种

- 接口URL：`/disease/add`
- 请求方式：`POST`
- 参数说明：

|     参数     |   中文   | 是否必须 |  类型  | 备注 |  案例   |
| :----------: | :------: | :------: | :----: | :--: | :-----: |
| diseaseName  | 疾病名称 |    是    | string |      | 传染111 |
| categoryName | 分类名称 |    是    | string |      | 传染病  |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "categoryName": "传染病",
            "diseaseName": "传染111"
        }
    ],
    "msg": "添加成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "相同名字已存在，请再换一个试试"
}
```

### 删除病种

- 接口URL：`/disease/delete`
- 请求方式：`POST`
- 参数说明：

|   参数    |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :-------: | :------: | :------: | :----: | :--: | :--: |
| diseaseId | 分类名称 |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": {},
    "msg": "删除成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "目前没有该病种，请再次确认"
}
```

### 更新病种

- 接口URL：`/disease/update`
- 请求方式：`POST`
- 参数说明：

|     参数     |   中文   | 是否必须 |  类型  | 备注 |  案例  |
| :----------: | :------: | :------: | :----: | :--: | :----: |
|  diseaseId   |  分类ID  |    是    | string |      |   1    |
| categoryName | 分类名称 |    是    | string |      | 传染病 |
| diseaseName  | 病种名称 |    是    | string |      |  犬瘟  |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "categoryName": "传染病",
            "diseaseId": "1",
            "diseaseName": "犬瘟修改"
        }
    ],
    "msg": "修改成功"
}
```

- 返回参数（分类表为空）

```json
{
    "code": -1,
    "data": {},
    "msg": "目前没有该分类，请确认后再试试。"
}
```

### 分页返回病种

- 接口URL：`/disease/list`
- 请求方式：`POST`
- 参数说明：

|     参数     |    中文    | 是否必须 |  类型  |     备注      | 案例 |
| :----------: | :--------: | :------: | :----: | :-----------: | :--: |
| categoryName |  分类名称  |    是    | string | 传all返回全部 |      |
|     page     |    页数    |    否    |  int   | 传空默认第1页 |      |
|   per_page   | 每页数据量 |    否    |  int   | 传空默认10条  |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "categoryName": "传染病",
            "diseaseId": 5,
            "diseaseName": "狂犬病1"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 7,
            "diseaseName": "狂犬病3"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 8,
            "diseaseName": "狂犬病4"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 9,
            "diseaseName": "狂犬病5"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 10,
            "diseaseName": "狂犬病6"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 11,
            "diseaseName": "狂犬病7"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 12,
            "diseaseName": "狂犬病8"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 13,
            "diseaseName": "狂犬病9"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 14,
            "diseaseName": "狂犬病10"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 15,
            "diseaseName": "狂犬病11"
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前该分类没有疾病"
}
```

### 分页返回模糊查询病种

- 接口URL：`/disease/fuzzy`
- 请求方式：`POST`
- 参数说明：

|    参数     |    中文    | 是否必须 |  类型  |     备注      | 案例 |
| :---------: | :--------: | :------: | :----: | :-----------: | :--: |
|    page     |    页数    |    否    |  int   | 传空默认第1页 |      |
|  per_page   | 每页数据量 |    否    |  int   | 传空默认10条  |      |
| diseaseName |  病种名称  |    是    | string |               |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "categoryName": "传染病",
            "diseaseId": 5,
            "diseaseName": "狂犬病1"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 7,
            "diseaseName": "狂犬病3"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 8,
            "diseaseName": "狂犬病4"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 9,
            "diseaseName": "狂犬病5"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 10,
            "diseaseName": "狂犬病6"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 11,
            "diseaseName": "狂犬病7"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 12,
            "diseaseName": "狂犬病8"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 13,
            "diseaseName": "狂犬病9"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 14,
            "diseaseName": "狂犬病10"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 15,
            "diseaseName": "狂犬病11"
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有病种"
}
```

### 病种查询

- 接口URL：`/disease/search`
- 请求方式：`POST`
- 参数说明：

|    参数    |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :--------: | :------: | :------: | :----: | :--: | :--: |
| diseaeName | 病种名称 |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "caseNum": 1,
            "categoryName": "传染病"
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "目前没有该病种，请再次确认"
}
```

## 病例管理

### 添加病例

- 接口URL：`/case/add`
- 请求方式：`POST`
- 参数说明：

|    参数     |     中文     | 是否必须 | 类型 | 备注 |    案例    |
| :---------: | :----------: | :------: | :--: | :--: | :--------: |
|  caseName   |   病例名称   |    是    |      |      | 小王的案例 |
| animalName  |   宠物名称   |    是    |      |      |    小王    |
| diseaseName |   病种名称   |    是    |      |      |   狂犬病   |
|  caseInfo   |   文字简介   |    是    |      |      |    怕水    |
|  videoUrl   |   视频信息   |    是    |      |      |    test    |
|  imageUrl   |   图片信息   |    是    |      |      |    test    |
| processUrl1 | 流程图片信息 |    是    |      |      |            |
| processUrl2 | 流程图片信息 |    是    |      |      |            |
| processUrl3 | 流程图片信息 |    是    |      |      |            |
|    info1    | 流程文字信息 |    是    |      |      |            |
|    info2    | 流程文字信息 |    是    |      |      |            |
|    info3    | 流程文字信息 |    是    |      |      |            |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "animalName": "小李",
            "caseInfo": "病例信息",
            "caseName": "小李的宠物",
            "diseaseName": "狂犬病",
            "imageUrl": "test",
            "processUrl1": "test",
            "processUrl2": "test",
            "processUrl3": "test",
            "videoUrl": "test"
        }
    ],
    "msg": "添加成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "相同病例已存在，请再换一个试试"
}
```

### 删除病例

- 接口URL：`/case/delete`
- 请求方式：`POST`
- 参数说明：

|  参数  |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :----: | :------: | :------: | :----: | :--: | :--: |
| caseId | 分类名称 |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "animalName": "小李",
            "caseInfo": "病例信息",
            "caseName": "小李的宠物",
            "diseaseName": "狂犬病",
            "imageUrl": "test",
            "processUrl1": "test",
            "processUrl2": "test",
            "processUrl3": "test",
            "videoUrl": "test"
        }
    ],
    "msg": "删除成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "目前没有该病例，请再次确认"
}
```

### 分页返回病例

- 接口URL：`/case/list`
- 请求方式：`POST`
- 参数说明：

|    参数     |    中文    | 是否必须 |  类型  |        备注         | 案例 |
| :---------: | :--------: | :------: | :----: | :-----------------: | :--: |
|    page     |    页数    |    否    |  int   |    传空默认第1页    |      |
|  per_page   | 每页数据量 |    否    |  int   |    传空默认10条     |      |
| diseaseName |  病种名称  |    否    | string | 传“all”默认全部分类 |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "animalName": "小李",
            "caseInfo": "发炎",
            "caseName": "小李的案例",
            "diseaseName": "炎症",
            "imageUrl": "testtest",
            "processUrl1": null,
            "processUrl2": null,
            "processUrl3": null,
            "videoUrl": "test"
        },
        {
            "animalName": "小明",
            "caseInfo": "怕水",
            "caseName": "小明的案例",
            "diseaseName": "狂犬病",
            "imageUrl": "testtest",
            "processUrl1": null,
            "processUrl2": null,
            "processUrl3": null,
            "videoUrl": "test"
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有病例"
}
```

### 分页返回模糊查询病例

- 接口URL：`/case/fuzzy`
- 请求方式：`POST`
- 参数说明：

|   参数   |    中文    | 是否必须 |  类型  |     备注      | 案例 |
| :------: | :--------: | :------: | :----: | :-----------: | :--: |
|   page   |    页数    |    否    |  int   | 传空默认第1页 |      |
| per_page | 每页数据量 |    否    |  int   | 传空默认10条  |      |
| caseName |  病例名称  |    是    | string |               |  小  |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "animalName": "小李",
            "caseInfo": "发炎",
            "caseName": "小李的案例",
            "diseaseName": "炎症",
            "imageUrl": "testtest",
            "processUrl1": null,
            "processUrl2": null,
            "processUrl3": null,
            "videoUrl": "test"
        },
        {
            "animalName": "小明",
            "caseInfo": "怕水",
            "caseName": "小明的案例",
            "diseaseName": "狂犬病",
            "imageUrl": "testtest",
            "processUrl1": null,
            "processUrl2": null,
            "processUrl3": null,
            "videoUrl": "test"
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有病例"
}
```

### 为病例添加药品

- 接口URL：`/case/addCaseMedicine`
- 请求方式：`POST`
- 参数说明：

|     参数     |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :----------: | :------: | :------: | :----: | :--: | :--: |
|    caseId    |  病例Id  |    是    | string |      |      |
| medicineName | 药品名称 |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "caseId": "21",
            "medicineName": "药品1"
        }
    ],
    "msg": "病例添加药品成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "没有这种药品，请确认后再添加"
}
```

## 宠物管理

### 添加宠物

- 接口URL：`/animal/add`
- 请求方式：`POST`
- 参数说明：

|    参数    |   中文   | 是否必须 |  类型  | 备注 | 案例  |
| :--------: | :------: | :------: | :----: | :--: | :---: |
| animalName | 宠物名称 |    是    | string |      | 小明  |
|    age     |   年龄   |    是    |  int   |      |  10   |
|  breathe   |   呼吸   |    是    |  int   |      |  10   |
|   temper   |   体温   |    是    | double |      |  10   |
| heartRate  |   心率   |    是    | string |      | 10~20 |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "age": "5",
            "animalName": "小白",
            "breathe": "30",
            "heartRate": "20~30",
            "temper": "20.5"
        }
    ],
    "msg": "添加成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "相同名字已存在，请再换一个试试"
}
```

### 删除宠物

- 接口URL：`/animal/delete`
- 请求方式：`POST`
- 参数说明：

|   参数   |  中文  | 是否必须 |  类型  | 备注 | 案例 |
| :------: | :----: | :------: | :----: | :--: | :--: |
| animalId | 宠物ID |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "age": 5,
            "animalId": 6,
            "animalName": "新小白",
            "breathe": 30,
            "heartRate": "20~30",
            "temper": 20.5000000000
        }
    ],
    "msg": "删除宠物成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "目前没有该宠物，请再次确认"
}
```

### 更新宠物

- 接口URL：`/animal/update`
- 请求方式：`POST`
- 参数说明：

|    参数    |   中文   | 是否必须 |  类型  | 备注 | 案例  |
| :--------: | :------: | :------: | :----: | :--: | :---: |
|  animalId  |  宠物Id  |    是    | string |      |       |
| animalName | 宠物名称 |    是    | string |      | 小明  |
|    age     |   年龄   |    是    |  int   |      |  10   |
|  breathe   |   呼吸   |    是    |  int   |      |  10   |
|   temper   |   体温   |    是    | double |      |  10   |
| heartRate  |   心率   |    是    | string |      | 10~20 |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "age": "5",
            "animalId": "6",
            "animalName": "新小白",
            "breathe": "30",
            "heartRate": "20~30",
            "temper": "20.5"
        }
    ],
    "msg": "修改宠物成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "相同宠物名已经存在，请换一个再试试。"
}
```

### 分页返回宠物

- 接口URL：`/animal/list`
- 请求方式：`POST`
- 参数说明：

|   参数   |    中文    | 是否必须 | 类型 |     备注      | 案例 |
| :------: | :--------: | :------: | :--: | :-----------: | :--: |
|   page   |    页数    |    否    | int  | 传空默认第1页 |      |
| per_page | 每页数据量 |    否    | int  | 传空默认10条  |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "age": 10,
            "animalId": 1,
            "animalName": "小王",
            "breathe": 10,
            "heartRate": "10",
            "temper": 10.0000000000
        },
        {
            "age": 10,
            "animalId": 2,
            "animalName": "小张",
            "breathe": 10,
            "heartRate": "10",
            "temper": 10.0000000000
        },
        {
            "age": 10,
            "animalId": 3,
            "animalName": "小赵",
            "breathe": 10,
            "heartRate": "10",
            "temper": 10.0000000000
        },
        {
            "age": 10,
            "animalId": 4,
            "animalName": "小孙",
            "breathe": 10,
            "heartRate": "10",
            "temper": 10.0000000000
        },
        {
            "age": 10,
            "animalId": 5,
            "animalName": "小李",
            "breathe": 10,
            "heartRate": "10",
            "temper": 10.0000000000
        },
        {
            "age": 5,
            "animalId": 6,
            "animalName": "小白",
            "breathe": 30,
            "heartRate": "20~30",
            "temper": 20.5000000000
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有宠物"
}
```

### 分页返回模糊查询宠物

- 接口URL：`/animal/fuzzy`
- 请求方式：`POST`
- 参数说明：

|    参数    |    中文    | 是否必须 |  类型  |     备注      | 案例 |
| :--------: | :--------: | :------: | :----: | :-----------: | :--: |
|    page    |    页数    |    否    |  int   | 传空默认第1页 |      |
|  per_page  | 每页数据量 |    否    |  int   | 传空默认10条  |      |
| animalName |  宠物名称  |    是    | string |               |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "age": 10,
            "animalId": 4,
            "animalName": "小孙",
            "breathe": 10,
            "heartRate": "10",
            "temper": 10.0000000000
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有"
}
```

## 住院管理

### 添加住院

- 接口URL：`/hospital/add`
- 请求方式：`POST`
- 参数说明：

|   参数   |   中文   | 是否必须 |  类型  | 备注 |    案例    |
| :------: | :------: | :------: | :----: | :--: | :--------: |
| caseName | 病例名称 |    是    | string |      | 小明的病例 |
|   day    | 住院天数 |    是    |  int   |      |     10     |
|   pay    | 住院费用 |    是    |  int   |      |     10     |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "caseName": "小明的案例",
            "day": "3",
            "hospitalId": 2,
            "pay": "100"
        }
    ],
    "msg": "添加病例成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "目前已有该病例的住院记录"
}
```

### 删除住院

- 接口URL：`/hospital/delete`
- 请求方式：`POST`
- 参数说明：

|    参数    |  中文  | 是否必须 |  类型  | 备注 | 案例 |
| :--------: | :----: | :------: | :----: | :--: | :--: |
| hospitalId | 住院ID |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "caseName": "小李的案例",
            "day": 3,
            "hospitalId": 1,
            "pay": 100
        }
    ],
    "msg": "删除住院成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "相同住院记录已经存在，请换一个再试试。"
}
```

### 更新住院

- 接口URL：`/hospital/update`
- 请求方式：`POST`
- 参数说明：

|    参数    |   中文   | 是否必须 |  类型  | 备注 |    案例    |
| :--------: | :------: | :------: | :----: | :--: | :--------: |
| hospitalId |  住院Id  |    是    | string |      |            |
|  caseName  | 病例名称 |    是    | string |      | 小明的病例 |
|    day     | 住院天数 |    是    |  int   |      |     10     |
|    pay     | 住院费用 |    是    |  int   |      |     10     |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "caseName": "小李的案例",
            "day": "3",
            "hospitalId": "1",
            "pay": "100"
        }
    ],
    "msg": "修改住院成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "相同宠物名已经存在，请换一个再试试。"
}
```

### 分页返回住院

- 接口URL：`/hospital/list`
- 请求方式：`POST`
- 参数说明：

|   参数   |    中文    | 是否必须 | 类型 |     备注      | 案例 |
| :------: | :--------: | :------: | :--: | :-----------: | :--: |
|   page   |    页数    |    否    | int  | 传空默认第1页 |      |
| per_page | 每页数据量 |    否    | int  | 传空默认10条  |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "caseName": "小李的案例",
            "day": 3,
            "hospitalId": 1,
            "pay": 100
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有住院记录"
}
```



# 科室模块

## 科室管理

### 添加科室

- 接口URL：`/room/add`
- 请求方式：`POST`
- 参数说明：

|   参数   |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :------: | :------: | :------: | :----: | :--: | :--: |
| roomName | 科室名称 |    是    | string |      |      |
|  intro   |   简介   |    是    | string |      |      |
| employee |  负责人  |    是    | string |      |      |
|  imgUrl  | 科室图片 |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "employee": "负责人小孙",
            "imgUrl": "test",
            "intro": "科室简介",
            "roomId": 10,
            "roomName": "科室4"
        }
    ],
    "msg": "添加成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "相同科室名已存在，请再换一个试试"
}
```

### 删除科室

- 接口URL：`/room/delete`
- 请求方式：`POST`
- 参数说明：

|  参数  |  中文  | 是否必须 |  类型  | 备注 | 案例 |
| :----: | :----: | :------: | :----: | :--: | :--: |
| roomId | 科室ID |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "employee": "负责人小孙",
            "imgUrl": "test",
            "intro": "科室简介",
            "roomId": 10,
            "roomName": "科室4"
        }
    ],
    "msg": "删除成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "目前没有该科室，请再次确认"
}
```

### 更新科室

- 接口URL：`/room/update`
- 请求方式：`POST`
- 参数说明：

|    参数     |    中文    | 是否必须 |  类型  | 备注 | 案例 |
| :---------: | :--------: | :------: | :----: | :--: | :--: |
| roomNameNew | 科室新名称 |    是    | string |      |      |
|  employee   |   负责人   |    否    | string |      |      |
|    intro    |    简介    |    否    | string |      |      |
|   imgUrl    |  科室图片  |    否    | string |      |      |
|   roomId    |   科室ID   |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "employee": "小王",
            "imgUrl": "pictureTest",
            "intro": "科室简介啦啦啦",
            "roomId": "9",
            "roomName": "新的科室111"
        }
    ],
    "msg": "修改成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "相同科室名已经存在，请换一个再试试。"
}
```

### 分页返回科室

- 接口URL：`/room/list`
- 请求方式：`POST`
- 参数说明：

|   参数   |    中文    | 是否必须 | 类型 |     备注      | 案例 |
| :------: | :--------: | :------: | :--: | :-----------: | :--: |
|   page   |    页数    |    否    | int  | 不传默认第1页 |      |
| per_page | 每页数据量 |    否    | int  | 不传默认10条  |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "employee": "小王",
            "imgUrl": "pictureTest",
            "intro": "科室简介啦啦啦",
            "roomId": 6,
            "roomName": "新的科室"
        },
        {
            "employee": "负责人小王",
            "imgUrl": "test",
            "intro": "科室简介",
            "roomId": 7,
            "roomName": "科室2"
        },
        {
            "employee": "负责人小王",
            "imgUrl": "test",
            "intro": "科室简介",
            "roomId": 8,
            "roomName": "科室1"
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有科室"
}
```

# 收费模块

## 药品管理

### 添加药品

- 接口URL：`/medicine/add`
- 请求方式：`POST`
- 参数说明：

|   参数   |   中文   | 是否必须 |  类型  |         备注         | 案例 |
| :------: | :------: | :------: | :----: | :------------------: | :--: |
|   name   | 药品名称 |    是    | string |                      |      |
|  intro   |   简介   |    是    | string |                      |      |
| storage  |   库存   |    是    |  int   |                      |      |
|  imgUrl  | 药品图片 |    是    | string |                      |      |
|   pay    |   价格   |    是    |  int   |                      |      |
| roomName | 科室名称 |    是    | string |                      |      |
|   type   |   种类   |    是    | string | 药品、疫苗、收费项目 |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "imgUrl": "test",
            "intro": "药品简介",
            "name": "消炎药",
            "pay": "10",
            "roomName": "科室1",
            "storage": "10",
            "type": "药品"
        }
    ],
    "msg": "药品添加成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "相同药品名已存在，请再换一个试试"
}
```

### 删除药品

- 接口URL：`/medicine/delete`
- 请求方式：`POST`
- 参数说明：

|    参数    |  中文  | 是否必须 |  类型  | 备注 | 案例 |
| :--------: | :----: | :------: | :----: | :--: | :--: |
| medicineId | 药品ID |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "imgUrl": "test",
            "intro": "药品简介",
            "medicineId": "16",
            "name": "最新药品",
            "pay": 10,
            "roomName": "科室1",
            "storage": 5,
            "type": "药品"
        }
    ],
    "msg": "删除成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "目前没有该药品，请再次确认"
}
```

### 更新药品

- 接口URL：`/medicine/update`
- 请求方式：`POST`
- 参数说明：

|    参数    |   中文   | 是否必须 |  类型  |         备注         | 案例 |
| :--------: | :------: | :------: | :----: | :------------------: | :--: |
|  nameNew   | 药品名称 |    是    | string |                      |      |
|   intro    |   简介   |    是    | string |                      |      |
|  storage   |   库存   |    是    |  int   |                      |      |
|   imgUrl   | 药品图片 |    是    | string |                      |      |
|    pay     |   价格   |    是    |  int   |                      |      |
| medicineId |  药品ID  |    是    | string |                      |      |
|  roomName  | 科室名称 |    是    | string |                      |      |
|    type    |   种类   |    是    | string | 药品、疫苗、收费项目 |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "imgUrl": "test",
            "intro": "药品简介",
            "medicineId": "16",
            "name": "最新药品",
            "pay": "10",
            "roomName": "科室1",
            "storage": "5",
            "type": "药品"
        }
    ],
    "msg": "修改药品成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "相同药品名已经存在，请换一个再试试。"
}
```

### 分页返回药品

- 接口URL：`/medicine/list`
- 请求方式：`POST`
- 参数说明：

|   参数   |    中文    | 是否必须 |  类型  |         备注         | 案例 |
| :------: | :--------: | :------: | :----: | :------------------: | :--: |
|   page   |    页数    |    否    |  int   |    传空默认第1页     |      |
| per_page | 每页数据量 |    否    |  int   |     传空默认10条     |      |
| roomName |  科室名称  |    否    | string | 传“all”默认全部返回  |      |
|   type   |  药品种类  |    是    | string | 根据种类不同实现管理 |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "imgUrl": "test",
            "intro": "简介",
            "medicineId": 18,
            "name": "药品1",
            "pay": 10,
            "roomName": "科室2",
            "storage": 10,
            "type": "药品"
        },
        {
            "imgUrl": "test",
            "intro": "简介",
            "medicineId": 19,
            "name": "药品2",
            "pay": 10,
            "roomName": "科室2",
            "storage": 10,
            "type": "药品"
        },
        {
            "imgUrl": "test",
            "intro": "简介",
            "medicineId": 20,
            "name": "药品3",
            "pay": 10,
            "roomName": "科室1",
            "storage": 10,
            "type": "药品"
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有药品"
}
```

### 分页返回模糊查询药品

- 接口URL：`/medicine/fuzzy`
- 请求方式：`POST`
- 参数说明：

|     参数     |    中文    | 是否必须 |  类型  |         备注         | 案例 |
| :----------: | :--------: | :------: | :----: | :------------------: | :--: |
|     page     |    页数    |    否    |  int   |    传空默认第1页     |      |
|   per_page   | 每页数据量 |    否    |  int   |     传空默认10条     |      |
| medicineName |  药品名称  |    是    | string |                      |      |
|     type     |  药品类别  |    是    | string | 药品、疫苗、化验项目 |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "imgUrl": "test",
            "intro": "药品简介",
            "medicineId": 17,
            "name": "最新药品",
            "pay": 10,
            "roomName": "科室1",
            "storage": 5,
            "type": "药品"
        },
        {
            "imgUrl": "test",
            "intro": "简介",
            "medicineId": 18,
            "name": "药品1",
            "pay": 10,
            "roomName": "科室2",
            "storage": 10,
            "type": "药品"
        },
        {
            "imgUrl": "test",
            "intro": "简介",
            "medicineId": 19,
            "name": "药品2",
            "pay": 10,
            "roomName": "科室2",
            "storage": 10,
            "type": "药品"
        },
        {
            "imgUrl": "test",
            "intro": "简介",
            "medicineId": 20,
            "name": "药品3",
            "pay": 10,
            "roomName": "科室1",
            "storage": 10,
            "type": "药品"
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有药品"
}
```

## 收费管理

### 分页返回费用

- 接口URL：`/fee/list`
- 请求方式：`POST`
- 参数说明：

|   参数   |    中文    | 是否必须 | 类型 |     备注      | 案例 |
| :------: | :--------: | :------: | :--: | :-----------: | :--: |
|   page   |    页数    |    否    | int  | 传空默认第1页 |      |
| per_page | 每页数据量 |    否    | int  | 传空默认10条  |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "caseId": 21,
            "caseName": "小李的案例",
            "count": 230,
            "usedMedicine": {
                "住院费用": 200,
                "药品1": 2,
                "药品2": 1
            }
        },
        {
            "caseId": 23,
            "caseName": "小明的案例",
            "count": 100,
            "usedMedicine": {
                "住院费用": 100
            }
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有费用"
}
```

# 统计模块

## 首页统计

### 返回病种、病例、测试总数

- 接口URL：`/count`
- 请求方式：`POST`
- 参数说明：

| 参数 | 中文 | 是否必须 | 类型 | 备注 | 案例 |
| :--: | :--: | :------: | :--: | :--: | :--: |
|  无  |      |          |      |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "caseCount": 2,
            "diseaseCount": 14,
            "testCount": 3
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
没有失败
```
