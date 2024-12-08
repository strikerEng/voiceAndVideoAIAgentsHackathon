import sys
from pathlib import Path
from datetime import datetime
import json

# Add the project root to Python path to enable absolute imports
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from pydantic import BaseModel
from dotenv import load_dotenv
from typing import List
# Use absolute import from project root
from models.CompanyReport import ResearchQuestions, CompanyReport
import os
from typing import Dict, Any
from langchain_community.chat_models import ChatPerplexity
from langchain_core.messages import SystemMessage, HumanMessage
import time

load_dotenv()

def generate_research_questions(company_name: str) -> ResearchQuestions:
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.1,
        stop_sequences=None
    ).with_structured_output(ResearchQuestions)
    
    prompt = ChatPromptTemplate.from_messages([
            ("system", 
             """For each of the categories below create 2 searchable questions that will help gather 
             comprehensive data about a company's annual performance. 
             Your questions should be designed to collect information that maps directly to our report structure. 
             Each question should:

                1. Focus on quantifiable metrics where possible
                2. Be answerable through public information
                3. Focus on annual data and year-over-year comparisons
                4. Start with words like "What", "How many", "How much"
                5. Cover multiple aspects of a section when possible

                Generate questions that will help populate these specific metrics:

                Business Metrics:
                - Annual product releases and major feature updates
                - Year-over-year user/customer growth rates
                - Annual service usage and engagement metrics

                Market Position:
                - Annual market share and year-over-year changes
                - Brand performance and recognition metrics
                - Year-end competitive positioning

                Financial Indicators:
                - Annual revenue and profitability metrics
                - Year-over-year financial performance indicators
                - Major strategic partnerships and investments for the fiscal year

                Technical Infrastructure:
                - Annual system reliability and performance metrics
                - Year-over-year platform improvements and scaling

                Team Dynamics:
                - Annual headcount and workforce composition
                - Significant organizational restructuring and leadership changes

                Innovation Metrics:
                - Annual R&D investments and outcomes
                - Yearly patent portfolio growth
                - Major technological achievements and contributions

                Your questions should be specific enough to gather data that can populate the CompanyReport structure shown in the example output."""),
            ("human", "Research the following company: {company_name}")
        ])
    messages = prompt.format_messages(company_name=company_name)
    questions = llm.invoke(messages)
    return questions if isinstance(questions, ResearchQuestions) else ResearchQuestions.model_validate(questions)

ResearchAnswers = List[str]

def compile_question_results(research_questions: ResearchQuestions) -> ResearchAnswers:
    # Initialize Perplexity chat model
    chat = ChatPerplexity(
        model="llama-3.1-sonar-large-128k-online",
        temperature=0.2,
        pplx_api_key=os.getenv("PPLX_API_KEY")
    )
    
    answers = []
    
    for category, questions in research_questions.model_dump().items():
        for question in questions:
            print(f"Researching question: {question}")
            messages = [
                SystemMessage(content=(
                    "You are a business research assistant. Provide concise, "
                    "factual answers focused on the most recent annual data. "
                    "Include specific numbers and metrics when available. "
                    f"This question relates to the category: {category}"
                )),
                HumanMessage(content=question)
            ]
            
            try:
                response = chat.invoke(messages)
                answers.append(response.content)
                print(f"Answer: {response.content}")
                
                # Add delay to stay within rate limits (20 requests/min)
                # time.sleep(3)
                
            except Exception as e:
                print(f"Error processing question '{question}': {str(e)}")
                answers.append(f"Error retrieving answer: {str(e)}")
    
    return answers

def generate_company_report(answers: ResearchAnswers, company_name: str) -> CompanyReport:
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.1,
        stop_sequences=None
    ).with_structured_output(CompanyReport)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", """
         You are a business analyst creating a comprehensive company report. For each section, provide detailed narratives (2-3 sentences minimum per field) that tell the complete story of the company's performance. Your analysis should:

            1. BUSINESS METRICS
            - product_highlights: List and describe each major product release, including its impact and market reception
            - user_growth: Describe user acquisition trends, engagement patterns, and any notable demographic or geographic expansion
            - service_performance: Detail platform performance metrics, including usage patterns, reliability statistics, and any notable improvements

            2. MARKET POSITION
            - market_standing: Analyze the company's position in their industry, including market share trends, growth trajectory, and competitive advantages
            - brand_performance: Evaluate brand strength, public perception, media coverage, and notable achievements or recognition
            - competitive_analysis: Compare against key competitors, including relative strengths, weaknesses, and competitive dynamics

            3. FINANCIAL INDICATORS
            - growth_summary: Provide detailed analysis of growth across key metrics, including revenue, user base, and market expansion
            - performance_highlights: Detail key financial achievements, including revenue figures, profitability metrics, and notable financial milestones
            - strategic_developments: Describe major partnerships, investments, and strategic initiatives, including their potential impact

            4. TECHNICAL INFRASTRUCTURE
            - platform_performance: Detail technical capabilities, including performance metrics, reliability statistics, and system improvements
            - infrastructure_developments: Describe major technical initiatives, scaling efforts, and infrastructure investments

            5. TEAM DYNAMICS
            - workforce_overview: Provide detailed analysis of team growth, including department expansion and expertise distribution
            - organizational_changes: Detail leadership changes, restructuring efforts, and their impact on company direction

            6. INNOVATION METRICS
            - development_highlights: Detail technological achievements, product innovations, and their market impact
            - research_impact: Analyze research contributions, including papers published, patents filed, and industry influence

            Include specific metrics when available, but embed them within detailed contextual descriptions that explain their significance. Focus on both quantitative achievements and qualitative impacts."""
),
        ("human", "Based on this research about {company_name}, generate a structured report: {answers}")
    ])
    
    messages = prompt.format_messages(company_name=company_name, answers=answers)
    report = llm.invoke(messages)
    return report if isinstance(report, CompanyReport) else CompanyReport.model_validate(report)

if __name__ == "__main__":
    questions = generate_research_questions("Mistral AI")
    print(questions)
    answers = compile_question_results(questions)
    # Save research results to JSON file
    results = {
        "questions": questions.model_dump(),
        "answers": answers
    }
    
    output_file = f"research_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    
    print(f"\nResults saved to: {output_file}")
    print(answers)
    
    # with open("research_results_20241207_160833.json", "r", encoding="utf-8") as f:
    #     results = json.load(f) 
    
    report = generate_company_report(results["answers"], "Anthropic AI")
    print(report)
    
    output_file = f"company_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(report.model_dump(), f, indent=4, ensure_ascii=False)
    
    print(f"\nFull report saved to: {output_file}")
