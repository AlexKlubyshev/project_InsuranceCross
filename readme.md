# Прогнозирование перекрёстных продаж медицинского страхования

## Задача
Предсказать владельцев медицинской страховки, которые заинтересованы в страховании автомобилей

## Данные
- **Источник:** [Kaggle: Health Insurance Cross Sell Prediction](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction)
- **Размер:** 381109 строк, 11 признаков
- **Целевая переменная:** 'Response' (бинарная: 0 - не заинтересован, 1 - заинтересован)

## Что сделано
1. **EDA и анализ корреляций**
2. **Предобработка признаков:** Frequency Encoding, Target Encoding, Feature Engineering
3. **Сравнение моделей** (кросс-валидация): LogisticRegression, LGBMClassifier, MClassifier, Random Forest, XGBoost, CatBoost
4. **Борьба с дисбалансом:** SMOTE + UnderSampling, параметр 'scale_pos_weight'
5. **Калибровка вероятностей** и подбор оптимального порога
6. **Подбор гиперпараметров:** RandomizedSearchCV
7. **Ансамбли:** Voting и Stacking
8. **Проектирование архитектуры нейросети:** (опционально)
9. **интерпретация результатов** модели

## Результаты
**Лучшая модель:** LightGBM с калибровкой вероятностей (оптимальный порог = 0.233)
- **ROC-AUC:** 0.86
- **F1-score:** 0.46

## Стек технологий
Python, Pandas, NumPy, Scikit-learn, LightGBM, XGBoost, CatBoost, Matplotlib, Seaborn, Imbalanced-learn 

## Установка и запуск
### 1. Клонирование репозитория
git clone https://github.com/AlexKlubyshev/project_InsuranceCross.git
cd project_InsuranceCross

### 2. Создание окружения используя conda(рекомендуемый способ) 
conda env create -f environment.yml
conda activate ml_base

### 3. Альтернативная установка (через pip): 
   pip install -r requirements.txt

### 4. Запуск проекта
jupyter notebook notebooks/insurance_cross_sell_prediction.ipynb

## Зависимости

Полный список зависимостей находится в файлах:
- environment.yml — для установки через conda
- requirements.txt — для установки через pip

## Основные библиотеки:

- Python 3.11
- pandas, numpy, scikit-learn
- lightgbm, xgboost, catboost
- matplotlib, seaborn
- jupyterlab

## Структура проекта

project_InsuranceCross/<br>
├── data/ # Данные (или ссылки на них)<br>
├── notebooks/ # Jupyter ноутбуки<br>
│ └── insurance_cross_sell_prediction.ipynb<br>
├── src/<br>
├── models/<br> 
├── environment.yml # Conda environment<br>
├── requirements.txt # Pip requirements<br>
└── README.md