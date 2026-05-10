import base_types
import ActiveCurrencyAndAmount
import InitialMarginExposure1

class InitialMarginRequirement1(base_types._BaseFieldType):

	__slots__ = ["_InitlMrgnXpsr", "_Cdt"]
	@property
	def InitlMrgnXpsr(self):
		return self._InitlMrgnXpsr

	@InitlMrgnXpsr.setter
	def InitlMrgnXpsr(self, value):
		self._InitlMrgnXpsr = value if type(value) != auto else self.make_default("InitlMrgnXpsr")

	@InitlMrgnXpsr.deleter
	def InitlMrgnXpsr(self):
		del self._InitlMrgnXpsr
		self._InitlMrgnXpsr = None

	@property
	def Cdt(self):
		return self._Cdt

	@Cdt.setter
	def Cdt(self, value):
		self._Cdt = value if type(value) != auto else self.make_default("Cdt")

	@Cdt.deleter
	def Cdt(self):
		del self._Cdt
		self._Cdt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InitlMrgnXpsr', type=InitialMarginExposure1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cdt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

