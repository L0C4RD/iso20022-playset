import base_types
import UndertakingAmendmentMessage1
import PartyAndSignature2
import AdvisingPartyAdditionalInformation1
import UndertakingConfirmation1

class Amendment2(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_UdrtkgAmdmntMsg", "_ConfDtls", "_FrstAdvsgPtyAddtlInf", "_ScndAdvsgPtyAddtlInf"]
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
	def UdrtkgAmdmntMsg(self):
		return self._UdrtkgAmdmntMsg

	@UdrtkgAmdmntMsg.setter
	def UdrtkgAmdmntMsg(self, value):
		self._UdrtkgAmdmntMsg = value if type(value) != auto else self.make_default("UdrtkgAmdmntMsg")

	@UdrtkgAmdmntMsg.deleter
	def UdrtkgAmdmntMsg(self):
		del self._UdrtkgAmdmntMsg
		self._UdrtkgAmdmntMsg = None

	@property
	def ConfDtls(self):
		return self._ConfDtls

	@ConfDtls.setter
	def ConfDtls(self, value):
		self._ConfDtls = value if type(value) != auto else self.make_default("ConfDtls")

	@ConfDtls.deleter
	def ConfDtls(self):
		del self._ConfDtls
		self._ConfDtls = None

	@property
	def FrstAdvsgPtyAddtlInf(self):
		return self._FrstAdvsgPtyAddtlInf

	@FrstAdvsgPtyAddtlInf.setter
	def FrstAdvsgPtyAddtlInf(self, value):
		self._FrstAdvsgPtyAddtlInf = value if type(value) != auto else self.make_default("FrstAdvsgPtyAddtlInf")

	@FrstAdvsgPtyAddtlInf.deleter
	def FrstAdvsgPtyAddtlInf(self):
		del self._FrstAdvsgPtyAddtlInf
		self._FrstAdvsgPtyAddtlInf = None

	@property
	def ScndAdvsgPtyAddtlInf(self):
		return self._ScndAdvsgPtyAddtlInf

	@ScndAdvsgPtyAddtlInf.setter
	def ScndAdvsgPtyAddtlInf(self, value):
		self._ScndAdvsgPtyAddtlInf = value if type(value) != auto else self.make_default("ScndAdvsgPtyAddtlInf")

	@ScndAdvsgPtyAddtlInf.deleter
	def ScndAdvsgPtyAddtlInf(self):
		del self._ScndAdvsgPtyAddtlInf
		self._ScndAdvsgPtyAddtlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=3, mutex_group=None, array=True),
		base_types.FieldEntry(name='UdrtkgAmdmntMsg', type=UndertakingAmendmentMessage1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfDtls', type=UndertakingConfirmation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstAdvsgPtyAddtlInf', type=AdvisingPartyAdditionalInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndAdvsgPtyAddtlInf', type=AdvisingPartyAdditionalInformation1, min=0, max=1, mutex_group=None, array=False),
	))

