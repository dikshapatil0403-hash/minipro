# Auto Claim Report Generator - User Guide

## 🎯 Overview
The Auto Claim Report Generator is a professional reporting system that allows insurance administrators to generate, view, and download comprehensive fraud detection and risk assessment reports for individual insurance claims.

## ✨ Features

### Professional Report Content
- **Fraud Risk Assessment** - Displays fraud probability percentage, risk level (LOW/MEDIUM/HIGH), and model confidence
- **Claim Details** - Complete claimant information, vehicle details, and accident information  
- **Financial Analysis** - Claim amount, dates, and claim status
- **Timeline Analysis** - Accident date, days to claim submission, previous claims history
- **Risk Factors** - Key risk indicators with impact percentages based on ML analysis
- **Professional Layout** - Clean, organized presentation with color-coded risk indicators

### Easy Access
- Available directly in the Claim Status section of the admin dashboard
- One-click "Generate Report" button
- Professional modal view for immediate preview
- Download as PDF or print directly

## 📋 How to Generate a Report

### Step 1: Navigate to Claim Status
1. Log in to the Admin Dashboard
2. Click on **"Claim Status"** in the sidebar menu

### Step 2: Select a Claim
1. Click on any claim row in the table
2. The claim details will appear in the right panel

### Step 3: Generate Report
1. In the claim details panel, click the **"📊 Generate Report"** button
2. A professional report modal will open
3. The system will fetch and compile all claim data and fraud analysis

### Step 4: View & Download
The report modal displays:
- **Report Preview** - Full formatted report with all sections
- **Close Button** - Close the modal
- **Download PDF Button** - Save the report as a PDF file

## 📊 Report Sections Explained

### Fraud Risk Assessment
Shows four key metrics:
- **Fraud Probability**: Percentage likelihood of fraud (0-100%)
- **Risk Level**: Classification (LOW, MEDIUM, HIGH)
- **Model Confidence**: How confident the AI model is in its assessment (0-100%)
- **System Version**: Report generation system version

Color coding:
- 🟢 LOW RISK: Green (< 25% fraud probability)
- 🟡 MEDIUM RISK: Yellow (25-50% fraud probability)
- 🔴 HIGH RISK: Red (> 50% fraud probability)

### Claimant Information
- Full name
- Email address
- Phone number
- Unique claim ID

### Vehicle Information
- Vehicle make and model
- Year and age of vehicle
- Accident location
- Description of damage

### Financial Details
- Claim amount (in INR ₹)
- Date claim was filed
- Current claim status (Pending/Approved/Rejected)

### Timeline Analysis
- Date of accident
- Number of days between accident and claim submission
- Number of previous claims filed by claimant

### Key Risk Factors
ML-identified risk factors with:
- Factor name (e.g., "Claim Amount", "Vehicle Age")
- Impact percentage (how much it contributes to the risk score)
- Risk classification for that factor

## 💾 Download & Print Options

### Download as PDF
1. Click **"⬇️ Download PDF"** button in the report modal
2. Report will be saved as `Claim_Report_[ClaimID]_[Timestamp].pdf`
3. File opens in default PDF viewer or downloads to your computer

### Print Report
1. Click **"⬇️ Download PDF"** button (or use browser print function)
2. Select your printer
3. Report will be printed with professional formatting
4. Optimized layout for both color and black & white printing

## 🎨 Report Design

The report features:
- **Professional Header** - With gradient background and report title
- **Color-Coded Risk Summary** - Visual indication of risk level
- **Two-Column Layout** - For efficient information presentation
- **Clear Typography** - Easy to read font sizes and hierarchy
- **Organized Sections** - Logical grouping of related information
- **Footer** - Generation timestamp and copyright information

## 🔍 Data Sources

All report data comes from:
1. **Claims Database** - Claimant, vehicle, and accident information
2. **ML Fraud Model** - AI-powered fraud probability and risk scoring
3. **System Analysis** - Timeline and historical claim analysis
4. **Feature Extraction** - Automated detection of key risk factors

## ⚙️ Technical Details

### Backend Processing
- `generate_report.php` - Fetches and compiles report data
- `download_report.php` - Generates formatted HTML and PDF output

### Frontend Components
- Modal interface for report viewing
- Real-time report generation
- Client-side and server-side PDF generation options
- Print-optimized CSS styling

### Data Processing
- ML model predictions (fraud probability, risk level, confidence)
- Fallback calculations if ML model unavailable
- Feature importance analysis
- Historical data aggregation

## 📈 Fraud Probability Scale

Understanding the numbers:
- **0-24%**: Low risk - standard claim processing recommended
- **25-49%**: Medium risk - requires additional verification
- **50-74%**: High risk - detailed investigation recommended
- **75-100%**: Critical risk - claim suspension and forensic audit

## 💡 Tips for Using Reports

1. **Regular Monitoring** - Generate reports for high-risk claims during batch review
2. **Documentation** - Download PDF reports for claim files and auditing
3. **Trend Analysis** - Review multiple reports to identify patterns
4. **Decision Support** - Use report data to support claim approval/rejection decisions
5. **Record Keeping** - Archive reports for compliance and audit trails

## 🚀 Keyboard Shortcuts

- **ESC Key** - Close report modal (if modal is focused)
- **Ctrl/Cmd + P** - Open print dialog while viewing report

## ❓ Troubleshooting

### Report Won't Generate
- Ensure the claim is properly selected
- Check that the claim ID exists in the database
- Verify Python ML model is running (if using advanced fraud detection)

### PDF Download Issues
- Try using the print preview method instead
- Ensure your browser allows downloads
- Check available disk space
- Try a different browser if issues persist

### Slow Report Generation
- Large datasets may take a few seconds to compile
- ML model predictions take longer if system is under load
- Try generating reports during off-peak hours

## 📞 Support

For issues or feature requests:
- Contact: admin@insurance.com
- System Version: 1.0
- Last Updated: 2026

---

**Note**: This report is generated automatically by the Insurance Fraud Detection System. All data is confidential and should be handled according to company policy.
