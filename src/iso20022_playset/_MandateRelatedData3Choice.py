from . import base_types
from .CreditTransferMandateData1 import CreditTransferMandateData1
from .MandateRelatedInformation16 import MandateRelatedInformation16

class MandateRelatedData3Choice(base_types._BaseFieldType):

	__slots__ = ["_CdtTrfMndt", "_DrctDbtMndt"]
	@property
	def CdtTrfMndt(self):
		return self._CdtTrfMndt

	@CdtTrfMndt.setter
	def CdtTrfMndt(self, value):
		self._CdtTrfMndt = value if type(value) != base_types.auto else self.make_default("CdtTrfMndt")

	@CdtTrfMndt.deleter
	def CdtTrfMndt(self):
		del self._CdtTrfMndt
		self._CdtTrfMndt = None

	@property
	def DrctDbtMndt(self):
		return self._DrctDbtMndt

	@DrctDbtMndt.setter
	def DrctDbtMndt(self, value):
		self._DrctDbtMndt = value if type(value) != base_types.auto else self.make_default("DrctDbtMndt")

	@DrctDbtMndt.deleter
	def DrctDbtMndt(self):
		del self._DrctDbtMndt
		self._DrctDbtMndt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtTrfMndt', type=CreditTransferMandateData1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DrctDbtMndt', type=MandateRelatedInformation16, min=0, max=1, mutex_group=1, array=False),
	))

