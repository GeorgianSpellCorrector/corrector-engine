python train_bart.py \
    --output_dir="./output_dir" \
#     --config_name="facebook/bart-base" \
#     --tokenizer_name="ZurabDz/ByteLevelBPETokenizer_BART" \
    --model_name_or_path="ZurabDz/BartGeo" \
    --dataset_name="ZurabDz/bart_tokenized_data_bpe_byte_level" \
    --dataset_config_name="unshuffled_deduplicated_no" \
    --max_seq_length="64" \
    --per_device_train_batch_size="4" \
    --per_device_eval_batch_size="4" \
    --learning_rate="1e-4" \
    --warmup_steps="2000" \
    --overwrite_output_dir \
    --logging_steps="500" \
    --save_steps="6000" \
    --eval_steps="6000" \
    --push_to_hub=True \
    --hub_model_id="ZurabDz/BartGeo" \
    --hub_token="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"