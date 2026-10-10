import streamlit as st

st.set_page_config(page_title="TechNest Support Bot", page_icon="📱")

st.title("🤖 TechNest Mobile Store")
st.write("AI Customer Support Chatbot - ask about products, pricing, orders and more")

# Product Database
products = {
    "iphone": {"name": "iPhone 15", "price": "₹79,999", "stock": "In Stock", "warranty": "1 Year"},
    "samsung": {"name": "Samsung Galaxy S23", "price": "₹69,999", "stock": "In Stock", "warranty": "1 Year"},
    "oneplus": {"name": "OnePlus 11R", "price": "₹39,999", "stock": "Limited Stock", "warranty": "1 Year"},
    "redmi": {"name": "Redmi Note 12", "price": "₹19,999", "stock": "In Stock", "warranty": "1 Year"},
    "laptop": {"name": "HP Laptop", "price": "₹55,999", "stock": "In Stock", "warranty": "2 Years"}
}

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "assistant", "content": "Hi! I'm the TechNest Mobile Store assistant. How can I help you?"})

for msg in st.session_state.messages:
    icon = "🤖" if msg["role"] == "assistant" else "😊"
    st.chat_message(msg["role"], avatar=icon).write(msg["content"])

def get_bot_reply(user_input):
    text = user_input.lower()
    
    for key, details in products.items():
        if key in text:
            return f"📱 **{details['name']}**\n\n💰 Price: {details['price']}\n📦 Stock: {details['stock']}\n🛡️ Warranty: {details['warranty']}\n\nWant to know about delivery or offers?"

    if "price" in text or "cost" in text:
        reply = "Here are our latest prices:\n"
        for p in products.values():
            reply += f"- {p['name']}: {p['price']}\n"
        return reply
    
    if "warranty" in text:
        return "We provide 1 Year warranty for mobiles and 2 Years for laptops. Bills must be kept safe!"
    
    if "order" in text or "delivery" in text:
        return "🚚 Delivery in 2-3 days all over Tamil Nadu! Free delivery above ₹10,000. COD available."
    
    if "contact" in text or "support" in text:
        return "📞 Contact us: 98765-43210 | Email: support@technest.com | 9AM - 9PM"
    
    if "hi" in text or "hello" in text:
        return "Hello bro! Ask me about iPhone, Samsung, OnePlus, Redmi prices, warranty, delivery etc."

    return "Got it bro! For that, contact our support: 98765-43210. Ask me about products, price, warranty etc."

if prompt := st.chat_input("Type your question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="😊").write(prompt)
    
    reply = get_bot_reply(prompt)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant", avatar="🤖").write(reply)