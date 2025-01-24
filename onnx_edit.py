import onnx

input_path = "mobile_sam_decoder.onnx"
output_path = "mobile_sam_decoder_sub.onnx"
input_names = [ "image_embeddings",
                "point_coords",
                "point_labels",
                "mask_input",
                "has_mask_input",]
output_names = ["iou_predictions","low_res_masks"]

onnx.utils.extract_model(input_path, output_path, input_names, output_names)
