from fastapi import FastAPI, Form
import gradio as gr

api_attention_texts: str | None = None


def daam_api(_: gr.Blocks, app: FastAPI):
    @app.post("/daam/v1/set-attention-text")
    async def set_daam_attention_text(
            texts: str = Form(description="Attention Texts for visualization")
    ):
        global api_attention_texts
        api_attention_texts = None if len(texts) == 0 else texts

    @app.get("/daam/v1/get-attention-text")
    async def return_daam_attention_text():
        return {
            "texts": api_attention_texts
        }


try:
    from modules import script_callbacks

    script_callbacks.on_app_started(daam_api)
except:
    print("[stable-diffusion-webui-daam] API failed to initialize")
