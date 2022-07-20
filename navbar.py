import justpy as jp


class About:
    path = '/about'

    def serve(self):
        wp = jp.QuasarPage(Tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text='This is the About page!', classes="text-4X1 m-2")
        jp.Div(a=div, text="""Hello""", classes='text-lg')
        return wp


jp.Route(About.path, About.serve)
jp.justpy(port=8001)
