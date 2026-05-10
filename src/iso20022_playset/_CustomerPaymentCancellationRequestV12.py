from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._Case6 import Case6
from ._CaseAssignment6 import CaseAssignment6
from ._ControlData1 import ControlData1
from ._UnderlyingTransaction33 import UnderlyingTransaction33

class CustomerPaymentCancellationRequestV12(base_types._BaseFieldType):

	__slots__ = ["_Assgnmt", "_CtrlData", "_Case", "_Undrlyg", "_SplmtryData"]
	@property
	def Assgnmt(self):
		return self._Assgnmt

	@Assgnmt.setter
	def Assgnmt(self, value):
		self._Assgnmt = value if type(value) != base_types.auto else self.make_default("Assgnmt")

	@Assgnmt.deleter
	def Assgnmt(self):
		del self._Assgnmt
		self._Assgnmt = None

	@property
	def CtrlData(self):
		return self._CtrlData

	@CtrlData.setter
	def CtrlData(self, value):
		self._CtrlData = value if type(value) != base_types.auto else self.make_default("CtrlData")

	@CtrlData.deleter
	def CtrlData(self):
		del self._CtrlData
		self._CtrlData = None

	@property
	def Case(self):
		return self._Case

	@Case.setter
	def Case(self, value):
		self._Case = value if type(value) != base_types.auto else self.make_default("Case")

	@Case.deleter
	def Case(self):
		del self._Case
		self._Case = None

	@property
	def Undrlyg(self):
		return self._Undrlyg

	@Undrlyg.setter
	def Undrlyg(self, value):
		self._Undrlyg = value if type(value) != base_types.auto else self.make_default("Undrlyg")

	@Undrlyg.deleter
	def Undrlyg(self):
		del self._Undrlyg
		self._Undrlyg = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assgnmt', type=CaseAssignment6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrlData', type=ControlData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Case', type=Case6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Undrlyg', type=UnderlyingTransaction33, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

