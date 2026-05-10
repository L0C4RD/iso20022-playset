from . import base_types
from ._Max2000Text import Max2000Text
from ._Max35Text import Max35Text

class AdvisingPartyAdditionalInformation1(base_types._BaseFieldType):

	__slots__ = ["_BkToBnfcryInf", "_RefNb"]
	@property
	def BkToBnfcryInf(self):
		return self._BkToBnfcryInf

	@BkToBnfcryInf.setter
	def BkToBnfcryInf(self, value):
		self._BkToBnfcryInf = value if type(value) != base_types.auto else self.make_default("BkToBnfcryInf")

	@BkToBnfcryInf.deleter
	def BkToBnfcryInf(self):
		del self._BkToBnfcryInf
		self._BkToBnfcryInf = None

	@property
	def RefNb(self):
		return self._RefNb

	@RefNb.setter
	def RefNb(self, value):
		self._RefNb = value if type(value) != base_types.auto else self.make_default("RefNb")

	@RefNb.deleter
	def RefNb(self):
		del self._RefNb
		self._RefNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BkToBnfcryInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='RefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

