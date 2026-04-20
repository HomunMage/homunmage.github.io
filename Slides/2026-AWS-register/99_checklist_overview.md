# 99 - 校對總覽 / QA Checklist Overview

---

## Story 1：帳號與權限基礎 / Account & Permission Basics (L-228)

### L-231：01 註冊 AWS Global 帳號

校對日期 (QA Date)：2026-04-19

| 檢查項 | 狀態 |
|--------|------|
| 有 §1 警告區塊 | ✅ |
| 有 §4 全部固定區塊（預估/名詞/步驟/回報/檢核/FAQ/出錯） | ✅ |
| 中英對照格式一致（無單語言步驟） | ✅ |
| 服務名英文未被誤譯（IAM、MFA、EC2、S3 等） | ✅ |
| 截圖 LLM 已讀過、確認對應內容、命名遵循 §3.3 | ✅ |
| placeholder 截圖列入本文件 | ✅ |
| 檢核清單可逐項勾（無模糊項） | ✅ |
| 安全規範 §6 在交付段落落實（只交 Account ID，不交密碼） | ✅ |

#### 已截圖（公開頁）/ Captured Screenshots

| 檔名 | 對應步驟 | 確認內容 |
|------|---------|---------|
| `01_register_home_zh.webp` | 步驟 1 | AWS 台灣首頁，繁體中文 UI ✅ |
| `01_register_home_en.webp` | 步驟 1 | AWS 英文首頁，"Discover AWS" + Free tier CTA ✅ |
| `01_register_form_en.webp` | 步驟 2 | AWS 註冊表單，含 email / account name / Verify email address 按鈕 ✅ |
| `01_warning_china.webp` | 步驟 1 | amazonaws.cn 中國區頁面，西雲數據/光環新網字樣，用作警告對照 ✅ |

#### 待補截圖（Console 登入後）/ Pending Placeholders

| Placeholder 檔名 | 說明 | 負責人 |
|-----------------|------|--------|
| `placeholder_01_password_en.webp` | 步驟 3：密碼設定頁面 | 助理操作後補 |
| `placeholder_01_account_type_en.webp` | 步驟 4：帳號類型選擇（Business/Personal）| 助理操作後補 |
| `placeholder_01_payment_en.webp` | 步驟 5：信用卡綁定頁 | 助理操作後補 |
| `placeholder_01_phone_en.webp` | 步驟 6：手機 SMS 驗證頁 | 助理操作後補 |
| `placeholder_01_support_plan_en.webp` | 步驟 7：Support Plan（Basic Free 選擇）| 助理操作後補 |
| `placeholder_01_console_en.webp` | 步驟 8：AWS Console 首頁（Region 下拉）| 助理操作後補 |
| `placeholder_01_mfa_iam_en.webp` | 步驟 9：IAM Security Credentials MFA 設定頁 | 助理操作後補 |

#### 備註 / Notes

- AWS 註冊表單（signup form）固定顯示英文，不隨瀏覽器語系改變，故 `01_register_form_zh.webp` 以英文版替代，文章內已加說明。

---

### L-232：02 建立 IAM 使用者與 Access Key

校對日期 (QA Date)：2026-04-19

| 檢查項 | 狀態 |
|--------|------|
| 有 §1 警告區塊（含 Sinnet/NWCD 關鍵字） | ✅ |
| 有 §4 全部固定區塊（預估/名詞/步驟/回報/檢核/FAQ/出錯） | ✅ |
| 中英對照格式一致（無單語言步驟） | ✅ |
| 服務名英文未被誤譯（IAM、Access Key、Policy 等） | ✅ |
| 截圖 LLM 已讀過、確認對應內容、命名遵循 §3.3 | ✅ |
| placeholder 截圖列入本文件 | ✅ |
| 檢核清單可逐項勾（無模糊項） | ✅ |
| 安全規範 §6 在交付段落落實（Access Key 僅限安全管道，禁 LINE/email 明文） | ✅ |

#### 已截圖（公開頁）/ Captured Screenshots

| 檔名 | 對應步驟 | 確認內容 |
|------|---------|---------|
| `02_console_signin_zh.webp` | 步驟 1 | AWS 管理主控台繁中產品頁，含「登入」按鈕 ✅ |
| `02_console_signin_en.webp` | 步驟 1 | AWS Management Console English page, "Sign in" button ✅ |

#### 待補截圖（Console 登入後）/ Pending Placeholders

| Placeholder 檔名 | 說明 | 負責人 |
|-----------------|------|--------|
| `placeholder_02_console_search_iam.webp` | Console 頂部搜尋 IAM 的畫面 | 助理操作後補 |
| `placeholder_02_iam_users_create_zh.webp` | IAM Users 頁面點擊 Create user（中文 UI）| 助理操作後補 |
| `placeholder_02_iam_users_create_en.webp` | IAM Users 頁面點擊 Create user（英文 UI）| 助理操作後補 |
| `placeholder_02_iam_username_zh.webp` | 填入 User name: lattice-cast-deploy | 助理操作後補 |
| `placeholder_02_iam_attach_policies_zh.webp` | 選擇 Attach policies directly | 助理操作後補 |
| `placeholder_02_iam_policies_selected_zh.webp` | 5 個 Policy 已勾選的畫面 | 助理操作後補 |
| `placeholder_02_iam_review_create_zh.webp` | Review and Create 確認畫面 | 助理操作後補 |
| `placeholder_02_iam_security_credentials_zh.webp` | 使用者 Security credentials 標籤 | 助理操作後補 |
| `placeholder_02_iam_key_usecase_zh.webp` | 選擇 Use case: Other | 助理操作後補 |
| `placeholder_02_iam_key_created_zh.webp` | Access Key ID + Secret Key 顯示畫面（唯一一次！）| 助理操作後補 |

