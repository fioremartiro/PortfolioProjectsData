import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar a Python el archivo “hotel_bookings.csv”
df = pd.read_csv('hotel_booking.csv')
# Validate the first 20 records
print(df.head(20))

# 2. Validate that the df contains the total of 119390 registries and columns
print(df.shape)  # Use df.shape to check the number of rows and columns.
print(df.columns)  # List columns to validate they match the original.

# 3. Start cleaning
# Para el campo Children se debe eliminar la etiqueta ‘NA’ y sustituirla con un 0 (Cero)
df["children"] = df["children"].fillna(0)
print(df['children'].isnull().sum())  # Checks sum of null values, we expect 0

# Para el campo Meal se debe eliminar la etiqueta “Undefined” y sustituirla por “AA”
df["meal"] = df["meal"].str.replace("Undefined", "AA")
print(df['meal'].unique())  # Checks unique value to view updates, we should look for "AA"

# Para el Campo Distribution_channel se debe eliminar la etiqueta “Undefined” y sustituirla por “Comercial”
df["distribution_channel"] = df["distribution_channel"].str.replace("Undefined", "Comercial")
print(df['distribution_channel'].unique())  # Checks unique value to view updates, we should look for "Comercial"

# Para el Campo Market_Segment se debe eliminar la etiqueta “Undefined” y sustituirla por “Comercial”
df['market_segment'] = df['market_segment'].str.replace("Undefined", "Comercial")
print(df['market_segment'].unique())  # Checks unique value to view updates, we should look for "Comercial"

# Para el Campo Agent se debe eliminar la etiqueta “Null” y sustituirla por 0 (Cero).
df['agent'] = df['agent'].apply(str).str.replace("NULL", "0")
print(df["agent"].unique())  # Checks unique value to view updates, we should look for 0 value.

# Para el Campo Company se debe eliminar la etiqueta “Null” y sustituirla por 0 (Cero).
df['company'] = df['company'].apply(str).str.replace("NULL", "0")
print(df["company"].unique())  # Checks unique value to view updates, we should look for 0 value.

# Asegúrese que no queden columnas con valores nulos, indefinidos o incongruentes, de ser así elimine estos registros del dataframe.
print(df.isnull().sum())  # Checks for null values, if we find drop those tables and Country has 488 records
df.dropna(subset=['country'], inplace=True)  # Drop the records from Country.
print(df.isnull().sum())  # Checks for null values, if we find drop those tables and Country has 0 records now.

# 4. Después de haber realizado la limpieza o depuración de datos, se debe realizar la siguiente transformación a la estructura de la tabla:
# Modificar el campo 'Children' para que ahora sea entero.
print(df.dtypes['children'])  # Checks the type which is initially a float
df['children'] = df['children'].astype(int)
print(df.dtypes['children'])  # Checks the type which is now a float/ entero

# Modificar el campo 'Agent' para que ahora sea entero.
print(df.dtypes['agent'])  # Checks the type which is initially an object
df['agent'] = pd.to_numeric(df['agent'], errors='coerce').convert_dtypes()  # I convert here from object to numeric,`convert_dtypes` call to convert to nullable int
print(df.dtypes['agent'])  # Checks the type which now is a int

# Modificar el campo 'Company' para que ahora sea entero.
print(df.dtypes['company'])  # Checks the type which is initially an object
df['company'] = pd.to_numeric(df['company'], errors='coerce').convert_dtypes() # I convert here from object to numeric,`convert_dtypes` call to convert to nullable int
print(df.dtypes['company'])  # Checks the type which is initially an object and now is a Int

# 5. Por último, obtenga los siguientes patrones que se pudieron presentar con los datos del hotel, puede utilizar herramientas de visualización para mostrar el resultado:
# Cantidad de reservaciones que se cancelaron y las que no por cada año.
reservations_by_year = df.groupby(['arrival_date_year', 'is_canceled']).size().unstack(fill_value=0)
reservations_by_year.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Cantidad de reservaciones canceladas y no canceladas por año')
plt.xlabel('Año de llegada')
plt.ylabel('Cantidad de reservaciones')
plt.legend(['No canceladas', 'Canceladas'])
plt.show()

# Cantidad de niños y bebes que estuvieron en las reservaciones que no se cancelaron.
non_canceled_reservations = df[df['is_canceled'] == 0]
children_babies = non_canceled_reservations[['children', 'babies']].sum()
children_babies.plot(kind='bar', figsize=(8, 6))
plt.title('Cantidad de niños y bebés en reservaciones no canceladas')
plt.xlabel('Categoría')
plt.ylabel('Cantidad')
plt.show()

# Cantidad de adultos que estuvieron según las reservaciones que no se cancelaron.
adults_count = non_canceled_reservations['adults'].sum()
print(f'Cantidad total de adultos en reservaciones no canceladas: {adults_count}')

# Cantidad de reservas por market_segment que no fueron canceladas.
reservations_by_market_segment = non_canceled_reservations['market_segment'].value_counts()
reservations_by_market_segment.plot(kind='bar', figsize=(10, 6))
plt.title('Cantidad de reservas por market_segment que no fueron canceladas')
plt.xlabel('Segmento de mercado')
plt.ylabel('Cantidad de reservaciones')
plt.show()

# Save the cleaned and processed DataFrame to a CSV file
output_file_path = 'hotel_bookings_cleaned.csv'
df.to_csv(output_file_path, index=False)
