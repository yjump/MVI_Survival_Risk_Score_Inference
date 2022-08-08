# [Hepatology International] A deep learning model with incorporation of microvascular invasion area as a factor in predicting prognosis of hepatocellular carcinoma after R0 hepatectomy

## Introduction
This is the inference code and the saved model for "A deep learning model with incorporation of microvascular invasion area as a factor in predicting prognosis of hepatocellular carcinoma after R0 hepatectomy" published in Hepatology International.

The model takes in four input features and predict a MVI survival risk score for each patient. Please refer to the paper for more details. 

## Dependencies:

Python 3.6+;

pandas;

torch;

numpy;

## Usage:

1. Prepare your data following the demo input file "./Input_Patient_Info.cvs".

2. Pay attention to the input file path and run:

```
python3 mvi_risk_predict.py
```

3. Obtain the prediction file "./Output_Patient_Info_with_Risk_Score".

## Disclaimer:

This tool is for research purpose and not approved for clinical use.

This is not an official Tencent product.

## Citation:

Please consider citing our paper in your publications if the project helps your research.

@article{wang2022a,

  title={A deep learning model with incorporation of microvascular invasion area as a factor in predicting prognosis of hepatocellular carcinoma after R0 hepatectomy},

  author={Kang, Wang and Yanjun, Xiang and Jiangpeng, Yan and Others},

  journal={Hepatology International},

  year={2022},

  publisher={Springer}
}

