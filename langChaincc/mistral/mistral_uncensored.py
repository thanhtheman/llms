import requests, os
from dotenv import load_dotenv
load_dotenv()
API_URL = os.getenv('HUGGINGFACE_PAID_URL_MISTRAL7B')
headers = {
	"Authorization": f"Bearer {os.getenv('HUGGINGFACE_PAID_API_KEY')}",
	"Content-Type": "application/json"
}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "if we lay 5 shirts out in the sun and it takes 4 hours to dry, how long would 20 shirts take to dry? Explain your reasoning step by step",
})

print(output[0]['generated_text'])



# curl_command = """curl https://api.endpoints.huggingface.cloud/v2/endpoint/thanhquach \
# -X POST \
# -d '{"compute":{"accelerator":"gpu","instanceSize":"medium","instanceType":"g5.2xlarge","scaling":{"maxReplica":1,"minReplica":1}},"model":{"framework":"pytorch","image":{"custom":{"health_route":"/health","env":{"MAX_BATCH_PREFILL_TOKENS":"2048","MAX_INPUT_LENGTH":"1024","MAX_TOTAL_TOKENS":"1512","MODEL_ID":"/repository"},"url":"ghcr.io/huggingface/text-generation-inference:1.1.0"}},"repository":"ehartford/dolphin-2.0-mistral-7b","task":"text-generation"},"name":"aws-dolphin-2-0-mistral-7b-0108","provider":{"region":"us-east-1","vendor":"aws"},"type":"protected"}' \
# -H "Content-Type: application/json" \
# -H "Authorization: Bearer ZejkvHhTjnYHtrdhKsUbEAkrgkIQIvQbqklcpBMSHeiCszvSyxGFYKfGIjLYfqJmczKcYBaRYLWLtTSIHNAlslXJFCMeATlHddlXPgiGdtTeyJfrslyiTYCbNDsvndTK"
# print(output)"""