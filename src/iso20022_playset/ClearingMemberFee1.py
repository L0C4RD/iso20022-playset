import base_types
import ActiveCurrencyAndAmount
import PartyIdentification118Choice

class ClearingMemberFee1(base_types._BaseFieldType):

	__slots__ = ["_ClrFee", "_ClrMmbId"]
	@property
	def ClrFee(self):
		return self._ClrFee

	@ClrFee.setter
	def ClrFee(self, value):
		self._ClrFee = value if type(value) != auto else self.make_default("ClrFee")

	@ClrFee.deleter
	def ClrFee(self):
		del self._ClrFee
		self._ClrFee = None

	@property
	def ClrMmbId(self):
		return self._ClrMmbId

	@ClrMmbId.setter
	def ClrMmbId(self, value):
		self._ClrMmbId = value if type(value) != auto else self.make_default("ClrMmbId")

	@ClrMmbId.deleter
	def ClrMmbId(self):
		del self._ClrMmbId
		self._ClrMmbId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrFee', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMmbId', type=PartyIdentification118Choice, min=1, max=1, mutex_group=None, array=False),
	))

