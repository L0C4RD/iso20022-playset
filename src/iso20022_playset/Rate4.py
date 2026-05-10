import base_types
import ActiveOrHistoricCurrencyAndAmountRange2
import RateType4Choice

class Rate4(base_types._BaseFieldType):

	__slots__ = ["_VldtyRg", "_Tp"]
	@property
	def VldtyRg(self):
		return self._VldtyRg

	@VldtyRg.setter
	def VldtyRg(self, value):
		self._VldtyRg = value if type(value) != auto else self.make_default("VldtyRg")

	@VldtyRg.deleter
	def VldtyRg(self):
		del self._VldtyRg
		self._VldtyRg = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='VldtyRg', type=ActiveOrHistoricCurrencyAndAmountRange2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=RateType4Choice, min=1, max=1, mutex_group=None, array=False),
	))

