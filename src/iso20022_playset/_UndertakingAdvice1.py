# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AdvisingPartyAdditionalInformation1 import AdvisingPartyAdditionalInformation1
from ._PartyAndSignature2 import PartyAndSignature2
from ._UndertakingConfirmation1 import UndertakingConfirmation1
from ._UndertakingIssuanceMessage import UndertakingIssuanceMessage

class UndertakingAdvice1(base_types._BaseFieldType):

	__slots__ = ["_ConfDtls", "_DgtlSgntr", "_FrstAdvsgPtyAddtlInf", "_ScndAdvsgPtyAddtlInf", "_UdrtkgIssncMsg"]
	@property
	def ConfDtls(self):
		return self._ConfDtls

	@ConfDtls.setter
	def ConfDtls(self, value):
		self._ConfDtls = value if type(value) != base_types.auto else self.make_default("ConfDtls")

	@ConfDtls.deleter
	def ConfDtls(self):
		del self._ConfDtls
		self._ConfDtls = None

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

	@property
	def FrstAdvsgPtyAddtlInf(self):
		return self._FrstAdvsgPtyAddtlInf

	@FrstAdvsgPtyAddtlInf.setter
	def FrstAdvsgPtyAddtlInf(self, value):
		self._FrstAdvsgPtyAddtlInf = value if type(value) != base_types.auto else self.make_default("FrstAdvsgPtyAddtlInf")

	@FrstAdvsgPtyAddtlInf.deleter
	def FrstAdvsgPtyAddtlInf(self):
		del self._FrstAdvsgPtyAddtlInf
		self._FrstAdvsgPtyAddtlInf = None

	@property
	def ScndAdvsgPtyAddtlInf(self):
		return self._ScndAdvsgPtyAddtlInf

	@ScndAdvsgPtyAddtlInf.setter
	def ScndAdvsgPtyAddtlInf(self, value):
		self._ScndAdvsgPtyAddtlInf = value if type(value) != base_types.auto else self.make_default("ScndAdvsgPtyAddtlInf")

	@ScndAdvsgPtyAddtlInf.deleter
	def ScndAdvsgPtyAddtlInf(self):
		del self._ScndAdvsgPtyAddtlInf
		self._ScndAdvsgPtyAddtlInf = None

	@property
	def UdrtkgIssncMsg(self):
		return self._UdrtkgIssncMsg

	@UdrtkgIssncMsg.setter
	def UdrtkgIssncMsg(self, value):
		self._UdrtkgIssncMsg = value if type(value) != base_types.auto else self.make_default("UdrtkgIssncMsg")

	@UdrtkgIssncMsg.deleter
	def UdrtkgIssncMsg(self):
		del self._UdrtkgIssncMsg
		self._UdrtkgIssncMsg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ConfDtls', type=UndertakingConfirmation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=3, mutex_group=None, array=True),
		base_types.FieldEntry(name='FrstAdvsgPtyAddtlInf', type=AdvisingPartyAdditionalInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndAdvsgPtyAddtlInf', type=AdvisingPartyAdditionalInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgIssncMsg', type=UndertakingIssuanceMessage, min=1, max=1, mutex_group=None, array=False),
	))