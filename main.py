import flet as ft
import flet.fastapi as flet_fastapi


async def root_main(page: ft.Page):
    await page.add_async(ft.Text("This is root app!"))


async def sub_main(page: ft.Page):
    page.title = "Банк ПТБ (ООО)"
    page.bgcolor = ft.colors.WHITE
    page.scroll = "adaptive"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    async def crete_buttons():
        l = ft.TextField(label="Логин", bgcolor='white', color="black100")
        p = ft.TextField(label="Пароль", bgcolor='white', color="black100")
        return l, p

    l,p = await crete_buttons()


    async def crete_appbar():
        return ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("AppBar Example"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False
                    ),
                ]
            ),
        ],
    )

    a = await crete_appbar()

    await page.add_async(a, ft.Text("Это тестовая страничка"), l, p)

app = flet_fastapi.FastAPI()


app.mount("/sub-app", flet_fastapi.app(sub_main))
app.mount("/", flet_fastapi.app(root_main))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)