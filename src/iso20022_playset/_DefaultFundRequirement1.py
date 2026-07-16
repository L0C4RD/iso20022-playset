# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import GenericIdentification165
from . import Max35Text

class DefaultFundRequirement1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_ClrMmbId", "_SvcId"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def ClrMmbId(self):
		return self._ClrMmbId

	@ClrMmbId.setter
	def ClrMmbId(self, value):
		self._ClrMmbId = value if value is not None else base_types.UninitialisedField(self, 'ClrMmbId', GenericIdentification165, False)

	@ClrMmbId.deleter
	def ClrMmbId(self):
		del self._ClrMmbId
		self._ClrMmbId = base_types.UninitialisedField(self, 'ClrMmbId', GenericIdentification165, False)

	@property
	def SvcId(self):
		return self._SvcId

	@SvcId.setter
	def SvcId(self, value):
		self._SvcId = value if value is not None else base_types.UninitialisedField(self, 'SvcId', Max35Text, False)

	@SvcId.deleter
	def SvcId(self):
		del self._SvcId
		self._SvcId = base_types.UninitialisedField(self, 'SvcId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMmbId', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))