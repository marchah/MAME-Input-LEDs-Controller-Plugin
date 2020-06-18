import { readdirSync } from 'fs';

const PlayModes = ['2_player_alternating'];
const Hardwares = ['arcade'];
const Genres = ['maze'];
const MAMEInputs = [
  'BUTTON0',
  'BUTTON1',
  'BUTTON2',
  'BUTTON3',
  'BUTTON4',
  'BUTTON5',
  'BUTTON6',
  'BUTTON7',
];
const PluginInputs = ['B_0', 'B_1', 'B_2', 'B_3', 'B_4', 'B_5', 'B_6', 'B_7'];
const Joysticks = ['4_way'];

describe('mame/plugins/milcp/config*', () => {
  const gameNames = {};
  let roms = [];

  describe.each(readdirSync('./mame/plugins/milcp/config'))(
    'config %s',
    filename => {
      const json = require(`../../../../../mame/plugins/milcp/config/${filename}`);

      it('should test name', () => {
        expect(gameNames[json.name]).not.toBeDefined();

        gameNames[json.name] = true;

        expect(json.name).toBeDefined();
        expect(json.name.length).toBeGreaterThan(0);
      });

      it('should test roms', () => {
        roms = [...roms, ...json.roms];
        expect(json.roms).toBeDefined();
        expect(json.roms.length).toBeGreaterThan(0);
      });

      it('should test hardware', () => {
        expect(json.hardware).toBeDefined();
        expect(Hardwares.includes(json.hardware)).toBe(true);
      });

      it('should test playMode', () => {
        expect(json.playMode).toBeDefined();
        expect(PlayModes.includes(json.playMode)).toBe(true);
      });

      it('should test genre', () => {
        expect(json.genre).toBeDefined();
        expect(Genres.includes(json.genre)).toBe(true);
      });

      it('should test inputs', () => {
        expect(json.inputs).toBeDefined();
        expect(json.inputs).toEqual(expect.any(Object));
        expect(json.inputs).not.toEqual({});

        Object.keys(json.inputs).forEach(key => {
          expect(MAMEInputs.includes(json.inputs[key])).toBe(true);
          expect(PluginInputs.includes(key)).toBe(true);
        });
      });

      it('should test joystick', () => {
        expect(json.joystick).toBeDefined();
        expect(Joysticks.includes(json.joystick)).toBe(true);
      });
    }
  );

  it('should not have duplicates roms', () => {
    const findDuplicates = arr =>
      arr.filter((item, index) => arr.indexOf(item) !== index);

    const duplicates = findDuplicates(roms);

    expect(duplicates).toEqual([]);
  });
});
