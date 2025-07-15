from kivy.app import App
import asynckivy as ak


async def metronome(duration=1, step=0.1):
    async with ak.move_on_after(duration):
        with ak.sleep_freq(step=step) as sleep:
            et = 0.
            while True:
                et += await sleep()
                yield et


class SampleApp(App):
    def on_start(self):
        ak.managed_start(self.main())

    async def main(self):
        await ak.n_frames(10)
        async for et in metronome():
            print(et)
            if et > 0.5:
                await ak.sleep_forever()



if __name__ == "__main__":
    SampleApp().run()
