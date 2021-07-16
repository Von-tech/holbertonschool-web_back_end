export default function guardrail(mathFunction) {
  try {
    return [mathFunction(), 'Guardrail was processed'];
  } catch (throwedError) {
    return [`${throwedError.message}: ${throwedError.message}`, 'Guardrail was processed'];
  }
}
