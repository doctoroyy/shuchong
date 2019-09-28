# shuchong
书虫小说后台，定义了前端所需的几个接口 https://api.doctoroyy.cf/
- getBookList: '/book/getAll',
  获取小说列表
  method: GET
  入参：无
  出参： 
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
      "description": "在破败中崛起，在寂灭中复苏。    沧海成尘，雷电枯竭，那一缕幽雾又一次临近大地，世间的枷锁被打开了，一个全新的世界就此揭开神秘的一角……",
      "imgSrc": "https://www.xbiquge6.com/cover/74/74821/74821s.jpg",
      "author": "辰东"
    },
    {
      "id": 3,
      "name": "元尊",
      "tags": null,
      "description": "天地为炉，万物为铜，阴阳为炭，造化为工。 气运之争，蟒雀吞龙。 究竟是蟒雀为尊，还是圣龙崛起，凌驾众生？ 这是气掌乾坤的世界，磅礴宏伟，一气可搬山，可倒海，可翻天，可掌阴阳乾坤。 世间源气分九品，三品称玄，六品成天，九品号圣。 吾有一口玄黄气，可吞天地日月星。",
      "imgSrc": "https://www.xbiquge6.com/cover/78/78513/78513s.jpg",
      "author": "天蚕土豆"
    },
    {
      "id": 4,
      "name": "万古神帝",
      "tags": null,
      "description": "【NEXTIDEA暨2015星创奖征文大赏（玄幻）】    八百年前，明帝之子张若尘，被他的未婚妻池瑶公主杀死，一代无上天骄，就此陨落。    八百年后，张若尘重新活了过来，却发现曾经杀死他的未婚妻，已经统一昆仑界，开辟出第一中央帝国，号称“池瑶女皇”。    池瑶女皇——统御天下，威临八方；青春永驻，不死不灭。    张若尘站在诸皇祠堂外，望着池瑶女皇的神像，心中",
      "imgSrc": "https://www.xbiquge6.com/cover/20/20331/20331s.jpg",
      "author": "飞天鱼"
    },
    {
      "id": 5,
      "name": "帝霸",
      "tags": null,
      "description": "千万年前，李七夜栽下一株翠竹。八百万年前，李七夜养了一条鲤鱼。五百万年前，李七夜收养一个小女孩。今天，李七夜一觉醒来，翠竹修练成神灵，鲤鱼化作金龙，小女孩成为九界女帝。这是一个养成的故事，一个不死的人族小子养成了妖神、养成了仙兽、养成了女帝的故事。请关注作者的公众号“萧府军团”。",
      "imgSrc": "https://www.xbiquge6.com/cover/8/8109/8109s.jpg",
      "author": "厌笔萧生"
    },
    {
      "id": 6,
      "name": "伏天氏",
      "tags": null,
      "description": "东方神州，有人皇立道统，有圣贤宗门传道，有诸侯雄踞一方王国，诸强林立，神州动乱千万载，执此之时，一代天骄叶青帝及东凰大帝横空出世，斩人皇，驭圣贤，诸侯臣服，东方神州一统！然，叶青帝忽然暴毙，世间雕像尽皆被毁，于世间除名，沦为禁忌；从此神州唯东凰大帝独尊！十五年后，东海青州城，一名为叶伏天的少年，开启了他的传奇之路…",
      "imgSrc": "https://www.xbiquge6.com/cover/9/9208/9208s.jpg",
      "author": "净无痕"
    },
    {
      "id": 7,
      "name": "凡人修仙之仙界篇（凡人修仙传仙界篇）",
      "tags": null,
      "description": "忘语新书，凡人修仙之仙界篇，忘语新书，凡人修仙之仙界篇，忘语新书，凡人修仙之仙界篇，忘语新书，凡人修仙之仙界篇，",
      "imgSrc": "https://www.xbiquge6.com/cover/1/1203/1203s.jpg",
      "author": "忘语"
    },
    {
      "id": 8,
      "name": "全球高武",
      "tags": null,
      "description": "今日头条——　　“大马宗师突破九品，征战全球！”　　“小马宗师问鼎至高，横扫欧亚！”　　“乔帮主再次出手，疑似九品大宗师境！”　　“股神宝刀未老，全球宗师榜再入前十！”　　“……”　　看着一条条新闻闪现，方平心好累，这剧本不对啊！",
      "imgSrc": "https://www.xbiquge6.com/cover/81/81336/81336s.jpg",
      "author": "老鹰吃小鸡"
    },
    {
      "id": 9,
      "name": "汉乡",
      "tags": null,
      "description": "我们接受了祖先的遗产，这让中华辉煌了数千年，我们是如此的心安理得，从未想过要回归那个在刀耕火种中苦苦寻找出路的时代。反哺我们苦难的祖先，并从中找到故乡的真正意义，将是本书要讲的故事。",
      "imgSrc": "https://www.xbiquge6.com/cover/78/78113/78113s.jpg",
      "author": "孑与2"
    },
    {
      "id": 10,
      "name": "大道朝天",
      "tags": null,
      "description": "我就是剑。　　千里杀一人，十步不愿行。　　千里杀一人，十步不得行。　　千里杀一人，十步？不行！　　我就是剑，剑就是我。　　大道朝天，各执一剑。　　（欢迎加入猫腻大道朝天官方群，群号码：311875513）",
      "imgSrc": "https://www.xbiquge6.com/cover/32/32972/32972s.jpg",
      "author": "猫腻"
    }
  ]
}
```
- getBookCatalog: '/book/catalog',
  获取小说目录详情
  method: POST
  入参：id
  出参：
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
- getChapter: '/book/chapter'
  获取小说章节详情
  method: POST
  入参：{id, chapterno}
  出参: 
```
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
