import justpy as jp
import definition


class Dictionary:
    path = '/dictionary'

    @classmethod  # now can be called using CLASSNAME.METHOD(), instead of having to initialize a class instance. Class methods can access class attributes but not instance attributes.
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        # Main background
        div = jp.Div(a=wp, classes="white-200 h-screen")

        # Container for main title
        jp.Div(a=div, text="Instant English Dictionary", classes="text-4xl m-2")

        # Container for subtitle
        jp.Div(a=div, text="Get the definition of any English work instantly as you type.", classes='text-lg')

        # Container for input box
        input_div = jp.Div(a=div, classes="grid grid-cols-2")

        # Container for output box
        output_div = jp.Div(a=div, classes='m-2 p-2 text-lg border-2 h-40')

        # Input box logic + styling
        input_box = jp.Input(a=input_div, placeholder="Type in a word here: ", outputdiv = output_div,
                             classes="m-2 bg-gray-100 border-2 border-gray-200 "
                                     "rounded w-64 focus:bg-white focus:outline-none "
                                     "focus:border-purple-500 py-2 px-4 ")

        # checks to see what is being inputted and auto calls the get definition function below
        input_box.on('input', cls.get_definition)

        return wp

    # Static method event handler that pulls definition.
    @staticmethod
    def get_definition(widget, msg):
        defined = definition.Definition(widget.value).get()
        widget.outputdiv.text = " ".join(defined)
