from models.CompanyReport import CompanyReport, BusinessMetrics, MarketPosition, FinancialIndicators, InnovationMetrics, TechnicalInfrastructure, TeamDynamics
import json
import os

file = open(os.path.expanduser("~/git_dir/voiceAndVideoAIAgentsHackathon/test_files/company_report_anthropic.json"))
company_report_anthropic = json.load(file)

print(f'The name is {company_report_anthropic["name"]}')

perplexity_q2_report = CompanyReport(
    name = company_report_anthropic["name"],
    time_period="This year",
    month=1,
    year=2024,
    business_metrics=BusinessMetrics(
        product_highlights= company_report_anthropic["business_metrics"]["product_highlights"],
        user_growth=company_report_anthropic["business_metrics"]["user_growth"],
        service_performance=company_report_anthropic["business_metrics"]["service_performance"],
    ),
    market_position=MarketPosition(
        market_standing=company_report_anthropic["market_position"]["market_standing"],
        brand_performance=company_report_anthropic["market_position"]["brand_performance"],
        competitive_analysis=company_report_anthropic["market_position"]["competitive_analysis"]
    ),
    financial_indicators=FinancialIndicators(
        growth_summary=company_report_anthropic["financial_indicators"]["growth_summary"],
        performance_highlights=company_report_anthropic["financial_indicators"]["performance_highlights"],
        strategic_developments=company_report_anthropic["financial_indicators"]["strategic_developments"]
    ),
    technical_infrastructure=TechnicalInfrastructure(
        platform_performance=company_report_anthropic["technical_infrastructure"]["platform_performance"],
        infrastructure_developments=company_report_anthropic["technical_infrastructure"]["infrastructure_developments"]
    ),
    team_dynamics=TeamDynamics(
        workforce_overview=company_report_anthropic["team_dynamics"]["workforce_overview"],
        organizational_changes=company_report_anthropic["team_dynamics"]["workforce_overview"]
    ),
    innovation_metrics=InnovationMetrics(
        development_highlights=company_report_anthropic["innovation_metrics"]["development_highlights"],
        research_impact=company_report_anthropic["innovation_metrics"]["research_impact"]
    ),
    raw_sources={"":""}
)