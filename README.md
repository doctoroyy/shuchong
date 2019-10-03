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

### /book/search 搜索小说
  - method: POST
  - 入参：
  ```
  {"keyword":"诛仙"}
  ```
  
  - 出参: 
```json
[
  {
    "name": "一念诛仙",
    "imgSrc": "https://www.xbiquge6.com/cover/72/72996/72996s.jpg",
    "url": "https://www.xbiquge6.com/72_72996/",
    "description": "死即是生，身陨又如何；神魄尚存，皇威镇苍生。修罗地狱吾驰骋，三十三天仍纵横。三界无人可相敌，浴火涅盘转人身。我欲成王怜万物，无奈独喜黄金甲。我欲卸甲以归田，苦叹人间烦恼多。我欲归隐山林静，却爱凡俗鼓乐...",
    "author": "离恨殇歌",
    "updateTime": "2016-12-10",
    "latestChapter": "第六十七章:开学跟我有什么关系"
  },
  {
    "name": "诛仙之天火",
    "imgSrc": "https://www.xbiquge6.com/cover/68/68706/68706s.jpg",
    "url": "https://www.xbiquge6.com/68_68706/",
    "description": "神州浩土，修罗之乱近百年后，流民回所，百废俱兴。南疆，七里峒，一个身世奇异足以惊天的少年，带上了舅舅送他的“合欢铃”，背井离乡，北上青云，为的是寻找一个可以救得自己的性命的人——张小凡！由此，一个新的...",
    "author": "旅艺",
    "updateTime": "2016-12-10",
    "latestChapter": "第五十二章 不是叛变"
  }
]
```