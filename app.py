import streamlit as st 
import pandas as pd 
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Data entry",
                   layout="wide",
                   page_icon='📝')

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://images.unsplash.com/photo-1515595967223-f9fa59af5a3b?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
}
[data-testid="stHeader"]{
background-color: rgba(0,0,0,0);
}
[data-testid="stSidebar"]{
background-color: rgba(0,0,0,0);
}
[data-testid="element-container"]{
background-color: rgba(0,0,0,0);
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)









df = pd.read_csv("database1.csv")

def clear_text():
    st.session_state[1]=""
    st.session_state[2]=""
    st.session_state[3]=""
    st.session_state[4]=""
    st.session_state[5]=""

navigation = option_menu(menu_title=None,
        options=[ "view data🔍","data entry⌨"],
        menu_icon=["🔍","⌨"],
        orientation='horizontal'
        )

if navigation == "data entry⌨" :
    with st.sidebar :
        st.header("options")
        options_forms = st.form('options form')
        name = options_forms.text_input(" name",key=1)
        surname = options_forms.text_input('surname',key=2)
        job = options_forms.text_input('job',key=5)
        email = options_forms.text_input('email',key=3)
        age = options_forms.text_input('age',key=4)
        submit = options_forms.form_submit_button()  
        clear = st.sidebar.button("clear",on_click=clear_text)
    with st.expander("preview old data"):
        st.table(df)    

        
    

    if submit :
        new_data = {"Name":name,
                "Surname":surname,
                "Job":job,
                "Email":email,
                "Age":int(age)}
        
        new_df = pd.DataFrame([new_data])
    
    # Concatenate the new DataFrame with the existing one
        df = pd.concat([df, new_df], ignore_index=True)
    
    # Save the updated DataFrame back to the CSV file

        df.to_csv("database1.csv", index=False)
    
    # Display the updated DataFrame
        st.success('you data has been added successfully')
        with st.expander('preview uppdated data ') :
            st.table(df)

if navigation == "view data🔍":
    st.subheader("data preview",divider="gray")
    st.table(df)



 






    





   
