from datetime import timedelta
from temporalio import workflow
from models.CompanyReport import CompanyReport
from typing import List

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from Storytelling import StoryTellingActivities
    
# do not instatiate anything in the workflow class

@workflow.defn
class SayHello:
    @workflow.run
    async def run(self, report: CompanyReport) -> List[str]:
        return await workflow.execute_activity(
            StoryTellingActivities.create_business_metric_slide, report, start_to_close_timeout=timedelta(seconds=600)
        )