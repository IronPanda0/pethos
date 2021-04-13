# 后台登录

## 管理员登录

|     参数     |   中文   | 是否必须 |  类型  | 备注 | 
| :----------:| :------: | :------: | :----: | :--: | 
|   username  |   用户名  |    是    | string |      |
|   password  |   密码    |    是    | string |      |

- 接口URL：`/mlogin`
- 请求方式：`POST`
- 参数说明：

- 返回参数(成功)

```json
{
    "code": 200,
    "data":
        {
            "token": "令牌"
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

## 管理员添加

|     参数     |   中文   | 是否必须 |  类型  | 备注 | 
| :----------:| :------: | :------: | :----: | :--: | 
|   username  |   用户名  |    是    | string |      |
|   password  |   密码    |    是    | string |      |

- 接口URL：`/mregister`
- 请求方式：`POST`
- 参数说明：

- 返回参数(成功)

```json
{
    "code": 200,
    "data": 
        {
            "token": "令牌"
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


# 测试模块

## 试题类

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

<<<<<<< HEAD
<<<<<<< HEAD
### 查询试题
=======
### 返回全部试题
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
### 返回全部试题
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af

- 接口URL：`/question/list`
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
            "answer": 1,
            "choiceA": "选A",
            "choiceB": "选B",
            "choiceC": "选C",
            "choiceD": "选D",
            "diseaseName": "狂犬病",
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
            "questionInfo": "题干题干",
            "score": null
        },
        {
            "answer": 1,
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "狂犬病",
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

### 查询试题

- 接口URL：`/question/search`
- 请求方式：`POST`
- 参数说明：

|    参数     |   中文   | 是否必须 |  类型  | 备注 |  案例  |
| :---------: | :------: | :------: | :----: | :--: | :----: |
| diseaseName | 病种名称 |    是    | string |      | 狂犬病 |

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
            "questionInfo": "题干题干",
            "score": null
        },
        {
            "answer": 1,
            "choiceA": "选项",
            "choiceB": "选项",
            "choiceC": "选项",
            "choiceD": "选项",
            "diseaseName": "狂犬病",
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
            "questionInfo": "题干题干题干题干题干",
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
    "msg": "查询失败，目前该病种没有试题"
}
```

## 试卷类

## 考试类

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

### 返回全部考试

- 接口URL：`/test/list`
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
            "beginTime": "Mon, 01 Mar 2021 08:00:00 GMT",
            "diseaseName": "狂犬病",
            "endTime": "Mon, 01 Mar 2021 10:00:00 GMT",
            "paperName": "期中考试狂犬病试卷",
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

## 分类类

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

<<<<<<< HEAD
<<<<<<< HEAD
### 查询分类
=======
### 返回全部分类
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
### 返回全部分类
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af

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
    "code": 200,
    "data": [],
    "msg": "查询成功"
}
```

=======
=======
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有分类"
}
```

### 更新病例

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

### 删除病例

<<<<<<< HEAD
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
## 病例类

### 添加病例

- 接口URL：`/case/add`
- 请求方式：`POST`
- 参数说明：

|     参数     |   中文   | 是否必须 | 类型 | 备注 |    案例    |
| :----------: | :------: | :------: | :--: | :--: | :--------: |
| categoryName | 病例名称 |    是    |      |      | 小王的案例 |
|  animalName  | 宠物名称 |    是    |      |      |    小王    |
| diseaseName  | 病种名称 |    是    |      |      |   狂犬病   |
| diseaseInfo  | 文字简介 |    是    |      |      |    怕水    |
|   videoUrl   | 视频信息 |    是    |      |      |    test    |
|   imageUrl   | 图片信息 |    是    |      |      |    test    |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "animalName": "大王",
            "caseName": "大王的案例",
            "diseaseInfo": "怕水",
            "diseaseName": "狂犬病",
            "imageUrl": "testtest",
<<<<<<< HEAD
<<<<<<< HEAD
            "videoUrl": "test\n"
=======
            "videoUrl": "test"
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
            "videoUrl": "test"
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
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

<<<<<<< HEAD
<<<<<<< HEAD
### 查询病例
=======
### 返回全部病例
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
### 返回全部病例
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af

- 接口URL：`/case/list`
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
            "animalName": "小郑",
            "caseName": "小郑的案例",
            "diseaseInfo": "怕水",
            "diseaseName": "狂犬病",
            "imageUrl": "test",
<<<<<<< HEAD
<<<<<<< HEAD
            "videoUrl": "test\n"
=======
            "videoUrl": "test"
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
            "videoUrl": "test"
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
        },
        {
            "animalName": "小李",
            "caseName": "小李的案例",
            "diseaseInfo": "怕水",
            "diseaseName": "狂犬病",
            "imageUrl": "test",
<<<<<<< HEAD
<<<<<<< HEAD
            "videoUrl": "test\n"
=======
            "videoUrl": "test"
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
            "videoUrl": "test"
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
        },
        {
            "animalName": "小王",
            "caseName": "小王的案例",
            "diseaseInfo": "怕水",
            "diseaseName": "狂犬病",
            "imageUrl": "test",
<<<<<<< HEAD
<<<<<<< HEAD
            "videoUrl": "test\n"
=======
            "videoUrl": "test"
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
            "videoUrl": "test"
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
        },
        {
            "animalName": "大王",
            "caseName": "大王的案例",
            "diseaseInfo": "怕水",
            "diseaseName": "狂犬病",
            "imageUrl": "testtest",
<<<<<<< HEAD
<<<<<<< HEAD
            "videoUrl": "test\n"
=======
            "videoUrl": "test"
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
            "videoUrl": "test"
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
<<<<<<< HEAD
<<<<<<< HEAD
    "code": 200,
    "data": [],
    "msg": "查询成功"
}
```

