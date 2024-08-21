class Door:
  def __init__(self, ref2door_lock, base_color):
    self._the_door_lock = ref2door_lock
    self.color = base_color
    self._door_is_open = False
    self._door_is_locked = False
  def open_the_door(self):
    if self._door_is_locked == False:
        self._door_is_open = True
  def close_the_door(self):
    self._door_is_open = False
  def lock_the_door(self):
    if self._door_is_open == False:
        self._door_is_locked = self._the_door_lock.lock()
  def unlock_the_door(self):

    if self._door_is_locked:
        self._door_is_locked = self._the_door_lock.unlock()
  def test(self):
    print(f'Türfarbe {self.color}'
            f'Türe offen: {self._door_is_open}'
            f'Türe verriegelt: {self._door_is_locked}')
    @property
  def door_is_open(self):
    return self._door_is_open
    @property
  def door_ist_locked(self):
    return self._door_is_locked
    @property
  def color(self):
    return self._color
    @color.setter
  def color(self, new_color):
    self._color = new_color
"""
nur für die korrekte Übersetzung und Ausführung 
"""
class DoorLock:
  def __init__(self):
    print("ein Schloss erzeugt")
  def lock(self):
    return True
  def unlock(self):
    return False
if __name__ == "__main__":
    print("Test für Tür-Objekt")
    the_door_lock = DoorLock()
    the_door = Door(the_door_lock, "grün")
    the_door.test()
    print("-- Türe jetzt öffnen")
    the_door.open_the_door()
    the_door.test()
