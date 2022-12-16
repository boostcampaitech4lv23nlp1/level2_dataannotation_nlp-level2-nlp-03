import pickle as pickle
import json
import pandas as pd
import argparse
import numpy as np
from utils import *
from metrics import *

def make_probs(probs):
  prob_temp = []
  probs = probs.apply(lambda x: x[1:-1].split(','))
  for i in probs:
    prob_temp.append(list(map(float, i)))
  return prob_temp

def evaluation(gt_path, pred_path):

  pred = pd.read_csv(pred_path) # model이 예측한 정답 csv [id,pred_label, probs]
  answer = pd.read_csv(gt_path)['label'] # test dataset의 정답 csv [id, label]

  micro_f1 = klue_re_micro_f1(label_to_num(pred["pred_label"]), label_to_num(answer), average='micro') 
  auprc = klue_re_auprc(np.array(make_probs(pred['probs'])), np.array(label_to_num(answer)))

  results = {}
  results['micro_f1'] = {
        'value': f'{micro_f1:.04f}',
        'rank': True,
        'decs': True,
    }
  results['auprc'] = {
      'value': f'{auprc:.04f}',
      'rank': False,
      'decs': True,
  }

  return json.dumps(results)

def main(args):
  print(evaluation(args.answer, args.pred))

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  # data dir
  parser.add_argument('--pred', type=str, default="./prediction/submission.csv")
  parser.add_argument('--answer', type=str, default="../dataset/test/test.csv")
  args = parser.parse_args()
  main(args)