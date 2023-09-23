from calcul import *
import streamlit as st
st.title('Bienvenu à notre calculatrice :abacus:')
st.write("---")
valeur1= st.number_input("enter first value" ,step=0.1)
valeur2= st.number_input("enter second value" ,step=0.1)

mon_calcul = Calcul(valeur1, valeur2)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Somme:"):
        result = mon_calcul.calcul_somme()
        st.success(f"your result is {result}")
with col2:
    if st.button("Soustraction:"):
        result = mon_calcul.calcul_soustraction()
        st.success(f"your result is {result}")
with col3:
    if st.button("Multiplication:"):
        result = mon_calcul.calcul_multiplication()
        st.success(f"your result is {result}")
with col4:
    if st.button("division:"):
      if (mon_calcul.calcul_division() == "the first value cannot divide by zero"):
        st.warning("Division by 0 error. Please enter a non-zero number.")
      else:
        result = mon_calcul.calcul_division()
        st.success(f"your result is {result}")