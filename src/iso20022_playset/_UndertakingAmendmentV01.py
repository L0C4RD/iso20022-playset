from . import base_types
from ._PartyAndSignature2 import PartyAndSignature2
from ._Amendment1 import Amendment1
from ._Max2000Text import Max2000Text

class UndertakingAmendmentV01(base_types._BaseFieldType):

	__slots__ = ["_UdrtkgAmdmntDtls", "_BkToBkInf", "_DgtlSgntr"]
	@property
	def UdrtkgAmdmntDtls(self):
		return self._UdrtkgAmdmntDtls

	@UdrtkgAmdmntDtls.setter
	def UdrtkgAmdmntDtls(self, value):
		self._UdrtkgAmdmntDtls = value if type(value) != base_types.auto else self.make_default("UdrtkgAmdmntDtls")

	@UdrtkgAmdmntDtls.deleter
	def UdrtkgAmdmntDtls(self):
		del self._UdrtkgAmdmntDtls
		self._UdrtkgAmdmntDtls = None

	@property
	def BkToBkInf(self):
		return self._BkToBkInf

	@BkToBkInf.setter
	def BkToBkInf(self, value):
		self._BkToBkInf = value if type(value) != base_types.auto else self.make_default("BkToBkInf")

	@BkToBkInf.deleter
	def BkToBkInf(self):
		del self._BkToBkInf
		self._BkToBkInf = None

	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if type(value) != base_types.auto else self.make_default("DgtlSgntr")

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UdrtkgAmdmntDtls', type=Amendment1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkToBkInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=None, mutex_group=None, array=True),
	))

