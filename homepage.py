import justpy as jp

class Home:
    path = "/"

    def serve(self):
        wp = jp.QuasarPage(Tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text='This is the Home page!', classes="text-4X1 m-2")
        jp.Div(a=div, text="""Hello""", classes='text-lg')

        return wp