#### 備註 / Notes

- 文章包含「為何不能用 Root Access Key」補充說明段（位於 Glossary 前），屬額外引導內容，符合助理受眾需求。
- `02_iam_product_zh.webp`、`02_iam_product_en.webp` 已截存於 `images/` 但目前文章未引用（備用）。

---

### L-233：03 帳單告警與成本控管

校對日期 (QA Date)：2026-04-19

| 檢查項 | 狀態 |
|--------|------|
| 有 §1 警告區塊（含 Sinnet/NWCD 關鍵字） | ✅ |
| 有 §4 全部固定區塊（預估/名詞/步驟/回報/檢核/FAQ/出錯） | ✅ |
| 中英對照格式一致（無單語言步驟） | ✅ |
| 服務名英文未被誤譯（Budgets、Cost Explorer、Free Tier 等） | ✅ |
| 截圖 LLM 已讀過、確認對應內容、命名遵循 §3.3 | ✅ |
| placeholder 截圖列入本文件 | ✅ |
| 檢核清單可逐項勾（無模糊項） | ✅ |
| 安全規範 §6 在交付段落落實（截圖非機密，無需加密管道） | ✅ |

#### 已截圖（公開頁）/ Captured Screenshots

| 檔名 | 對應步驟 | 確認內容 |
|------|---------|---------|
| `03_budgets_zh.webp` | 步驟 6 參考 | AWS Budgets 繁中產品頁，含「開始使用 AWS Budgets」、優勢/使用案例 ✅ |
| `03_budgets_en.webp` | 步驟 6 參考 | AWS Budgets English, "Get started with AWS Budgets", Benefits/Use cases ✅ |
| `03_cost_explorer_zh.webp` | 步驟 6 參考 | AWS Cost Explorer 繁中產品頁，服務說明 ✅ |
| `03_cost_explorer_en.webp` | 步驟 6 參考 | AWS Cost Explorer English, Benefits/How it works ✅ |

#### 待補截圖（Console 登入後）/ Pending Placeholders

| Placeholder 檔名 | 對應步驟 | 說明 | 負責人 |
|-----------------|---------|------|--------|
| `placeholder_03_billing_menu_zh.webp` | 步驟 2 | 帳號下拉選單中文版 | 助理操作後補 |
| `placeholder_03_billing_menu_en.webp` | 步驟 2 | Account dropdown menu 英文版 | 助理操作後補 |
| `placeholder_03_budgets_console_zh.webp` | 步驟 2 | Budgets 主控台頁面中文版 | 助理操作後補 |
| `placeholder_03_budgets_console_en.webp` | 步驟 2 | Budgets landing page 英文版 | 助理操作後補 |
| `placeholder_03_budget_config_zh.webp` | 步驟 3 | Cost Budget 設定頁中文版 | 助理操作後補 |
| `placeholder_03_budget_config_en.webp` | 步驟 3 | Cost Budget config page 英文版 | 助理操作後補 |
| `placeholder_03_alert_threshold_zh.webp` | 步驟 4 | 告警門檻設定頁中文版 | 助理操作後補 |
| `placeholder_03_alert_threshold_en.webp` | 步驟 4 | Alert threshold setup 英文版 | 助理操作後補 |
| `placeholder_03_budget_confirm_zh.webp` | 步驟 5 | 預算建立確認頁中文版 | 助理操作後補 |
| `placeholder_03_budget_confirm_en.webp` | 步驟 5 | Budget creation confirm 英文版 | 助理操作後補 |
| `placeholder_03_cost_explorer_enable_zh.webp` | 步驟 6 | 啟用 Cost Explorer 頁面中文版 | 助理操作後補 |
| `placeholder_03_cost_explorer_enable_en.webp` | 步驟 6 | Enable Cost Explorer 英文版 | 助理操作後補 |
| `placeholder_03_freetier_alert_zh.webp` | 步驟 7 | Free Tier 告警設定中文版 | 助理操作後補 |
| `placeholder_03_freetier_alert_en.webp` | 步驟 7 | Free Tier alert setting 英文版 | 助理操作後補 |

#### 備註 / Notes

- 文章在 Estimate 前有「為何這一步不能跳過」引導段（含真實帳單暴增案例），有效提升助理操作動機。
- 此文件交付物為截圖（非機密），安全規範適度寬鬆，符合 §6 精神。

---

## Story 2：基礎設施設置 / Infrastructure Setup (L-229)

### L-235：04 Route 53 域名設置

校對日期 (QA Date)：2026-04-19

| 檢查項 | 狀態 |
|--------|------|
| 有 §1 警告區塊 | ✅ |
| 有 §4 全部固定區塊（預估/名詞/步驟/回報/檢核/FAQ/出錯） | ✅ |
| 中英對照格式一致（無單語言步驟） | ✅ |
| 服務名英文未被誤譯（Route 53、Hosted Zone、NS 等） | ✅ |
| 截圖 LLM 已讀過、確認對應內容、命名遵循 §3.3 | ✅ |
| placeholder 截圖列入本文件 | ✅ |
| 檢核清單可逐項勾（無模糊項） | ✅ |
| 安全規範 §6 在交付段落落實（只交 Hosted Zone ID + 域名） | ✅ |

### L-236：校對 Story 2（04 Route 53 域名設置）

校對日期 (QA Date)：2026-04-19

L-236 票特定校對項目：

