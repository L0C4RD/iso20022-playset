from . import base_types
from .Max15NumericText import Max15NumericText
from .RejectionReason45 import RejectionReason45

class NumberOfTransactionsPerValidationRule5(base_types._BaseFieldType):

	__slots__ = ["_DtldNb", "_RptSts"]
	@property
	def DtldNb(self):
		return self._DtldNb

	@DtldNb.setter
	def DtldNb(self, value):
		self._DtldNb = value if type(value) != auto else self.make_default("DtldNb")

	@DtldNb.deleter
	def DtldNb(self):
		del self._DtldNb
		self._DtldNb = None

	@property
	def RptSts(self):
		return self._RptSts

	@RptSts.setter
	def RptSts(self, value):
		self._RptSts = value if type(value) != auto else self.make_default("RptSts")

	@RptSts.deleter
	def RptSts(self):
		del self._RptSts
		self._RptSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtldNb', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSts', type=RejectionReason45, min=1, max=None, mutex_group=None, array=True),
	))

