import streamlit as st


# Find more emoji's here:https://www.webfx.com/tools/emoji_cheat_sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


# ---- Header ----
with st.container():
    st.title("MY WEBPAGE: I Will Be For Who I am!")
    image_column, text_column=st.columns(2)
    #Image from a local file
    with image_column:
        st.image("liz.jpg", caption="Computer Engineering student in SNSU")
    with text_column: 
        st.header("I am Lizamie Garayan Carangue") 
        st.write("PLACE OF BIRTH: Purok-5, Rosita, Libjo, Dinagat Islands")
        st.write("TEMPORARY ADDRESS: Purok-3, San Juan, Surigao City, Surigao del Norte")
        st.write("BIRTH DATE: February 10, 2005")    
        st.write("AGE: 18 years old")
        st.write("I believe that, Life is full of love, you can't live without it because we rely around but life also is full of trials/challenges that makes us strong because we can't learn about life if there's no problem that come.")
        st.write("I'm a person who doesn't pursue other to stay, friends or care a lot of me because person can stay when they accept me for who I am undiconditionally. I'm perfect for who i am kind and deserve to be treated as a human.")
        st.write("But, I also a bad atittude that can be see like being sarcastic, plastic; depends on the attitude of others which is sorrounded myself.And I'm good of loving someone who doesnt love me back :)")  
    
# ----Background ----
with st.container():
    st.write("---")
    st.header("History of my life")
    st.write(" Daughter of: Pablito Carangue and Becon Carangue")   
    st.write("Graduated from: Rosita National High School")    
    st.write("Siblings: I have 3 brothers and 3 sisters and i'm the youngest daughter(6th). Me and my youngest brother's remain studying while others build thier own family.")
    st.write("I'm an achiever students since Day-care up to Senior High School But now People Change.")
    st.write("Came from the poor family but i didn't make it shy instead i'm proud of it because we can eat more than 3 times a day and my parents do everything for us through our ups and down.")
    st.write("if you want to know me more, just click below.")   
    st.markdown("[Learn More >](https://www.facebook.com/smilyliza.carangue)")
    

with st.container():
    st.title("Hobbies")  
    st.write("I'm not dancers but i kmow how to dance,act,sing and etc.") 
    st.write("if your interest , just click my tiktok account.")   
    st.markdown("[Learn More >](https://www.tiktok.com/@lizagarayancarang?_t=8hvJQ7ZFDjW&_r=1)")    
            

# ---- Contact ----
with st.container():
    st.write("---") 
    st.header("Get In Touch With Me!") 
    st.write("##")

# Documentation: https://formsubmit.com/!!!Change email Address!!!
    contact_form = """  
        <form_action = "https://formsubmit.com/your_@email.com", method="POST">
            <input type="hidden" name="captcha" value="false">
            <input type="text" name="name" required>
            <input type="email" name="email" required>
            <button type="Submit">Send</button>
        </form>
        """
    left_column, right_column = st.columns(2)   
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
 