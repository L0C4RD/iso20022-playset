# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DirectDebitMandate7
from . import PaymentCard29
from . import YesNoIndicator

class PaymentInstrument24Choice(base_types._BaseFieldType):

	__slots__ = ["_BkrsDrft", "_Chq", "_DrctDbtDtls", "_PmtCardDtls"]
	@property
	def BkrsDrft(self):
		return self._BkrsDrft

	@BkrsDrft.setter
	def BkrsDrft(self, value):
		self._BkrsDrft = value if value is not None else base_types.UninitialisedField(self, 'BkrsDrft', YesNoIndicator, False)

	@BkrsDrft.deleter
	def BkrsDrft(self):
		del self._BkrsDrft
		self._BkrsDrft = base_types.UninitialisedField(self, 'BkrsDrft', YesNoIndicator, False)

	@property
	def Chq(self):
		return self._Chq

	@Chq.setter
	def Chq(self, value):
		self._Chq = value if value is not None else base_types.UninitialisedField(self, 'Chq', YesNoIndicator, False)

	@Chq.deleter
	def Chq(self):
		del self._Chq
		self._Chq = base_types.UninitialisedField(self, 'Chq', YesNoIndicator, False)

	@property
	def DrctDbtDtls(self):
		return self._DrctDbtDtls

	@DrctDbtDtls.setter
	def DrctDbtDtls(self, value):
		self._DrctDbtDtls = value if value is not None else base_types.UninitialisedField(self, 'DrctDbtDtls', DirectDebitMandate7, False)

	@DrctDbtDtls.deleter
	def DrctDbtDtls(self):
		del self._DrctDbtDtls
		self._DrctDbtDtls = base_types.UninitialisedField(self, 'DrctDbtDtls', DirectDebitMandate7, False)

	@property
	def PmtCardDtls(self):
		return self._PmtCardDtls

	@PmtCardDtls.setter
	def PmtCardDtls(self, value):
		self._PmtCardDtls = value if value is not None else base_types.UninitialisedField(self, 'PmtCardDtls', PaymentCard29, False)

	@PmtCardDtls.deleter
	def PmtCardDtls(self):
		del self._PmtCardDtls
		self._PmtCardDtls = base_types.UninitialisedField(self, 'PmtCardDtls', PaymentCard29, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BkrsDrft', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Chq', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DrctDbtDtls', type=DirectDebitMandate7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PmtCardDtls', type=PaymentCard29, min=0, max=1, mutex_group=1, array=False),
	))