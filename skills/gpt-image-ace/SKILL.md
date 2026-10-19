---
name: gpt-image-ace
description: Generate or edit GPT Image image through Ace Data Cloud and retrieve the same task’s final result in Kimi Code. Use for explicit GPT Image requests, not other media providers.
---

# GPT Image by Ace Data Cloud

This plugin exposes only the GPT Image workflow through the existing dedicated GPT Image stdio profile. It does not change the conversation’s LLM provider.

Start by checking the connected tool schema. For a local metadata-only setup check call `gpt_image_list_models` only, and report available GPT Image options. Never read, echo, or ask the user to paste an API Token into the conversation; it belongs in `ACEDATACLOUD_API_TOKEN` before Kimi starts.

For a new request, confirm the requested model/action, required inputs and current price are understood. Submit `gpt_image_generate` once only when the user has authorized the operation and its cost. Do not enable automatic generation retries or substitute a different model family.

Save the exact returned task_id. Use `gpt_image_get_task` to query that same task, observing server polling guidance. When it is still pending, explain that status and stop after a bounded check; let the user resume with the same ID. Never submit another generation to poll. Pass the original task_id as id to gpt_image_get_task. A finished_at timestamp is terminal, but still inspect the response for success or failure before showing final image URLs. Filter the image-model list to gpt-image models; do not substitute DALL-E or Nano Banana without the user asking.

If the user supplies an existing task ID, query it directly without generating. If a request returns 401/403, explain key/scope or moderation errors without requesting secrets; for 429 wait and reduce concurrency; for 5xx/timeout inspect the existing task before any separately approved resubmission.

Setup and current service information: https://platform.acedata.cloud/documents/openai-images-generations?utm_source=agent_skill&utm_medium=referral&utm_campaign=evergreen&utm_content=gpt_image_kimi_readme_docs
