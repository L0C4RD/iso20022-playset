# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IdentificationAssignment4
from . import MessageIdentification8
from . import SupplementaryData1
from . import VerificationReport5

class IdentificationVerificationReportV04(base_types._BaseFieldType):

	__slots__ = ["_Assgnmt", "_OrgnlAssgnmt", "_Rpt", "_SplmtryData"]
	@property
	def Assgnmt(self):
		return self._Assgnmt

	@Assgnmt.setter
	def Assgnmt(self, value):
		self._Assgnmt = value if value is not None else base_types.UninitialisedField(self, 'Assgnmt', IdentificationAssignment4, False)

	@Assgnmt.deleter
	def Assgnmt(self):
		del self._Assgnmt
		self._Assgnmt = base_types.UninitialisedField(self, 'Assgnmt', IdentificationAssignment4, False)

	@property
	def OrgnlAssgnmt(self):
		return self._OrgnlAssgnmt

	@OrgnlAssgnmt.setter
	def OrgnlAssgnmt(self, value):
		self._OrgnlAssgnmt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlAssgnmt', MessageIdentification8, False)

	@OrgnlAssgnmt.deleter
	def OrgnlAssgnmt(self):
		del self._OrgnlAssgnmt
		self._OrgnlAssgnmt = base_types.UninitialisedField(self, 'OrgnlAssgnmt', MessageIdentification8, False)

	@property
	def Rpt(self):
		return self._Rpt

	@Rpt.setter
	def Rpt(self, value):
		self._Rpt = value if value is not None else base_types.UninitialisedField(self, 'Rpt', VerificationReport5, True)

	@Rpt.deleter
	def Rpt(self):
		del self._Rpt
		self._Rpt = base_types.UninitialisedField(self, 'Rpt', VerificationReport5, True)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assgnmt', type=IdentificationAssignment4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlAssgnmt', type=MessageIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rpt', type=VerificationReport5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))