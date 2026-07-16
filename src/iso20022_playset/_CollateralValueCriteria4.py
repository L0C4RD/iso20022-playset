# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralValueReturnCriteria1
from . import CollateralValueSearchCriteria4
from . import Max35Text

class CollateralValueCriteria4(base_types._BaseFieldType):

	__slots__ = ["_QryNm", "_RtrCrit", "_SchCrit"]
	@property
	def QryNm(self):
		return self._QryNm

	@QryNm.setter
	def QryNm(self, value):
		self._QryNm = value if value is not None else base_types.UninitialisedField(self, 'QryNm', Max35Text, False)

	@QryNm.deleter
	def QryNm(self):
		del self._QryNm
		self._QryNm = base_types.UninitialisedField(self, 'QryNm', Max35Text, False)

	@property
	def RtrCrit(self):
		return self._RtrCrit

	@RtrCrit.setter
	def RtrCrit(self, value):
		self._RtrCrit = value if value is not None else base_types.UninitialisedField(self, 'RtrCrit', CollateralValueReturnCriteria1, False)

	@RtrCrit.deleter
	def RtrCrit(self):
		del self._RtrCrit
		self._RtrCrit = base_types.UninitialisedField(self, 'RtrCrit', CollateralValueReturnCriteria1, False)

	@property
	def SchCrit(self):
		return self._SchCrit

	@SchCrit.setter
	def SchCrit(self, value):
		self._SchCrit = value if value is not None else base_types.UninitialisedField(self, 'SchCrit', CollateralValueSearchCriteria4, False)

	@SchCrit.deleter
	def SchCrit(self):
		del self._SchCrit
		self._SchCrit = base_types.UninitialisedField(self, 'SchCrit', CollateralValueSearchCriteria4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='QryNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrCrit', type=CollateralValueReturnCriteria1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchCrit', type=CollateralValueSearchCriteria4, min=0, max=1, mutex_group=None, array=False),
	))