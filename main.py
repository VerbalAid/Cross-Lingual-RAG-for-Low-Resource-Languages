import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Actual multilingual documents
DOCUMENTS = {
    'Irish': [
        "Ceol traidisiúnta na hÉireann: an bodhrán, an fheadóg stáin, agus na píobaí uilleann. Seanfhocal: 'Is fearr Gaeilge bhriste ná Béarla cliste'.",
        "Miotaseolaíocht Éireannach: Tuatha Dé Danann agus laochra cosúil le Cú Chulainn. Údair: James Joyce, W.B. Yeats, Samuel Beckett.",
        "Aillte an Mhothair: 214 méadar ar airde. Clochán na bhFomhórach: 40,000 colún basalt. Sí an Bhrú: tuama pasáiste 5,000 bliain d'aois."
    ],
    'French': [
        "La cuisine française est patrimoine de l'UNESCO. Plats célèbres: coq au vin, bouillabaisse, ratatouille. La France a plus de 400 fromages comme le camembert et le roquefort.",
        "La culture française: philosophes comme Descartes et Voltaire. L'Académie française, fondée en 1635, préserve la langue française.",
        "Monuments parisiens: Tour Eiffel (1889), cathédrale Notre-Dame, musée du Louvre qui abrite la Joconde."
    ],
    'Spanish': [
        "El español lo hablan más de 500 millones de personas. Miguel de Cervantes escribió Don Quijote, considerada la primera novela moderna.",
        "Arte español: Picasso, Dalí y Miró. El flamenco de Andalucía combina cante, baile y guitarra como patrimonio de la UNESCO.",
        "La Sagrada Familia y el Park Güell de Gaudí muestran arquitectura modernista única. Cocina española: paella, gazpacho y tapas."
    ]
}

class SimpleRAG:
    def __init__(self):
        self.model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
        self.embeddings = None
        self.docs = []
    
    def build_index(self, documents_dict):
        """Build search index from documents"""
        self.docs = []
        for docs in documents_dict.values():
            self.docs.extend(docs)
        
        self.embeddings = self.model.encode(self.docs, convert_to_numpy=True)
        return len(self.docs)
    
    def search(self, query, top_k=3):
        """Search for relevant documents"""
        query_embedding = self.model.encode([query], convert_to_numpy=True)
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        return [(self.docs[idx], float(similarities[idx])) for idx in top_indices]

# --- Streamlit App ---
st.set_page_config(page_title="Cross-Lingual RAG", page_icon="🌍")

# Landing Page Header
st.title("🌍 Cross-Lingual RAG Project")
st.markdown("""
### Search across Irish, French & Spanish documents
Ask questions in any language and find relevant information from our multilingual collection.
""")

# Initialize RAG
if 'rag' not in st.session_state:
    st.session_state.rag = SimpleRAG()
    with st.spinner("Loading AI model and building search index..."):
        num_docs = st.session_state.rag.build_index(DOCUMENTS)
    st.success(f"✅ Ready! Loaded {num_docs} documents in 3 languages")

st.divider()

# Search Interface
query = st.text_input(
    "**Ask your question:**",
    placeholder="e.g., Tell me about traditional music or famous artists...",
    key="search_query"
)

if query:
    with st.spinner("Searching through multilingual documents..."):
        results = st.session_state.rag.search(query, top_k=3)
    
    st.subheader("📚 Search Results")
    
    for i, (doc, similarity) in enumerate(results):
        score_color = "green" if similarity > 0.7 else "orange" if similarity > 0.5 else "red"
        
        st.markdown(f"**Result {i+1}** • :{score_color}[**Relevance: {similarity:.1%}**]")
        st.info(doc)
        st.write("")

st.markdown("---")
