from . import base_types
from .TotalFilter1 import TotalFilter1
from .TotalDetails1Code import TotalDetails1Code

class ReportGetTotalsRequest1(base_types._BaseFieldType):

	__slots__ = ["_TtlDtls", "_TtlFltr"]
	@property
	def TtlDtls(self):
		return self._TtlDtls

	@TtlDtls.setter
	def TtlDtls(self, value):
		self._TtlDtls = value if type(value) != base_types.auto else self.make_default("TtlDtls")

	@TtlDtls.deleter
	def TtlDtls(self):
		del self._TtlDtls
		self._TtlDtls = None

	@property
	def TtlFltr(self):
		return self._TtlFltr

	@TtlFltr.setter
	def TtlFltr(self, value):
		self._TtlFltr = value if type(value) != base_types.auto else self.make_default("TtlFltr")

	@TtlFltr.deleter
	def TtlFltr(self):
		del self._TtlFltr
		self._TtlFltr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlDtls', type=TotalDetails1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlFltr', type=TotalFilter1, min=0, max=1, mutex_group=None, array=False),
	))