| 票定檢查項 | 狀態 | 備註 |
|-----------|------|------|
| A/B 兩種流程分章節清楚 | ✅ | 方案 A/B/C 各有獨立 `##` 章節，每節末有「跳至通用步驟」導引 |
| NS 修改步驟不模糊 | ✅ | 方案 B Step 5 及方案 C Step 3 均有明確 4 步 NS 更新說明，含「全部替換」提醒 |
| 轉入 auth code 說明有 | ✅ | 方案 B Step 1 說明如何取得 EPP Code；Step 3 說明如何在 Route 53 輸入 |
| Hosted Zone ID 交付格式範例正確 | ✅ | 通用步驟與「完成後請回報」均標明格式：`Z` 開頭，如 `Z1234567890ABC` |

#### 已截圖（公開頁）/ Captured Screenshots

| 檔名 | 對應位置 | 確認內容 |
|------|---------|---------|
| `04_route53_product_zh.webp` | 服務說明 | AWS Route 53 繁中產品頁，"Route 53 的優勢" ✅ |
| `04_route53_product_en.webp` | 服務說明 | AWS Route 53 English product page, "Benefits of Route 53" ✅ |
| `04_route53_pricing_zh.webp` | 費用說明 | Route 53 定價頁，含"AWS 定價計算器"、"權威 DNS"、"網域" ✅ |
| `04_route53_pricing_en.webp` | 費用說明 | Route 53 Pricing, AWS Pricing Calculator, "Authoritative DNS", "Domains" ✅ |

#### 待補截圖（Console 登入後）/ Pending Placeholders

| Placeholder 檔名 | 說明 | 負責人 |
|-----------------|------|--------|
| `placeholder_04_route53_console_zh.webp` | Route 53 Console 首頁（繁中）| 助理操作後補 |
| `placeholder_04_route53_console_en.webp` | Route 53 Console Home (English) | 助理操作後補 |
| `placeholder_04_route53_search_result_zh.webp` | 域名搜尋結果頁（繁中）| 助理操作後補 |
| `placeholder_04_route53_search_result_en.webp` | Domain Search Results (English) | 助理操作後補 |
| `placeholder_04_route53_contact_zh.webp` | 聯絡資訊填寫頁（繁中）| 助理操作後補 |
| `placeholder_04_route53_contact_en.webp` | Contact Info Form (English) | 助理操作後補 |
| `placeholder_04_route53_order_zh.webp` | 訂單確認頁（繁中）| 助理操作後補 |
| `placeholder_04_route53_order_en.webp` | Order Confirmation (English) | 助理操作後補 |
| `placeholder_04_route53_transfer_btn_zh.webp` | Transfer Domain 按鈕（繁中）| 助理操作後補 |
| `placeholder_04_route53_transfer_btn_en.webp` | Transfer Domain Button (English) | 助理操作後補 |
| `placeholder_04_route53_authcode_zh.webp` | Auth Code 輸入頁（繁中）| 助理操作後補 |
| `placeholder_04_route53_authcode_en.webp` | Auth Code Input (English) | 助理操作後補 |
| `placeholder_04_route53_ns_zh.webp` | Hosted Zone NS 記錄（繁中）| 助理操作後補 |
| `placeholder_04_route53_ns_en.webp` | Hosted Zone NS Records (English) | 助理操作後補 |
| `placeholder_04_route53_create_hz_zh.webp` | Create Hosted Zone 頁面（繁中）| 助理操作後補 |
| `placeholder_04_route53_create_hz_en.webp` | Create Hosted Zone (English) | 助理操作後補 |
| `placeholder_04_route53_hz_ns_zh.webp` | NS Records 顯示（繁中）| 助理操作後補 |
| `placeholder_04_route53_hz_ns_en.webp` | NS Records Display (English) | 助理操作後補 |
| `placeholder_04_route53_hz_id_zh.webp` | Hosted Zone ID 位置（繁中）| 助理操作後補 |
| `placeholder_04_route53_hz_id_en.webp` | Hosted Zone ID Location (English) | 助理操作後補 |

---

## Story 3：服務佈署 / Service Deployment (L-230)

### L-237：05 啟動 EC2 執行個體

校對日期 (QA Date)：2026-04-19

| 檢查項 | 狀態 |
|--------|------|
| 有 §1 警告區塊（含 Sinnet/NWCD 關鍵字） | ✅ |
| 有 §4 全部固定區塊（預估/名詞/步驟/回報/檢核/FAQ/出錯） | ✅ |
| 中英對照格式一致（無單語言步驟） | ✅ |
| 服務名英文未被誤譯（EC2、AMI、VPC、Security Group、EBS、gp3 等） | ✅ |
| 截圖 LLM 已讀過、確認對應內容、命名遵循 §3.3 | ✅ |
| placeholder 截圖列入本文件 | ✅ |
| 檢核清單可逐項勾（無模糊項） | ✅ |
| 安全規範 §6 在交付段落落實（Instance ID、Public IP、SG ID、.pem via 1Password） | ✅ |

#### L-240 票定額外校對項

| 票定檢查項 | 狀態 | 備註 |
|-----------|------|------|
| EC2/RDS/S3 同 Region 提示明確 | ✅ | 步驟 1 專章提示、檢核清單第 2 項「Region 已確認與 RDS/S3 相同」 |
| SSH(22) 來源設為 My IP（不對外） | ✅ | 步驟 7 安全群組表格明確標示 + ⚠️ 警告 |
| 密碼/金鑰走 1Password 交付 | ✅ | 步驟 6 警告「立即存入 1Password」、交付段落明確禁止明文管道 |

