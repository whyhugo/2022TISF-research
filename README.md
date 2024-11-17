# Preventing One-sided(Incomplete) News on the Social Platform Using Deep Learning and Transfer Learning Methods
2022 Taiwan International Science Fair<br>
作者：AHSNCCU 王修佑  Hsiu-Yu, Wang<br>
指導老師：NTUST CSIE 鮑興國教授<br>
<br>
> 研究計畫指導/研究經費：<br>
> 國立台灣科教館、國立台灣大學電機工程學系 未來之星培訓營（林晃巖教授、黃定洧教授）<br>
> 聯發科技教育基金會<br>
<br>

## 🗂️Details
* Documents `📁成果報告&研究計畫`<br>
  * 研究計畫<br>
  * 研究報告書<br>
  * 研究海報<br>
  * 研究英文解說<br>
* 程式與資料集<br>
  * 資料 `📁data`<br>
    * 模型開發<br>
      fnc-1 資料集: 由美國機構邀請記者共同標註建立之資料集，可用於訓練預測兩文本之間相關關係程度之 NLP 模型；並從其中切割 train 與 evaluate 資料。<br>
    * 實務驗證<br>
      為求研究獨特性，我以 Selenium 與 BeautifulSoup 工具爬取美國數家新聞媒體 (New York Times、Wall Street Journal、Buzzfeed 等) 於 Facebook 發布新聞貼文時的貼文文本與該則報導文本，用於實驗中實務分析美國媒體現況。<br>
  * 模型 `📁train_and_models`<br>
    * 使用建立於 Hugging Face Transformers library 的 Simple Transformers 進行 NLP 模型訓練 (Pytorch)<br>
    * 其中使用 BERT, XLNet, RoBERTa 三種預訓練模型分別進行遷移式學習<br>
    * 訓練過程透過 Wandb 工具觀察參數數據變化<br>
    
## 🏆獲獎<br>
* 2022 TISF 台灣國際科學展覽會 電腦與資工程科 決賽入圍<br>
* 國立政大附中校內科展 電腦與資訊學科 特優<br>
