---
description: Retrieve an existing GPT Image task without generating again
---

Use `gpt_image_get_task` with the existing task ID in $ARGUMENTS. Pass the original task_id as id to gpt_image_get_task. A finished_at timestamp is terminal, but still inspect the response for success or failure before showing final image URLs. Filter the image-model list to gpt-image models; do not substitute DALL-E or Nano Banana without the user asking. Never create a new task to retrieve this result.
