python scripts/export_onnx_model.py --checkpoint ./weights/mobile_sam.pt --model-type vit_t --output ./mobile_sam_decoder.onnx

python onnx_edit.py 

onnxsim mobile_sam_decoder_sub.onnx mobile_sam_decoder_sub_sim.onnx --input-shape point_coords:1,5,2 point_labels:1,5