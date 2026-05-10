from . import base_types
from ._Cheque4 import Cheque4

class PaymentInstrument19Choice(base_types._BaseFieldType):

	__slots__ = ["_BkrsDrftDtls", "_ChqDtls"]
	@property
	def BkrsDrftDtls(self):
		return self._BkrsDrftDtls

	@BkrsDrftDtls.setter
	def BkrsDrftDtls(self, value):
		self._BkrsDrftDtls = value if type(value) != base_types.auto else self.make_default("BkrsDrftDtls")

	@BkrsDrftDtls.deleter
	def BkrsDrftDtls(self):
		del self._BkrsDrftDtls
		self._BkrsDrftDtls = None

	@property
	def ChqDtls(self):
		return self._ChqDtls

	@ChqDtls.setter
	def ChqDtls(self, value):
		self._ChqDtls = value if type(value) != base_types.auto else self.make_default("ChqDtls")

	@ChqDtls.deleter
	def ChqDtls(self):
		del self._ChqDtls
		self._ChqDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BkrsDrftDtls', type=Cheque4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ChqDtls', type=Cheque4, min=0, max=1, mutex_group=1, array=False),
	))

