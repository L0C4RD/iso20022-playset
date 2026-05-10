from . import base_types
from .Amendment2 import Amendment2
from .PartyAndSignature2 import PartyAndSignature2
from .Max2000Text import Max2000Text
from .ISODate import ISODate
from .PartyIdentification43 import PartyIdentification43

class UndertakingAmendmentAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_UdrtkgAmdmntAdvcDtls", "_AdvsgPty", "_ScndAdvsgPty", "_DtOfAdvc", "_DgtlSgntr", "_BkToBkInf"]
	@property
	def UdrtkgAmdmntAdvcDtls(self):
		return self._UdrtkgAmdmntAdvcDtls

	@UdrtkgAmdmntAdvcDtls.setter
	def UdrtkgAmdmntAdvcDtls(self, value):
		self._UdrtkgAmdmntAdvcDtls = value if type(value) != base_types.auto else self.make_default("UdrtkgAmdmntAdvcDtls")

	@UdrtkgAmdmntAdvcDtls.deleter
	def UdrtkgAmdmntAdvcDtls(self):
		del self._UdrtkgAmdmntAdvcDtls
		self._UdrtkgAmdmntAdvcDtls = None

	@property
	def AdvsgPty(self):
		return self._AdvsgPty

	@AdvsgPty.setter
	def AdvsgPty(self, value):
		self._AdvsgPty = value if type(value) != base_types.auto else self.make_default("AdvsgPty")

	@AdvsgPty.deleter
	def AdvsgPty(self):
		del self._AdvsgPty
		self._AdvsgPty = None

	@property
	def ScndAdvsgPty(self):
		return self._ScndAdvsgPty

	@ScndAdvsgPty.setter
	def ScndAdvsgPty(self, value):
		self._ScndAdvsgPty = value if type(value) != base_types.auto else self.make_default("ScndAdvsgPty")

	@ScndAdvsgPty.deleter
	def ScndAdvsgPty(self):
		del self._ScndAdvsgPty
		self._ScndAdvsgPty = None

	@property
	def DtOfAdvc(self):
		return self._DtOfAdvc

	@DtOfAdvc.setter
	def DtOfAdvc(self, value):
		self._DtOfAdvc = value if type(value) != base_types.auto else self.make_default("DtOfAdvc")

	@DtOfAdvc.deleter
	def DtOfAdvc(self):
		del self._DtOfAdvc
		self._DtOfAdvc = None

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
	def BkToBkInf(self):
		return self._BkToBkInf

	@BkToBkInf.setter
	def BkToBkInf(self, value):
		self._BkToBkInf = value if type(value) != base_types.auto else self.make_default("BkToBkInf")

	@BkToBkInf.deleter
	def BkToBkInf(self):
		del self._BkToBkInf
		self._BkToBkInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UdrtkgAmdmntAdvcDtls', type=Amendment2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdvsgPty', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndAdvsgPty', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtOfAdvc', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkToBkInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
	))

