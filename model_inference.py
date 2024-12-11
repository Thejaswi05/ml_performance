from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import LLMChain
import json


def refine_summary(json_data: dict) -> str:
    ollama = Ollama(model="llama3")
    json_str = json.dumps(json_data, indent=2)

    prompt_template = PromptTemplate(
        input_variables=["json_str"],
        template="""
        You are a professional performance test engineer. Based on the following API performance data, provide a detailed analysis and summary.
        Here is the data extracted from a JMeter HTML report:

        {json_str}

        Performance SLA for all the APIs - 5% error rate and 500 milliseconds response time. Transaction metrics under this range should be considered as well-performing.
        Your task:
        1. **Overall Summary**:
        - List only the pct2ResTime key's values from the json file that are above 500 ms. Use the exact values from the pct2ResTime key.
        - Provide a summary of the performance test results, specifically highlighting the overall 95th percentile response time, error rate, and adjusted throughput (Passed Requests Throughput - Failed Requests Throughput).
        - Highlight the metrics of APIs with high error rates and high response times.
        2. **Key Observations**:
        - Highlight critical issues observed during the test.
        - Identify areas that need improvement.
        - Point out well-performing areas.
        3. **Calculations**:
        - Calculate the pct2ResTime (95th percentile response time) for transactions that are critical and need improvement.
        - Calculate the error rate for transactions that are critical and need improvement.
        - Calculate the adjusted throughput for transactions that are critical and need improvement.

        Specify each transaction by its name.
        Structure the summary using headings and bullet points where appropriate to ensure clarity and readability.
        Also, don't specify how calculations are done, only give the results.
        """
    )

    llm_chain = LLMChain(prompt=prompt_template, llm=ollama)
    inputs = {"json_str": json_str}
    refined_summary = llm_chain.run(inputs)

    return refined_summary if isinstance(refined_summary, str) else str(refined_summary)
