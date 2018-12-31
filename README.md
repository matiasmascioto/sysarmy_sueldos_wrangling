# sysarmy Salary Surveys *(Data Wrangling)*

*keywords: data wrangling, python, jupyter notebook, pandas, excel, csv*

This project cleans and concatenates the results of IT salary surveys made by [sysarmy](https://sysarmy.com.ar/blog/) in South America.

## Datasets
### Input
*  Salary surveys:
  *  */data/input/2015_2.csv*: [Link](https://goo.gl/xx11f7)
  *  */data/input/2016_1.csv*: [Link](https://goo.gl/Jd2NzQ)
  *  */data/input/2016_2.xlsx*: [Link](https://goo.gl/RqzrJd)
  *  */data/input/2017_1.xlsx*: [Link](https://goo.gl/SyDpKo)
  *  */data/input/2017_2.xlsx*: [Link](https://goo.gl/g3C1bj)
  *  */data/input/2018_1.xlsx*: [Link](https://goo.gl/bFDCnA)
  *  */data/input/2018_2.xslx*: [Link](https://goo.gl/Lf2d8Z)
*  Currencies data
  *  */data/input/USDARS_CUR.json*: [Link](https://www.bloomberg.com/markets/api/bulk-time-series/price/USDARS%3ACUR?timeFrame=5_YEAR)
  *  */data/input/USDBOB_CUR.json*: [Link](https://www.bloomberg.com/markets/api/bulk-time-series/price/USDBOB%3ACUR?timeFrame=5_YEAR)
  *  */data/input/USDCLP_CUR.json*: [Link](https://www.bloomberg.com/markets/api/bulk-time-series/price/USDCLP%3ACUR?timeFrame=5_YEAR)
  *  */data/input/USDCOP_CUR.json*: [Link](https://www.bloomberg.com/markets/api/bulk-time-series/price/USDCOP%3ACUR?timeFrame=5_YEAR)
  *  */data/input/USDCRC_CUR.json*: [Link](https://www.bloomberg.com/markets/api/bulk-time-series/price/USDCRC%3ACUR?timeFrame=5_YEAR)
  *  */data/input/USDCUP_CUR.json*: [Link](https://www.bloomberg.com/markets/api/bulk-time-series/price/USDCUP%3ACUR?timeFrame=5_YEAR)
  *  */data/input/USDDOP_CUR.json*: [Link](https://www.bloomberg.com/markets/api/bulk-time-series/price/USDDOP%3ACUR?timeFrame=5_YEAR)
  *  */data/input/USDGTQ_CUR.json*: [Link](https://www.bloomberg.com/markets/api/bulk-time-series/price/USDGTQ%3ACUR?timeFrame=5_YEAR)
  *  */data/input/USDHNL_CUR.json*: [Link](https://www.bloomberg.com/markets/api/bulk-time-series/price/USDHNL%3ACUR?timeFrame=5_YEAR)
  *  */data/input/USDMXN_CUR.json*: [Link](https://www.bloomberg.com/markets/api/bulk-time-series/price/USDMXN%3ACUR?timeFrame=5_YEAR)
  *  */data/input/USDNIO_CUR.json*: [Link](https://www.bloomberg.com/markets/api/bulk-time-series/price/USDNIO%3ACUR?timeFrame=5_YEAR)
  *  */data/input/USDPAB_CUR.json*: [Link](https://www.bloomberg.com/markets/api/bulk-time-series/price/USDPAB%3ACUR?timeFrame=5_YEAR)
  *  */data/input/USDPEN_CUR.json*: [Link](https://www.bloomberg.com/markets/api/bulk-time-series/price/USDPEN%3ACUR?timeFrame=5_YEAR)
  *  */data/input/USDPYG_CUR.json*: [Link](https://www.bloomberg.com/markets/api/bulk-time-series/price/USDPYG%3ACUR?timeFrame=5_YEAR)
  *  */data/input/USDUYU_CUR.json*: [Link](https://www.bloomberg.com/markets/api/bulk-time-series/price/USDUYU%3ACUR?timeFrame=5_YEAR)
  *  */data/input/USDVEF_CUR.json*: [Link](https://www.bloomberg.com/markets/api/bulk-time-series/price/USDVEF%3ACUR?timeFrame=5_YEAR)

### Output
*  */data/output/encuestas.csv*: unified, cleaned and normalized dataset with the salary surveys results.

## Other files
*  *sysarmy_sueldos_wrangling.ipynb*: Jupyter Notebook that contains details and codes for the data wrangling process.
*  *sysarmy_sueldos_wrangling.yml*: Configuration file

## Sources
*  I took some ideas from this project: https://github.com/gerardobort/sysarmy-data 