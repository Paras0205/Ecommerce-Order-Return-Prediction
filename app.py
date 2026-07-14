import streamlit as st
import joblib
import pandas as pd

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="E-Commerce Order Return Prediction",
    page_icon="🛒",
    layout="wide"
)

# ----------------------------
# Load Model
# ----------------------------
try:
    model = joblib.load("model/ecommerce_order_return_prediction_model_v1.pkl")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# ----------------------------
# Load Dropdown Options
# ----------------------------

options = joblib.load("model/options.pkl")

# ----------------------------
# Arrange Order Days
# ----------------------------

day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

options["order_day"] = day_order

# ----------------------------
# Arrange Order Months
# ----------------------------

month_order = [
    "June",
    "July",
    "August",
    "September"
]

options["order_month"] = month_order

# ----------------------------
# Title
# ----------------------------

st.title("🛒 E-Commerce Order Return Prediction")

st.markdown("""An intelligent decision-support application that predicts whether an online order
is likely to be **Returned** or **Not Returned** using **Machine Learning**.

The application analyzes customer, product, and order information to estimate
return risk, helping businesses make smarter shipping decisions, reduce return-related
costs, and support data-driven decision-making.
""")

st.success("✅ Machine Learning Model Loaded Successfully")

# =====================================================
# Customer Information
# =====================================================

with st.container(border=True):

    st.subheader("👤 Customer Information")
    st.caption("Enter customer-related information.")

    col1, col2 = st.columns(2)

    with col1:

        customer_age = st.number_input(
            "Customer Age",
            min_value=0,
            max_value=120,
            value=30
        )

        customer_total_orders = st.number_input(
            "Customer Total Orders",
            min_value=1,
            value=1
        )

        customer_return_rate = st.slider(
            "Customer Return Rate",
            min_value=0.0,
            max_value=1.0,
            value=0.10,
            step=0.01
        )

    with col2:

        user_title = st.selectbox(
            "User Title",
            options["user_title"]
        )

        user_state = st.selectbox(
            "User State",
            options["user_state"]
        )

# =====================================================
# Product Information
# =====================================================

with st.container(border=True):

    st.subheader("📦 Product Information")
    st.caption("Enter product-related information.")

    col3, col4 = st.columns(2)

    with col3:

        item_price = st.number_input(
            "Item Price (₹)",
            min_value=0.0,
            value=1000.0,
        )

        brand_id = st.selectbox(
            "Brand ID",
            options["brand_id"],
        )

        item_color = st.selectbox(
            "Item Color",
            options["item_color"],
        )

    with col4:

        size_type = st.selectbox(
            "Size Type",
            options["size_type"],
        )

        size_value = st.selectbox(
            "Size Value",
            options["size_value"],
        )

        waist_size = st.number_input(
            "Waist Size",
            min_value=0.0,
            value=0.0,
        )

        inseam_size = st.number_input(
            "Inseam Size",
            min_value=0.0,
            value=0.0,
        )

# =====================================================
# Order Information
# =====================================================

with st.container(border=True):

    st.subheader("🛒 Order Information")
    st.caption("Enter order-related information.")

    col5, col6 = st.columns(2)

    with col5:

        order_month = st.selectbox(
            "Order Month",
            options["order_month"]
        )

        order_day = st.selectbox(
            "Order Day",
            options["order_day"]
        )

        is_weekend = order_day in ["Saturday", "Sunday"]


# =====================================================
# Prediction
# =====================================================

st.divider()

st.subheader("📊 Prediction")

st.caption(
    "Click the button below to predict whether the order is likely to be returned."
)

# =====================================================
# Order Summary
# =====================================================

with st.expander("📋 View Order Summary"):

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("#### 👤 Customer Information")

        st.write(f"**Customer Age:** {customer_age}")
        st.write(f"**Customer Total Orders:** {customer_total_orders}")
        st.write(f"**Customer Return Rate:** {customer_return_rate:.2%}")
        st.write(f"**User Title:** {user_title}")
        st.write(f"**User State:** {user_state}")

        st.markdown("---")

        st.markdown("#### 📦 Product Information")

        st.write(f"**Item Price:** ₹{item_price:,.2f}")
        st.write(f"**Brand ID:** {brand_id}")
        st.write(f"**Item Color:** {item_color}")

    with col2:

        st.markdown("#### 📏 Size Information")

        st.write(f"**Size Type:** {size_type}")
        st.write(f"**Size Value:** {size_value}")
        st.write(f"**Waist Size:** {waist_size}")
        st.write(f"**Inseam Size:** {inseam_size}")

        st.markdown("---")

        st.markdown("#### 🛒 Order Information")

        st.write(f"**Order Month:** {order_month}")
        st.write(f"**Order Day:** {order_day}")
        st.write(f"**Weekend Order:** {'Yes' if is_weekend else 'No'}")

