# shuchong
书虫小说后台，定义了前端所需的几个接口 https://api.doctoroyy.cf/
###  /book/getAll   获取小说列表

  - method: POST
  - 入参：
  ```
  	{"page":1,"pageSize":100} 
  ```
  
  - 出参： 
```
{
  "page": 1,
  "pageSize": 100,
  "total": 10,
  "data": [
    {
      "id": 1,
      "name": "苏厨",
      "tags": null,
      "description": "治大国如烹小鲜，因此，这是一个吃货治国的故事，从北宋皇佑四年开始……",
      "imgSrc": "https://www.xbiquge6.com/cover/85/85379/85379s.jpg",
      "author": "二子从周"
    },
    {
      "id": 2,
      "name": "圣墟（圣虚）",
      "tags": null,
      "description": "在破败中崛起，在寂灭中复苏。    沧海成尘，雷电枯竭，那一缕幽雾又一次临近大地，世间的枷锁被打开了，一个全新的世界就此揭开神秘的一角……",
      "imgSrc": "https://www.xbiquge6.com/cover/74/74821/74821s.jpg",
      "author": "辰东"
    },
  ]
}
```
### /book/catalog 获取小说目录详情
  - method: POST
  - 入参：
 ```
 {"id": 1}
 ```
 
  - 出参：
```
{
  "code": 0,
  "data": {
    "chapters": [
      {
        "id": 2,
        "novel_id_id": 1,
        "no": 2,
        "name": "第二章 嘴炮堂哥",
        "context_url": "/85_85379/169915.html"
      }
    ],
    "bookInfo": {
      "id": 1,
      "name": "苏厨",
      "tags": null,
      "description": "治大国如烹小鲜，因此，这是一个吃货治国的故事，从北宋皇佑四年开始……",
      "imgSrc": "https://www.xbiquge6.com/cover/85/85379/85379s.jpg",
      "author": "二子从周"
    }
  }
}
```

### /book/chapter 获取小说章节详情
  - method: POST
  - 入参：
  ```
  {"id": 1,  "chapterno": 1}
  ```
  
  - 出参: 
```json
{
  "context": [
    "",
    "“啊！”",
    "柳乐儿本欲施法阻挡青色怪马，怎奈心神动摇下，体内法力运转不灵，口中不由发出一声惊呼。",
    "千钧一发之际，她只觉眼前一暗，却是柳石蓦然一步跨出，高大身躯挡在了身前，同时单手闪电般伸出，一把扣住了怪马如水桶般粗细的脖子，身体一侧，和青色怪马撞在了一起。",
    "“轰”的一声巨响！",
    "青色怪马在高昂嘶鸣声中，犹如撞在了一堵巨墙上，庞大身躯硬生生停在了原地，由于冲势过猛，甚至附近街道上的坚硬石板都被铁蹄踏得的碎石四溅。",
    "银色马车则在惯性作用下一头撞在了青色怪马后股上，偏侧的飞出书丈远去，又“砰”的重重落在地面上。",
    "此车虽然没有翻个顶朝天，但也车身形状大变，掉落一地杂七杂八的零碎东西。",
  ],
  "name": "第六章 白袍少年"
}
```
