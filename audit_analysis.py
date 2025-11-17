import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('compas-scores-two-years.csv')

df_filtered = df[
    (df['days_b_screening_arrest'] <= 30) &
    (df['days_b_screening_arrest'] >= -30) &
    (df['is_recid'] != -1) &
    (df['c_charge_degree'] != 'O') &
    (df['score_text'] != 'N/A')
].copy()

df_filtered['high_risk'] = (df_filtered['decile_score'] >= 5).astype(int)

def calculate_fairness_metrics(df, group_col, group_value):
    group_data = df[df[group_col] == group_value]
    
    tp = len(group_data[(group_data['high_risk'] == 1) & (group_data['two_year_recid'] == 1)])
    fp = len(group_data[(group_data['high_risk'] == 1) & (group_data['two_year_recid'] == 0)])
    tn = len(group_data[(group_data['high_risk'] == 0) & (group_data['two_year_recid'] == 0)])
    fn = len(group_data[(group_data['high_risk'] == 0) & (group_data['two_year_recid'] == 1)])
    
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
    fnr = fn / (fn + tp) if (fn + tp) > 0 else 0
    ppv = tp / (tp + fp) if (tp + fp) > 0 else 0
    npv = tn / (tn + fn) if (tn + fn) > 0 else 0
    selection_rate = (tp + fp) / len(group_data) if len(group_data) > 0 else 0
    
    return {
        'Group': group_value,
        'Sample Size': len(group_data),
        'False Positive Rate': fpr,
        'False Negative Rate': fnr,
        'Positive Predictive Value': ppv,
        'Negative Predictive Value': npv,
        'Selection Rate': selection_rate
    }

races = ['African-American', 'Caucasian']
metrics_list = []

for race in races:
    metrics = calculate_fairness_metrics(df_filtered, 'race', race)
    metrics_list.append(metrics)

metrics_df = pd.DataFrame(metrics_list)

african_american = metrics_df[metrics_df['Group'] == 'African-American'].iloc[0]
caucasian = metrics_df[metrics_df['Group'] == 'Caucasian'].iloc[0]

disparate_impact = african_american['Selection Rate'] / caucasian['Selection Rate']
fpr_disparity = african_american['False Positive Rate'] / caucasian['False Positive Rate']
fnr_disparity = caucasian['False Negative Rate'] / african_american['False Negative Rate']

print("="*70)
print("COMPAS BIAS AUDIT REPORT")
print("="*70)
print("\nFAIRNESS METRICS BY RACE:")
print(metrics_df.to_string(index=False))

print("\n" + "="*70)
print("DISPARITY ANALYSIS:")
print("="*70)
print(f"Disparate Impact Ratio: {disparate_impact:.3f}")
print(f"  (80% rule threshold: >= 0.8, Current: {'FAIL' if disparate_impact < 0.8 else 'PASS'})")
print(f"\nFalse Positive Rate Ratio (AA/Caucasian): {fpr_disparity:.3f}")
print(f"  African-American FPR: {african_american['False Positive Rate']:.1%}")
print(f"  Caucasian FPR: {caucasian['False Positive Rate']:.1%}")
print(f"\nFalse Negative Rate Ratio (Caucasian/AA): {fnr_disparity:.3f}")
print(f"  African-American FNR: {african_american['False Negative Rate']:.1%}")
print(f"  Caucasian FNR: {caucasian['False Negative Rate']:.1%}")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('COMPAS Racial Bias Analysis', fontsize=16, fontweight='bold')

metrics_plot = metrics_df.set_index('Group')[['False Positive Rate', 'False Negative Rate']]
metrics_plot.plot(kind='bar', ax=axes[0, 0], color=['#e74c3c', '#3498db'])
axes[0, 0].set_title('Error Rates by Race')
axes[0, 0].set_ylabel('Rate')
axes[0, 0].set_xlabel('')
axes[0, 0].legend(['False Positive Rate', 'False Negative Rate'])
axes[0, 0].set_xticklabels(axes[0, 0].get_xticklabels(), rotation=45)
axes[0, 0].axhline(y=0.3, color='red', linestyle='--', alpha=0.5, label='30% threshold')

selection_rates = metrics_df.set_index('Group')['Selection Rate']
selection_rates.plot(kind='bar', ax=axes[0, 1], color=['#9b59b6', '#2ecc71'])
axes[0, 1].set_title('Selection Rate (Predicted High Risk) by Race')
axes[0, 1].set_ylabel('Selection Rate')
axes[0, 1].set_xlabel('')
axes[0, 1].axhline(y=0.8 * selection_rates.max(), color='orange', linestyle='--', 
                    alpha=0.5, label='80% Rule Threshold')
axes[0, 1].set_xticklabels(axes[0, 1].get_xticklabels(), rotation=45)
axes[0, 1].legend()

score_distribution = df_filtered.groupby(['race', 'decile_score']).size().unstack(fill_value=0)
score_distribution_pct = score_distribution.div(score_distribution.sum(axis=1), axis=0) * 100
score_distribution_pct.loc[races].T.plot(kind='bar', ax=axes[1, 0], 
                                          color=['#e67e22', '#1abc9c'])
axes[1, 0].set_title('Risk Score Distribution by Race')
axes[1, 0].set_xlabel('Decile Score')
axes[1, 0].set_ylabel('Percentage (%)')
axes[1, 0].legend(['African-American', 'Caucasian'])

recidivism_by_race = df_filtered.groupby('race')['two_year_recid'].apply(
    lambda x: pd.Series({
        'Recidivated': (x == 1).sum(),
        'Did Not Recidivate': (x == 0).sum()
    })
)
recidivism_by_race_pct = recidivism_by_race.div(recidivism_by_race.sum(axis=1), axis=0) * 100
recidivism_by_race_pct.loc[races].plot(kind='bar', stacked=True, ax=axes[1, 1],
                                        color=['#c0392b', '#27ae60'])
axes[1, 1].set_title('Actual Recidivism Rates by Race')
axes[1, 1].set_ylabel('Percentage (%)')
axes[1, 1].set_xlabel('')
axes[1, 1].legend(['Recidivated', 'Did Not Recidivate'])
axes[1, 1].set_xticklabels(axes[1, 1].get_xticklabels(), rotation=45)

plt.tight_layout()
plt.savefig('compas_bias_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n" + "="*70)
print("Visualizations saved as 'compas_bias_analysis.png'")
print("="*70)