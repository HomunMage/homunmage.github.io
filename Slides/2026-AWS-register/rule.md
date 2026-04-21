---
layout: page/note/basic
---

# AWS 教學文件撰寫規範 (rule.md)

> **canonical spec** — 每張 ticket 引用本檔。Worker 開始撰寫任一文章前 **必須先讀完本檔**。

---

## 0. 受眾與目的(**極重要**,寫錯整篇 reject)

- **讀者**:**我方客戶**。他們不懂程式、不懂 AWS、不懂雲端。
- **關係**:他們是在**幫我們**把 AWS 環境架起來,再把 Access Key 交給我們部署 lattice-cast。**我們是求他們協助的一方**,不是在分派工作給下屬。
- **語氣**:
  - 像寫「感謝您幫忙,以下是流程」的 onboarding 信
  - 禮貌、簡單、白話、每個技術名詞第一次出現要解釋
  - **不可**用命令式(「請助理截圖補上」「助理需做 X」這類通通刪)
  - **不可**稱呼「助理」,改用「您」或客戶姓名占位「{{客戶稱呼}}」
  - 表達感謝(開頭一句、結尾一句)
  - 口吻示範:
    - ✅「感謝您協助設定這部分,只需要 10 分鐘,照下方步驟即可」
    - ✅「這個欄位 AWS 的介面有時會略不同,若找不到,來信告訴我們,我們協助您」
    - ❌「請助理點擊 X」「完成後助理回傳 Y」
- **非技術化**:用日常比喻(「Region 就像選一個機房城市」「IAM 使用者就像在 AWS 幫我們開一個專用帳號」)
- **禁止**:要求對方做任何「截圖給我們」之外的非必要動作(他們不是我們的助理)

---

## 1. 平台選擇(關鍵安全規則)

**必須使用 AWS Global**:`https://aws.amazon.com`

**禁止 AWS China**:
- `https://www.amazonaws.com.cn`(由光環新網 Sinnet 或西雲 NWCD 營運)
- 中國區帳號獨立、需 ICP 備案、服務不全、與 lattice-cast 部署不相容

**每篇文章開頭必須有警告區塊**:

```markdown
> ⚠️ **重要警告 / Critical Warning**
> 本教學僅適用 AWS Global(`aws.amazon.com`)。
> 若註冊頁出現「中國區 / 由光環新網或西雲營運 / Sinnet / NWCD」字樣,請立即關閉重來。
> This guide applies to AWS Global only. Close and restart if you see "China region / operated by Sinnet or NWCD".
```

---

## 2. 中英對照格式

### 2.1 行內步驟
每個按鈕、選單、欄位採「繁體中文 (English)」格式:

✅ 正確:
> 點擊左側選單「執行個體 (Instances)」→「啟動執行個體 (Launch instance)」

❌ 錯誤:
> 點擊「執行個體」→「啟動執行個體」  ← 缺英文,助理切換英文 UI 找不到
> Click "Instances" → "Launch instance"  ← 缺中文,助理看不懂

### 2.2 服務名稱
保留英文,**不翻譯**:`EC2`、`S3`、`RDS`、`Route 53`、`IAM`、`VPC`、`CloudWatch`、`Budget`

### 2.3 標題
雙語並列:`# 01 - 註冊 AWS 帳號 / Register AWS Account`

### 2.4 截圖
- 關鍵步驟(每篇 ≥ 3 張關鍵步驟):中英 UI 各一張
- 次要步驟:單張即可,圖內元素加雙語標註

---

## 3. 截圖工作流(snapshot + image-move)

### 3.1 來源
- **可截圖**:AWS 公開頁(`aws.amazon.com`、`docs.aws.amazon.com`、產品頁、定價頁、註冊頁、登入著陸頁、`amazonaws.com.cn` 警告對照)
- **不可截圖**:Console 內頁(需登入)— 此處用 placeholder + 文字描述,等對方助理操作時實際截給我們補

### 3.2 步驟
1. 用 `./browser/` Playwright 截圖目標 URL,輸出到 `./.browser/`
   ```bash
   docker compose --profile browser up -d browser
   docker compose exec browser python browse.py screenshot <name> <url>
   # 例: docker compose exec browser python browse.py screenshot 01_register_step1_zh https://aws.amazon.com/tw/
   ```
2. **LLM 必須讀取截圖**(用 Read tool 讀 PNG)確認:
   - 內容是否符合文章宣稱(例:「點此註冊」按鈕真的存在)
   - UI 語言切換是否成功
   - 沒誤截到中國區站台
