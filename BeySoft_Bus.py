class BeySoft_Bus:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required":{},
            "optional": {
                "bus": ("BUS", ),
                "model": ("MODEL", ),
                "clip": ("CLIP", ),
                "vae": ("VAE", ),
                "positive": ("CONDITIONING", ),
                "negative": ("CONDITIONING", ),
                "latent": ("LATENT", ),
                "image": ("IMAGE", ),
            }
        }    
    
    RETURN_TYPES = ("BUS", "MODEL", "CLIP", "VAE", "CONDITIONING", "CONDITIONING", "LATENT", "IMAGE", )
    RETURN_NAMES = ("bus", "model", "clip", "vae", "positive",     "negative",     "latent", "image", )

    FUNCTION = "beysoft_bus_fn"

    #OUTPUT_NODE = False

    CATEGORY = "BeySoft"

    def beysoft_bus_fn(self, bus=(None,None,None,None,None,None,None), model=None, clip=None, vae=None, positive=None, negative=None, latent=None, image=None):
        # Unpack the 5 constituents of the bus from the bus tuple.
        (bus_model, bus_clip, bus_vae, bus_positive, bus_negative, bus_latent, bus_image) = bus

        # If you pass in specific inputs, they override what comes from the bus.
        out_model       = model     or bus_model
        out_clip        = clip      or bus_clip
        out_vae         = vae       or bus_vae
        out_positive    = positive  or bus_positive
        out_negative    = negative  or bus_negative
        out_latent      = latent    or bus_latent
        out_image       = image     or bus_image

        # Squash all 5 inputs into the output bus tuple.
        out_bus = (out_model, out_clip, out_vae, out_positive, out_negative, out_latent, out_image)

        if not out_model:
            raise ValueError('Either model or bus containing a model should be supplied')
        if not out_clip:
            raise ValueError('Either clip or bus containing a clip should be supplied')
        if not out_vae:
            raise ValueError('Either vae or bus containing a vae should be supplied')
        # We don't insist that a bus contains conditioning.

        return (out_bus, out_model, out_clip, out_vae, out_positive, out_negative, out_latent, out_image)

    """
        The node will always be re executed if any of the inputs change but
        this method can be used to force the node to execute again even when the inputs don't change.
        You can make this node return a number or a string. This value will be compared to the one returned the last time the node was
        executed, if it is different the node will be executed again.
        This method is used in the core repo for the LoadImage node where they return the image hash as a string, if the image hash
        changes between executions the LoadImage node is executed again.
    """
    #@classmethod
    #def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""

# Set the web directory, any .js file in that directory will be loaded by the frontend as a frontend extension
# WEB_DIRECTORY = "./somejs"

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "BeySoft": BeySoft_Bus
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "BeySoft": "Bey's Bus Node"
}
