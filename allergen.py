"""
FastMCP Allergen Server
"""

import os
from langchain_openai import OpenAIEmbeddings
from supabase import create_client, Client
from fastmcp import FastMCP

OPEN_AI_API = os.getenv("OPENAI_API_KEY")
# TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")


# Create server
mcp = FastMCP("Allergen Server")

@mcp.tool()
def allergen_tool(ing: str) -> str:
    """Find allergen from database

    Args:
        ing: ingredient.
    """

    ing = ing + " allergy"
    vector = embeddings.embed_query(ing)
    data = supabase.rpc('match_documents', params={'query_embedding': vector}).execute()
    if data.data[0]['similarity']>=0.5:
        return data.data[0]['content']
    else:
        return "No allergen found for " + ing

