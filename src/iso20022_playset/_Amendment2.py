# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdvisingPartyAdditionalInformation1
from . import PartyAndSignature2
from . import UndertakingAmendmentMessage1
from . import UndertakingConfirmation1

class Amendment2(base_types._BaseFieldType):

	__slots__ = ["_ConfDtls", "_DgtlSgntr", "_FrstAdvsgPtyAddtlInf", "_ScndAdvsgPtyAddtlInf", "_UdrtkgAmdmntMsg"]
	@property
	def ConfDtls(self):
		return self._ConfDtls

	@ConfDtls.setter
	def ConfDtls(self, value):
		self._ConfDtls = value if value is not None else base_types.UninitialisedField(self, 'ConfDtls', UndertakingConfirmation1, False)

	@ConfDtls.deleter
	def ConfDtls(self):
		del self._ConfDtls
		self._ConfDtls = base_types.UninitialisedField(self, 'ConfDtls', UndertakingConfirmation1, False)

	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if value is not None else base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature2, True)

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature2, True)

	@property
	def FrstAdvsgPtyAddtlInf(self):
		return self._FrstAdvsgPtyAddtlInf

	@FrstAdvsgPtyAddtlInf.setter
	def FrstAdvsgPtyAddtlInf(self, value):
		self._FrstAdvsgPtyAddtlInf = value if value is not None else base_types.UninitialisedField(self, 'FrstAdvsgPtyAddtlInf', AdvisingPartyAdditionalInformation1, False)

	@FrstAdvsgPtyAddtlInf.deleter
	def FrstAdvsgPtyAddtlInf(self):
		del self._FrstAdvsgPtyAddtlInf
		self._FrstAdvsgPtyAddtlInf = base_types.UninitialisedField(self, 'FrstAdvsgPtyAddtlInf', AdvisingPartyAdditionalInformation1, False)

	@property
	def ScndAdvsgPtyAddtlInf(self):
		return self._ScndAdvsgPtyAddtlInf

	@ScndAdvsgPtyAddtlInf.setter
	def ScndAdvsgPtyAddtlInf(self, value):
		self._ScndAdvsgPtyAddtlInf = value if value is not None else base_types.UninitialisedField(self, 'ScndAdvsgPtyAddtlInf', AdvisingPartyAdditionalInformation1, False)

	@ScndAdvsgPtyAddtlInf.deleter
	def ScndAdvsgPtyAddtlInf(self):
		del self._ScndAdvsgPtyAddtlInf
		self._ScndAdvsgPtyAddtlInf = base_types.UninitialisedField(self, 'ScndAdvsgPtyAddtlInf', AdvisingPartyAdditionalInformation1, False)

	@property
	def UdrtkgAmdmntMsg(self):
		return self._UdrtkgAmdmntMsg

	@UdrtkgAmdmntMsg.setter
	def UdrtkgAmdmntMsg(self, value):
		self._UdrtkgAmdmntMsg = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgAmdmntMsg', UndertakingAmendmentMessage1, False)

	@UdrtkgAmdmntMsg.deleter
	def UdrtkgAmdmntMsg(self):
		del self._UdrtkgAmdmntMsg
		self._UdrtkgAmdmntMsg = base_types.UninitialisedField(self, 'UdrtkgAmdmntMsg', UndertakingAmendmentMessage1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ConfDtls', type=UndertakingConfirmation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=3, mutex_group=None, array=True),
		base_types.FieldEntry(name='FrstAdvsgPtyAddtlInf', type=AdvisingPartyAdditionalInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndAdvsgPtyAddtlInf', type=AdvisingPartyAdditionalInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgAmdmntMsg', type=UndertakingAmendmentMessage1, min=1, max=1, mutex_group=None, array=False),
	))