# 🌍 Global Waste & Recycling Analysis  
**Excel Dashboard & Python (pandas) Data Analysis**

This project analyzes **municipal solid waste (MSW) generation and recycling performance** across countries using a combination of **interactive Excel dashboards** and **reproducible Python analysis**.

The objective is to compare waste generation, recycling rates, and treatment methods across **income groups and regions**, while identifying **top-performing and underperforming countries**.

---

## 📊 Dataset Overview

The dataset contains country-level indicators related to population, waste generation, recycling performance, and waste treatment methods.

### Key Columns
- `country_name`, `iso3c`, `region_id`
- `Income_Label` *(High / Upper-middle / Lower-middle / Low income)*
- `population_population_number_of_people`
- `MSW_per_capita (kg/year)`
- `Recycling gap (%)`
- `waste_treatment_recycling_percent`
- `waste_treatment_incineration_percent`
- `waste_treatment_controlled_landfill_percent`
- `waste_treatment_open_dump_percent`
- `waste_treatment_compost_percent`
- `Recycling performance` *(Low / Medium / High)*

---

## ✅ Excel Component  
### **Dashboard: Global Waste & Recycling Overview**

The Excel file contains an interactive dashboard built with **PivotTables, PivotCharts, KPI cards, and slicers**.

### 🔢 KPI Cards
- Average MSW per Capita (kg/year)
- Average Recycling Gap (%)
- Average Recycling Rate (%)

### 📈 Visualizations
- Country Distribution Across Income Groups  
- Recycling Performance by Income Group  
- Top Countries with Highest Recycling Rates  
- Waste Treatment Method Comparison by Income Group:
  - Recycling  
  - Incineration  
  - Controlled landfill  
  - Open dump  
  - Composting  

### 🎛 Interactive Filters (Slicers)
- `Income_Label`
- `Recycling performance`

All slicers are connected to the underlying PivotTables to dynamically update the dashboard visuals.

> **Note:**  
> Ensure slicers are connected to all PivotTables:  
> *Slicer → Report Connections → Select all PivotTables*

---

## 📑 PivotTables (Data Layer)

The PivotTables calculate:
- Average recycling rate by income group
- Average MSW per capita and recycling gap
- Number of countries by income group
- Top countries by recycling rate
- Average waste treatment method shares by income group

---

## 🐍 Python Component  
### Script: `country_data_analysis.py`

The Python script mirrors and extends the Excel analysis using **pandas**.

### 🔧 Script Functionality

1. Loads `Country_data_project.xlsx`
2. Automatically cleans column names
3. Creates friendly aliases for analysis:
   - `country`, `region`, `population`
   - `msw_per_capita_kg_year`
   - `recycling_rate_percent`
4. Generates key insights:
   - Top 10 countries by recycling rate
   - Average recycling rate by region
   - Recycling performance distribution (Low / Medium / High)
   - Identification of low-performing (“problem”) countries
5. Creates a calculated metric:
   - `waste_per_1000_people = (MSW per capita × population) / 1000`
6. *(Optional)* Visualization:
   - Bar chart of average recycling rate by region
7. Exports cleaned data to:
   - `Country_data_cleaned.xlsx`

---

## 📁 Project Structure
1. Install required packages:
   ```bash
   pip install pandas matplotlib openpyxl
