# 頭骨 Landmark 標註（網頁版）

在瀏覽器裡旋轉 3D 頭骨、點選 landmark、匯出標註 JSON；學習頁可以看標好的點與解剖講解。

- 標註頁：`標註.html`（網站首頁會自動導過去）
- 學習頁：`學習.html`
- 目前的模型：`models/Model-mobile.glb`（塑膠教學頭骨，MAKAR／iPhone 手機掃描）。
  網頁版把貼圖從 PNG 轉成 JPEG（9.6 MB → 2.1 MB），網格一個位元組都沒動：幾何雜湊值與原檔相同，原檔標出的 JSON 可以直接用。
- 大檔由 jsDelivr CDN 傳送（部分網路連 GitHub Pages 很慢），失敗時自動改從本站讀。

> 這是公開網站：任何拿到網址的人都看得到。**不要上傳大體老師資料**（標成 `sensitive` 的模型會被自動拒絕）。

## 怎麼標

1. 打開網站 → 模型庫 → 選頭骨。
2. 選清單上的點 → 在模型上點選位置；可以量測、做卡尺校正與擺正。
3. 標到一半關掉也沒關係：草稿會存在這台電腦的瀏覽器裡。
4. 標完按「存成 JSON」→ 下載一個 `.json` 檔。**網站本身不能存檔**（GitHub Pages 沒有後端），要留存就交這個檔案。

## 怎麼把標註放上網站、替換、刪除

標註 JSON 放在 `models/Model-mobile.landmarks/`，**檔名就是標註名稱**（例如 `王小明_第1次.json`）。

- **新增或替換**：在 GitHub 網頁進到該資料夾 → `Add file` → `Upload files` → 拖入 JSON → `Commit changes`。
  - 同檔名＝直接覆蓋替換。
- **刪除**：點該檔案 → 右上角 `…` → `Delete file` → `Commit changes`。
- 約 1–2 分鐘後網站自動更新（`Actions` 分頁可以看進度）；模型目錄 `library.json` 由部署流程自動產生，不用手改。

JSON 裡記有模型的幾何雜湊值：同一個 `.glb` 標出來的 JSON 才對得上。換了模型檔，舊標註會被標註器提醒不相容。

## 新增模型

上傳 `models/新模型.glb`，再放一個同名的 `models/新模型.meta.json`：

```json
{ "title": "顯示名稱", "description": "一兩句說明", "preset": "skull", "sensitive": false }
```

`preset` 用 `skull`（頭骨清單）或 `blank`（自訂點）。單檔上限 100 MB（GitHub 限制）。
