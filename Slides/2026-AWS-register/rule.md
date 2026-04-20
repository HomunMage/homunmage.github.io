# AWS 教學文件撰寫規範 (rule.md)

> **canonical spec** — 每張 ticket 引用本檔。Worker 開始撰寫任一文章前 **必須先讀完本檔**。

---

## 0. 受眾與目的

- **讀者**:客戶的助理。完全不懂 AWS、不懂雲端、只會操作信用卡與按按鈕。
- **目的**:讓對方獨立完成 AWS 帳號註冊、域名、EC2、S3、RDS 設置,最後交付 IAM Access Key 給我們以部署 lattice-cast。
- **語氣**:像對長輩說明,每一步都要可執行、可勾選、可回報。

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

### 3.4 待補截圖
Console 內頁無法登入截,使用 placeholder:
```markdown
![待補:EC2 Launch Wizard 第 2 步 (zh)](images/placeholder_05_ec2_step2_zh)
```
校對票會列出所有 placeholder 清單給助理操作時補。

---

## 4. 文章結構模板

每篇文章必須包含以下區塊,順序固定:

```markdown
# <NN> - <繁中標題> / <English Title>

> ⚠️ **重要警告 / Critical Warning**
> (見 §1 警告區塊原文)

## 預估 / Estimate
- 時間 (Time):約 XX 分鐘
- 費用 (Cost):USD $X / 月,或免費方案說明
- 需準備 (Prerequisites):
  - 信用卡(VISA / Master,需可付外幣)
  - email 信箱(建議用公司 email,非 Gmail)
  - 手機(收驗證碼)
  - (其他依文章而定)

## 名詞快查 / Glossary
| 中文 | English | 說明 |
|------|---------|------|
| 區域 | Region | AWS 機房地理位置 |
| ... | ... | ... |

## 操作步驟 / Steps

### 步驟 1:xxx (Step 1: xxx)
1. 開啟瀏覽器,前往 `https://...`
2. 點擊「xxx (Xxx)」按鈕
   ![中文 UI](images/NN_topic_step1_zh)
   ![English UI](images/NN_topic_step1_en)
3. 填入...
4. ...

### 步驟 2: ...

## 完成後請回報 / Deliverables to Send Us

完成後請把以下資訊用安全管道(1Password / Bitwarden / 加密 email)傳給我們:
- xxx
- yyy

## 檢核清單 / Checklist
助理操作完逐項打勾後回傳本文件:

- [ ] 已確認使用 `aws.amazon.com`(非 .cn)
- [ ] 已開啟 Root 帳號 MFA
- [ ] (其他依文章而定)
- [ ] 已將上方「完成後請回報」的資訊傳給我方

## 常見問題 / FAQ
**Q: 信用卡刷不過怎麼辦?**
A: ...

**Q: 註冊頁顯示中文但網址有 .cn?**
A: 立即關閉,從 https://aws.amazon.com 重新進入。

## 出問題時 / If Something Goes Wrong
聯絡:lifetreemastery@gmail.com,附上錯誤訊息截圖。
```

---

## 5. 檔案命名與輸出位置

```
./.tmp/AWS/
├── rule.md                          # 本檔
├── 01_register_aws_account.md
├── 02_iam_user_access_key.md
├── 03_billing_alert.md
├── 04_route53_domain.md
├── 05_ec2_launch.md
├── 06_s3_bucket.md
├── 07_rds_postgres.md
├── 99_checklist_overview.md         # 校對票輸出總覽
└── images/                          # 所有截圖,從 .browser/ 搬入
    ├── 01_register_step1_zh
    ├── 01_register_step1_en
    └── placeholder_*            # console 內頁待補
```

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
- [ ] 截圖 LLM 已讀過、確認對應內容、命名遵循 §3.3
- [ ] placeholder 截圖列入 `99_checklist_overview.md`
- [ ] 檢核清單可逐項勾(無模糊項)
- [ ] 安全規範 §6 在交付段落落實

校對結果輸出/更新到 `./.tmp/AWS/99_checklist_overview.md`。

---

## 8. 撰寫順序建議(worker 給單篇 issue 時遵循)

1. 讀 `rule.md`(本檔)
2. 讀該篇 issue 的 ticket doc(具體 scope)
3. 開 browser container,截圖該篇所需公開頁
4. **Read tool 讀每張 PNG**,確認內容
5. 搬移 PNG 到 `./.tmp/AWS/images/` + 重新命名
6. 撰寫 markdown,套用 §4 模板
7. 列出 placeholder 清單(console 內頁)寫入文章末尾「## 待補截圖」
8. 跑自檢:對照本檔 §7 逐項過
9. 更新 ticket doc work log,提交
