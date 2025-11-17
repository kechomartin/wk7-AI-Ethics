# AI Ethics Assignment - README

## Designing Responsible and Fair AI Systems

## 📋 Project Overview

This assignment evaluates our understanding of AI ethics principles, ability to identify and mitigate biases, and skill in applying ethical frameworks to real-world scenarios. We analyzed case studies, audited AI systems for bias, and proposed solutions to ethical dilemmas.

---

## 📁 Repository Structure

```
ai-ethics-assignment/
│
├── README.md                          # This file
├── written_answers.pdf                # Parts 1, 2, and 4 responses
├── compas_bias_audit.py              # Part 3: COMPAS dataset analysis
├── compas_bias_analysis.png          # Generated visualizations
├── healthcare_ai_policy.pdf          # Bonus: Policy proposal
├── compas-scores-two-years.csv       # Dataset (not included - see below)
└── requirements.txt                   # Python dependencies
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/[your-username]/ai-ethics-assignment.git
   cd ai-ethics-assignment
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the COMPAS dataset**
   
   Download `compas-scores-two-years.csv` from [ProPublica's GitHub](https://github.com/propublica/compas-analysis)
   
   Or use this direct link:
   ```bash
   wget https://raw.githubusercontent.com/propublica/compas-analysis/master/compas-scores-two-years.csv
   ```

### Running the Bias Audit

```bash
python compas_bias_audit.py
```

This will:
- Load and preprocess the COMPAS dataset
- Calculate fairness metrics across racial groups
- Generate visualizations showing bias disparities
- Print a detailed audit report to the console
- Save visualizations as `compas_bias_analysis.png`

---

## 📊 Assignment Components

### Part 1: Theoretical Understanding (30%)
**Location:** `written_answers.pdf` (Pages 1-3)

- Short answer questions on algorithmic bias, transparency, and GDPR
- Ethical principles matching exercise

### Part 2: Case Study Analysis (40%)
**Location:** `written_answers.pdf` (Pages 4-7)

**Case 1: Amazon's Biased Hiring Tool**
- Source of bias identification
- Three proposed fixes
- Fairness evaluation metrics

**Case 2: Facial Recognition in Policing**
- Ethical risks discussion
- Policy recommendations for responsible deployment

### Part 3: Practical Audit (25%)
**Location:** `compas_bias_audit.py`

- Bias analysis of COMPAS recidivism risk assessment
- Fairness metrics calculation (FPR, FNR, Disparate Impact)
- Data visualizations
- 300-word audit report (included in console output)

### Part 4: Ethical Reflection (5%)
**Location:** `written_answers.pdf` (Pages 8-9)

- Personal reflection on applying ethical AI principles to future projects

### Bonus Task: Healthcare AI Policy (10%)
**Location:** `healthcare_ai_policy.pdf`

- 1-page ethical AI guidelines for healthcare
- Patient consent protocols
- Bias mitigation strategies
- Transparency requirements

---

## 🔍 Key Findings

Our COMPAS audit revealed significant racial bias:

- **False Positive Rate:** African-American defendants experience 44.9% FPR vs 23.5% for Caucasian defendants (1.91x higher)
- **False Negative Rate:** Caucasian defendants have 47.7% FNR vs 28.0% for African-American defendants
- **Disparate Impact:** Selection rate ratio of 0.66 (fails the 80% rule)

**Conclusion:** The COMPAS system perpetuates racial injustice and should not be used in its current form.

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **Pandas** - Data manipulation
- **NumPy** - Numerical computations
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical visualizations
- **Scikit-learn** - Machine learning metrics

---

## 📚 Resources & References

- [AI Fairness 360 (IBM)](https://github.com/Trusted-AI/AIF360)
- [ProPublica COMPAS Analysis](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)
- [EU Ethics Guidelines for Trustworthy AI](https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai)
- [GDPR Official Text](https://gdpr-info.eu/)

---
## 📝 License

This project is submitted as coursework for PLP Academy's AI Ethics module.

---

## 🤝 Acknowledgments

- PLP Academy instructors and community
- ProPublica for making the COMPAS dataset publicly available
- IBM for the AI Fairness 360 toolkit

---

## 📧 Contact

For questions about this assignment:
- **PLP Community:** #AIEthicsAssignment

* Designing Responsible and Fair AI Systems
