## Dataset

### https://www.kaggle.com/mihirhalai/sydney-house-prices

- 200,000 Sydney property sales from 2000-2019 scraped from realestate.com.au
- This dataset does not include the current trending

### Data Cleaning - Remove null, Outliers using STD, MEAN

- Drop null, Outliers using STD and MEAN
- Any suburb having less than 10 data points should be tagged as "other" suburb. This way number of categories can be reduced by huge amount.
- Transform Propperty types to numbers for training
  ['house', 'townhouse', 'duplex/semi-detached', 'villa', 'other','terrace', 'warehouse', 'acreage']
- Data entry : Number of bedroom, bath and property types

### Data Modelling

- LinearRegression Model
- K Fold cross validation to measure accuracy
- Testing for a few properties

### Tech stacks

- Pandas, Numpy, Sci-kit learn
- Flask, React, Antd
- AWS, Github
