import base_types
import ReinvestmentType1Code
import ActiveOrHistoricCurrencyCode

class ReinvestedCashTypeAndAmount2(base_types._BaseFieldType):

	__slots__ = ["_RinvstdCshCcy", "_Tp"]
	@property
	def RinvstdCshCcy(self):
		return self._RinvstdCshCcy

	@RinvstdCshCcy.setter
	def RinvstdCshCcy(self, value):
		self._RinvstdCshCcy = value if type(value) != auto else self.make_default("RinvstdCshCcy")

	@RinvstdCshCcy.deleter
	def RinvstdCshCcy(self):
		del self._RinvstdCshCcy
		self._RinvstdCshCcy = None

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
		base_types.FieldEntry(name='RinvstdCshCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ReinvestmentType1Code, min=1, max=1, mutex_group=None, array=False),
	))

