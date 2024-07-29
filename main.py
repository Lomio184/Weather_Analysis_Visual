import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def convert_to_df( path ):
    df = pd.read_excel( path )
    return df

def convert_to_visual_rain( path ):
    df = pd.read_excel( path )
    
    plt.figure(figsize=(10, 6))
    plt.bar(df['년'], df['강수량'], color='skyblue', label='precipitation')
    

    plt.xlabel('Year')
    plt.ylabel('precipitation (mm)')
    plt.title('precipitation per Year')
    plt.legend()
    plt.grid(True)
    plt.show()
    
def deviation_converting_rain( path ):
    df = pd.read_excel( path )
    
    baseline_year = 2021
    baseline = df[df['년'] == baseline_year]['강수량'].mean()
    
    df['deviation'] = df['강수량'] - baseline
    
    plt.figure(figsize=(10, 6))
    plt.bar(df['년'], df['deviation'], color='skyblue', label='deviation')

    plt.xlabel('Year')
    plt.ylabel('deviation (mm)')
    plt.title('deviation per Year')
    plt.legend()
    plt.grid(True)
    plt.show()
    
def convert_to_visual_temp( path ):
    df = pd.read_excel( path )
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['년'], df['평균기온'], marker='o', label='Avg Temp')
    plt.plot(df['년'], df['평균최저기온'], marker='o', label='AvgMean Temp')
    plt.plot(df['년'], df['평균최고기온'], marker='o', label='AvgMax Temp')

    plt.xlabel('Year')
    plt.ylabel('Temperature (°C)')
    plt.title('Avg Temp per Year, Avg Mean Temp, Avg Max Temp')
    plt.legend()
    plt.grid(True)
    plt.show()
    
def deviation_converting_temp( path ):
    df = pd.read_excel(path)

    baseline_year = 2000
    baseline = df[df['년'] == baseline_year][['평균기온', '평균최저기온', '평균최고기온']].mean()

    df['평균기온 편차'] = df['평균기온'] - baseline['평균기온']
    df['평균최저기온 편차'] = df['평균최저기온'] - baseline['평균최저기온']
    df['평균최고기온 편차'] = df['평균최고기온'] - baseline['평균최고기온']

    plt.figure(figsize=(10, 6))
    plt.bar(df['년'], df['평균기온 편차'], color='green', label='Avg Temp')
    plt.bar(df['년'], df['평균최저기온 편차'], color='blue', label='AvgMean Temp', alpha=0.7)
    plt.bar(df['년'], df['평균최고기온 편차'], color='red', label='AvgMax Temp', alpha=0.5)

    plt.xlabel('Year')
    plt.ylabel('Temp Deviation')
    plt.title('Temp Deviation per Year')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    rain_path = "rain.xlsx"
    temp_path = "temp.xlsx"
    
    rain_df = convert_to_df( rain_path )
    temp_df = convert_to_df( temp_path )
    
    # 피어슨 상관 계수
    corr = rain_df['강수량'].corr(temp_df['평균기온'])
    print(corr)
    