# E-commerce Campaign Performance Analysis Scenario

## Business Question
**Analyze quarterly digital marketing campaign performance by aggregating individual campaign executions to show each Marketing Manager's overall effectiveness, including total revenue generated, conversion rates, cost efficiency, and ROI metrics.**

---

## Input Data Structure

### Campaign Executions Table
Each row represents a single marketing campaign execution with the following columns:

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| campaign_id | String | Unique identifier for each campaign execution |
| marketing_manager | String | Name of the manager overseeing campaigns |
| campaign_specialist | String | Name of the specialist who executed the campaign |
| platform | String | Marketing platform (Google Ads, Facebook, Instagram, LinkedIn, TikTok) |
| campaign_budget | Decimal | Total budget spent on campaign (in USD) |
| revenue_generated | Decimal | Revenue attributed to campaign (in USD) |
| impressions | Integer | Number of ad impressions |
| clicks | Integer | Number of clicks received |
| conversions | Integer | Number of completed purchases |
| campaign_start_date | Date | Campaign launch date |
| campaign_type | String | Type of campaign (Brand Awareness, Lead Gen, Direct Sales, Retargeting) |
| target_audience | String | Primary audience (Young Adults, Professionals, Seniors, Students) |

### Sample Input Data (First 10 rows)

| campaign_id | marketing_manager | campaign_specialist | platform | campaign_budget | revenue_generated | impressions | clicks | conversions | campaign_start_date | campaign_type | target_audience |
|-------------|-------------------|---------------------|----------|-----------------|-------------------|-------------|--------|-------------|---------------------|---------------|-----------------|
| C1001 | Jennifer Martinez | Alex Thompson | Google Ads | 5,000 | 25,000 | 150,000 | 4,500 | 125 | 2024-01-05 | Direct Sales | Professionals |
| C1002 | Jennifer Martinez | Sarah Kim | Facebook | 3,500 | 18,500 | 200,000 | 6,000 | 92 | 2024-01-08 | Brand Awareness | Young Adults |
| C1003 | Jennifer Martinez | Alex Thompson | Instagram | 4,200 | 21,000 | 180,000 | 5,400 | 105 | 2024-01-12 | Direct Sales | Young Adults |
| C1004 | Robert Jackson | Michael Chang | LinkedIn | 6,500 | 32,500 | 100,000 | 3,000 | 162 | 2024-01-06 | Lead Gen | Professionals |
| C1005 | Robert Jackson | Emily Davis | Google Ads | 5,800 | 29,000 | 175,000 | 5,250 | 145 | 2024-01-10 | Direct Sales | Professionals |
| C1006 | Robert Jackson | Michael Chang | TikTok | 2,800 | 14,000 | 250,000 | 7,500 | 70 | 2024-01-15 | Brand Awareness | Students |
| C1007 | Amanda Foster | David Lee | Facebook | 4,500 | 22,500 | 190,000 | 5,700 | 112 | 2024-01-07 | Retargeting | Returning |
| C1008 | Amanda Foster | Rachel Green | Instagram | 3,900 | 19,500 | 165,000 | 4,950 | 97 | 2024-01-11 | Direct Sales | Young Adults |
| C1009 | Amanda Foster | David Lee | Google Ads | 5,500 | 27,500 | 160,000 | 4,800 | 137 | 2024-01-14 | Lead Gen | Professionals |
| C1010 | Daniel Park | Lisa Wang | LinkedIn | 7,000 | 35,000 | 120,000 | 3,600 | 175 | 2024-01-09 | Lead Gen | Professionals |

---

## Expected Output Structure

### Aggregated Performance by Marketing Manager

The output should aggregate all campaign executions to the Marketing Manager level with these columns:

| Column Name | Calculation Method | Description |
|-------------|-------------------|-------------|
| marketing_manager | GROUP BY | Name of the Marketing Manager |
| total_campaigns | COUNT | Total number of campaigns executed |
| total_budget_spent | SUM | Total budget across all campaigns |
| total_revenue_generated | SUM | Total revenue from all campaigns |
| roi_percentage | CALCULATED | (Total Revenue - Total Budget) / Total Budget * 100 |
| total_impressions | SUM | Total ad impressions across campaigns |
| total_clicks | SUM | Total clicks across campaigns |
| total_conversions | SUM | Total conversions across campaigns |
| avg_click_through_rate | CALCULATED | (Total Clicks / Total Impressions) * 100 |
| avg_conversion_rate | CALCULATED | (Total Conversions / Total Clicks) * 100 |
| cost_per_conversion | CALCULATED | Total Budget / Total Conversions |

### Sample Expected Output

| marketing_manager | total_campaigns | total_budget_spent | total_revenue_generated | roi_percentage | total_impressions | total_clicks | total_conversions | avg_click_through_rate | avg_conversion_rate | cost_per_conversion |
|-------------------|----------------|-------------------|------------------------|---------------|------------------|--------------|-------------------|----------------------|---------------------|---------------------|
| Jennifer Martinez | 48 | $215,400 | $1,077,000 | 400.0% | 8,640,000 | 259,200 | 5,390 | 3.0% | 2.08% | $39.96 |
| Robert Jackson | 52 | $268,000 | $1,340,000 | 400.0% | 9,360,000 | 280,800 | 6,696 | 3.0% | 2.38% | $40.02 |
| Amanda Foster | 45 | $196,200 | $981,000 | 400.0% | 8,100,000 | 243,000 | 5,062 | 3.0% | 2.08% | $38.76 |
| Daniel Park | 55 | $302,500 | $1,512,500 | 400.0% | 9,900,000 | 297,000 | 7,425 | 3.0% | 2.50% | $40.74 |

---

## Analysis Requirements

1. **Aggregation Level**: Group all individual campaign executions by Marketing Manager only
2. **Time Period**: Q1 2024 (January - March)
3. **Metrics to Calculate**:
   - Sum of all budget spent per manager
   - Sum of all revenue generated per manager
   - ROI percentage: ((Revenue - Budget) / Budget) * 100
   - Average click-through rate: (Total Clicks / Total Impressions) * 100
   - Average conversion rate: (Total Conversions / Total Clicks) * 100
   - Cost per conversion: Total Budget / Total Conversions
4. **No Individual Details**: Output should NOT show individual campaign specialists or campaign breakdowns
5. **Sorting**: Order results by total_revenue_generated descending
6. **Formatting**: 
   - Currency values with $ and comma separators
   - Percentages with 1-2 decimal places
   - Whole numbers for counts

---

## Business Use Cases

This aggregated view helps answer:
- Which Marketing Manager is delivering the highest ROI?
- Which manager's campaigns are most cost-efficient?
- Which manager has the best conversion rates?
- How does total spend correlate with revenue generation?
- Which managers need additional budget or training?
- Are certain managers better at specific campaign types?

---

## Key Differences from Team-Level Analysis

Unlike team-level analysis that shows individual contributors:
- **No team member breakdown** - Individual campaign specialists are in input but not in output
- **Manager-level summary only** - All metrics rolled up to manager level
- **Simplified output** - Fewer columns, focused on key performance indicators
- **Strategic view** - Designed for executive decision-making rather than team management