import base_types
import Undertaking3
import Max2000Text
import PartyAndSignature2

class UndertakingIssuanceV01(base_types._BaseFieldType):

	__slots__ = ["_UdrtkgIssncDtls", "_BkToBkInf", "_DgtlSgntr", "_BkToBnfcryInf"]
	@property
	def UdrtkgIssncDtls(self):
		return self._UdrtkgIssncDtls

	@UdrtkgIssncDtls.setter
	def UdrtkgIssncDtls(self, value):
		self._UdrtkgIssncDtls = value if type(value) != auto else self.make_default("UdrtkgIssncDtls")

	@UdrtkgIssncDtls.deleter
	def UdrtkgIssncDtls(self):
		del self._UdrtkgIssncDtls
		self._UdrtkgIssncDtls = None

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
	def BkToBnfcryInf(self):
		return self._BkToBnfcryInf

	@BkToBnfcryInf.setter
	def BkToBnfcryInf(self, value):
		self._BkToBnfcryInf = value if type(value) != auto else self.make_default("BkToBnfcryInf")

	@BkToBnfcryInf.deleter
	def BkToBnfcryInf(self):
		del self._BkToBnfcryInf
		self._BkToBnfcryInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UdrtkgIssncDtls', type=Undertaking3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkToBkInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BkToBnfcryInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
	))

