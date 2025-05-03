# ✅ Checklist de Code Review para QA

## 🔍 1. Validação de Requisitos
- A implementação atende exatamente ao que está descrito na história de usuário ou requisito?
- Há algum comportamento ausente ou divergente?
- Há regras de negócio que foram ignoradas?

## 🧪 2. Testabilidade
- O código permite escrita de testes automatizados?
- A lógica foi separada da interface (ex: regras fora do controller ou UI)?
- Os dados externos (ex: APIs, banco) podem ser simulados (mocks/stubs)?

## 🧪 3. Testes Automatizados
- Existem testes cobrindo a funcionalidade alterada?
- Os testes cobrem casos positivos e negativos?
- O QA ou o time executou os testes localmente ou no pipeline?
- O nome dos testes é claro e descritivo?

## ⚠️ 4. Avaliação de Risco
- Essa alteração pode afetar outras partes do sistema (efeito colateral)?
- A alteração envolve partes críticas do sistema (ex: login, pagamento)?
- Houve testes de regressão suficientes?

## 📊 5. Dados e Validações
- Os dados de entrada estão sendo validados corretamente?
- Há proteção contra entradas inválidas ou maliciosas (ex: SQL Injection)?
- Há mensagens de erro claras e úteis para o usuário?

## 👁️‍🗨️ 6. Acessibilidade e UX (se aplicável)
- Mensagens de erro são compreensíveis?
- Há feedback visual adequado para o usuário após ações?
- O fluxo é consistente com o restante da aplicação?

## 🧾 7. Documentação e Comentários
- Há comentários úteis no código, se necessário?
- A documentação técnica (ex: README, swagger, comentários) foi atualizada?

---

## 📌 Dica final:
> Sempre leia o código com os olhos de quem quer garantir que ele funciona como esperado, pode ser testado e não vai causar dor de cabeça depois.
