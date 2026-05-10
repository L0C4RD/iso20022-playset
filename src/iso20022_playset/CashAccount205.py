import base_types
import CashAccount206
import ActiveCurrencyCode

class CashAccount205(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_ScndryAcct", "_PmryAcct"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def ScndryAcct(self):
		return self._ScndryAcct

	@ScndryAcct.setter
	def ScndryAcct(self, value):
		self._ScndryAcct = value if type(value) != auto else self.make_default("ScndryAcct")

	@ScndryAcct.deleter
	def ScndryAcct(self):
		del self._ScndryAcct
		self._ScndryAcct = None

	@property
	def PmryAcct(self):
		return self._PmryAcct

	@PmryAcct.setter
	def PmryAcct(self, value):
		self._PmryAcct = value if type(value) != auto else self.make_default("PmryAcct")

	@PmryAcct.deleter
	def PmryAcct(self):
		del self._PmryAcct
		self._PmryAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndryAcct', type=CashAccount206, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmryAcct', type=CashAccount206, min=0, max=1, mutex_group=None, array=False),
	))

