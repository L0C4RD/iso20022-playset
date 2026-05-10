import base_types
import Max2000Text
import PartyAndSignature2
import Demand1

class UndertakingDemandV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_UdrtkgDmndDtls", "_BkToBkInf"]
	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if type(value) != auto else self.make_default("DgtlSgntr")

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = None

	@property
	def UdrtkgDmndDtls(self):
		return self._UdrtkgDmndDtls

	@UdrtkgDmndDtls.setter
	def UdrtkgDmndDtls(self, value):
		self._UdrtkgDmndDtls = value if type(value) != auto else self.make_default("UdrtkgDmndDtls")

	@UdrtkgDmndDtls.deleter
	def UdrtkgDmndDtls(self):
		del self._UdrtkgDmndDtls
		self._UdrtkgDmndDtls = None

	@property
	def BkToBkInf(self):
		return self._BkToBkInf

	@BkToBkInf.setter
	def BkToBkInf(self, value):
		self._BkToBkInf = value if type(value) != auto else self.make_default("BkToBkInf")

	@BkToBkInf.deleter
	def BkToBkInf(self):
		del self._BkToBkInf
		self._BkToBkInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgDmndDtls', type=Demand1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkToBkInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
	))

