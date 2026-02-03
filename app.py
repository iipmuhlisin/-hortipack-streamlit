import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Data training
data = {
    'gramatur': [125, 150, 175, 150, 125, 175, 150, 125, 175, 150],
    'L': [400, 350, 300, 400, 350, 300, 400, 350, 300, 400],
    'W': [300, 280, 250, 300, 280, 250, 300, 280, 250, 300],
    'H': [250, 200, 180, 250, 200, 180, 250, 200, 180, 250],
    'RH': [70, 80, 90, 75, 85, 70, 80, 90, 75, 85],
    'BCT': [3200, 2800, 2100,
