# Przewidywanie Odejścia Klientów (Telco Customer Churn)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange.svg)

## Opis Projektu
Projekt ten rozwiązuje jeden z najważniejszych problemów w branży telekomunikacyjnej: **Customer Churn** (rezygnacja klientów z usług). Głównym celem było zbudowanie modelu uczenia maszynowego, który na podstawie danych historycznych potrafi zidentyfikować klientów z wysokim ryzykiem odejścia do konkurencji.

Dzięki temu firma może podjąć działania prewencyjne (np. zaoferować zniżkę), zanim klient faktycznie zerwie umowę. Projekt został zwieńczony **interaktywną aplikacją webową** napisaną w Streamlit, która pozwala na wprowadzanie danych klienta i wyliczanie ryzyka w czasie rzeczywistym.

## Główne Wnioski Biznesowe i Wyzwania
1. **Niezbalansowanie klas (Class Imbalance):** W zbiorze danych tylko ~27% klientów odeszło z firmy. Aby zmusić model do skutecznego wyłapywania takich przypadków, zastosowałem technikę ważenia klas (`class_weight='balanced'`).
2. **Interpretowalność vs Skomplikowanie:** Przetestowałem potężne algorytmy takie jak Random Forest oraz CatBoost. Ostatecznie najlepiej sprawdziła się **Zbalansowana Regresja Logistyczna**. Osiągnęła najwyższy wskaźnik Czułości (Recall) dla klasy mniejszościowej i była najprostsza do zinterpretowania pod kątem biznesowym.
3. **Kluczowe czynniki odejść (Feature Importance):**
   * **Odpychające:** Umowy z miesiąca na miesiąc (Month-to-month) oraz wysokie opłaty miesięczne.
   * **Zatrzymujące:** Długi staż klienta (Tenure) oraz umowy długoterminowe (Two-year contract).

## Wykorzystane Technologie
* **Język:** Python
* **Analiza i obróbka danych:** Pandas, NumPy
* **Wizualizacja:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (Logistic Regression, Random Forest), CatBoost
* **Wdrożenie (Deployment):** Streamlit, Joblib

## Jak uruchomić aplikację lokalnie?

1. Sklonuj to repozytorium na swój komputer:
   git clone https://github.com/sebastianczerwinski2/clients_classification.git
2. Zainstaluj wymagane biblioteki:
   pip install pandas scikit-learn streamlit joblib
3. Uruchom aplikację Streamlit:
   streamlit run app.py

   SCREENY Z DZIAŁANIA APLIKACJ:
<img width="892" height="951" alt="Zrzut ekranu 2026-03-31 131639" src="https://github.com/user-attachments/assets/0be9c955-8d4e-407c-abb8-412304d1c567" />
<img width="868" height="931" alt="Zrzut ekranu 2026-03-31 131630" src="https://github.com/user-attachments/assets/a9da1331-4703-4128-8524-18de3ca7fa58" />
<img width="819" height="858" alt="Zrzut ekranu 2026-03-31 131846" src="https://github.com/user-attachments/assets/b1a91d4e-ea00-4475-8974-b22a39fa2ba9" />
<img width="828" height="861" alt="Zrzut ekranu 2026-03-31 131749" src="https://github.com/user-attachments/assets/a9130585-7713-43f3-86db-64546029c038" />
<img width="821" height="865" alt="Zrzut ekranu 2026-03-31 131726" src="https://github.com/user-attachments/assets/0d6237b5-a5a8-485f-bcad-b7dab0bc0007" />
<img width="837" height="937" alt="Zrzut ekranu 2026-03-31 131654" src="https://github.com/user-attachments/assets/ec92c495-3493-4436-bcf3-41f9a163750b" />

SCREENY WYKRESÓW Z GOOGLE COLAB:
<img width="651" height="548" alt="Zrzut ekranu 2026-03-31 132433" src="https://github.com/user-attachments/assets/88d6bad9-cd22-4747-a063-7979917db211" />
<img width="666" height="549" alt="Zrzut ekranu 2026-03-31 132429" src="https://github.com/user-attachments/assets/de0fb62c-65aa-4db4-8fef-f2f00650b98a" />
<img width="1157" height="422" alt="Zrzut ekranu 2026-03-31 132418" src="https://github.com/user-attachments/assets/2d40043e-1932-4db3-960f-0db4519591c8" />
<img width="995" height="793" alt="Zrzut ekranu 2026-03-31 132414" src="https://github.com/user-attachments/assets/0a9ba360-3ddb-4287-acdd-e6e38d50e7ae" />

Autor:
Sebastian Czerwiński
