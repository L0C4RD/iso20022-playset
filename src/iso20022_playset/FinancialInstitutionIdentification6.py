import base_types
import ClearingSystemMemberIdentification2Choice
import BICIdentifier
import GenericIdentification4

class FinancialInstitutionIdentification6(base_types._BaseFieldType):

	__slots__ = ["_BIC", "_ClrSysMmbId", "_PrtryId"]
	@property
	def BIC(self):
		return self._BIC

	@BIC.setter
	def BIC(self, value):
		self._BIC = value if type(value) != auto else self.make_default("BIC")

	@BIC.deleter
	def BIC(self):
		del self._BIC
		self._BIC = None

	@property
	def ClrSysMmbId(self):
		return self._ClrSysMmbId

	@ClrSysMmbId.setter
	def ClrSysMmbId(self, value):
		self._ClrSysMmbId = value if type(value) != auto else self.make_default("ClrSysMmbId")

	@ClrSysMmbId.deleter
	def ClrSysMmbId(self):
		del self._ClrSysMmbId
		self._ClrSysMmbId = None

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if type(value) != auto else self.make_default("PrtryId")

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BIC', type=BICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSysMmbId', type=ClearingSystemMemberIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification4, min=0, max=1, mutex_group=None, array=False),
	))

