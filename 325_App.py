import streamlit as st
import pandas as pd


#################################

data=pd.read_csv("country.csv")
#st.set_page_config(layout="wide")

#################################

st.image("f4k.jpg")
st.image("Head.jpg")
st.write("“According to the UNICEF, one in 5 children in the least developed countries are engaged in child labor. A problem that was aggravated by COVID-19 and global economic decline that it takes a walk in Beirut to believe these numbers. Children require different systems of protection that starts with parents and extends to every office, business, institution, organization and agency, local and international, governmental or otherwise. Everyone, who is not a child, is responsible”")
st.markdown("----")

#################################

tabs_font_css = """
<style>
button[data-baseweb="tab"] {
  font-size: 26px;
}
</style>
"""
st.write(tabs_font_css, unsafe_allow_html=True)

################################

listTabs = ["About" ,"NGO", "Get Involved","Donate"]

whitespace = 9
tab1, tab2, tab3, tab4 = st.tabs([s.center(whitespace,"\u2001") for s in listTabs])

################################

with tab1:
    st.write("Future 4 kids is an initiative that provides education to children forcibly engaged in labor due to the economic situation in Lebanon. Through F4K, we aspire to shift the children from workplaces to classrooms through NGOs specialized in quality education.")
    st.write("In our belief, no child should be exploited, regardless of his\her race, sex, nationality, religion, place of residence, or occupation. The term **_child labor_** refers to employment that is compelled, forced bound, slave, or otherwise, harmful to children's health and safety, and that prevents a child from accessing education or reduces the child's academic success. ")
    st.write('**Our Mission**')
    st.write("**Future4kids** believes every child should be taught to learn, not forced to earn. ")
    st.write("We aim every day to provide kids with a healthy start in life, the chance to learn, and safety from harm. We go above and beyond to transform the lives and future of children. ")
    #st.write("**Our Values**")
    #st.markdown("**Commitment**")
    #st.markdown("**Integrity**")
    #st.markdown("**Respect**")
    #st.markdown("**Ambition**")

with tab2:
    st.write("The F4K initiative will connect three parties: NGOs providing humanitarian and financial aids, NGOs providing quality education to non-privileged children, and donors.")
    col1, col2 = st.columns((1,1))
    with col1:
        with st.expander("Financial Support NGOs"):
        
            st.subheader("Ajialouna")
            st.image("Ajialouna.jpg",output_format="JPEG",width=250)

            st.subheader("Nusaned")
            st.image("nusa3ed.jpg",output_format="JPEG",width=250)

            st.subheader("Caritas")
            st.image("Caritas.jpg",output_format="JPEG",width=250)

            st.subheader("HelpLebanon")
            st.image("Help_leb.jpg",output_format="JPEG",width=250)

            st.subheader("El Da3em")
            st.image("El_Da3em.jpg",output_format="JPEG",width=250)

    with col2:
        with st.expander("Educational Support NGOs"):

            st.subheader("Save the Children")
            st.image("Save_the_children.jpg",output_format="JPEG",width=250)

            st.subheader("Teach for Lebanon")
            st.image("Teach_for_lebanon.jpg",output_format="JPEG",width=250)

            st.subheader("Teach a Child")
            st.image("Teach_a_child.jpg",output_format="JPEG",width=250)

            st.subheader("Tahaddi Lebanon")
            st.image("Tahaddi_lebanon.jpg",output_format="JPEG",width=250)

            st.subheader("T.I.E.S Education ")
            st.image("x.jpg",output_format="JPEG",width=250)

with tab3:
    st.header("Education")
    st.write("Join us in educating non-privileged children through after-school activities")

    st.header("Outreach")
    st.write("Join us in reaching out to more NGOs to be part of our initiative, and raise awareness on the imporatnace of children's education.")

    st.header("Research")
    st.write("Help us with our reseach and data collection, be part of our team and aid us in reaching a better future ")



with tab4:
    st.markdown("-----")
    
    st.header("Make a monthly|single donation of:")
    col1, col2, col3 = st.columns((1.5,1,1))
    with col1:
        st.selectbox("Country",options=data.loc[:,"Country"])
    with col2:
        st.selectbox("Amount -$",options=[10,15,20,25,30,35,40])
    with col3:
        number = st.number_input('Insert a number')
        st.write('Your donation is ', number,"$")
    
    s_or_r = st.checkbox('Check if you want your donation to be monthly')

    if s_or_r:
        st.write('Great!')
    st.markdown("-----")
    st.header("Your Contact Details :)")
    title = st.text_input('E-mail', 'e.g.   example@gmail.com')

    agree = st.checkbox('Yes, I am happy for F4K to use the personal information I share to send me communications about F4K programs, services, and events by email')
    if agree:
        st.write('Thank you for your trust!')

    title = st.text_input('Phone Number', 'e.g.   0123456789')
    st.markdown("By providing your phone number you agree that F4K will use the personal information you share with us to send you information about our programs, services and events by SMS, telephone (voice) and via messenger platforms i.e. WhatsApp.")
        #st.write('The current movie title is', title)


st.markdown("-----")
st.markdown("-----")
st.header("Contact Us")
st.write("+96101000000","|","future4kids00@gmail.com")