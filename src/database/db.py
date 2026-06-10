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
    response = (
        Supabase.table("users")
        .select("user_email, password_hash")
        .eq("user_email", email)
        .execute()
    )

    if not response.data:
        return False

    stored_hash = response.data[0]["password_hash"]

    return bcrypt.checkpw(
        password.encode("utf-8"),
        stored_hash.encode("utf-8")
    )