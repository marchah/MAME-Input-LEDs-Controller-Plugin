import { promises } from 'fs';

(async () => {
  const files = await promises.readdir('./mame/plugins/milcp/config');

  const mapping = {};

  files.forEach(file => {
    const json = require(`../mame/plugins/milcp/config/${file}`);

    const fileName = file.substr(0, file.length - '.json'.length);

    if (!json.roms || json.roms.length <= 0) {
      throw new Error(`Missing roms list for ${file}`);
    }

    json.roms.forEach(rom => {
      mapping[rom] = fileName;
    });
  });

  await promises.writeFile(
    './mame/plugins/milcp/mapping.json',
    JSON.stringify(mapping, null, 2)
  );

  process.exit(0);
})();
