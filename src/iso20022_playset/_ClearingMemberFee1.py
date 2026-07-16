# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import PartyIdentification118Choice

class ClearingMemberFee1(base_types._BaseFieldType):

	__slots__ = ["_ClrFee", "_ClrMmbId"]
	@property
	def ClrFee(self):
		return self._ClrFee

	@ClrFee.setter
	def ClrFee(self, value):
		self._ClrFee = value if value is not None else base_types.UninitialisedField(self, 'ClrFee', ActiveCurrencyAndAmount, False)

	@ClrFee.deleter
	def ClrFee(self):
		del self._ClrFee
		self._ClrFee = base_types.UninitialisedField(self, 'ClrFee', ActiveCurrencyAndAmount, False)

	@property
	def ClrMmbId(self):
		return self._ClrMmbId

	@ClrMmbId.setter
	def ClrMmbId(self, value):
		self._ClrMmbId = value if value is not None else base_types.UninitialisedField(self, 'ClrMmbId', PartyIdentification118Choice, False)

	@ClrMmbId.deleter
	def ClrMmbId(self):
		del self._ClrMmbId
		self._ClrMmbId = base_types.UninitialisedField(self, 'ClrMmbId', PartyIdentification118Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrFee', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMmbId', type=PartyIdentification118Choice, min=1, max=1, mutex_group=None, array=False),
	))