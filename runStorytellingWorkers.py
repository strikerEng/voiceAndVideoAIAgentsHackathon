import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from Storytelling import StoryTellingActivities
from shared import STORY_TELLING_TASK_QUEUE_NAME
from mockMonthlyReport import perplexity_q2_report
from workflows import SayHello


async def main() -> None:
    client: Client = await Client.connect("localhost:7233", namespace="default")
    # Run the worker
    activities = StoryTellingActivities()
    worker: Worker = Worker(
        client,
        task_queue=STORY_TELLING_TASK_QUEUE_NAME,
        workflows=[SayHello],
        activities=[activities.create_business_metric_slide],
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())