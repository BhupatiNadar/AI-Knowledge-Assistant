import streamlit as st
import bcrypt
from src.database.config import Supabase


def create_new_user(name, email, hashed_password):
    return (
        Supabase.table("users")
        .insert({
            "user_name": name,
            "user_email": email,
            "password_hash": hashed_password
        })
        .execute()
    )


def check_user(email, password):
    response1 = (
        Supabase.table("users")
        .select("user_email, password_hash")
        .eq("user_email", email)
        .execute()
    )
    
    response2=(
        Supabase.table("users").select("user_id,user_name,user_email").eq("user_email",email).execute()
    )

    
    if not response1.data or not response2.data:
        return False,{}

    stored_hash = response1.data[0]["password_hash"]

    return bcrypt.checkpw(
        password.encode("utf-8"),
        stored_hash.encode("utf-8")
    ),response2.data
    

def insert_document(user_id, file_name):

    response = (
        Supabase.table("documents")
        .insert({
            "user_id": user_id,
            "file_name": file_name
        })
        .execute()
    )

    return response.data[0]["document_id"]


def insert_document_pages(document_id, pages):

    rows = [
        {
            "document_id": document_id,
            "page_number": page["page_number"],
            "page_content": page["page_content"]
        }
        for page in pages
    ]

    return (
        Supabase.table("document_pages")
        .insert(rows)
        .execute()
    )


def fetch_documents(user_id):

    response = (
        Supabase.table("documents")
        .select("document_id,file_name,uploaded_at")
        .eq("user_id", user_id)
        .order("uploaded_at", desc=True)
        .execute()
    )

    return response.data


def remove_user_document(document_id, user_id):

    response = (
        Supabase.table("documents")
        .delete()
        .eq("document_id", document_id)
        .eq("user_id", user_id)
        .execute()
    )

    return response

def fetch_document_pages(user_id):
    response = (
    Supabase.table("document_pages")
    .select("""
        page_id,
        page_number,
        page_content,
        documents!inner(
            document_id,
            file_name,
            user_id
        )
    """)
    .eq("documents.user_id", user_id)
    .execute()
)
    
    return response.data

def insert_document_chunks(rows):

    response = (
        Supabase.table("document_chunks")
        .insert(rows)
        .execute()
    )

    return response.data

def save_message(conversation_id, role, content):
    Supabase.table("messages").insert({
        "conversation_id": conversation_id,
        "role": role,
        "content": content
    }).execute()
    
def get_history(conversation_id):
    response = (
        Supabase.table("messages")
        .select("role,content")
        .eq("conversation_id", conversation_id)
        .order("created_at")
        .execute()
    )

    return response.data


def create_conversation(user_id):
    response = (
        Supabase.table("conversations")
        .insert({"user_id": user_id})
        .execute()
    )
    return response.data[0]["conversation_id"]


def fetch_conversations(user_id):
    response = (
        Supabase.table("conversations")
        .select("conversation_id, created_at")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .execute()
    )
    return response.data


def delete_conversation(conversation_id, user_id):
    Supabase.table("messages").delete().eq(
        "conversation_id", conversation_id
    ).execute()

    Supabase.table("conversations").delete().eq(
        "conversation_id", conversation_id
    ).eq("user_id", user_id).execute()


def get_conversation_title(conversation_id):
    response = (
        Supabase.table("messages")
        .select("content")
        .eq("conversation_id", conversation_id)
        .eq("role", "user")
        .order("created_at")
        .limit(1)
        .execute()
    )

    if response.data:
        title = response.data[0]["content"]
        return title[:50] + "..." if len(title) > 50 else title

    return "New Conversation"