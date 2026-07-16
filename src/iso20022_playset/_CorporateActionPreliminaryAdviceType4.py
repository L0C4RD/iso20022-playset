# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionMovementPreliminaryAdviceFunction1Code
from . import CorporateActionPreliminaryAdviceType1Code
from . import Max35Text

class CorporateActionPreliminaryAdviceType4(base_types._BaseFieldType):

	__slots__ = ["_Fctn", "_MvmntPrlimryAdvcId", "_Tp"]
	@property
	def Fctn(self):
		return self._Fctn

	@Fctn.setter
	def Fctn(self, value):
		self._Fctn = value if value is not None else base_types.UninitialisedField(self, 'Fctn', CorporateActionMovementPreliminaryAdviceFunction1Code, False)

	@Fctn.deleter
	def Fctn(self):
		del self._Fctn
		self._Fctn = base_types.UninitialisedField(self, 'Fctn', CorporateActionMovementPreliminaryAdviceFunction1Code, False)

	@property
	def MvmntPrlimryAdvcId(self):
		return self._MvmntPrlimryAdvcId

	@MvmntPrlimryAdvcId.setter
	def MvmntPrlimryAdvcId(self, value):
		self._MvmntPrlimryAdvcId = value if value is not None else base_types.UninitialisedField(self, 'MvmntPrlimryAdvcId', Max35Text, False)

	@MvmntPrlimryAdvcId.deleter
	def MvmntPrlimryAdvcId(self):
		del self._MvmntPrlimryAdvcId
		self._MvmntPrlimryAdvcId = base_types.UninitialisedField(self, 'MvmntPrlimryAdvcId', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', CorporateActionPreliminaryAdviceType1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', CorporateActionPreliminaryAdviceType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Fctn', type=CorporateActionMovementPreliminaryAdviceFunction1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntPrlimryAdvcId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CorporateActionPreliminaryAdviceType1Code, min=1, max=1, mutex_group=None, array=False),
	))