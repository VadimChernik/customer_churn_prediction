# Customer Churn Prediction

This project aims to build a machine learning model to predict the probability of customer churn for eCommerce project and deploy it locally with Docker.

# Use Cases

Customer churn prediction is a vital tool for eCommerce businesses to identify at-risk customers and take proactive measures to retain them. Below are the top 5 use cases where churn prediction can deliver the most impact:

---

## 1. **Personalized Retention Campaigns**

### Description
Identify customers who are at high risk of churning and deploy targeted retention campaigns, such as personalized offers, discounts, or loyalty rewards.

### Benefits
- Boosts customer loyalty.
- Reduces churn by addressing individual customer needs.
- Improves customer satisfaction and lifetime value.

---

## 2. **Optimizing Marketing Spend**

### Description
Focus marketing resources on retaining high-value customers who are likely to churn, rather than spending uniformly across the entire customer base.

### Benefits
- Maximizes return on investment (ROI) for marketing campaigns.
- Helps prioritize high-value customers for retention efforts.
- Reduces wasted marketing spend.

---

## 3. **Improving Customer Support**

### Description
Leverage churn predictions to proactively engage with dissatisfied customers by addressing their concerns and resolving complaints quickly.

### Benefits
- Enhances overall customer experience.
- Reduces churn caused by poor support.
- Builds trust and brand loyalty.

---

## 4. **Enhancing Subscription Retention**

### Description
For subscription-based eCommerce models, predict when customers are likely to cancel their subscriptions and offer targeted incentives like free trials or upgrades to retain them.

### Benefits
- Stabilizes recurring revenue streams.
- Reduces subscription cancellations.
- Strengthens customer relationships.

---

## 5. **Refining Product/Service Offerings**

### Description
Analyze churned customers' behavior to uncover issues with product offerings, pricing, or the overall shopping experience, and implement improvements.

### Benefits
- Aligns products/services with customer expectations.
- Reduces churn drivers by addressing key pain points.
- Enhances competitiveness in the market.

---

By implementing these use cases, eCommerce businesses can effectively reduce customer churn, boost revenue, and create a more loyal customer base.


## Data

The dataset used for training the machine learning model can be found on Kaggle: [Ecommerce Customer Churn Analysis and Prediction](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction).


## Dependencies

This project uses `pipenv` for managing the Python environment and dependencies. Ensure you have the following installed:

- Python (version 3.12)
- `pipenv` (Python package for managing virtual environments)

## Installation

### Clone the Repository

Clone this repository to your local machine:

```bash
git https://github.com/VadimChernik/customer_churn_prediction.git
cd customer_churn_prediction
```

### Set Up the Environment

Ensure `pipenv` is installed. If not, install it via pip:

```bash
pip install pipenv
```

Then, create the virtual environment and install dependencies using `pipenv`:

```bash
pipenv install
```

### Activate the Environment

Activate the virtual environment to work within it:

```bash
pipenv shell
```


## Local Deployment with Docker

1. **Build the Docker Image:**
   - Use the following command to build the Docker image:
   ```bash
   docker build -t midterm-project .
   ```

2. **Run the Docker Container:**
   - Start a container locally using the following command:
   ```bash
   docker run -it --rm -p 9696:9696 midterm-project
   ```

3. **Access the Application:**
   - Update the `url` variable in the `test.py`. After making this change, execute the `test.py` script. This will enable you to view the response in JSON format.
