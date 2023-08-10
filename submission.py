import pandas as pd
submission = pd.read_csv('/content/data/sample_submission.csv')

import json
with open('/content/result.jsonl', 'r') as file:
  answer = []
  for line in file:
    info = json.loads(line)
    answer.append(info['text'].strip())

submission['answer'] = pd.DataFrame(answer)
submission.to_csv('LLaVA_submission.csv', index=False)
