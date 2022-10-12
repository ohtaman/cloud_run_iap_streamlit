import streamlit as st


def main():
    with st.sidebar:
        n = st.number_input('any number')

    st.write(n**2)


if __name__ == '__main__':
    main()