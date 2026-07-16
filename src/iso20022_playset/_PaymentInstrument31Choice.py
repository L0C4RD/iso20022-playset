# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Cheque12
from . import CreditTransfer13

class PaymentInstrument31Choice(base_types._BaseFieldType):

	__slots__ = ["_CdtTrfDtls", "_ChqDtls"]
	@property
	def CdtTrfDtls(self):
		return self._CdtTrfDtls

	@CdtTrfDtls.setter
	def CdtTrfDtls(self, value):
		self._CdtTrfDtls = value if value is not None else base_types.UninitialisedField(self, 'CdtTrfDtls', CreditTransfer13, False)

	@CdtTrfDtls.deleter
	def CdtTrfDtls(self):
		del self._CdtTrfDtls
		self._CdtTrfDtls = base_types.UninitialisedField(self, 'CdtTrfDtls', CreditTransfer13, False)

	@property
	def ChqDtls(self):
		return self._ChqDtls

	@ChqDtls.setter
	def ChqDtls(self, value):
		self._ChqDtls = value if value is not None else base_types.UninitialisedField(self, 'ChqDtls', Cheque12, False)

	@ChqDtls.deleter
	def ChqDtls(self):
		del self._ChqDtls
		self._ChqDtls = base_types.UninitialisedField(self, 'ChqDtls', Cheque12, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtTrfDtls', type=CreditTransfer13, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ChqDtls', type=Cheque12, min=0, max=1, mutex_group=1, array=False),
	))