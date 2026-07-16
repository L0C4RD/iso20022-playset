# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTimeChoice
from . import Max2000Text
from . import PartyAndSignature2
from . import PartyIdentification43
from . import UndertakingAdvice1

class UndertakingIssuanceAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AdvsgPty", "_BkToBkInf", "_DgtlSgntr", "_DtOfAdvc", "_ScndAdvsgPty", "_UdrtkgIssncAdvcDtls"]
	@property
	def AdvsgPty(self):
		return self._AdvsgPty

	@AdvsgPty.setter
	def AdvsgPty(self, value):
		self._AdvsgPty = value if value is not None else base_types.UninitialisedField(self, 'AdvsgPty', PartyIdentification43, False)

	@AdvsgPty.deleter
	def AdvsgPty(self):
		del self._AdvsgPty
		self._AdvsgPty = base_types.UninitialisedField(self, 'AdvsgPty', PartyIdentification43, False)

	@property
	def BkToBkInf(self):
		return self._BkToBkInf

	@BkToBkInf.setter
	def BkToBkInf(self, value):
		self._BkToBkInf = value if value is not None else base_types.UninitialisedField(self, 'BkToBkInf', Max2000Text, True)

	@BkToBkInf.deleter
	def BkToBkInf(self):
		del self._BkToBkInf
		self._BkToBkInf = base_types.UninitialisedField(self, 'BkToBkInf', Max2000Text, True)

	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if value is not None else base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature2, False)

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature2, False)

	@property
	def DtOfAdvc(self):
		return self._DtOfAdvc

	@DtOfAdvc.setter
	def DtOfAdvc(self, value):
		self._DtOfAdvc = value if value is not None else base_types.UninitialisedField(self, 'DtOfAdvc', DateAndDateTimeChoice, False)

	@DtOfAdvc.deleter
	def DtOfAdvc(self):
		del self._DtOfAdvc
		self._DtOfAdvc = base_types.UninitialisedField(self, 'DtOfAdvc', DateAndDateTimeChoice, False)

	@property
	def ScndAdvsgPty(self):
		return self._ScndAdvsgPty

	@ScndAdvsgPty.setter
	def ScndAdvsgPty(self, value):
		self._ScndAdvsgPty = value if value is not None else base_types.UninitialisedField(self, 'ScndAdvsgPty', PartyIdentification43, False)

	@ScndAdvsgPty.deleter
	def ScndAdvsgPty(self):
		del self._ScndAdvsgPty
		self._ScndAdvsgPty = base_types.UninitialisedField(self, 'ScndAdvsgPty', PartyIdentification43, False)

	@property
	def UdrtkgIssncAdvcDtls(self):
		return self._UdrtkgIssncAdvcDtls

	@UdrtkgIssncAdvcDtls.setter
	def UdrtkgIssncAdvcDtls(self, value):
		self._UdrtkgIssncAdvcDtls = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgIssncAdvcDtls', UndertakingAdvice1, False)

	@UdrtkgIssncAdvcDtls.deleter
	def UdrtkgIssncAdvcDtls(self):
		del self._UdrtkgIssncAdvcDtls
		self._UdrtkgIssncAdvcDtls = base_types.UninitialisedField(self, 'UdrtkgIssncAdvcDtls', UndertakingAdvice1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdvsgPty', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkToBkInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtOfAdvc', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndAdvsgPty', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgIssncAdvcDtls', type=UndertakingAdvice1, min=1, max=1, mutex_group=None, array=False),
	))