#### 已截圖（公開頁）/ Captured Screenshots

| 檔名 | 對應步驟 | 確認內容 |
|------|---------|---------|
| `05_ec2_product_zh.webp` | 步驟 2 服務介紹 | EC2 繁中產品頁 ✅ |
| `05_ec2_product_en.webp` | 步驟 2 服務介紹 | EC2 English product page ✅ |
| `05_ec2_t3_types_zh.webp` | 步驟 5 規格比較 | T3 執行個體規格比較（繁中）✅ |
| `05_ec2_t3_types_en.webp` | 步驟 5 規格比較 | T3 Instance Type Comparison (English) ✅ |
| `05_ec2_pricing_zh.webp` | 步驟 5 費用參考 | EC2 隨需定價頁（繁中）✅ |
| `05_ec2_pricing_en.webp` | 步驟 5 費用參考 | EC2 On-Demand Pricing (English) ✅ |

#### 待補截圖（Console 登入後）/ Pending Placeholders

| Placeholder 檔名 | 說明 | 負責人 |
|-----------------|------|--------|
| `placeholder_05_ec2_step1_region_zh.webp` | 右上角 Region 選擇器（繁中）| 助理操作後補 |
| `placeholder_05_ec2_step1_region_en.webp` | Region selector top-right (English) | 助理操作後補 |
| `placeholder_05_ec2_step2_launch_btn_zh.webp` | EC2 Dashboard 左側選單與啟動按鈕（繁中）| 助理操作後補 |
| `placeholder_05_ec2_step2_launch_btn_en.webp` | EC2 Dashboard left menu & Launch button (English) | 助理操作後補 |
| `placeholder_05_ec2_step3_name_zh.webp` | 名稱與標籤填寫（繁中）| 助理操作後補 |
| `placeholder_05_ec2_step3_name_en.webp` | Name and Tags input (English) | 助理操作後補 |
| `placeholder_05_ec2_step4_ami_zh.webp` | AMI 選擇 Ubuntu 22.04 LTS（繁中）| 助理操作後補 |
| `placeholder_05_ec2_step4_ami_en.webp` | AMI selection Ubuntu 22.04 LTS (English) | 助理操作後補 |
| `placeholder_05_ec2_step6_keypair_zh.webp` | 建立金鑰對 RSA + .pem 設定（繁中）| 助理操作後補 |
| `placeholder_05_ec2_step6_keypair_en.webp` | Create key pair RSA + .pem settings (English) | 助理操作後補 |
| `placeholder_05_ec2_step7_sg_zh.webp` | 安全群組規則設定（繁中）| 助理操作後補 |
| `placeholder_05_ec2_step7_sg_en.webp` | Security Group rules configuration (English) | 助理操作後補 |
| `placeholder_05_ec2_step8_storage_zh.webp` | 儲存 30 GB gp3 設定（繁中）| 助理操作後補 |
| `placeholder_05_ec2_step8_storage_en.webp` | Storage 30 GB gp3 (English) | 助理操作後補 |
| `placeholder_05_ec2_step9_launch_zh.webp` | 啟動摘要與 Launch 按鈕（繁中）| 助理操作後補 |
| `placeholder_05_ec2_step9_launch_en.webp` | Launch summary & button (English) | 助理操作後補 |
| `placeholder_05_ec2_step10_details_zh.webp` | 執行個體詳細資訊頁（繁中）| 助理操作後補 |
| `placeholder_05_ec2_step10_details_en.webp` | Instance details page (English) | 助理操作後補 |

---

### L-238：06 建立 S3 儲存桶

校對日期 (QA Date)：2026-04-19

| 檢查項 | 狀態 |
|--------|------|
| 有 §1 警告區塊（含 Sinnet/NWCD 關鍵字） | ✅ |
| 有 §4 全部固定區塊（預估/名詞/步驟/回報/檢核/FAQ/出錯） | ✅ |
| 中英對照格式一致（無單語言步驟） | ✅ |
| 服務名英文未被誤譯（S3、Bucket、ACL、CORS、SSE-S3、Presigned URL 等） | ✅ |
| 截圖 LLM 已讀過、確認對應內容、命名遵循 §3.3 | ✅ |
| placeholder 截圖列入本文件 | ✅ |
| 檢核清單可逐項勾（無模糊項） | ✅ |
| 安全規範 §6 在交付段落落實（Bucket 名稱 + Region，禁明文管道） | ✅ |

#### L-240 票定額外校對項

| 票定檢查項 | 狀態 | 備註 |
|-----------|------|------|
| S3 與 EC2 同 Region 提示明確 | ✅ | Estimate Prerequisites 要求「已知 EC2 所在 Region」；步驟 3 明確要求選與 EC2 相同 Region |
| Block Public Access 全開（5 項） | ✅ | 步驟 4 列出全部 5 個子項目逐一確認 ✅；並說明為何要全封鎖（Presigned URL 流程） |
| S3 透過 IAM 存取（非公開） | ✅ | 步驟 9 提供最小 IAM Policy JSON，明確說明不給 S3FullAccess |
| CORS `AllowedOrigins` 有客戶域名 placeholder | ✅ | 步驟 8 CORS JSON 含 `"https://<客戶域名>"` placeholder + 填寫範例 |
| 密碼/key 走 1Password 交付 | ✅ | 交付段落明確列出禁止/建議管道 |

#### 已截圖（公開頁）/ Captured Screenshots