3. 確認 OK 後,把 PNG 從 `./.browser/` **搬到** `./.tmp/AWS/images/<NN>_<topic>_<step>`
4. 文章 markdown 用相對路徑引用:`![中文版:啟動 EC2 步驟 3](images/05_ec2_step3_zh)`

### 3.3 命名約定
```
images/
  01_register_step1_zh   # 文章 01 第 1 步 中文 UI
  01_register_step1_en   # 文章 01 第 1 步 英文 UI
  01_warning_china       # 警告對照(無語言版本之分)
  ...
```

### 3.4 找不到合適圖時 — **絕不留 placeholder**

**禁止**寫「待補截圖」「請助理截圖補上」這類字眼。文件是給對方**預讀預習**用,所有圖必須我方備齊。

替代方案(任一):
- (a) **WebFetch AWS 官方 Getting Started / docs / Blog**,從 HTML 抓 `<img>` URL,curl 下載到 `images/`
- (b) 改截 AWS 該服務的 marketing/pricing 頁(`browse.py screenshot`),內文寫「以下為產品頁示意」
- (c) 用 mermaid / ASCII 畫流程示意圖代替
- (d) 引用第三方教學 blog 圖(註明來源 + 取用日期 + 原作者)

**圖片下方必標來源**,範例:
```markdown
![EC2 啟動精靈](images/05_ec2_launch_wizard.webp)
*來源: [AWS Docs — Get started with Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html), 取用日期 2026-04-20*
```

**過時 OK**:即使 AWS 改版 UI,只要主要按鈕/欄位仍可辨認即可,文章開頭加一句「截圖可能因 AWS 介面更新略有差異,以實際畫面為準」。

### 3.5 圖片來源優先順序
1. `docs.aws.amazon.com/<service>/...` — 官方文件,授權清楚
2. `aws.amazon.com/blogs/...` — AWS Blog
3. `aws.amazon.com/getting-started/...` — Hands-on 教學
4. AWS 公開頁(產品/定價/註冊著陸頁)用 browse.py 自截
5. 第三方 blog(Medium、TutorialsPoint、AWS Hero blogs)— 註明出處

---

## 4. 文章結構模板

每篇文章必須包含以下區塊,順序固定:

