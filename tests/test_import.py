import sys
print(f"Python {sys.version.split()[0]}\n")

# Список для проверки
libs_to_test = [
    ("tensorflow","2.13"),
    ("numpy", "1.24.3"),
    ("scipy", "1.10.1"),
    ("sklearn", "1.3.0"),
    ("catboost", "1.2.7"),
    ("lightgbm", "4.6.0"),
    ("xgboost", "3.1.3"),
    ("imblearn", "0.10.1"),
    ("pandas", None),
    ("matplotlib", None),
    ("seaborn", None),
    ("plotly", None),
]

for lib_name, expected_version in libs_to_test:
    try:
        if lib_name == "tensorflow":
            import tensorflow as lib
        elif lib_name == "sklearn":
            import sklearn as lib
        elif lib_name == "imblearn":
            import imblearn as lib
        else:
            lib = __import__(lib_name)
        
        version = getattr(lib, '__version__', 'unknown')
        
        if expected_version and version == expected_version:
            print(f"✅ {lib_name}=={version}")
        elif expected_version:
            print(f"⚠  {lib_name}: {version} (ожидалось {expected_version})")
        else:
            print(f"✅ {lib_name}: {version}")
            
    except ImportError as e:
        print(f"❌ {lib_name}: {e}")
    except Exception as e:
        print(f"❌ {lib_name} ошибка: {e}")

# Проверяем проблемные импорты из imblearn
print("\n" + "="*50)
print("Проверка imblearn компонентов:")

try:
    from imblearn.pipeline import Pipeline
    print("✅ imblearn.pipeline.Pipeline")
except Exception as e:
    print(f"❌ imblearn.pipeline: {e}")

try:
    from imblearn.over_sampling import SMOTE
    print("✅ imblearn.over_sampling.SMOTE")
except Exception as e:
    print(f"❌ imblearn.over_sampling: {e}")

try:
    from imblearn.under_sampling import RandomUnderSampler
    print("✅ imblearn.under_sampling.RandomUnderSampler")
except Exception as e:
    print(f"❌ imblearn.under_sampling: {e}")