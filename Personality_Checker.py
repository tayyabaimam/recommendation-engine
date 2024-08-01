import streamlit as st
import joblib

model = joblib.load('linear_regression_model.pkl')

st.markdown("""
    <style>
    body {
        background-color: #f0f8ff;
        font-family: 'Monaco', monospace;
    }
    .title {
        font-size: 50px;
        color: #3498db;
        text-align: center;
        font-family: 'Monaco', monospace;
    }
    .instructions {
        font-size: 20px;
        color: #2ecc71;
        font-family: 'Monaco', monospace;
    }
    .slider-box {
        border: 2px solid #95a5a6;
        padding: 20px;
        border-radius: 10px;
        background-color: #ecf0f1;
        margin-bottom: 20px;
        font-family: 'Monaco', monospace;
    }
    .expander {
        font-size: 18px;
        color: #8e44ad;
        font-family: 'Monaco', monospace;
    }
    .footer {
        font-size: 16px;
        text-align: center;
        color: #e74c3c;
        font-family: 'Monaco', monospace;
    }
    .prediction {
        font-size: 24px;
        color: #2980b9;
        font-weight: bold;
        font-family: 'Monaco', monospace;
    }
    .form-container {
        border: 3px solid #3498db;
        border-radius: 15px;
        padding: 30px;
        background-color: #f9f9f9;
        max-width: 800px;
        margin: auto;
        font-family: 'Monaco', monospace;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='title' style='font-size: 50px; color: #3498db; text-align: center; font-family: Monaco, monospace;'>Big Five Personality Test</div>", unsafe_allow_html=True)

st.markdown("<div class='form-container'>", unsafe_allow_html=True)

st.markdown("""
<div class='instructions'>
-----Instructions-----\n
Please rate how accurately each of the following statements describes you on a scale from 1 to 5:\n
1 = Strongly disagree
2 = Disagree
3 = Neutral
4 = Agree
5 = Strongly agree
</div>
""", unsafe_allow_html=True)

def create_sliders(statements, trait_name):
    with st.expander(f"Rate your {trait_name}", expanded=True):
        st.markdown('<div class="slider-box">', unsafe_allow_html=True)
        ratings = []
        for i, statement in enumerate(statements):
            rating = st.slider(statement, 1, 5, 3, key=f"{trait_name}{i+1}")
            ratings.append(rating)
        st.markdown('</div>', unsafe_allow_html=True)
    return ratings

agr_statements = [
    "I am interested in people.",
    "I sympathize with others' feelings.",
    "I have a soft heart.",
    "I take time out for others.",
    "I feel others' emotions.",
    "I make people feel at ease.",
    "I am not really interested in others. (Reversed)",
    "I insult people. (Reversed)",
    "I am not interested in other people's problems. (Reversed)",
    "I feel little concern for others. (Reversed)"
]

csn_statements = [
    "I am always prepared.",
    "I pay attention to details.",
    "I get chores done right away.",
    "I like order.",
    "I follow a schedule.",
    "I am exacting in my work.",
    "I leave my belongings around. (Reversed)",
    "I make a mess of things. (Reversed)",
    "I often forget to put things back in their proper place. (Reversed)",
    "I shirk my duties. (Reversed)"
]

est_statements = [
    "I get stressed out easily.",
    "I worry about things.",
    "I am easily disturbed.",
    "I get upset easily.",
    "I change my mood a lot.",
    "I have frequent mood swings.",
    "I get irritated easily.",
    "I often feel blue.",
    "I get nervous easily.",
    "I am relaxed most of the time. (Reversed)"
]

opn_statements = [
    "I have a rich vocabulary.",
    "I have a vivid imagination.",
    "I have excellent ideas.",
    "I am quick to understand things.",
    "I use difficult words.",
    "I spend time reflecting on things.",
    "I am full of ideas.",
    "I am not interested in abstract ideas. (Reversed)",
    "I do not have a good imagination. (Reversed)",
    "I have difficulty understanding abstract ideas. (Reversed)"
]

st.header("Rate the Following Statements")

agr_ratings = create_sliders(agr_statements, "Agreeableness (AGR)")
csn_ratings = create_sliders(csn_statements, "Conscientiousness (CSN)")
est_ratings = create_sliders(est_statements, "Emotional Stability (EST)")
opn_ratings = create_sliders(opn_statements, "Openness to Experience (OPN)")

agreeableness = sum(agr_ratings) / len(agr_ratings)
conscientiousness = sum(csn_ratings) / len(csn_ratings)
emotional_stability = sum(est_ratings) / len(est_ratings)
openness = sum(opn_ratings) / len(opn_ratings)

all_ratings = [agreeableness, conscientiousness, emotional_stability, openness]

if st.button('Get Your Extraversion Score'):
    prediction = model.predict([all_ratings])
    extraversion_score = prediction[0]
    st.subheader("Prediction")
    st.markdown(f"<div class='prediction'>Based on your responses, your predicted Extraversion score is: {extraversion_score:.2f}</div>", unsafe_allow_html=True)

    if extraversion_score > 4:
        st.write("You are highly extroverted. You enjoy social interactions and feel energized by being around others.")
    elif extraversion_score > 3:
        st.write("You have a moderate level of extraversion. You enjoy social activities but also appreciate some quiet time.")
    elif extraversion_score > 2:
        st.write("You are somewhat introverted. You may enjoy social interactions, but you also value your alone time.")
    else:
        st.write("You are highly introverted. You prefer solitary activities and feel more comfortable in quiet environments.")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
---
Created with ❤️ using Streamlit.
</div>
""", unsafe_allow_html=True)
