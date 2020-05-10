## Xpath

## 例子：

### 获取某个标签后的元素

```
url:https://movie.douban.com/subject/34807129/
```

```
//span[./text()="制片国家/地区:"]/following::text()[1]
```

### 获取节点的属性值

```
url:https://www.baidu.com/
```

```
//div[@id="s-top-left"]/a[1]/@href
```

