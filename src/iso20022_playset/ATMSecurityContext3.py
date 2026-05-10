from . import base_types
import ATMEquipment3
import ATMSecurityConfiguration1
import ATMSecurityScheme3Code

class ATMSecurityContext3(base_types._BaseFieldType):

	__slots__ = ["_CurCfgtn", "_DvcPrprty", "_CurSctySchme"]
	@property
	def CurCfgtn(self):
		return self._CurCfgtn

	@CurCfgtn.setter
	def CurCfgtn(self, value):
		self._CurCfgtn = value if type(value) != auto else self.make_default("CurCfgtn")

	@CurCfgtn.deleter
	def CurCfgtn(self):
		del self._CurCfgtn
		self._CurCfgtn = None

	@property
	def DvcPrprty(self):
		return self._DvcPrprty

	@DvcPrprty.setter
	def DvcPrprty(self, value):
		self._DvcPrprty = value if type(value) != auto else self.make_default("DvcPrprty")

	@DvcPrprty.deleter
	def DvcPrprty(self):
		del self._DvcPrprty
		self._DvcPrprty = None

	@property
	def CurSctySchme(self):
		return self._CurSctySchme

	@CurSctySchme.setter
	def CurSctySchme(self, value):
		self._CurSctySchme = value if type(value) != auto else self.make_default("CurSctySchme")

	@CurSctySchme.deleter
	def CurSctySchme(self):
		del self._CurSctySchme
		self._CurSctySchme = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurCfgtn', type=ATMSecurityConfiguration1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvcPrprty', type=ATMEquipment3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurSctySchme', type=ATMSecurityScheme3Code, min=1, max=1, mutex_group=None, array=False),
	))

