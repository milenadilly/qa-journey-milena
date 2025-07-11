# Bug Report – Campo de Email Aceita Formato Inválido

**Título do Bug:** Campo de email aceita entrada sem "@" ou "." sem exibir erro

**Passos para reproduzir:**
1. Acesse https://www.magazineluiza.com.br/
2. Clique em "Entrar"
3. Digite "aaaaaa" no campo de email (sem @ e sem .)
4. Clique em "Continuar"

**Resultado Esperado:**
- O sistema deveria mostrar uma mensagem de erro como “Email inválido”

**Resultado Atual:**
- Nenhuma mensagem é exibida
- O botão "Continuar" permanece habilitado

**Ambiente de Teste:**
- Sistema: macOS Sonoma 14.5
- Navegador: Google Chrome 117.0

**Severidade:** Média  
**Prioridade:** Alta

**Notas adicionais:**
- Esse erro pode permitir que o usuário tente continuar o cadastro sem email válido, o que pode causar confusão e falha no processo.
