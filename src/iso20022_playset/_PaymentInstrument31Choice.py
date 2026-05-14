from . import base_types
from ._Cheque12 import Cheque12
from ._CreditTransfer13 import CreditTransfer13

class PaymentInstrument31Choice(base_types._BaseFieldType):

	__slots__ = ["_CdtTrfDtls", "_ChqDtls"]
	@property
	def CdtTrfDtls(self):
		return self._CdtTrfDtls

	@CdtTrfDtls.setter
	def CdtTrfDtls(self, value):
		self._CdtTrfDtls = value if type(value) != base_types.auto else self.make_default("CdtTrfDtls")

	@CdtTrfDtls.deleter
	def CdtTrfDtls(self):
		del self._CdtTrfDtls
		self._CdtTrfDtls = None

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
		base_types.FieldEntry(name='CdtTrfDtls', type=CreditTransfer13, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ChqDtls', type=Cheque12, min=0, max=1, mutex_group=1, array=False),
	))

