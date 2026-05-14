# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BuyerProtectionSelectionCriteria1 import BuyerProtectionSelectionCriteria1
from ._Max35Text import Max35Text
from ._SupplementaryData1 import SupplementaryData1

class BuyerProtectionInstructionReportRequestV01(base_types._BaseFieldType):

	__slots__ = ["_BuyrPrtcnSelctnCrit", "_QryRef", "_SplmtryData"]
	@property
	def BuyrPrtcnSelctnCrit(self):
		return self._BuyrPrtcnSelctnCrit

	@BuyrPrtcnSelctnCrit.setter
	def BuyrPrtcnSelctnCrit(self, value):
		self._BuyrPrtcnSelctnCrit = value if type(value) != base_types.auto else self.make_default("BuyrPrtcnSelctnCrit")

	@BuyrPrtcnSelctnCrit.deleter
	def BuyrPrtcnSelctnCrit(self):
		del self._BuyrPrtcnSelctnCrit
		self._BuyrPrtcnSelctnCrit = None

	@property
	def QryRef(self):
		return self._QryRef

	@QryRef.setter
	def QryRef(self, value):
		self._QryRef = value if type(value) != base_types.auto else self.make_default("QryRef")

	@QryRef.deleter
	def QryRef(self):
		del self._QryRef
		self._QryRef = None

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
		base_types.FieldEntry(name='BuyrPrtcnSelctnCrit', type=BuyerProtectionSelectionCriteria1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))