## 疾病类

### 添加疾病
=======
=======
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有病例"
}
```

## 病种类

### 添加病种
<<<<<<< HEAD
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af

- 接口URL：`/disease/add`
- 请求方式：`POST`
- 参数说明：

<<<<<<< HEAD
<<<<<<< HEAD
|    参数     |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :---------: | :------: | :------: | :----: | :--: | :--: |
| diseaseName | 疾病名称 |    是    | string |      | 肺炎 |
=======
=======
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
|     参数     |   中文   | 是否必须 |  类型  | 备注 |  案例   |
| :----------: | :------: | :------: | :----: | :--: | :-----: |
| diseaseName  | 疾病名称 |    是    | string |      | 传染111 |
| categoryName | 分类名称 |    是    | string |      | 传染病  |
<<<<<<< HEAD
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
<<<<<<< HEAD
<<<<<<< HEAD
            "diseaseName": "感染"
=======
            "categoryName": "传染病",
            "diseaseName": "传染111"
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
            "categoryName": "传染病",
            "diseaseName": "传染111"
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
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

<<<<<<< HEAD
<<<<<<< HEAD
### 查询疾病
=======
=======
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
### 查询病种

- 接口URL：`/disease/search`
- 请求方式：`POST`
- 参数说明：

|     参数     |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :----------: | :------: | :------: | :----: | :--: | :--: |
| categoryName | 分类名称 |    是    | string |      |      |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "categoryName": "传染病",
            "diseaseId": 1,
            "diseaseName": "狂犬病"
        },
        {
            "categoryName": "传染病",
            "diseaseId": 2,
            "diseaseName": "肺炎"
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

### 返回全部病种
<<<<<<< HEAD
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af

- 接口URL：`/disease/list`
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
            "categoryName": "传染病",
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
            "categoryName": "传染病",
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
            "diseaseId": 1,
            "diseaseName": "狂犬病"
        },
        {
<<<<<<< HEAD
<<<<<<< HEAD
=======
            "categoryName": "传染病",
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
            "categoryName": "传染病",
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
            "diseaseId": 2,
            "diseaseName": "肺炎"
        },
        {
<<<<<<< HEAD
<<<<<<< HEAD
            "diseaseId": 3,
            "diseaseName": "感染"
=======
            "categoryName": "皮肤病",
            "diseaseId": 3,
            "diseaseName": "脱毛"
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
            "categoryName": "皮肤病",
            "diseaseId": 3,
            "diseaseName": "脱毛"
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
<<<<<<< HEAD
<<<<<<< HEAD
    "code": 200,
    "data": [],
    "msg": "查询成功"
=======
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有疾病"
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
    "code": -1,
    "data": {},
    "msg": "查询失败，目前没有疾病"
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
}
```

## 宠物类

### 添加宠物

- 接口URL：`/animal/add`
- 请求方式：`POST`
- 参数说明：

|    参数    |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :--------: | :------: | :------: | :----: | :--: | :--: |
| animalName | 宠物名称 |    是    | string |      | 小明 |
|    age     |   年龄   |    是    |  int   |      |  10  |
|  breathe   |   呼吸   |    是    |  int   |      |  10  |
|   temper   |   体温   |    是    | double |      |  10  |
| heartRate  |   心率   |    是    |  int   |      |  10  |

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

<<<<<<< HEAD
<<<<<<< HEAD
### 查询宠物
=======
### 返回全部宠物
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
### 返回全部宠物
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af

- 接口URL：`/disease/list`
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
<<<<<<< HEAD
<<<<<<< HEAD
    "msg": "相同名字已存在，请再换一个试试"
=======
    "msg": "查询失败，目前没有宠物"
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
    "msg": "查询失败，目前没有宠物"
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
}
```