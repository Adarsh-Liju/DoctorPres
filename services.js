const db = require('./database');

async function getMultiple(page = 1){
  const rows = await db.query(
    `SELECT * FROM Medicine`
  );
  const data=rows[0]
  return data
}

module.exports = {
  getMultiple
}