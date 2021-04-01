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

### 查询试题

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
            "choiceA": null,
            "choiceB": null,
            "choiceC": null,
            "choiceD": null,
            "diseaseName": null,
            "questionInfo": "题目1",
            "score": null
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
    "code": 200,
    "data": [],
    "msg": "查询成功"
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

### 查询分类

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
            "videoUrl": "test\n"
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

### 查询病例

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
            "videoUrl": "test\n"
        },
        {
            "animalName": "小李",
            "caseName": "小李的案例",
            "diseaseInfo": "怕水",
            "diseaseName": "狂犬病",
            "imageUrl": "test",
            "videoUrl": "test\n"
        },
        {
            "animalName": "小王",
            "caseName": "小王的案例",
            "diseaseInfo": "怕水",
            "diseaseName": "狂犬病",
            "imageUrl": "test",
            "videoUrl": "test\n"
        },
        {
            "animalName": "大王",
            "caseName": "大王的案例",
            "diseaseInfo": "怕水",
            "diseaseName": "狂犬病",
            "imageUrl": "testtest",
            "videoUrl": "test\n"
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": 200,
    "data": [],
    "msg": "查询成功"
}
```

## 疾病类

### 添加疾病

- 接口URL：`/disease/add`
- 请求方式：`POST`
- 参数说明：

|    参数     |   中文   | 是否必须 |  类型  | 备注 | 案例 |
| :---------: | :------: | :------: | :----: | :--: | :--: |
| diseaseName | 疾病名称 |    是    | string |      | 肺炎 |

- 返回参数（成功）

```json
{
    "code": 200,
    "data": [
        {
            "diseaseName": "感染"
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

### 查询疾病

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
            "diseaseId": 1,
            "diseaseName": "狂犬病"
        },
        {
            "diseaseId": 2,
            "diseaseName": "肺炎"
        },
        {
            "diseaseId": 3,
            "diseaseName": "感染"
        }
    ],
    "msg": "查询成功"
}
```

- 返回参数（失败）

```json
{
    "code": 200,
    "data": [],
    "msg": "查询成功"
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

### 查询宠物

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
    "msg": "相同名字已存在，请再换一个试试"
}
```