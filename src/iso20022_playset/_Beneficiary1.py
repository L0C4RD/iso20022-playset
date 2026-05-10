from . import base_types
from .Max2000Text import Max2000Text
from .AddressOrParty1Choice import AddressOrParty1Choice

class Beneficiary1(base_types._BaseFieldType):

	__slots__ = ["_NewAdrOrNewBnfcry", "_AddtlInf"]
	@property
	def NewAdrOrNewBnfcry(self):
		return self._NewAdrOrNewBnfcry

	@NewAdrOrNewBnfcry.setter
	def NewAdrOrNewBnfcry(self, value):
		self._NewAdrOrNewBnfcry = value if type(value) != base_types.auto else self.make_default("NewAdrOrNewBnfcry")

	@NewAdrOrNewBnfcry.deleter
	def NewAdrOrNewBnfcry(self):
		del self._NewAdrOrNewBnfcry
		self._NewAdrOrNewBnfcry = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NewAdrOrNewBnfcry', type=AddressOrParty1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
	))

