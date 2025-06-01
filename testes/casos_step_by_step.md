# ✅ Casos de Teste - Passo a Passo

Este arquivo contém exemplos de testes funcionais manuais escritos no formato step-by-step.

---

## 🔹 Caso de Teste 1: Login com credenciais válidas

**ID:** CT001  
**Título:** Login com usuário e senha válidos  
**Pré-condição:** O usuário já possui uma conta válida no sistema  
**Ambiente:** Web – Google Chrome

### Passos:
1. Acessar o site: https://sistema.exemplo.com
2. Clicar em “Entrar”
3. Preencher o campo **E-mail** com `usuario@teste.com`
4. Preencher o campo **Senha** com `Senha123`
5. Clicar no botão **Login**

### Resultado Esperado:
- O usuário deve ser redirecionado para a página de dashboard
- A mensagem “Bem-vindo, usuário!” deve ser exibida

---

## 🔹 Caso de Teste 2: Cadastro com e-mail já existente

**ID:** CT002  
**Título:** Cadastro de novo usuário com e-mail já cadastrado  
**Pré-condição:** O e-mail `joao@teste.com` já está registrado no sistema  
**Ambiente:** Web – Firefox

### Passos:
1. Acessar a página de cadastro: https://sistema.exemplo.com/cadastro
2. Preencher o campo **Nome** com `João Silva`
3. Preencher o campo **E-mail** com `joao@teste.com`
4. Preencher o campo **Senha** com `Teste1234`
5. Confirmar senha com `Teste1234`
6. Clicar no botão **Cadastrar**

### Resultado Esperado:
- O sistema deve exibir a mensagem de erro: **"Este e-mail já está em uso."**
- O cadastro não deve ser concluído
