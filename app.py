import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load(r"C:\Users\Gebruiker\Desktop\IronHack\Projects\Online Payments Fraud Detection\random_forest_model SMOTETomek.pkl")

# Set layout
st.set_page_config(layout="wide")

# Inject CSS: center layout + red button + animated image
st.markdown("""
    <style>
    .centered {
        max-width: 600px;
        margin: auto;
        padding: 2rem;
        text-align: center;
    }
    .stButton > button {
        background-color: red;
        color: white;
        width: 100%;
        padding: 10px;
        border: none;
        border-radius: 6px;
    }
    .animated-icon {
        animation: bounce 2s infinite;
        width: 80px;
        margin-bottom: 0.5rem;
    }
    @keyframes bounce {
        0%, 100% {
            transform: translateY(0);
        }
        50% {
            transform: translateY(-8px);
        }
    }
    </style>
""", unsafe_allow_html=True)

# Use columns to center content
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<div class="centered">', unsafe_allow_html=True)

    # Animated Attention Sign
    st.markdown(
        "<img src='https://cdn-icons-png.flaticon.com/512/595/595067.png' class='animated-icon'>",
        unsafe_allow_html=True
    )
    st.caption("Attention")

    # Header and title
    st.markdown("<h2 style='color:red;'>Fraud Detection System</h2>", unsafe_allow_html=True)
    st.title("Welcome to the Online Payment System")

    # Inputs
    amount = st.number_input(
        "Transaction amount (0 - 1M typical, but can be higher)",
        min_value=0.0,
        value=1000.0
    )
    oldbalanceOrg = st.number_input(
        "Old balance of sender (0 to 10,000,000 is typical)",
        min_value=0.0,
        max_value=1e8,
        value=5000.0
    )
    newbalanceOrg = oldbalanceOrg - amount
    if newbalanceOrg < 0:
        newbalanceOrg = 0.0

    newbalanceDest = st.number_input(
        "New balance of receiver (0 to 10,000,000 is typical)",
        min_value=0.0,
        max_value=1e8,
        value=1000.0
    )
    oldbalanceDest = newbalanceDest - amount

    tx_type = st.selectbox("Transaction type", ["CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"])
    type_CASH_OUT = 1 if tx_type == "CASH_OUT" else 0
    type_DEBIT = 1 if tx_type == "DEBIT" else 0
    type_PAYMENT = 1 if tx_type == "PAYMENT" else 0
    type_TRANSFER = 1 if tx_type == "TRANSFER" else 0

    # Button and prediction
    if st.button("Predict Fraud"):
        input_data = pd.DataFrame([{
            'amount': amount,
            'oldbalanceOrg': oldbalanceOrg,
            'newbalanceOrig': newbalanceOrg,
            'oldbalanceDest': oldbalanceDest,
            'newbalanceDest': newbalanceDest,
            'type_CASH_OUT': type_CASH_OUT,
            'type_DEBIT': type_DEBIT,
            'type_PAYMENT': type_PAYMENT,
            'type_TRANSFER': type_TRANSFER
        }])

        prediction = model.predict(input_data)[0]
        proba = model.predict_proba(input_data)[0]

        st.info(f"Probability Legitimate: {proba[0]:.2%}")
        st.info(f"Probability Fraud: {proba[1]:.2%}")

        if prediction == 1:
            st.error(f":rotating_light: Fraudulent transaction detected! Confidence: {proba[1]:.2%}")
        else:
            st.success(f":white_check_mark: Transaction appears legitimate. Confidence: {proba[0]:.2%}")

    st.markdown('</div>', unsafe_allow_html=True)





