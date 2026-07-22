res.cookie('session', token, { httpOnly: true, secure: true, sameSite: 'strict' });
