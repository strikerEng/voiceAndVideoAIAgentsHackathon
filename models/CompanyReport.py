from pydantic import BaseModel, Field
from typing import Optional, List, Dict

class BusinessMetrics(BaseModel):
    product_releases: int = Field(..., description="Number of new products, features, or significant updates launched")
    user_metrics: Dict[str, float] = Field(default_factory=dict, description="Key user metrics including adoption, engagement, or satisfaction scores")
    service_metrics: Dict[str, float] = Field(default_factory=dict, description="Service usage statistics, API calls, or platform metrics")

class MarketPosition(BaseModel):
    market_metrics: Dict[str, float] = Field(default_factory=dict, description="Market-related metrics including share, ranking, or category position")
    brand_metrics: Dict[str, float] = Field(default_factory=dict, description="Brand performance indicators including sentiment and awareness")
    competitive_metrics: Dict[str, float] = Field(default_factory=dict, description="Competitive analysis and industry benchmark comparisons")

class FinancialIndicators(BaseModel):
    growth_metrics: Dict[str, float] = Field(default_factory=dict, description="Growth-related metrics including revenue, user base, or market expansion")
    performance_metrics: Dict[str, float] = Field(default_factory=dict, description="Financial performance indicators and efficiency metrics")
    partnership_metrics: Dict[str, float] = Field(default_factory=dict, description="Partnership and business development metrics")

class TechnicalInfrastructure(BaseModel):
    reliability_metrics: Dict[str, float] = Field(default_factory=dict, description="System reliability and performance metrics")
    efficiency_metrics: Dict[str, float] = Field(default_factory=dict, description="Infrastructure efficiency and optimization metrics")

class TeamDynamics(BaseModel):
    team_metrics: Dict[str, float] = Field(default_factory=dict, description="Team-related metrics including headcount, retention, and distribution")
    growth_indicators: Dict[str, float] = Field(default_factory=dict, description="Team growth and expansion metrics")

class InnovationMetrics(BaseModel):
    development_metrics: Dict[str, float] = Field(default_factory=dict, description="Development velocity and shipping metrics")
    innovation_indicators: Dict[str, float] = Field(default_factory=dict, description="Innovation measurements including research, patents, and contributions")

class MonthlyReport(BaseModel):
    month: int = Field(..., description="Month number (1-12) of the report")
    year: int = Field(..., description="Year of the report")
    business_metrics: BusinessMetrics
    market_position: MarketPosition
    financial_indicators: FinancialIndicators
    technical_infrastructure: TechnicalInfrastructure
    team_dynamics: TeamDynamics
    innovation_metrics: InnovationMetrics
    raw_sources: Dict[str, str] = Field(default_factory=dict, description="Dictionary of raw data sources and their content used for this report")

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