| 檔名 | 對應步驟 | 確認內容 |
|------|---------|---------|
| `06_s3_product_zh.webp` | Estimate 說明 | S3 繁中產品頁 ✅ |
| `06_s3_product_en.webp` | Estimate 說明 | S3 English product page ✅ |
| `06_s3_pricing_zh.webp` | 步驟 9 費用參考 | S3 定價頁（繁中）✅ |
| `06_s3_pricing_en.webp` | 步驟 9 費用參考 | S3 Pricing Page (English) ✅ |

#### 待補截圖（Console 登入後）/ Pending Placeholders

| Placeholder 檔名 | 說明 | 負責人 |
|-----------------|------|--------|
| `placeholder_06_s3_console_zh.webp` | S3 Console 首頁（繁中）| 助理操作後補 |
| `placeholder_06_s3_console_en.webp` | S3 Console Home (English) | 助理操作後補 |
| `placeholder_06_s3_create_btn_zh.webp` | 「建立儲存桶」按鈕（繁中）| 助理操作後補 |
| `placeholder_06_s3_create_btn_en.webp` | "Create bucket" button (English) | 助理操作後補 |
| `placeholder_06_s3_name_region_zh.webp` | Bucket 名稱與 Region 設定（繁中）| 助理操作後補 |
| `placeholder_06_s3_name_region_en.webp` | Bucket name and Region setting (English) | 助理操作後補 |
| `placeholder_06_s3_block_public_zh.webp` | 封鎖公開存取設定（繁中）| 助理操作後補 |
| `placeholder_06_s3_block_public_en.webp` | Block Public Access settings (English) | 助理操作後補 |
| `placeholder_06_s3_versioning_zh.webp` | 版本控制設定（繁中）| 助理操作後補 |
| `placeholder_06_s3_versioning_en.webp` | Versioning setting (English) | 助理操作後補 |
| `placeholder_06_s3_encryption_zh.webp` | 預設加密設定（繁中）| 助理操作後補 |
| `placeholder_06_s3_encryption_en.webp` | Default encryption setting (English) | 助理操作後補 |
| `placeholder_06_s3_created_zh.webp` | Bucket 建立成功畫面（繁中）| 助理操作後補 |
| `placeholder_06_s3_created_en.webp` | Bucket created success (English) | 助理操作後補 |
| `placeholder_06_s3_cors_zh.webp` | CORS 設定畫面（繁中）| 助理操作後補 |
| `placeholder_06_s3_cors_en.webp` | CORS configuration (English) | 助理操作後補 |

---

### L-239：07 建立 RDS PostgreSQL 資料庫

校對日期 (QA Date)：2026-04-19

| 檢查項 | 狀態 |
|--------|------|
| 有 §1 警告區塊 | ✅ |
| 有 §4 全部固定區塊（預估/名詞/步驟/回報/檢核/FAQ/出錯） | ✅ |
| 中英對照格式一致（無單語言步驟） | ✅ |
| 服務名英文未被誤譯（RDS、VPC、Security Group、gp3 等） | ✅ |
| 截圖 LLM 已讀過、確認對應內容、命名遵循 §3.3 | ✅ |
| placeholder 截圖列入本文件 | ✅ |
| 檢核清單可逐項勾（無模糊項） | ✅ |
| 安全規範 §6 在交付段落落實（Endpoint / Port / DB / User / Pass，禁明文傳送） | ✅ |

#### L-240 票定額外校對項

| 票定檢查項 | 狀態 | 備註 |
|-----------|------|------|
| RDS 與 EC2 同 Region | ✅ | 步驟 1 明確要求「確認右上角區域與您的 EC2 相同」；檢核清單第 2 項確認 |
| RDS SG 只允許 EC2 SG 的 Port 5432（不對外） | ✅ | 步驟 11 專章設定 rds-sg Inbound Rule：來源為 EC2 SG ID，Type = PostgreSQL (5432) |
| Public access = No | ✅ | 步驟 7 第 3 點明確選「否 (No)」，說明禁止網際網路直接存取 |
| 密碼走 1Password 交付 | ✅ | 步驟 5 警告「立即儲存密碼到 1Password / Bitwarden」；交付段落表格 + 禁止管道清單 |

#### 已截圖（公開頁）/ Captured Screenshots

| 檔名 | 對應位置 | 確認內容 |
|------|---------|---------|
| `07_rds_product_zh.webp` | 服務說明 | RDS for PostgreSQL 繁中產品頁，"什麼是 PostgreSQL？" ✅ |
| `07_rds_product_en.webp` | 服務說明 | RDS for PostgreSQL English product page, "What is RDS for PostgreSQL" ✅ |
| `07_rds_pricing_zh.webp` | 費用說明 | RDS 定價頁（繁中），含免費方案、db 執行個體定價 ✅ |
| `07_rds_pricing_en.webp` | 費用說明 | RDS Pricing (English), Free Tier, instance pricing ✅ |

#### 待補截圖（Console 登入後）/ Pending Placeholders

