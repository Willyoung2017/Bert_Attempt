export SQUAD_DIR=~/data/squad
export OUTPUT_DIR=./bert_large
export BERT_MODEL_DIR=./bert-base-uncased
export SQUAD_TAG_DIR=!/data/squad/srl_tags
export PYTHONPATH=./
source activate pytorch
CUDA_VISIBLE_DEVICES=1,2,3,6 python examples/run_squad.py \
  --bert_model bert-large-uncased \
  --do_train \
  --do_predict \
  --train_file $SQUAD_DIR/train-v1.1.json \
  --predict_file $SQUAD_DIR/dev-v1.1.json \
  --learning_rate 3e-5 \
  --num_train_epochs 2 \
  --max_seq_length 384 \
  --doc_stride 128 \
  --output_dir $OUTPUT_DIR \
  --train_batch_size 24 \
  --gradient_accumulation_steps 2 \
  --optimize_on_cpu \
  --fp16 \
  --loss_scale 128 \
  --train_context_tag_file $SQUAD_TAG_DIR/srl_squad_train
  --train_question_tag_file $SQUAD_TAG_DIR/srl_squad_question_train
  --predict_context_tag_file $SQUAD_TAG_DIR/srl_squad_dev
  --predict_question_tag_file $SQUAD_TAG_DIR/srl_squad_question_dev