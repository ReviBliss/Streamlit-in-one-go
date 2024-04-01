import streamlit as st

st.title('Hello Revija! Welcome to Streamlit Course!')
st.header('Hello Revija! This is header')              #header
st.subheader('Hello Revija! This is sub-header')           #sub-header
st.text('Hello Revija! This is text')                #text

#markdown
st.markdown('Hi')
st.markdown('# Hi, this is markdown with one hash')
st.markdown('## Hi, this is markdown with 2 hash')
st.markdown('### Hi, this is markdown with 3 hash')
st.markdown('#### Hi, this is markdown with 4 hash')
st.markdown('##### Hi, this is markdown with 5 \#')

st.success('This represents success!')
st.info('This represents information')
st.warning('This represents warning')
st.error('This represents error')

st.exception('This represents exception')
exp = ZeroDivisionError('Division not possible with Zero')
st.exception(exp)
st.help(ZeroDivisionError)

st.write('range(1,10)')
st.write(range(1,10))
st.write(1+2+4)

st.subheader('Code')
st.code('x = 10 \n'
        'for i in range(x):\n'
        '\tprint i')

st.subheader('Checkbox')
if (st.checkbox('Data Science')):
    st.write('DS is selected')

if (st.checkbox('ML')):
    st.write('ML is selected')

if (st.checkbox('Artificial Intelligence')):
    st.write('AI is selected')

st.subheader('Radio')
rB = st.radio('Select: ', ('Male', 'Female', 'Other'))
if (rB == 'Male'):
    st.write('YOu are a Male')
elif (rB == 'Female'):
    st.write('You are a female')
elif (rB== 'Other'):
    st.write('You are neither Male nor Female')

st.subheader('Select Box')
selectBox = st.selectbox('Data Science:', ['Data Analysis', 'Machine Learning', 'Data Structure and Algorithms',                                                 'Natural Language Processing', 'Python', 'Deep Learning', 'R'])
st.write('You have selected ', selectBox)

st.subheader('Multi Select box')
multiSelect = st.multiselect('Data Science:', ['Data Analysis', 'Machine Learning', 'Data Structure and Algorithms',                                                 'Natural Language Processing', 'Python', 'Deep Learning', 'R'])
st.write('You have selected ', len(multiSelect), ' courses. ',multiSelect)

st.subheader('Button')
if (st.button('Click here')):
    st.write('Hurray! You have clicked the button')

st.subheader('Slider')
vol = st.slider('Select the volume:', 1, 100, step=1)
st.write('Volume is ', vol)

st.subheader('Text Input')
username = st.text_input('Name: ')

if(username):
    st.write('Hi ', username)

passwd = st.text_input('Password: ', type='password')

st.subheader('Text Area')
textArea = st.text_area('Write a brief note about yourself')
if (textArea):
    st.write(textArea)
    
st.subheader('Input number')
st.number_input('Age:', 0, 120)

st.subheader('Input Date')
st.date_input('Date:')

st.subheader('Input Time')
st.time_input('Time:')
