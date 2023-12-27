import pickle
import streamlit as st
import time

model = pickle.load(open("model/animal_model.sav", "rb"))

st.image("assets/header.jpg")
st.header(":rainbow[Prediction Animal Class Type]", divider="rainbow")
st.write(
    "Please input the characteristics of the animal you are going to predict here!"
)

hair = st.selectbox("Does the animal have Hair?", ["No", "Yes"])
if hair == "No":
    hair = 0
else:
    hair = 1

feathers = st.selectbox("Does the animal have Feathers?", ["No", "Yes"])
if feathers == "No":
    feathers = 0
else:
    feathers = 1

eggs = st.selectbox("Is the animal lays Eggs?", ["No", "Yes"])
if eggs == "No":
    eggs = 0
else:
    eggs = 1

milk = st.selectbox("Is the animal produces Milk?", ["No", "Yes"])
if milk == "No":
    milk = 0
else:
    milk = 1

airborne = st.selectbox(
    "Is the animal has the ability to fly in the air?", ["No", "Yes"]
)
if airborne == "No":
    airborne = 0
else:
    airborne = 1

aquatic = st.selectbox("Is the animal live in the water?", ["No", "Yes"])
if aquatic == "No":
    aquatic = 0
else:
    aquatic = 1

predator = st.selectbox("Is the animal a Predator?", ["No", "Yes"])
if predator == "No":
    predator = 0
else:
    predator = 1

toothed = st.selectbox("Does the animal have teeth?", ["No", "Yes"])
if toothed == "No":
    toothed = 0
else:
    toothed = 1

backbone = st.selectbox("Does the animal have Backbone", ["No", "Yes"])
if backbone == "No":
    backbone = 0
else:
    backbone = 1

breathes = st.selectbox("Is the animal breathe?", ["No", "Yes"])
if breathes == "No":
    breathes = 0
else:
    breathes = 1

venomous = st.selectbox("Does the animal have venom?", ["No", "Yes"])
if venomous == "No":
    venomous = 0
else:
    venomous = 1

fins = st.selectbox("Does the animal have Fins", ["No", "Yes"])
if fins == "No":
    fins = 0
else:
    fins = 1

legs = st.selectbox(
    "How many legs does the animal have?",
    ["0 Leg", "2 Legs", "4 Legs", "5 Legs", "6 Legs", "8 Legs"],
)
if legs == "0 Leg":
    legs = 0
elif legs == "2 Legs":
    legs = 2
elif legs == "4 Legs":
    legs = 3
elif legs == "5 Legs":
    legs = 5
elif legs == "6 Legs":
    legs = 6
else:
    legs = 8

tail = st.selectbox("Does the animal have Tail", ["No", "Yes"])
if tail == "No":
    tail = 0
else:
    tail = 1

domestic = st.selectbox("Can the animal be a pet?", ["No", "Yes"])
if domestic == "No":
    domestic = 0
else:
    domestic = 1

catsize = st.selectbox("Is the animal the size of a cat?", ["No", "Yes"])
if catsize == "No":
    catsize = 0
else:
    catsize = 1

if st.button("Prediction"):
    X = [
        [
            hair,
            feathers,
            eggs,
            milk,
            airborne,
            aquatic,
            predator,
            toothed,
            backbone,
            breathes,
            venomous,
            fins,
            legs,
            tail,
            domestic,
            catsize,
        ]
    ]
    result = model.predict(X)
    category = ["Mammal", "Bird", "Reptile", "Fish", "Amphibian", "Bug", "Invertebrate"]

    progress_text = "Prediction in progress. Please wait..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

    st.success("The animal category is : " + category[result[0] - 1])
