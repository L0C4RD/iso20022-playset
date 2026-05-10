import base_types
import ActiveCurrencyAndAmount
import GenericIdentification165
import Max35Text

class DefaultFundRequirement1(base_types._BaseFieldType):

	__slots__ = ["_SvcId", "_ClrMmbId", "_Amt"]
	@property
	def SvcId(self):
		return self._SvcId

	@SvcId.setter
	def SvcId(self, value):
		self._SvcId = value if type(value) != auto else self.make_default("SvcId")

	@SvcId.deleter
	def SvcId(self):
		del self._SvcId
		self._SvcId = None

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

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMmbId', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

