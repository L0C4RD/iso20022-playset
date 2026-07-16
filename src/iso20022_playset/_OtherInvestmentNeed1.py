# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import Max35Text
from . import TargetMarket1Choice

class OtherInvestmentNeed1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_ClntObjctvsAndNeedsTp", "_Trgt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, False)

	@property
	def ClntObjctvsAndNeedsTp(self):
		return self._ClntObjctvsAndNeedsTp

	@ClntObjctvsAndNeedsTp.setter
	def ClntObjctvsAndNeedsTp(self, value):
		self._ClntObjctvsAndNeedsTp = value if value is not None else base_types.UninitialisedField(self, 'ClntObjctvsAndNeedsTp', Max35Text, False)

	@ClntObjctvsAndNeedsTp.deleter
	def ClntObjctvsAndNeedsTp(self):
		del self._ClntObjctvsAndNeedsTp
		self._ClntObjctvsAndNeedsTp = base_types.UninitialisedField(self, 'ClntObjctvsAndNeedsTp', Max35Text, False)

	@property
	def Trgt(self):
		return self._Trgt

	@Trgt.setter
	def Trgt(self, value):
		self._Trgt = value if value is not None else base_types.UninitialisedField(self, 'Trgt', TargetMarket1Choice, False)

	@Trgt.deleter
	def Trgt(self):
		del self._Trgt
		self._Trgt = base_types.UninitialisedField(self, 'Trgt', TargetMarket1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntObjctvsAndNeedsTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trgt', type=TargetMarket1Choice, min=0, max=1, mutex_group=None, array=False),
	))