| Placeholder 檔名 | 說明 | 負責人 |
|-----------------|------|--------|
| `placeholder_07_rds_console_zh.webp` | RDS 控制台首頁 — Create database 按鈕（繁中）| 助理操作後補 |
| `placeholder_07_rds_console_en.webp` | RDS Console — Create database button (English) | 助理操作後補 |
| `placeholder_07_rds_create_method_zh.webp` | Standard create 選項（繁中）| 助理操作後補 |
| `placeholder_07_rds_create_method_en.webp` | Standard create option (English) | 助理操作後補 |
| `placeholder_07_rds_engine_zh.webp` | 選擇 PostgreSQL 引擎與 16.x 版本（繁中）| 助理操作後補 |
| `placeholder_07_rds_engine_en.webp` | PostgreSQL engine and version selection (English) | 助理操作後補 |
| `placeholder_07_rds_template_zh.webp` | Free tier / Production Template 選擇（繁中）| 助理操作後補 |
| `placeholder_07_rds_template_en.webp` | Template selection (English) | 助理操作後補 |
| `placeholder_07_rds_credentials_zh.webp` | DB identifier `lattice-cast-pg` + username + password 設定（繁中）| 助理操作後補 |
| `placeholder_07_rds_credentials_en.webp` | DB identifier and credentials setup (English) | 助理操作後補 |
| `placeholder_07_rds_instance_zh.webp` | db.t4g.micro + 20GB gp3 設定（繁中）| 助理操作後補 |
| `placeholder_07_rds_instance_en.webp` | Instance type and storage settings (English) | 助理操作後補 |
| `placeholder_07_rds_vpc_zh.webp` | VPC 選擇 + Public access = No（繁中）| 助理操作後補 |
| `placeholder_07_rds_vpc_en.webp` | VPC and Public access = No (English) | 助理操作後補 |
| `placeholder_07_rds_additional_zh.webp` | Initial DB name `latticecast` + Backup 7 天（繁中）| 助理操作後補 |
| `placeholder_07_rds_additional_en.webp` | Initial DB name and backup settings (English) | 助理操作後補 |
| `placeholder_07_rds_creating_zh.webp` | 資料庫狀態 — Creating（繁中）| 助理操作後補 |
| `placeholder_07_rds_creating_en.webp` | Database status — Creating (English) | 助理操作後補 |
| `placeholder_07_rds_sg_zh.webp` | rds-sg Inbound rule — EC2 SG 來源（繁中）| 助理操作後補 |
| `placeholder_07_rds_sg_en.webp` | rds-sg inbound rule — EC2 SG as source (English) | 助理操作後補 |
| `placeholder_07_rds_endpoint_zh.webp` | RDS Endpoint 位置（繁中）| 助理操作後補 |
| `placeholder_07_rds_endpoint_en.webp` | RDS Endpoint location (English) | 助理操作後補 |

---

## 總目錄 / Master Index (01–07)

### 全篇校對狀態 / QA Status All Articles

| 文章 | 標題 | Story | 校對狀態 | 校對日期 |
|------|------|-------|---------|---------|
| 01 | 註冊 AWS Global 帳號 | Story 1 | ✅ 完成 | 2026-04-19 |
| 02 | 建立 IAM 使用者與 Access Key | Story 1 | ✅ 完成 | 2026-04-19 |
| 03 | 帳單告警與成本控管 | Story 1 | ✅ 完成 | 2026-04-19 |
| 04 | Route 53 域名設置 | Story 2 | ✅ 完成 | 2026-04-19 |
| 05 | 啟動 EC2 執行個體 | Story 3 | ✅ 完成 | 2026-04-19 |
| 06 | 建立 S3 儲存桶 | Story 3 | ✅ 完成 | 2026-04-19 |
| 07 | 建立 RDS PostgreSQL 資料庫 | Story 3 | ✅ 完成 | 2026-04-19 |

---

### 待補截圖總清單 / All Pending Placeholders (01–07)

助理操作後，請逐一截圖並回傳，依檔名命名後補入對應文章。

#### 01 — 註冊 AWS Global 帳號
| Placeholder 檔名 | 說明 |
|-----------------|------|
| `placeholder_01_password_en.webp` | 步驟 3：密碼設定頁面 |
| `placeholder_01_account_type_en.webp` | 步驟 4：帳號類型選擇（Business/Personal）|
| `placeholder_01_payment_en.webp` | 步驟 5：信用卡綁定頁 |
| `placeholder_01_phone_en.webp` | 步驟 6：手機 SMS 驗證頁 |
| `placeholder_01_support_plan_en.webp` | 步驟 7：Support Plan（Basic Free 選擇）|
| `placeholder_01_console_en.webp` | 步驟 8：AWS Console 首頁（Region 下拉）|
| `placeholder_01_mfa_iam_en.webp` | 步驟 9：IAM Security Credentials MFA 設定頁 |

#### 02 — 建立 IAM 使用者與 Access Key
| Placeholder 檔名 | 說明 |
|-----------------|------|
| `placeholder_02_console_search_iam.webp` | Console 頂部搜尋 IAM 的畫面 |
| `placeholder_02_iam_users_create_zh.webp` | IAM Users 頁面點擊 Create user（繁中）|
| `placeholder_02_iam_users_create_en.webp` | IAM Users 頁面點擊 Create user (English) |
| `placeholder_02_iam_username_zh.webp` | 填入 User name: lattice-cast-deploy |
| `placeholder_02_iam_attach_policies_zh.webp` | 選擇 Attach policies directly |
| `placeholder_02_iam_policies_selected_zh.webp` | 5 個 Policy 已勾選的畫面 |
| `placeholder_02_iam_review_create_zh.webp` | Review and Create 確認畫面 |
| `placeholder_02_iam_security_credentials_zh.webp` | 使用者 Security credentials 標籤 |
| `placeholder_02_iam_key_usecase_zh.webp` | 選擇 Use case: Other |
| `placeholder_02_iam_key_created_zh.webp` | Access Key ID + Secret Key 顯示畫面（唯一一次！）|

