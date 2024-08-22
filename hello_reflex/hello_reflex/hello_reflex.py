import reflex as rx 

def index():
    return rx.vstack(
        rx.hstack(
            rx.button(
                "Decrement",
                color_scheme="red",
                border_radius="1em"
            ),
            rx.heading(font_size="2em"),
            rx.button(
                "Increment",
                color_scheme="grass",
                border_radius="1em"
            ),
        )
    )
 

    
app = rx.App()
app.add_page(index)
app._compile()