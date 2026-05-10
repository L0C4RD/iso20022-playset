from . import base_types
from ._IdentificationAssignment4 import IdentificationAssignment4
from ._MessageIdentification8 import MessageIdentification8
from ._SupplementaryData1 import SupplementaryData1
from ._VerificationReport5 import VerificationReport5

class IdentificationVerificationReportV04(base_types._BaseFieldType):

	__slots__ = ["_Assgnmt", "_OrgnlAssgnmt", "_Rpt", "_SplmtryData"]
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
	def OrgnlAssgnmt(self):
		return self._OrgnlAssgnmt

	@OrgnlAssgnmt.setter
	def OrgnlAssgnmt(self, value):
		self._OrgnlAssgnmt = value if type(value) != base_types.auto else self.make_default("OrgnlAssgnmt")

	@OrgnlAssgnmt.deleter
	def OrgnlAssgnmt(self):
		del self._OrgnlAssgnmt
		self._OrgnlAssgnmt = None

	@property
	def Rpt(self):
		return self._Rpt

	@Rpt.setter
	def Rpt(self, value):
		self._Rpt = value if type(value) != base_types.auto else self.make_default("Rpt")

	@Rpt.deleter
	def Rpt(self):
		del self._Rpt
		self._Rpt = None

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
		base_types.FieldEntry(name='Assgnmt', type=IdentificationAssignment4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlAssgnmt', type=MessageIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rpt', type=VerificationReport5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

