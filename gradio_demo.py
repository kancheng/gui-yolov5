import torch
import gradio as gr

model = torch.hub.load("./", "custom", path="./weights/yolov5s.pt", source="local")

title = "Video Detection Yolov5 Model Test"
desc = "This is a Yolov5 demo project based on Gradio, very convenient!"
base_conf, base_iou = 0.25, 0.45
 
 
def det_image(img, conf_thres, iou_thres):
    model.conf = conf_thres
    model.iou = iou_thres
    return model(img).render()[0]


 
# The parameters in examples should correspond to those in inputs
# To get the camera photo detection, modify inputs: inputs=[gr.Webcam(),...], and dynamically update and add the attribute: live=True
# If you change launch() to launch(share=True), this code will be available on the public network.

gr.Interface(
    inputs=["image", gr.Slider(minimum=0, maximum=1, value=base_conf), gr.Slider(minimum=0, maximum=1, value=base_iou)],
    outputs=["image"],
    fn=det_image,
    title=title,
    description=desc,
    live=True,
    examples=[["./data/images/bus.jpg", base_conf, base_iou],
              ["./data/images/zidane.jpg", base_conf, base_iou]]
).launch(share=True)
