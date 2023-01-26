1. In **Vehicle.cs**, build an empty `Vehicle` class.

2. In **Vehicle.cs**, define:

- `string LicensePlate` property (getter only)
- `double Speed` property (getter and private setter)
- `int Wheels` property (getter only)
- `void Honk()` method
- `SpeedUp()` method
- `SlowDown()` method

3. In **Sedan.cs**, use colon syntax to announce that `Sedan` inherits the `Vehicle` class.
    
> HINT: Make sure that `Vehicle` is listed before `IAutomobile`. The inherited class comes before any interfaces.

4. `Sedan` now inherits the members you defined in `Vehicle`. Remove them from **Sedan.cs**. *You may still see errors and that’s okay! We’ll fix those in the next exercise.*