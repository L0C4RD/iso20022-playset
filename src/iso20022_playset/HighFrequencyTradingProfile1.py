import base_types
import ConsolidationType1Choice
import ISODate
import SettlementFrequency1Choice

class HighFrequencyTradingProfile1(base_types._BaseFieldType):

	__slots__ = ["_CnsldtnTp", "_SttlmFrqcy", "_Dt"]
	@property
	def CnsldtnTp(self):
		return self._CnsldtnTp

	@CnsldtnTp.setter
	def CnsldtnTp(self, value):
		self._CnsldtnTp = value if type(value) != auto else self.make_default("CnsldtnTp")

	@CnsldtnTp.deleter
	def CnsldtnTp(self):
		del self._CnsldtnTp
		self._CnsldtnTp = None

	@property
	def SttlmFrqcy(self):
		return self._SttlmFrqcy

	@SttlmFrqcy.setter
	def SttlmFrqcy(self, value):
		self._SttlmFrqcy = value if type(value) != auto else self.make_default("SttlmFrqcy")

	@SttlmFrqcy.deleter
	def SttlmFrqcy(self):
		del self._SttlmFrqcy
		self._SttlmFrqcy = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnsldtnTp', type=ConsolidationType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmFrqcy', type=SettlementFrequency1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

