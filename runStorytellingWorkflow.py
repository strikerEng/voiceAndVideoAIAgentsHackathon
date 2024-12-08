import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
import traceback
from workflows import SayHello
from Storytelling import StoryTellingActivities
from temporalio.client import Client, WorkflowFailureError
from shared import STORY_TELLING_TASK_QUEUE_NAME

from mockMonthlyReport import perplexity_q2_report
from temporalio.client import Client, WorkflowFailureError

async def main() -> None:
    # Create client connected to server at the given address
    client: Client = await Client.connect("localhost:7233")

    try:
        result = await client.execute_workflow(
            SayHello.run,
            perplexity_q2_report,
            id="start-storytelling-03",
            task_queue=STORY_TELLING_TASK_QUEUE_NAME,
        )
        print(f"Result: {result}")

    except:
        print("Got expected exception: ", traceback.format_exc())


if __name__ == "__main__":
    asyncio.run(main())