predict_btn = st.button(
    "Predict Return",
    use_container_width=True
)

if predict_btn:

    with st.spinner(
    "Analyzing customer, product and order information..."
):

    # ----------------------------------------
    # Create Input DataFrame
    # ----------------------------------------

        new_order = pd.DataFrame({

            "order_item_id": [0],
            "order_date": ["2026-01-01"],
            "delivery_date": ["2026-01-05"],
            "item_id": [0],

            "item_color": [item_color],
            "brand_id": [brand_id],
            "item_price": [item_price],

            "user_title": [user_title],
            "user_dob": ["1995-01-01"],
            "user_state": [user_state],
            "user_reg_date": ["2023-01-01"],

            "size_type": [size_type],
            "size_value": [size_value],

            "waist_size": [waist_size],
            "inseam_size": [inseam_size],

            "waist_size_missing": [1 if waist_size == 0 else 0],
            "inseam_size_missing": [1 if inseam_size == 0 else 0],

            "customer_age": [customer_age],

            "order_month": [order_month],
            "order_day": [order_day],

            "is_weekend": [int(is_weekend)],

            "customer_total_orders": [customer_total_orders],
            "customer_return_rate": [customer_return_rate]

        })

        prediction = model.predict(new_order)

        probability = model.predict_proba(new_order)

        # =====================================================
        # Prediction Result
        # =====================================================

        st.divider()

        with st.container(border=True):

            return_prob = probability[0][1]
            not_return_prob = probability[0][0]

            st.subheader("📊 Prediction Result")

            # ---------------------------------------
            # Prediction + Risk Level
            # ---------------------------------------

            col1, col2, col3 = st.columns(3)

            with col1:

                st.markdown("### Prediction")

                if prediction[0] == 1:
                    st.error("🔴 Returned")
                else:
                    st.success("🟢 Not Returned")

            with col2:

                st.markdown("### Risk Level")

                if return_prob < 0.40:
                    st.success("🟢 Ready to Process")

                elif return_prob < 0.70:
                    st.warning("🟡 Review Risk")

                else:
                    st.error("🔴 Immediate Attention")

            st.divider()

            # ---------------------------------------
            # Return Probability
            # ---------------------------------------

            st.markdown("### Return Probability")

            st.progress(return_prob)

            st.write(f"**{return_prob:.2%}**")

            st.divider()

            # ---------------------------------------
            # Recommendation
            # ---------------------------------------

            st.markdown("### 💡 Business Recommendation")

            if return_prob < 0.40:

                st.success("""
            ### ✅ Recommended Action

            • Proceed with normal order processing.

            • The order has a **low probability of being returned**.

            • No additional action is required before shipping.
            """)

            elif return_prob < 0.70:

                st.warning("""
            ### ⚠ Review Before Shipping
                           
            The order has a **moderate probability of being returned**.

            Consider verifying:

            • Product size selection

            • Customer order history

            • Delivery details

            before processing.
            """)

            else:

                st.error("""
            ### 🚨 Immediate Attention
                         
            The order has a **high probability of being returned**.

            Recommended actions:

            • Verify customer details

            • Review return history

            • Consider additional confirmation before shipment
            """)

reset_btn = st.button(
    "🧹 Clear All",
    use_container_width=True
)

if reset_btn:
    st.rerun()

st.divider()

st.divider()

st.markdown("""
<style>
.footer{
    text-align:center;
    color:#9CA3AF;
    font-size:15px;
    padding:20px;
}
.footer a{
    color:#9CA3AF;
    text-decoration:none;
}
.footer a:hover{
    color:#FFFFFF;
}
</style>

<div class="footer">
© 2026 <b>Paras</b> | Data Analyst |
<a href="https://www.linkedin.com/in/paras-dhankhar/" target="_blank">LinkedIn</a> |
<a href="https://github.com/Paras0205" target="_blank">GitHub</a>
</div>
""", unsafe_allow_html=True)