```markdown
# <NN> - <繁中標題> / <English Title>

您好 {{客戶稱呼}},感謝您協助我們設定 AWS!以下是這部分的操作說明,遇到任何不清楚的地方都可以來信詢問,我們會協助您。

> 💡 **貼心提醒**:截圖可能因 AWS 介面更新略有差異,以實際畫面為準。若畫面找不到按鈕,請寄信告訴我們,我們立刻協助。

> ⚠️ **重要:請勿使用 AWS 中國區**
> 註冊請使用 `aws.amazon.com`。若頁面出現「中國區 / 光環新網 / 西雲 / Sinnet / NWCD」字樣,請關閉視窗從 `aws.amazon.com` 重新進入。
> (中國區是另一個獨立服務,與我們要的系統不相容。)

## 預估 / Estimate
- 時間:約 XX 分鐘
- 費用:USD $X / 月,或免費方案可用 Y 個月
- 需準備:
  - 信用卡(VISA / Master / JCB,能付美元即可)
  - email 信箱
  - 手機(收驗證碼)

## 名詞解說 / Glossary
用白話解釋 — 假設讀者從未接觸過雲端。
| 名詞 | 說明 |
|------|------|
| Region(區域) | AWS 的機房位置,就像選一個城市。建議選「東京 (ap-northeast-1)」速度最快 |
| IAM 使用者 | 為我們開一個專用帳號,讓我們能存取特定服務,但不能動到您的根帳號 |
| Access Key | IAM 使用者的「密碼」,我們用這個連到您的 AWS 幫您部署 |

## 操作步驟 / Steps

### 步驟 1:xxx (Step 1: xxx)
1. 開啟瀏覽器,前往 `https://...`
2. 點擊「xxx (Xxx)」按鈕
   ![步驟示意](images/NN_topic_step1.webp)
   *來源: [AWS Docs — XXX](https://docs.aws.amazon.com/...), 取用日期 2026-04-20*
3. 填入...
4. ...

### 步驟 2: ...

## 完成後請提供以下資訊 / Please Send Us

完成後,麻煩您把以下資訊用安全方式(1Password / Bitwarden / 加密訊息)傳給我們,我們收到後就可以幫您把 lattice-cast 架起來:
- xxx
- yyy

**若不知道如何用加密方式傳送,來信告訴我們,我們提供 1Password 共享連結。**

## 操作確認清單 / Checklist
以下項目您完成了就打勾,方便您和我們對照進度:

- [ ] 已使用 `aws.amazon.com`(不是 `.cn` 結尾的網址)
- [ ] 已開啟 Root 帳號的兩步驟驗證 (MFA)
- [ ] (其他依文章而定)
- [ ] 已把上方「請提供以下資訊」的內容傳給我們

## 常見問題 / FAQ
**Q:信用卡一直刷不過?**
A:AWS 有時會刷 $1 美金驗證卡片,若銀行擋下,請改用另一張卡,或聯絡發卡銀行開通境外扣款。

**Q:不小心進到中國區怎麼辦?**
A:沒關係,關閉視窗重開,從 `aws.amazon.com` 重新進入即可,不會扣款。

**Q:看不懂某個英文按鈕?**
A:直接把畫面截圖寄給我們(lifetreemastery@gmail.com),我們立刻告訴您要按哪裡。

## 遇到問題聯絡我們 / If Something Goes Wrong
📧 lifetreemastery@gmail.com — 附上畫面截圖,我們會儘快回覆協助您。

---

再次感謝您協助完成這部分!設定完成後,我們會接手把系統架起來,不會再打擾您。
```

---

## 5. 檔案命名與輸出位置

```
./.tmp/2026-AWS-register/
├── rule.md                          # 本檔
├── index.md                         # Jekyll directory page
├── 01_register_aws_account.md
├── 02_iam_user_access_key.md
├── 03_billing_alert.md
├── 04_route53_domain.md
├── 05_ec2_launch.md
├── 06_s3_bucket.md
├── 07_rds_postgres.md
├── 99_checklist_overview.md         # 校對票輸出總覽
└── images/                          # 所有圖,curl/browse.py 抓
    ├── 01_register_step1.png
    ├── 01_warning_china.png
    └── 05_ec2_launch_wizard.png
```

**注意**:檔案位置已從 `./.tmp/AWS/` 移至 `./.tmp/2026-AWS-register/`(Jekyll page 結構)。

---

## 6. 安全 & 交付規範

### 6.1 給我方的東西
- IAM Access Key ID + Secret(**不是** Root 帳號密碼)
- AWS Region
- (RDS 篇) DB endpoint / port / db name / username / password
- (S3 篇) bucket name / region
- (Route 53 篇) hosted zone ID / 域名
- (EC2 篇) public IP / key pair `.pem` 檔

### 6.2 傳遞管道
**禁止**:純文字 email、LINE、Slack 明文、Telegram、寫進 Google Doc
**建議**:1Password / Bitwarden 共享、ProtonMail 加密、PGP

### 6.3 IAM 最小權限
不要給 `AdministratorAccess`。每篇文章列出該服務的最小 policy。

---

## 7. 校對票檢查項(每 Story 結束)

校對 worker 必須驗證:
- [ ] 每篇有 §1 警告區塊
- [ ] 每篇有 §4 全部固定區塊(預估/名詞/步驟/回報/檢核/FAQ/出錯)
- [ ] 中英對照格式一致(無單語言步驟)
- [ ] 服務名英文未被誤譯
- [ ] **每張圖都有來源標註**(§3.4 範例格式)
- [ ] **無 placeholder.png、無「待補截圖」字眼**
- [ ] 圖片 LLM 已 Read 確認對應內容
- [ ] 檢核清單可逐項勾(無模糊項)
- [ ] 安全規範 §6 在交付段落落實
- [ ] 開頭加「截圖可能因 AWS 介面更新略有差異」免責句

校對結果輸出/更新到 `./.tmp/2026-AWS-register/99_checklist_overview.md`。

---

## 8. 撰寫順序(worker 給單篇 issue 時遵循)

1. 讀 `rule.md`(本檔)
2. 讀該篇 issue 的 ticket doc(具體 scope)
3. **找圖**:
   - WebFetch AWS 官方 Getting Started / Docs / Blog 頁,從 HTML 找 `<img src>`
   - curl 下載到 `./.tmp/2026-AWS-register/images/<NN>_<step>.png`
   - 補不足的:browse.py 截 AWS 公開頁(產品/定價/註冊著陸/.cn 警告對照)
4. **Read tool 讀每張圖**,確認對應步驟
5. 撰寫 markdown,套用 §4 模板,**每張圖下方加來源標註**
6. **絕不留 placeholder**;若真的找不到圖照 §3.4 替代方案處理
7. 跑自檢:對照本檔 §7 逐項過
8. 更新 ticket doc work log,提交
