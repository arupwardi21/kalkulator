from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp

class TrackerApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(5))
        root.add_widget(Label(text='55five Tracker', bold=True, size_hint_y=None, height=dp(45), font_size='22sp'))
        root.add_widget(Label(text='0839 : K/3 KECIL (0-4)', color=(0,1,0,1), bold=True, size_hint_y=None, height=dp(35)))
        data = [('0838','7','B/7 BESAR'),('0837','4','K/4 KECIL'),('0836','9','B/9 BESAR'),('0835','1','K/1 KECIL'),('0834','8','B/8 BESAR'),('0833','7','B/7 BESAR'),('0832','0','K/0 KECIL'),('0831','3','K/3 KECIL'),('0830','5','B/5 BESAR'),('0829','0','K/0 KECIL')]
        scroll = ScrollView()
        grid = GridLayout(cols=1, size_hint_y=None, spacing=dp(2))
        grid.bind(minimum_height=grid.setter('height'))
        for per, angka, ket in data:
            c = (1,0.6,0,1) if 'BESAR' in ket else (0,1,0,1)
            grid.add_widget(Label(text=f"{per} : {angka} - {ket}", color=c, size_hint_y=None, height=dp(32)))
        scroll.add_widget(grid)
        root.add_widget(scroll)
        return root
TrackerApp().run()
