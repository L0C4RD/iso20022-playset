from . import base_types
from ._Max10NumericText import Max10NumericText
from ._ReportContent2Choice import ReportContent2Choice

class ReportContent2(base_types._BaseFieldType):

	__slots__ = ["_FrmtdCntt", "_RptLineSeq"]
	@property
	def FrmtdCntt(self):
		return self._FrmtdCntt

	@FrmtdCntt.setter
	def FrmtdCntt(self, value):
		self._FrmtdCntt = value if type(value) != base_types.auto else self.make_default("FrmtdCntt")

	@FrmtdCntt.deleter
	def FrmtdCntt(self):
		del self._FrmtdCntt
		self._FrmtdCntt = None

	@property
	def RptLineSeq(self):
		return self._RptLineSeq

	@RptLineSeq.setter
	def RptLineSeq(self, value):
		self._RptLineSeq = value if type(value) != base_types.auto else self.make_default("RptLineSeq")

	@RptLineSeq.deleter
	def RptLineSeq(self):
		del self._RptLineSeq
		self._RptLineSeq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrmtdCntt', type=ReportContent2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptLineSeq', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
	))

