from . import base_types
import PartyIdentification43
import PartyAndSignature2
import UndertakingAdvice1
import DateAndDateTimeChoice
import Max2000Text

class UndertakingIssuanceAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_DtOfAdvc", "_ScndAdvsgPty", "_AdvsgPty", "_DgtlSgntr", "_BkToBkInf", "_UdrtkgIssncAdvcDtls"]
	@property
	def DtOfAdvc(self):
		return self._DtOfAdvc

	@DtOfAdvc.setter
	def DtOfAdvc(self, value):
		self._DtOfAdvc = value if type(value) != auto else self.make_default("DtOfAdvc")

	@DtOfAdvc.deleter
	def DtOfAdvc(self):
		del self._DtOfAdvc
		self._DtOfAdvc = None

	@property
	def ScndAdvsgPty(self):
		return self._ScndAdvsgPty

	@ScndAdvsgPty.setter
	def ScndAdvsgPty(self, value):
		self._ScndAdvsgPty = value if type(value) != auto else self.make_default("ScndAdvsgPty")

	@ScndAdvsgPty.deleter
	def ScndAdvsgPty(self):
		del self._ScndAdvsgPty
		self._ScndAdvsgPty = None

	@property
	def AdvsgPty(self):
		return self._AdvsgPty

	@AdvsgPty.setter
	def AdvsgPty(self, value):
		self._AdvsgPty = value if type(value) != auto else self.make_default("AdvsgPty")

	@AdvsgPty.deleter
	def AdvsgPty(self):
		del self._AdvsgPty
		self._AdvsgPty = None

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
	def UdrtkgIssncAdvcDtls(self):
		return self._UdrtkgIssncAdvcDtls

	@UdrtkgIssncAdvcDtls.setter
	def UdrtkgIssncAdvcDtls(self, value):
		self._UdrtkgIssncAdvcDtls = value if type(value) != auto else self.make_default("UdrtkgIssncAdvcDtls")

	@UdrtkgIssncAdvcDtls.deleter
	def UdrtkgIssncAdvcDtls(self):
		del self._UdrtkgIssncAdvcDtls
		self._UdrtkgIssncAdvcDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtOfAdvc', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndAdvsgPty', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdvsgPty', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkToBkInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='UdrtkgIssncAdvcDtls', type=UndertakingAdvice1, min=1, max=1, mutex_group=None, array=False),
	))

