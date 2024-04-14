import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('user_budget.csv')

with st.sidebar:
    with st.form("new_expense"):
        st.title("New Expense")
        expense = st.text_input("Expense")
        cost = st.number_input("Cost")
        category = st.selectbox("Category", options=["Need", "Want", "Savings/Debt"])
        submitted = st.form_submit_button("Add")
    # with st.form("edit_expense"):
    #     st.title("Edit Expense")
    #     expense = st.text_input("Expense Name")
    #     cost = st.text_input("Cost")
    #     delete = st.button("Delete")
    #     submitted = st.form_submit_button("Save")

if submitted:
    new_expense = {"Expense": expense, "Cost": cost, "Category": category}
    df.loc[len(df.index)] = new_expense
    df.to_csv('user_budget.csv', index=False)


df = df.sort_values(by='Cost', ascending=False)

st.title("Spending Visualizer")
total_cost = df['Cost'].sum()
st.markdown(f"**Total Expenses: {total_cost}**")
col1, col2 = st.columns(2)
with col1:
    fig_pie = px.pie(df, values="Cost", names='Expense', title="Individual Costs")
    fig_pie.update_layout(showlegend=False)
    st.plotly_chart(fig_pie, use_container_width=True)
with col2:
    grouped = df.groupby('Category')['Cost'].sum().reset_index()
    fig = px.pie(grouped, values='Cost', names='Category', title='Expenses by Category')
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig)

fig_bar = px.bar(df, x='Expense', y='Cost', title="Expenses Sorted by Cost")
st.plotly_chart(fig_bar, use_container_width=True)








