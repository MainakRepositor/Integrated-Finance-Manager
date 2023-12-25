import streamlit as st 

# Configure the app
st.set_page_config(
    page_title = 'Integrated Finance Manager',
    page_icon = '📈',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

st.header("Integrated Finance Manager")

st.image("images/home.png", width=700)

st.markdown('''<p>An efficient stock portfolio manager possesses several key features and skills:

1. **Financial Analysis:** Strong analytical skills to assess the financial health, performance, and potential risks of different stocks and industries. This includes evaluating financial statements, ratios, and market trends.

2. **Risk Management:** Ability to assess and manage risk effectively. This involves diversification across various asset classes and industries to reduce risk exposure.

3. **Research Skills:** Constantly staying updated with market news, economic trends, and company-specific developments. This helps in making informed investment decisions.

4. **Portfolio Diversification:** Building a diversified portfolio to spread risk across different stocks, sectors, and sometimes even geographic regions. This helps to mitigate the impact of market volatility.

5. **Goal Alignment:** Understanding clients' or stakeholders' investment objectives and aligning portfolio strategies to meet those goals, whether they're seeking income, growth, or a mix of both.

6. **Performance Tracking and Adaptability:** Monitoring portfolio performance regularly and being adaptable to market changes. Adjusting the portfolio allocation based on market conditions and the performance of individual assets.

7. **Communication Skills:** Ability to communicate complex financial information in a clear and understandable manner to clients or stakeholders.

8. **Emotional Discipline:** Keeping emotions in check, avoiding impulsive decisions based on market fluctuations, and adhering to a well-thought-out investment strategy.

9. **Tech Savvy:** Proficiency with financial software, trading platforms, and analytical tools to optimize decision-making processes.

10. **Regulatory Compliance:** Adhering to regulatory standards and maintaining ethical practices in managing clients' investments.

11. **Continuous Learning:** Being open to learning new investment strategies, keeping up with industry trends, and evolving with the changing dynamics of the financial markets.

An efficient portfolio manager combines these skills to construct and manage portfolios that align with investors' objectives while optimizing risk-adjusted returns.</p>''',unsafe_allow_html=True)

