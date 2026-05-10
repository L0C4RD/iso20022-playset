from . import base_types
from .Max140Text import Max140Text
from .ISINIdentifier import ISINIdentifier
from .AlternateSecurityIdentification3 import AlternateSecurityIdentification3

class SecurityIdentification7(base_types._BaseFieldType):

	__slots__ = ["_ISIN", "_OthrId", "_Desc"]
	@property
	def ISIN(self):
		return self._ISIN

	@ISIN.setter
	def ISIN(self, value):
		self._ISIN = value if type(value) != auto else self.make_default("ISIN")

	@ISIN.deleter
	def ISIN(self):
		del self._ISIN
		self._ISIN = None

	@property
	def OthrId(self):
		return self._OthrId

	@OthrId.setter
	def OthrId(self, value):
		self._OthrId = value if type(value) != auto else self.make_default("OthrId")

	@OthrId.deleter
	def OthrId(self):
		del self._OthrId
		self._OthrId = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ISIN', type=ISINIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OthrId', type=AlternateSecurityIdentification3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

