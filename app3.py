import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

# --------------------------
# Données des utilisateurs
# --------------------------
lesDonneesDesComptes = {
    'usernames': {
        'testeur': {  # Nom d'utilisateur (doit être en minuscule ici)
            'name': 'Testeur',
            'password': 'testMDP',
            'role': 'utilisateur'
        },
        'root': {
            'name': 'Admin',
            'password': 'adminMDP',
            'role': 'administrateur'
        }
    }
}

# --------------------------
# Authentification
# --------------------------
authenticator = Authenticate(
    lesDonneesDesComptes,
    "cookie_name",
    "cookie_key",
    30
)

authenticator.login(fields={
    "Form name": "Connexion",
    "Username": "Nom d’utilisateur (Testeur)",
    "Password": "Mot de passe (testMDP)",
    "Login": "Se connecter"
})

# --------------------------
# Interface utilisateur
# --------------------------
if st.session_state["authentication_status"]:
    # Bouton de déconnexion
    authenticator.logout("Déconnexion", location="sidebar")

    # Menu principal horizontal
    
    
    with st.sidebar:selection = option_menu(
        menu_title=None,
        options=["Accueil", "Les photos de mon chat"],
        icons=["house", "camera"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical"
    )

    # Affichage conditionnel selon la sélection
    if selection == "Accueil":
        st.header("Bienvenue sur la page d'accueil !")

    elif selection == "Les photos de mon chat":
        st.header("Bienvenue dans l'album de mon chat 🐱")

        # Trois colonnes avec images
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("images/roro1.jpg")
        with col2:
            st.image("images/roro2.jpg")
        with col3:
            st.image("images/roro3.jpg")



elif st.session_state["authentication_status"] is False:
    st.error("Le nom d’utilisateur ou le mot de passe est incorrect.")

elif st.session_state["authentication_status"] is None:
    st.warning("Veuillez entrer vos identifiants.")


