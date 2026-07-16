# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BuyerProtectionSelectionCriteria1
from . import Max35Text
from . import SupplementaryData1

class BuyerProtectionInstructionReportRequestV01(base_types._BaseFieldType):

	__slots__ = ["_BuyrPrtcnSelctnCrit", "_QryRef", "_SplmtryData"]
	@property
	def BuyrPrtcnSelctnCrit(self):
		return self._BuyrPrtcnSelctnCrit

	@BuyrPrtcnSelctnCrit.setter
	def BuyrPrtcnSelctnCrit(self, value):
		self._BuyrPrtcnSelctnCrit = value if value is not None else base_types.UninitialisedField(self, 'BuyrPrtcnSelctnCrit', BuyerProtectionSelectionCriteria1, False)

	@BuyrPrtcnSelctnCrit.deleter
	def BuyrPrtcnSelctnCrit(self):
		del self._BuyrPrtcnSelctnCrit
		self._BuyrPrtcnSelctnCrit = base_types.UninitialisedField(self, 'BuyrPrtcnSelctnCrit', BuyerProtectionSelectionCriteria1, False)

	@property
	def QryRef(self):
		return self._QryRef

	@QryRef.setter
	def QryRef(self, value):
		self._QryRef = value if value is not None else base_types.UninitialisedField(self, 'QryRef', Max35Text, False)

	@QryRef.deleter
	def QryRef(self):
		del self._QryRef
		self._QryRef = base_types.UninitialisedField(self, 'QryRef', Max35Text, False)

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
		base_types.FieldEntry(name='BuyrPrtcnSelctnCrit', type=BuyerProtectionSelectionCriteria1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))