        with gr.Box(visible=is_spaces):
            if(is_spaces and is_shared_ui):
                gr.HTML('')
            elif(is_spaces):
                import torch
                if(not torch.cuda.is_available()):
                    gr.HTML('')
                else:
                    gr.HTML('')
