export function logSecurity(event, user) {
  logger.info({ event, userId: user.id, ts: Date.now() });
}
