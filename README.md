# Przewidywanie Odejścia Klientów (Telco Customer Churn)

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
   
4. Zainstaluj wymagane biblioteki:

   
   pip install pandas scikit-learn streamlit joblib
   
6. Uruchom aplikację Streamlit:
   
   streamlit run app.py

   SCREENY Z DZIAŁANIA APLIKACJ:
   
![Aplikacja Streamlit](screeny/screen(1).png)

![Aplikacja Streamlit](screeny/screen(2).png)

![Aplikacja Streamlit](screeny/screen(3).png)

![Aplikacja Streamlit](screeny/screen(4).png)

![Aplikacja Streamlit](screeny/screen(5).png)

![Aplikacja Streamlit](screeny/screen(10).png)

SCREENY WYKRESÓW Z GOOGLE COLAB:

![Wykresy](screeny/screen(6).png)

![Wykresy](screeny/screen(7).png)

![Wykresy](screeny/screen(8).png)

![Wykresy](screeny/screen(9).png)

Autor:

Sebastian Czerwiński