#### 03 — 帳單告警與成本控管
| Placeholder 檔名 | 說明 |
|-----------------|------|
| `placeholder_03_billing_menu_zh.webp` | 帳號下拉選單繁中 |
| `placeholder_03_billing_menu_en.webp` | Account dropdown menu (English) |
| `placeholder_03_budgets_console_zh.webp` | Budgets 主控台頁面繁中 |
| `placeholder_03_budgets_console_en.webp` | Budgets landing page (English) |
| `placeholder_03_budget_config_zh.webp` | Cost Budget 設定頁繁中 |
| `placeholder_03_budget_config_en.webp` | Cost Budget config page (English) |
| `placeholder_03_alert_threshold_zh.webp` | 告警門檻設定頁繁中 |
| `placeholder_03_alert_threshold_en.webp` | Alert threshold setup (English) |
| `placeholder_03_budget_confirm_zh.webp` | 預算建立確認頁繁中 |
| `placeholder_03_budget_confirm_en.webp` | Budget creation confirm (English) |
| `placeholder_03_cost_explorer_enable_zh.webp` | 啟用 Cost Explorer 頁面繁中 |
| `placeholder_03_cost_explorer_enable_en.webp` | Enable Cost Explorer (English) |
| `placeholder_03_freetier_alert_zh.webp` | Free Tier 告警設定繁中 |
| `placeholder_03_freetier_alert_en.webp` | Free Tier alert setting (English) |

#### 04 — Route 53 域名設置
| Placeholder 檔名 | 說明 |
|-----------------|------|
| `placeholder_04_route53_console_zh.webp` | Route 53 Console 首頁（繁中）|
| `placeholder_04_route53_console_en.webp` | Route 53 Console Home (English) |
| `placeholder_04_route53_search_result_zh.webp` | 域名搜尋結果頁（繁中）|
| `placeholder_04_route53_search_result_en.webp` | Domain Search Results (English) |
| `placeholder_04_route53_contact_zh.webp` | 聯絡資訊填寫頁（繁中）|
| `placeholder_04_route53_contact_en.webp` | Contact Info Form (English) |
| `placeholder_04_route53_order_zh.webp` | 訂單確認頁（繁中）|
| `placeholder_04_route53_order_en.webp` | Order Confirmation (English) |
| `placeholder_04_route53_transfer_btn_zh.webp` | Transfer Domain 按鈕（繁中）|
| `placeholder_04_route53_transfer_btn_en.webp` | Transfer Domain Button (English) |
| `placeholder_04_route53_authcode_zh.webp` | Auth Code 輸入頁（繁中）|
| `placeholder_04_route53_authcode_en.webp` | Auth Code Input (English) |
| `placeholder_04_route53_ns_zh.webp` | Hosted Zone NS 記錄（繁中）|
| `placeholder_04_route53_ns_en.webp` | Hosted Zone NS Records (English) |
| `placeholder_04_route53_create_hz_zh.webp` | Create Hosted Zone 頁面（繁中）|
| `placeholder_04_route53_create_hz_en.webp` | Create Hosted Zone (English) |
| `placeholder_04_route53_hz_ns_zh.webp` | NS Records 顯示（繁中）|
| `placeholder_04_route53_hz_ns_en.webp` | NS Records Display (English) |
| `placeholder_04_route53_hz_id_zh.webp` | Hosted Zone ID 位置（繁中）|
| `placeholder_04_route53_hz_id_en.webp` | Hosted Zone ID Location (English) |

#### 05 — 啟動 EC2 執行個體
| Placeholder 檔名 | 說明 |
|-----------------|------|
| `placeholder_05_ec2_step1_region_zh.webp` | 右上角 Region 選擇器（繁中）|
| `placeholder_05_ec2_step1_region_en.webp` | Region selector top-right (English) |
| `placeholder_05_ec2_step2_launch_btn_zh.webp` | EC2 Dashboard 左側選單與啟動按鈕（繁中）|
| `placeholder_05_ec2_step2_launch_btn_en.webp` | EC2 Dashboard left menu & Launch button (English) |
| `placeholder_05_ec2_step3_name_zh.webp` | 名稱與標籤填寫（繁中）|
| `placeholder_05_ec2_step3_name_en.webp` | Name and Tags input (English) |
| `placeholder_05_ec2_step4_ami_zh.webp` | AMI 選擇 Ubuntu 22.04 LTS（繁中）|
| `placeholder_05_ec2_step4_ami_en.webp` | AMI selection Ubuntu 22.04 LTS (English) |
| `placeholder_05_ec2_step6_keypair_zh.webp` | 建立金鑰對 RSA + .pem 設定（繁中）|
| `placeholder_05_ec2_step6_keypair_en.webp` | Create key pair RSA + .pem settings (English) |
| `placeholder_05_ec2_step7_sg_zh.webp` | 安全群組規則設定（繁中）|
| `placeholder_05_ec2_step7_sg_en.webp` | Security Group rules configuration (English) |
| `placeholder_05_ec2_step8_storage_zh.webp` | 儲存 30 GB gp3 設定（繁中）|
| `placeholder_05_ec2_step8_storage_en.webp` | Storage 30 GB gp3 (English) |
| `placeholder_05_ec2_step9_launch_zh.webp` | 啟動摘要與 Launch 按鈕（繁中）|
| `placeholder_05_ec2_step9_launch_en.webp` | Launch summary & button (English) |
| `placeholder_05_ec2_step10_details_zh.webp` | 執行個體詳細資訊頁（繁中）|
| `placeholder_05_ec2_step10_details_en.webp` | Instance details page (English) |

