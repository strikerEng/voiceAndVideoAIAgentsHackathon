import autogen
import os

config_list_gpt4 = autogen.config_list_from_json(
    os.path.expanduser("~/git_dir/voiceAndVideoAIAgentsHackathon/config_list.json"),
    filter_dict={
        "model": ["gpt-4", "gpt-4-0314", "gpt4", "gpt-4-32k", "gpt-4-32k-0314", "gpt-4-32k-v0314"],
    },
)

llm_config = {"config_list": config_list_gpt4, "cache_seed": 42}
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    code_execution_config={
        "last_n_messages": 3,
        "work_dir": "artifacts",
        "use_docker": False,
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    human_input_mode="NEVER",
)
coder = autogen.AssistantAgent(
    name="Coder",  # the default assistant agent is capable of solving problems with code
    llm_config=llm_config,
)
critic = autogen.AssistantAgent(
    name="Storyteller",
    system_message="""Storyteller. You are like the Spotify wrapped for company performance. You are a storyteller that is supposed to write a story of a company's metrics while taking influence from the Spotify wrapped. Write a summary of a company's performance using 10 sentences or less. Focus on key metrics such as product releases, user metrics, and service metrics. Use clear, engaging language and include specific numbers or percentages to showcase a company's success.""",
    llm_config=llm_config,
)

groupchat = autogen.GroupChat(agents=[user_proxy, coder, critic], messages=[], max_round=100)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)