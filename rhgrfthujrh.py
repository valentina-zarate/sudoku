import requests
import tkinter as tk
from tkinter import ttk

url="https://sudoku-api.vercel.app/api/dosuku"
sudoku=[]
entrada="f"
dificultad= ""
if entrada == "f":
    while dificultad != "Easy":
        resp=requests.get(url)
        print(resp)
        if dificultad=="Easy":
            break
        
        <Response [504]>