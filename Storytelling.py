import asyncio
import autogen
from ag2Setup import user_proxy, coder, critic, llm_config
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
from mockMonthlyReport import perplexity_q2_report
from models.CompanyReport import CompanyReport
from typing import List
from temporalio import activity
import asyncio

class StoryTellingActivities:
    def __init__(self) -> None:
        groupchat = autogen.GroupChat(agents=[user_proxy, coder, critic], messages=[], max_round=20)
        self.manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)
        self.user_proxy = user_proxy

    @activity.defn
    async def create_business_metric_slide(self, data: CompanyReport) -> List[str]:
        human_message = f"Create the company wrapped information for the company {data.name} with the following business metrics {data.business_metrics}. Save the summary to a file."

        try:
            path_of_saved_image = await asyncio.to_thread(
                self.user_proxy.initiate_chat, recipient=self.manager, message=human_message
            )
            return path_of_saved_image
        except Exception:
            activity.logger.exception(f"Could not create an image")
            raise


    
#  Create and save an image influenced by Spotify wrapped for company OpenAI showcasing their 4 product release and their direct traffic percentage 76%. Make sure to save the image to my computer and return the path to the image as a string.