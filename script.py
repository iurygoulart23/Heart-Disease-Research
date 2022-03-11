# import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import binom_test

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

# print(yes_hd.head())
# print(no_hd.head())

#1
chol_hd = yes_hd.chol

#2 calculate the average cholesterollevel for patients who have heart disease
mean_chol_hd = np.mean(chol_hd)
print('The average cholesterol of heart disease patients:', mean_chol_hd)
#the average cholesterol is higher thant the healthy status

#3, 4
tstat, pval = ttest_1samp(chol_hd, 240)
print('The p-value for hd patients:',pval/2, '\n')
#the patients have a cholesterol significantly higher than the average because the p-value is smaller than the significance threshold of 0.05

#5 repeating the steps to patients without heart disease
chol_no_hd = no_hd.chol
mean_chol_no_hd = np.mean(chol_no_hd)
print('The average cholesterol of no heart disease patients:',mean_chol_no_hd)

tstat, pval = ttest_1samp(chol_no_hd, 240)
print('The p-value for no hd patients:',pval/2, '\n')
#the p-value is greater than the significance threshold of 0.05 so the chol mean is not significantly higher than the healthy status

#6 lets discover how many patients do we have
num_patients = len(heart)
print('There are {} patients in the dataset'.format(num_patients), '\n')

#7 calculating the number of patients have fasting blood sugar greater than 120 mg/dl
num_highfbs_patients = np.sum(heart.fbs == 1)
print('There are {} patients with fasting blood sugar greater than 120 mg/dl'.format(num_highfbs_patients), '\n')

#8 calculating the number of diabetes patients in a population with 303 patients with 8% chance to have the disease
diabetes_chance = 0.08 * num_patients
print('The total patients of 8% chance to have diabetes in a population of 303 patients are:', round(diabetes_chance, 4), '\n')

#9, 10 hypothesis test Null: sample was drawn from a population where 8% of people have fasting blood sugar >120, Alternative: more than 8% have fasting blood sugar > 120
pval = binom_test(num_highfbs_patients, num_patients, .08, alternative='greater')
print(pval)
