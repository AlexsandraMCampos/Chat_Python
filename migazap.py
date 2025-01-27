import flet as ft

def main(pagina):
    # Set page background color
    pagina.bgcolor = ft.colors.GREY_100
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Styled title
    titulo = ft.Text(
        "MigaZap 💬",
        size=32,
        color=ft.colors.BLUE_600,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    def enviar_mensagem_tunel(mensagem):
        texto = ft.Container(
            content=ft.Text(
                mensagem,
                size=16,
                color=ft.colors.BLUE_900,
                weight=ft.FontWeight.W_500,
                text_align=ft.TextAlign.CENTER
            ),
            alignment=ft.alignment.center,
            width=500
        )
        chat.controls.append(texto)
        chat.scroll_to(offset=-1)  # Auto-scroll to latest message
        pagina.update()
             
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        if campo_enviar_mensagem.value:
            nome_usuario = caixa_nome.value
            texto_campo_mensagem = campo_enviar_mensagem.value
            mensagem = f"{nome_usuario} ➜ {texto_campo_mensagem}"
            pagina.pubsub.send_all(mensagem)
            campo_enviar_mensagem.value = ""
            pagina.update()

    # Styled message input field
    campo_enviar_mensagem = ft.TextField(
        label="Digite aqui sua mensagem",
        border_color=ft.colors.BLUE_400,
        width=400,
        text_size=16,
        text_align=ft.TextAlign.CENTER,
        on_submit=enviar_mensagem
    )

    # Styled send button
    botao_enviar = ft.ElevatedButton(
        "Enviar 📤",
        on_click=enviar_mensagem,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE_600,
        )
    )

    # Container for input field and button
    linha_enviar = ft.Container(
        content=ft.Row(
            [campo_enviar_mensagem, botao_enviar],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        padding=20
    )

    # Styled chat container with centered content
    chat = ft.Column(
        spacing=10,
        scroll=ft.ScrollMode.ALWAYS,
        height=500,
        width=500,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    
    # Phone-styled container
    phone_container = ft.Container(
        content=ft.Column([
            # Phone top bar with camera notch
            ft.Container(
                content=ft.Row(
                    [
                        ft.Container(
                            content=ft.Text("⚫", size=12),
                            padding=5
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                bgcolor=ft.colors.BLACK,
                border_radius=ft.border_radius.only(top_left=20, top_right=20),
                height=30
            ),
            # Main content area
            ft.Container(
                content=ft.Column([chat_header := ft.Container(
                    content=ft.Text(
                        "MigaZap Chat 💬",
                        size=20,
                        color=ft.colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    ),
                    bgcolor=ft.colors.BLUE_600,
                    padding=10
                ), chat, linha_enviar]),
                bgcolor=ft.colors.WHITE
            ),
            # Phone bottom bar
            ft.Container(
                content=ft.Row(
                    [ft.Container(
                        content=ft.Text("⎯", size=20, color=ft.colors.WHITE),
                        padding=5
                    )],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                bgcolor=ft.colors.BLACK,
                border_radius=ft.border_radius.only(bottom_left=20, bottom_right=20),
                height=30
            )
        ]),
        width=550,
        bgcolor=ft.colors.BLACK,
        border_radius=20,
        padding=2  # This creates the phone border effect
    )

    def entrar_chat(evento):
        if caixa_nome.value:
            popup.open = False
            pagina.remove(titulo)
            pagina.remove(botao_inicial_container)
            pagina.add(phone_container)
            
            nome_usuario = caixa_nome.value
            mensagem = f"👋 {nome_usuario} entrou no chat!"
            pagina.pubsub.send_all(mensagem)
            pagina.update()

    # Styled popup elements
    titulo_popup = ft.Text(
        "Bem vindo ao MigaZap ✨",
        size=24,
        color=ft.colors.BLUE_600,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    caixa_nome = ft.TextField(
        label="Digite seu nome",
        border_color=ft.colors.BLUE_400,
        width=300,
        text_align=ft.TextAlign.CENTER
    )
    
    botao_popup = ft.ElevatedButton(
        "Entrar no Chat 🚀",
        on_click=entrar_chat,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE_600,
        )
    )

    # Styled popup
    popup = ft.AlertDialog(
        title=titulo_popup,
        content=caixa_nome,
        actions=[botao_popup],
        actions_alignment=ft.MainAxisAlignment.CENTER
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    # Styled initial button
    botao = ft.ElevatedButton(
        "Iniciar Chat 💭",
        on_click=abrir_popup,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE_600,
        )
    )

    # Container for initial button to center it
    botao_inicial_container = ft.Container(
        content=botao,
        alignment=ft.alignment.center,
        padding=20
    )

    # Add elements to page
    pagina.add(titulo)
    pagina.add(botao_inicial_container)

ft.app(main, view=ft.WEB_BROWSER)