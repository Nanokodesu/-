# 武康路Citywalk Cesium本地单HTML项目

## 目录结构

```text
E:/321/nano/学习中/-数字孪生与智慧城市/-/
├─ index.html                 # 最终运行入口，HTML+CSS+JS集中在一个文件
├─ Build/
│  └─ Cesium/                 # 从原始课程文件夹复制来的Cesium本地包
├─ Data/                      # 从原始课程文件夹复制来的数据与插件
│  ├─ CZML/
│  ├─ GeoJSON/
│  ├─ KML/
│  ├─ Plug-in/
│  ├─ Texture/
│  └─ video/
└─ samples/                   # 原始课程HTML样例备份，便于回看课堂代码
```

## 本地资源调用

`index.html`当前使用本地路径调用Cesium和ECharts：

```html
<script>
  window.CESIUM_BASE_URL = "./Build/Cesium/";
</script>
<script src="./Build/Cesium/Cesium.js"></script>
<script src="./Data/Plug-in/echarts-6.0.0/echarts-6.0.0/dist/echarts.min.js"></script>
<link rel="stylesheet" href="./Build/Cesium/Widgets/widgets.css">
```

这意味着项目不再依赖之前误生成的`node_modules`或Vite工程。

## 推荐启动方式

建议在本目录启动本地静态服务器后访问：

```bash
python -m http.server 8088
```

然后打开：

```text
http://localhost:8088/index.html
```

如果直接双击HTML也可以打开，但Cesium部分Worker、贴图、视频或后续3DTiles数据更适合通过本地服务器访问。

## 当前功能入口

- `initApp()`：初始化CesiumViewer、基础场景、POI、路线、人流与图表。
- `openPanel(panelName)`：切换导览、分析、课程功能三个收纳式抽屉。
- `addPoiLayer()`：添加武康路POI点位和动态光环。
- `showRoute(routeId)`：显示文学、建筑、安静避让三类路线。
- `toggleCrowdLayer()`：开启/关闭人流热力点。
- `switchCrowdTime(timeKey)`：切换上午、下午、夜间人流。
- `startStoryGuide()`：开启游客故事导览模块。
- `runVoiceCommand()`：模拟AI语音意图识别并触发空间跳转。
- `toggleHistorySplit()`：开启历史卷帘对比。
- `applyBuildingStyle()`：示范建筑设色逻辑。
- `enableDraw(mode)`：范围/矩形绘制入口。
- `loadLocalTileset()`：加载`Data/Slice_shp/tileset.json`本地3DTiles并应用设色。
- `loadGeoJsonLayers()`：加载本地GeoJSON路网和绿地图层。
- `loadKmlLayer()`：加载本地KML边界图层。
- `loadCzmlVehicle()`：用本地`GroundVehicle.glb`生成CZML动态轨迹。
- `addPlantingLayer()`：沿安静路线布置本地树木GLB模型。
- `showPanorama()`：添加全景图入口。
- `addHeatmapPluginLayer()`：调用本地CesiumHeatmap插件；若插件兼容性不足则回退为实体热力点。
- `toggleNavigation()`：启用本地CesiumNavigation导航控件。
- `addViewshedDemo()`：添加轻量可视域/视锥分析。
- `addFloodDemo()`：添加动态淹没分析演示。
- `toggleWeather()`：开启/关闭粒子天气。
- `toggleContour()`：开启/关闭等高线和雾效。
- `addRadarScan()`：添加雷达扫描特效。

## 后续数据替换建议

1. 将真实武康路POI整理为`Data/project/poi.geojson`。
2. 将路线整理为`Data/project/routes.json`或CZML。
3. 将人流分时数据整理为`Data/project/crowd.json`。
4. 将历史照片、视频、全景图放入`Data/project/media/`。
5. 如果获得3DTiles建筑模型，放入`Data/project/tilesets/`，再在`index.html`中接入`Cesium.Cesium3DTileset`。

## 界面调整

当前版本已从“多个窗口常驻一级页面”改为“场景全屏+侧边Dock+收纳式抽屉+底部状态卡”的结构：

- 顶部工具栏：黑色半透明，只保留全局模式、时间段和少量高频按钮。
- 左侧Dock：导览、分析、课程功能三个入口，默认不遮挡主场景。
- 左右功能抽屉：点击后滑出，面板收起后只看Cesium场景。
- 底部状态卡：显示当前模式、核心点位、临时图层和课程功能覆盖度。
- 图表：深色主题。
- 状态栏与故事卡片：低透明彩色底，减少大块白色遮挡。

这样更接近三维城市可视化大屏气质，也不会遮挡Cesium场景主体。

## 本轮新增课程功能覆盖

- 本地Cesium调用：`Build/Cesium/Cesium.js`与`Widgets/widgets.css`。
- 本地ECharts调用：`Data/Plug-in/echarts-6.0.0/.../echarts.min.js`。
- 本地3DTiles：`Data/Slice_shp/tileset.json`。
- GeoJSON：`Data/GeoJSON/Road_bjfu.geojson`、`Grass_bjfu.geojson`。
- KML：`Data/KML/BJFU_SLA.kml`。
- CZML动态轨迹：运行时生成CZML并调用`Data/CZML/GroundVehicle.glb`。
- 模型种植：调用`Data/CZML/CommonTree_*.glb`。
- 全景入口：调用`Data/quanjing.jpg`。
- 插件热力：调用`Data/Plug-in/cesium-heatmap/cesium-heatmap/CesiumHeatmap.js`。
- 导航控件：调用`Data/Plug-in/cesium-navigation/cesium-navigation/viewerCesiumNavigationMixin.min.js`。
- 可视域、淹没、粒子天气、等高线/雾效：用课程代码思想在主页面内轻量实现。
