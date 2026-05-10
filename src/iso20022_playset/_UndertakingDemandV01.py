from . import base_types
from ._PartyAndSignature2 import PartyAndSignature2
from ._Demand1 import Demand1
from ._Max2000Text import Max2000Text

class UndertakingDemandV01(base_types._BaseFieldType):

	__slots__ = ["_UdrtkgDmndDtls", "_BkToBkInf", "_DgtlSgntr"]
	@property
	def UdrtkgDmndDtls(self):
		return self._UdrtkgDmndDtls

	@UdrtkgDmndDtls.setter
	def UdrtkgDmndDtls(self, value):
		self._UdrtkgDmndDtls = value if type(value) != base_types.auto else self.make_default("UdrtkgDmndDtls")

	@UdrtkgDmndDtls.deleter
	def UdrtkgDmndDtls(self):
		del self._UdrtkgDmndDtls
		self._UdrtkgDmndDtls = None

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
		base_types.FieldEntry(name='UdrtkgDmndDtls', type=Demand1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkToBkInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
	))

