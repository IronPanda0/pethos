

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
            "duty": "什么的干活",
            "process": "流程1，2，3",
            "role": "医师",
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

|   参数   |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :------: | :------: | :------: | :----: | :--: | :--: |
| userName | 用户名称 |    是    | string |      |      |
|   role   |   角色   |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "role": "更新测试",
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
            "duty": "什么的干活",
            "process": "流程1，2，3",
            "role": "更新测试",
            "userName": "小王"
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
            "answer": "1",
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "狂犬病",
            "questionInfo": "题干题干题干题干题干",
            "score": "10"
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
    "msg": "相同题干已存在，请再换一个试试"
}
```

### 删除试题

- 接口URL：`/question/delete`
- 请求方式：`POST`
- 参数说明：

|    参数    |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :--------: | :------: | :------: | :----: | :--: | :--: |
| questionId | 用户名称 |    是    | string |      |      |
|    role    |   角色   |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "role": "更新测试",
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

### 分页返回试题

- 接口URL：`/question/list`
- 请求方式：`POST`
- 参数说明：

|    参数     |    中文    | 是否必须 |  类型  |         备注         | 案例 |
| :---------: | :--------: | :------: | :----: | :------------------: | :--: |
|    page     |    页数    |    否    |  int   |    不传默认第1页     |      |
|  per_page   | 每页数据量 |    否    |  int   |     不传默认10条     |      |
| diseaseName |  病种名称  |    否    | string | 不传默认返回全部试题 |      |

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

|   参数    |   中文   | 是否必须 |  类型  | 备注 |        案例        |
| :-------: | :------: | :------: | :----: | :--: | :----------------: |
| paperName | 试卷名称 |    是    | string |      | 期末考试狂犬病试卷 |

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

## 考试管理

### 添加考试

- 接口URL：`/test/add`
- 请求方式：`POST`
- 参数说明：

|    参数     |   中文   | 是否必须 |  类型  | 备注 |        案例        |
| :---------: | :------: | :------: | :----: | :--: | :----------------: |
|  testName   | 考试名称 |    是    | string |      |      期末考试      |
| diseaseName | 相关病种 |    是    | string |      |       狂犬病       |
|  paperName  | 试卷名称 |    是    | string |      | 期末考试狂犬病试卷 |
|  beginTime  | 考试时间 |    是    | string |      |   20210301 8:00    |
|   endTime   | 结束时间 |    是    | string |      |   20210301 10:00   |

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

### 删除考试

- 接口URL：`/test/delete`
- 请求方式：`POST`
- 参数说明：

|   参数   |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :------: | :------: | :------: | :----: | :--: | :--: |
| testName | 考试名称 |    否    | string |      |      |

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

|    参数     |    中文    | 是否必须 |  类型  |         备注         | 案例 |
| :---------: | :--------: | :------: | :----: | :------------------: | :--: |
|    page     |    页数    |    否    |  int   |    不传默认第1页     |      |
|  per_page   | 每页数据量 |    否    |  int   |     不传默认10条     |      |
| diseaseName |  病种名称  |    否    | string | 不传默认返回全部考试 |      |

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
        },
        {
            "beginTime": "Mon, 01 Mar 2021 08:00:00 GMT",
            "diseaseName": "狂犬病",
            "endTime": "Mon, 01 Mar 2021 10:00:00 GMT",
            "paperName": "期末中考试狂犬病试卷",
            "testId": 2,
            "testName": "期末考试"
        },
        {
            "beginTime": "Mon, 01 Mar 2021 08:00:00 GMT",
            "diseaseName": "狂犬病",
            "endTime": "Mon, 01 Mar 2021 10:00:00 GMT",
            "paperName": "入学中考试狂犬病试卷",
            "testId": 3,
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

|      参数       |   中文   | 是否必须 |  类型  | 备注 |    案例    |
| :-------------: | :------: | :------: | :----: | :--: | :--------: |
| categoryNameNew | 分类名称 |    是    | string |      | 呼吸道疾病 |
| categoryNameOld | 分类名称 |    是    | string |      |   传染病   |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "categoryName": "呼吸道疾病"
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

## 病例管理

### 添加病例

- 接口URL：`/case/add`
- 请求方式：`POST`
- 参数说明：

|     参数     |   中文   | 是否必须 | 类型 | 备注 |    案例    |
| :----------: | :------: | :------: | :--: | :--: | :--------: |
| categoryName | 病例名称 |    是    |      |      | 小王的案例 |
|  animalName  | 宠物名称 |    是    |      |      |    小王    |
| diseaseName  | 病种名称 |    是    |      |      |   狂犬病   |
|   caseInfo   | 文字简介 |    是    |      |      |    怕水    |
|   videoUrl   | 视频信息 |    是    |      |      |    test    |
|   imageUrl   | 图片信息 |    是    |      |      |    test    |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "animalName": "大王",
            "caseInfo": "怕水",
            "caseName": "大王的案例",
            "diseaseName": "狂犬病",
            "imageUrl": "testtest",
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
    "msg": "相同题干已存在，请再换一个试试"
}
```

### 删除病例

- 接口URL：`/case/delete`
- 请求方式：`POST`
- 参数说明：

