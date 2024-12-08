from pydantic import BaseModel, Field
from typing import Optional, List, Dict

class ResearchQuestions(BaseModel):
    business_metrics_questions: List[str] = Field(
        default_factory=list,
        description="Questions about product releases, user metrics, and service performance"
    )
    market_position_questions: List[str] = Field(
        default_factory=list,
        description="Questions about market metrics, brand performance, and competitive analysis"
    )
    financial_indicators_questions: List[str] = Field(
        default_factory=list,
        description="Questions about growth, financial performance, and partnerships"
    )
    technical_infrastructure_questions: List[str] = Field(
        default_factory=list,
        description="Questions about system reliability and infrastructure efficiency"
    )
    team_dynamics_questions: List[str] = Field(
        default_factory=list,
        description="Questions about team metrics and growth indicators"
    )
    innovation_metrics_questions: List[str] = Field(
        default_factory=list,
        description="Questions about development velocity and innovation indicators"
    )

class BusinessMetrics(BaseModel):
    product_highlights: List[str] = Field(default_factory=list, description="Key product launches and feature updates")
    user_growth: str = Field(..., description="Description of user base growth and engagement trends")
    service_performance: str = Field(..., description="Overview of service usage and performance metrics")

class MarketPosition(BaseModel):
    market_standing: str = Field(..., description="Analysis of market position and share")
    brand_performance: str = Field(..., description="Overview of brand strength and perception")
    competitive_analysis: str = Field(..., description="Summary of competitive positioning and benchmarks")

class FinancialIndicators(BaseModel):
    growth_summary: str = Field(..., description="Overview of key growth metrics and trends")
    performance_highlights: str = Field(..., description="Summary of financial performance and key metrics")
    strategic_developments: str = Field(..., description="Key partnerships, investments, and strategic moves")

class TechnicalInfrastructure(BaseModel):
    platform_performance: str = Field(..., description="Analysis of technical reliability and performance")
    infrastructure_developments: str = Field(..., description="Key technical improvements and scaling initiatives")

class TeamDynamics(BaseModel):
    workforce_overview: str = Field(..., description="Summary of team growth and composition")
    organizational_changes: str = Field(..., description="Key leadership changes and restructuring")

class InnovationMetrics(BaseModel):
    development_highlights: str = Field(..., description="Key technological achievements and developments")
    research_impact: str = Field(..., description="Summary of research contributions and patents")

class CompanyReport(BaseModel):
    time_period: str = Field(..., description="Time period covered by the report")
    business_metrics: BusinessMetrics
    market_position: MarketPosition
    financial_indicators: FinancialIndicators
    technical_infrastructure: TechnicalInfrastructure
    team_dynamics: TeamDynamics
    innovation_metrics: InnovationMetrics

### example output
# perplexity_q2_report = MonthlyReport(
#     month=6,
#     year=2024,
#     business_metrics=BusinessMetrics(
#         product_releases=2,
#         user_metrics={
#             "monthly_active_users": 15000000,
#             "website_visits": 67420000,
#             "avg_session_duration": 10.85,
#             "pages_per_visit": 1.81,
#             "bounce_rate": 62.63
#         },
#         service_metrics={
#             "direct_traffic_percentage": 76.87
#         }
#     ),
#     market_position=MarketPosition(
#         market_metrics={
#             "monthly_growth_rate": 20.71
#         },
#         brand_metrics={
#             "accuracy_rate": 80.0
#         },
#         competitive_metrics={}
#     ),
#     financial_indicators=FinancialIndicators(
#         growth_metrics={
#             "revenue_run_rate": 50000000,
#             "valuation": 3000000000
#         },
#         performance_metrics={
#             "subscription_price": 20.0
#         },
#         partnership_metrics={
#             "funding_raised": 250000000
#         }
#     ),
#     technical_infrastructure=TechnicalInfrastructure(
#         reliability_metrics={
#             "accuracy_rate": 80.0
#         },
#         efficiency_metrics={}
#     ),
#     team_dynamics=TeamDynamics(
#         team_metrics={},
#         growth_indicators={}
#     ),
#     innovation_metrics=InnovationMetrics(
#         development_metrics={},
#         innovation_indicators={}
#     ),
#     raw_sources={}
# )
