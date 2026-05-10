from . import base_types
import GenericIdentification1
import ActiveCurrencyAndAmount

class OtherAmount3(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Amt"]
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

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=GenericIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

