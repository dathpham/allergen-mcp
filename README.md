# Allergen MCP Server
MCP Server for checking food allergen.

This MCP server will be decorated with Langraph tool for AI agent

## System Architecture

```mermaid
graph TD;
    Start-->ReActAgent;
    ReActAgent-->Tool;
    Tool-->MCP Server;
    MCP Server-->|RAG|Supabase_PostgreSQL_Vector_Store;
    Supabase_PostgreSQL_Vector_Store-->MCP_Server
    MCP_Server-->Tool
    Tool-->Agent
    Agent-->|Structured_Return|End
```

## Features
- LangGraph Agent with ReAct reasoning
- MCP Server integration for allergen lookup
- RAG implementation with Supabase vector store

## Components
- **LangGraph Agent**: Orchestrates interactions between tools and LLM
- **MCP Server**: Provides allergen detection tool 
- **Supabase Vector Store**: Stores embeddings for allergen information
- **RAG Tool**: Enables semantic search across allergen data

Langgraph Tool agent is located in [agent/agent.py](agent/agent.py).

This repo has license implication