|   参数    |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :-------: | :------: | :------: | :----: | :--: | :--: |
| casesName | 分类名称 |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "animalName": "小王",
            "caseInfo": "怕水",
            "caseName": "小王的案例",
            "diseaseName": "狂犬病",
            "imageUrl": "testtest",
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

|    参数     |    中文    | 是否必须 |  类型  |       备注       | 案例 |
| :---------: | :--------: | :------: | :----: | :--------------: | :--: |
|    page     |    页数    |    否    |  int   |  不传默认第1页   |      |
|  per_page   | 每页数据量 |    否    |  int   |   不传默认10条   |      |
| diseaseName |  病种名称  |    否    | string | 不传默认全部分类 |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "animalName": "小王",
            "caseInfo": "怕水",
            "caseName": "小王的案例",
            "diseaseName": "狂犬病",
            "imageUrl": "testtest",
            "videoUrl": "test"
        },
        {
            "animalName": "小明",
            "caseInfo": "怕水",
            "caseName": "小明的案例",
            "diseaseName": "狂犬病",
            "imageUrl": "testtest",
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

|    参数     |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :---------: | :------: | :------: | :----: | :--: | :--: |
| diseaseName | 分类名称 |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "categoryName": "传染病",
            "diseaseName": "狂犬病2"
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
    "msg": "目前没有该病种，请再次确认"
}
```

### 分页返回病种

- 接口URL：`/disease/list`
- 请求方式：`POST`
- 参数说明：

|     参数     |    中文    | 是否必须 |  类型  |     备注      | 案例 |
| :----------: | :--------: | :------: | :----: | :-----------: | :--: |
| categoryName |  分类名称  |    是    | string |               |      |
|     page     |    页数    |    否    |  int   | 不传默认第1页 |      |
|   per_page   | 每页数据量 |    否    |  int   | 不传默认10条  |      |

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
            "age": "10",
            "animalName": "小李",
            "breathe": "10",
            "heartRate": "10",
            "temper": "10"
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

### 返回全部宠物

- 接口URL：`/animal/list`
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
            "age": 10,
            "animalName": "小王",
            "breathe": 10,
            "heartRate": 10,
            "temper": 10.0000000000
        },
        {
            "age": 10,
            "animalName": "小张",
            "breathe": 10,
            "heartRate": 10,
            "temper": 10.0000000000
        },
        {
            "age": 10,
            "animalName": "小赵",
            "breathe": 10,
            "heartRate": 10,
            "temper": 10.0000000000
        },
        {
            "age": 10,
            "animalName": "小孙",
            "breathe": 10,
            "heartRate": 10,
            "temper": 10.0000000000
        },
        {
            "age": 10,
            "animalName": "小李",
            "breathe": 10,
            "heartRate": 10,
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
    "msg": "查询失败，目前没有宠物"
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

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "employee": "小王",
            "intro": "这是科室1的简介",
            "roomName": "科室1"
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
    "msg": "相同科室已存在，请再换一个试试"
}
```

### 删除科室

- 接口URL：`/room/delete`
- 请求方式：`POST`
- 参数说明：

|   参数   |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :------: | :------: | :------: | :----: | :--: | :--: |
| roomName | 科室名称 |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "employee": "小王",
            "intro": "这是科室2的简介",
            "roomName": "科室2"
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
    "msg": "目前没有该科室，请再次确认"
}
```

### 更新科室

- 接口URL：`/room/update`
- 请求方式：`POST`
- 参数说明：

|   参数   |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :------: | :------: | :------: | :----: | :--: | :--: |
| roomName | 科室名称 |    是    | string |      |      |
|  intro   |   简介   |    否    | string |      |      |
| employee |  负责人  |    否    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "employee": "小王",
            "intro": "这是科室2的简介",
            "roomName": "科室2"
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
    "msg": "科室已经存在，请换一个再试试。"
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
            "intro": "这是科室1的简介",
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



## 药品管理

### 添加药品

- 接口URL：`/medicine/add`
- 请求方式：`POST`
- 参数说明：

|     参数      |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :-----------: | :------: | :------: | :----: | :--: | :--: |
| medicineName  | 药品名称 |    是    | string |      |      |
| medicineIntro |   简介   |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "medicineIntro": "专治狂犬病",
            "medicineName": "狂犬病疫苗"
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
    "msg": "相同药品已存在，请再换一个试试"
}
```

### 删除药品

- 接口URL：`/medicine/delete`
- 请求方式：`POST`
- 参数说明：

|     参数     |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :----------: | :------: | :------: | :----: | :--: | :--: |
| medicineName | 药品名称 |    否    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "medicineIntro": "狂犬病特效药",
            "medicineName": "狂犬病新疫苗"
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

|     参数      |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :-----------: | :------: | :------: | :----: | :--: | :--: |
| medicineName  | 药品名称 |    是    | string |      |      |
| medicineIntro |   简介   |    否    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "medicineIntro": "狂犬病特效药",
            "medicineName": "狂犬病新疫苗"
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
    "msg": "药品已经存在，请换一个再试试。"
}
```

### 分页返回药品

- 接口URL：`/medicine/list`
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
            "medicineIntro": "专治传染病",
            "medicineName": "传染病疫苗"
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
