import { readdirSync } from 'fs';

const PlayModes = [
  '1_player',
  '2_player_alternating',
  '2_player_simultaneous',
  '3_player_simultaneous',
  '4_player_simultaneous',
  '4_player_alternating_2_player_simultaneous',
  '8_player_alternating_2_player_simultaneous',
];
const Hardwares = ['arcade', 'cps1', 'cps2', 'cps3', 'neogeo'];
const Genres = [
  'maze',
  'shooter',
  'platform',
  'fighter',
  'sports',
  'puzzle',
  'driving',
];
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
const Joysticks = ['2_way', '4_way', '8_way'];

describe('mame/plugins/milcp/config*', () => {
  const gameNames = {};
  let roms = [];

  describe.each(readdirSync('./mame/plugins/milcp/config'))(
    'config %s',
    filename => {
      const json = require(`../../../../../mame/plugins/milcp/config/${filename}`);

      it('should test name', () => {
        // some game have diff roms for nb players
        //expect(gameNames[json.name]).not.toBeDefined();

        gameNames[json.name] = true;

        expect(json.name).toBeDefined();
        expect(json.name.length).toBeGreaterThan(0);
      });

      it('should test roms', () => {
        roms = [...roms, ...json.roms];
        expect(json.roms).toBeDefined();
        expect(json.roms.length).toBeGreaterThan(0);
      });

      it('should test that main rom is first (excuse my OCD)', () => {
        expect(json.roms[0]).toEqual(
          filename.substr(0, filename.length - '.json'.length)
        );
      });

      it('should test developer', () => {
        expect(json.developer).toBeDefined();
      });

      it('should test publisher', () => {
        expect(json.publisher).toBeDefined();
      });

      it('should test hardware', () => {
        expect(json.hardware).toBeDefined();

        expect(Hardwares).toContain(json.hardware);
      });

      it('should test playMode', () => {
        expect(json.playMode).toBeDefined();
        expect(PlayModes).toContain(json.playMode);
      });

      it('should test genre', () => {
        expect(json.genre).toBeDefined();
        expect(Genres).toContain(json.genre);
      });

      it('should test inputs', () => {
        expect(json.inputs).toBeDefined();
        expect(json.inputs).toEqual(expect.any(Object));

        Object.keys(json.inputs).forEach(key => {
          expect(MAMEInputs).toContain(json.inputs[key]);
          expect(PluginInputs).toContain(key);
        });
      });

      it('should test joystick', () => {
        expect(json.joystick).toBeDefined();
        expect(Joysticks).toContain(json.joystick);
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
