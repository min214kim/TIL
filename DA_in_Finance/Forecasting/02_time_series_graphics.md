# 2.1 tsibble
## 1. Why use?
- allow storage, manipulation of multiple time series in R
- works with tidyverse functions

## 2. Content
- index
- measured variable
- key variable

## 3. Code
### Create tsibble
- creating
```R
mydata <- tible(
    year = 2015:2019,
    y = c(123, 39, 78, 52, 110)
) |>
    as_tsibble(index = year)
# %>% and |> are pretty much same in this lecture
```
- reading month 
```R
mutate(Month = yearmonth(Month)) |>
as_tsibble(index = Month)
```
- reading Quarter : `mutate(Quarter = yearquarter(date)) |>`
- reading csv data & turning into tsibble
```R
data <- readr::read_csv('data.csv') |>
as_tsibble(
    index = Year,
    key = c(state, gender, etc..) # 필수
)
```
### time class
|Frequency|Function|
|---|---|
|Annual|`start:end`|
|Quarterly|`yearquarter()`|
|Monthly|`yearmonth()`|
|Weekly|`yearweek()`|
|Daily|`as_date()`, `ymd()`|
|Sub-daily|`as_datetime()`,`ymd_hms()`|
### Functions
- `mutate()` : create new variables(col)
- `select()` : select particular columns
- `filter()` : select particular rows
- `summarise()` : combine data across keys #?
  ```R
  data |>
    filter(Col == 'value') |>
    select(col1, col2,...) |>
    summarise(colname = sum(col)) |>
  ```
- `distinct()`  : shows categories of variables(col)
- `period()` : 
- `lubridate package` :