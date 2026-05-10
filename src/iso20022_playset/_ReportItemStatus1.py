from . import base_types
from ._ReportItemRejectionReason1Choice import ReportItemRejectionReason1Choice
from ._ReportItem1 import ReportItem1
from ._Max210Text import Max210Text

class ReportItemStatus1(base_types._BaseFieldType):

	__slots__ = ["_AddtlRsnInf", "_Xcptn", "_RptItm"]
	@property
	def AddtlRsnInf(self):
		return self._AddtlRsnInf

	@AddtlRsnInf.setter
	def AddtlRsnInf(self, value):
		self._AddtlRsnInf = value if type(value) != base_types.auto else self.make_default("AddtlRsnInf")

	@AddtlRsnInf.deleter
	def AddtlRsnInf(self):
		del self._AddtlRsnInf
		self._AddtlRsnInf = None

	@property
	def Xcptn(self):
		return self._Xcptn

	@Xcptn.setter
	def Xcptn(self, value):
		self._Xcptn = value if type(value) != base_types.auto else self.make_default("Xcptn")

	@Xcptn.deleter
	def Xcptn(self):
		del self._Xcptn
		self._Xcptn = None

	@property
	def RptItm(self):
		return self._RptItm

	@RptItm.setter
	def RptItm(self, value):
		self._RptItm = value if type(value) != base_types.auto else self.make_default("RptItm")

	@RptItm.deleter
	def RptItm(self):
		del self._RptItm
		self._RptItm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRsnInf', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xcptn', type=ReportItemRejectionReason1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptItm', type=ReportItem1, min=0, max=None, mutex_group=None, array=True),
	))

