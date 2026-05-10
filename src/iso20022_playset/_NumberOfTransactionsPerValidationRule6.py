from . import base_types
from ._Max15NumericText import Max15NumericText
from ._RejectionReason70 import RejectionReason70

class NumberOfTransactionsPerValidationRule6(base_types._BaseFieldType):

	__slots__ = ["_RptSts", "_DtldNb"]
	@property
	def RptSts(self):
		return self._RptSts

	@RptSts.setter
	def RptSts(self, value):
		self._RptSts = value if type(value) != base_types.auto else self.make_default("RptSts")

	@RptSts.deleter
	def RptSts(self):
		del self._RptSts
		self._RptSts = None

	@property
	def DtldNb(self):
		return self._DtldNb

	@DtldNb.setter
	def DtldNb(self, value):
		self._DtldNb = value if type(value) != base_types.auto else self.make_default("DtldNb")

	@DtldNb.deleter
	def DtldNb(self):
		del self._DtldNb
		self._DtldNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptSts', type=RejectionReason70, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtldNb', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
	))

