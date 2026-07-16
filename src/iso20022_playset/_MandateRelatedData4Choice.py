# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditTransferMandateData1
from . import MandateRelatedInformation15

class MandateRelatedData4Choice(base_types._BaseFieldType):

	__slots__ = ["_CdtTrfMndt", "_DrctDbtMndt"]
	@property
	def CdtTrfMndt(self):
		return self._CdtTrfMndt

	@CdtTrfMndt.setter
	def CdtTrfMndt(self, value):
		self._CdtTrfMndt = value if value is not None else base_types.UninitialisedField(self, 'CdtTrfMndt', CreditTransferMandateData1, False)

	@CdtTrfMndt.deleter
	def CdtTrfMndt(self):
		del self._CdtTrfMndt
		self._CdtTrfMndt = base_types.UninitialisedField(self, 'CdtTrfMndt', CreditTransferMandateData1, False)

	@property
	def DrctDbtMndt(self):
		return self._DrctDbtMndt

	@DrctDbtMndt.setter
	def DrctDbtMndt(self, value):
		self._DrctDbtMndt = value if value is not None else base_types.UninitialisedField(self, 'DrctDbtMndt', MandateRelatedInformation15, False)

	@DrctDbtMndt.deleter
	def DrctDbtMndt(self):
		del self._DrctDbtMndt
		self._DrctDbtMndt = base_types.UninitialisedField(self, 'DrctDbtMndt', MandateRelatedInformation15, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtTrfMndt', type=CreditTransferMandateData1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DrctDbtMndt', type=MandateRelatedInformation15, min=0, max=1, mutex_group=1, array=False),
	))