#### 06 — 建立 S3 儲存桶
| Placeholder 檔名 | 說明 |
|-----------------|------|
| `placeholder_06_s3_console_zh.webp` | S3 Console 首頁（繁中）|
| `placeholder_06_s3_console_en.webp` | S3 Console Home (English) |
| `placeholder_06_s3_create_btn_zh.webp` | 「建立儲存桶」按鈕（繁中）|
| `placeholder_06_s3_create_btn_en.webp` | "Create bucket" button (English) |
| `placeholder_06_s3_name_region_zh.webp` | Bucket 名稱與 Region 設定（繁中）|
| `placeholder_06_s3_name_region_en.webp` | Bucket name and Region setting (English) |
| `placeholder_06_s3_block_public_zh.webp` | 封鎖公開存取設定（繁中）|
| `placeholder_06_s3_block_public_en.webp` | Block Public Access settings (English) |
| `placeholder_06_s3_versioning_zh.webp` | 版本控制設定（繁中）|
| `placeholder_06_s3_versioning_en.webp` | Versioning setting (English) |
| `placeholder_06_s3_encryption_zh.webp` | 預設加密設定（繁中）|
| `placeholder_06_s3_encryption_en.webp` | Default encryption setting (English) |
| `placeholder_06_s3_created_zh.webp` | Bucket 建立成功畫面（繁中）|
| `placeholder_06_s3_created_en.webp` | Bucket created success (English) |
| `placeholder_06_s3_cors_zh.webp` | CORS 設定畫面（繁中）|
| `placeholder_06_s3_cors_en.webp` | CORS configuration (English) |

#### 07 — 建立 RDS PostgreSQL 資料庫
| Placeholder 檔名 | 說明 |
|-----------------|------|
| `placeholder_07_rds_console_zh.webp` | RDS 控制台首頁 — Create database 按鈕（繁中）|
| `placeholder_07_rds_console_en.webp` | RDS Console — Create database button (English) |
| `placeholder_07_rds_create_method_zh.webp` | Standard create 選項（繁中）|
| `placeholder_07_rds_create_method_en.webp` | Standard create option (English) |
| `placeholder_07_rds_engine_zh.webp` | 選擇 PostgreSQL 引擎與 16.x 版本（繁中）|
| `placeholder_07_rds_engine_en.webp` | PostgreSQL engine and version selection (English) |
| `placeholder_07_rds_template_zh.webp` | Free tier / Production Template 選擇（繁中）|
| `placeholder_07_rds_template_en.webp` | Template selection (English) |
| `placeholder_07_rds_credentials_zh.webp` | DB identifier `lattice-cast-pg` + username + password 設定（繁中）|
| `placeholder_07_rds_credentials_en.webp` | DB identifier and credentials setup (English) |
| `placeholder_07_rds_instance_zh.webp` | db.t4g.micro + 20GB gp3 設定（繁中）|
| `placeholder_07_rds_instance_en.webp` | Instance type and storage settings (English) |
| `placeholder_07_rds_vpc_zh.webp` | VPC 選擇 + Public access = No（繁中）|
| `placeholder_07_rds_vpc_en.webp` | VPC and Public access = No (English) |
| `placeholder_07_rds_additional_zh.webp` | Initial DB name `latticecast` + Backup 7 天（繁中）|
| `placeholder_07_rds_additional_en.webp` | Initial DB name and backup settings (English) |
| `placeholder_07_rds_creating_zh.webp` | 資料庫狀態 — Creating（繁中）|
| `placeholder_07_rds_creating_en.webp` | Database status — Creating (English) |
| `placeholder_07_rds_sg_zh.webp` | rds-sg Inbound rule — EC2 SG 來源（繁中）|
| `placeholder_07_rds_sg_en.webp` | rds-sg inbound rule — EC2 SG as source (English) |
| `placeholder_07_rds_endpoint_zh.webp` | RDS Endpoint 位置（繁中）|
| `placeholder_07_rds_endpoint_en.webp` | RDS Endpoint location (English) |

---

### 交付物總清單 / All Deliverables (01–07)

助理完成所有文章後，請透過 **1Password / Bitwarden 共享保險庫** 提供以下資訊：

| 文章 | 交付項目 | 格式 / 範例 |
|------|---------|------------|
| 01 | AWS Account ID | 12 位數字，例：`123456789012` |
| 02 | IAM Access Key ID | `AKIA...`（20 字元）|
| 02 | IAM Secret Access Key | 40 字元隨機字串 |
| 04 | Route 53 Hosted Zone ID | `Z` 開頭，例：`Z1234567890ABC` |
| 04 | 域名 (Domain name) | 例：`example.com` |
| 05 | EC2 Instance ID | 例：`i-0abc123def456789` |
| 05 | EC2 Public IPv4 | 例：`54.123.45.67` |
| 05 | EC2 Security Group ID | 例：`sg-0abc123def456789` |
| 05 | AWS Region | 例：`ap-northeast-1` |
| 05 | Key Pair `.pem` 檔 | `lattice-cast-key.pem`（透過 1Password 附件）|
| 06 | S3 Bucket 名稱 | 例：`lattice-cast-acmecorp-blob` |
| 06 | S3 Bucket Region | 與 EC2 相同，例：`ap-northeast-1` |
| 07 | RDS Endpoint | 例：`lattice-cast-pg.xxx.ap-northeast-1.rds.amazonaws.com` |
| 07 | RDS Port | `5432` |
| 07 | RDS Database Name | `latticecast` |
| 07 | RDS Master Username | `lattice_admin` |
| 07 | RDS Master Password | 16 碼隨機密碼（1Password 存取）|

> ⚠️ **嚴禁透過** LINE、Slack 明文、Telegram、純文字 email、Google Doc 傳送任何上述資訊。

---

_最後更新 / Last Updated：2026-04-19_
