# 🧑‍💼 TalentScout – AI Hiring Assistant

## 📌 Project Overview

**TalentScout** is an AI-powered Hiring Assistant chatbot built with **Streamlit** and **Cohere LLM**. It revolutionizes the initial candidate screening process by providing an intelligent, structured, and efficient interview experience.

### ✨ Key Features

- 📝 **Smart Candidate Data Collection** - Captures essential candidate information including contact details, experience, desired roles, and technical skills
- 🤖 **AI-Powered Question Generation** - Uses Cohere's LLM to generate up to 5 tailored technical interview questions based on the candidate's declared tech stack
- 💬 **Guided Conversation Flow** - Presents questions one by one, maintaining context and ensuring structured responses
- 📊 **Comprehensive Summaries** - Records all answers and provides detailed interview summaries
- 🚀 **Professional Conclusion** - Gracefully concludes interviews with next steps and thank you messages

### 🎯 Use Cases

- **Initial Technical Screening** - Perfect for filtering candidates before human interviews
- **Standardized Assessment** - Ensures all candidates face consistent, relevant questions
- **Remote Recruitment** - Enables 24/7 candidate screening without human intervention
- **Documentation** - Maintains detailed records of all candidate interactions

## ⚙️ Installation Instructions

### 1. **Clone Repository**
```bash
git clone https://github.com/murali954/Talentscout-assisstant.git
```


### 2. **Install Dependencies**
```bash
streamlit>=1.28.0
cohere>=4.37.0
```

### 3. **Set API Key**

For demo purposes, the code contains a placeholder for the Cohere API Key. For production:

#### Environment Variable Method (Recommended):
```bash
# Linux/Mac
export COHERE_API_KEY="your_actual_cohere_api_key_here"

# Windows
set COHERE_API_KEY=your_actual_cohere_api_key_here
```

#### .env File Method:
Create a `.env` file in the project root:
```env
COHERE_API_KEY=your_actual_cohere_api_key_here
```

### 5. **Run the Application**
```bash
streamlit run app.py
```

The application will automatically open in your browser at `http://localhost:8501`.

## 🚀 Usage Guide

### Step 1: Launch Application
- Run `streamlit run app.py`
- Browser automatically opens to `http://localhost:8501`

### Step 2: Complete Candidate Form
- Fill in required information:
  - **Personal Details**: Name, email, phone number
  - **Professional Info**: Years of experience, desired position, location
  - **Technical Skills**: Complete tech stack (e.g., "Python, React, PostgreSQL, AWS")
- Click **"Save & Start Interview"**

### Step 3: Answer Interview Questions
- AI generates up to 5 tailored questions based on your tech stack
- Questions appear **one at a time**
- Provide detailed answers in the text area
- Click **"Submit Answer"** to proceed to the next question
- Progress bar shows your completion status

### Step 4: Review Summary
- After completing all questions, view comprehensive summary
- Summary includes:
  - All candidate information
  - Complete Q&A transcript
  - Interview completion statistics
- Download summary as JSON file for records

### Step 5: Next Steps
- Application provides clear next steps information
- Option to start a new interview session
- Professional conclusion with timeline expectations

## 🛠 Technical Architecture

### **Technology Stack**
- **Frontend**: Streamlit (Python web framework)
- **AI Engine**: Cohere LLM (command-r-plus model)
- **Backend**: Python 3.10+
-

### **Core Libraries**
- `streamlit`: Web application framework and UI components
- `cohere`: LLM integration for intelligent question generation
- `re`: Regular expression parsing for question extraction
- `datetime`: Timestamp generation and formatting
- `os`: Environment variable management

### **Application Flow**
```
User Input → Streamlit Form → Validation → 
Cohere API → Question Generation → 
Session State Management → Q&A Loop → 
```

### **State Management**
The application uses Streamlit's session state to maintain:
- `candidate_info`: Personal and professional details
- `questions`: Generated interview questions list
- `answers`: Complete Q&A pairs with metadata
- `current_question`: Interview progress tracking
- `interview_started`: Application flow control
- `interview_completed`: Summary display trigger

## 🎯 AI Prompt Design

### **Question Generation Strategy**
The system sends carefully crafted prompts to Cohere that include:

```python
prompt = f"""
You are an expert technical recruiter. Generate exactly 5 focused technical interview questions for a candidate with the following tech stack: {tech_stack}

Rules:
1. Generate EXACTLY 5 questions, no more, no less
2. Cover the most important and commonly used technologies first
3. Make questions practical and relevant to real-world scenarios
4. Vary difficulty from basic to intermediate
5. Each question should be clear and concise
6. Format as a numbered list (1. 2. 3. 4. 5.)

Tech Stack: {tech_stack}
"""
```

### **Prompt Engineering Benefits**
- **Consistency**: Ensures exactly 5 questions every time
- **Relevance**: Focuses on candidate's declared skills
- **Priority**: Covers most important technologies first
- **Practicality**: Questions relate to real-world scenarios
- **Structure**: Numbered format for easy parsing

## ⚡ Challenges & Solutions

### 1. **API Reliability**
- **Challenge**: Cohere API failures could break the application
- **Solution**: Comprehensive error handling with user-friendly messages
- **Implementation**: Try-catch blocks with graceful degradation

```python
try:
    response = co.generate(...)
    # Process response
except Exception as e:
    st.error("⚠️ Unable to generate questions now, please try later")
    # Offer retry option
```

### 2. **Question Parsing Consistency**
- **Challenge**: LLM responses can vary in format
- **Solution**: Robust regex parsing with fallback handling
- **Implementation**: Multiple parsing strategies and validation

### 3. **Conversation Flow Control**
- **Challenge**: Maintaining structured Q&A without free-form chat
- **Solution**: Session state management with strict progression logic
- **Implementation**: Sequential question presentation with validation



**TalentScout** - Transforming technical recruitment through AI-powered conversations 🚀
