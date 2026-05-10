from . import base_types
from ._BBANIdentifier import BBANIdentifier
from ._UPICIdentifier import UPICIdentifier
from ._IBANIdentifier import IBANIdentifier
from ._SimpleIdentificationInformation import SimpleIdentificationInformation

class CashAccountIdentification1Choice(base_types._BaseFieldType):

	__slots__ = ["_DmstAcct", "_IBAN", "_BBAN", "_UPIC"]
	@property
	def BBAN(self):
		return self._BBAN

	@BBAN.setter
	def BBAN(self, value):
		self._BBAN = value if type(value) != base_types.auto else self.make_default("BBAN")

	@BBAN.deleter
	def BBAN(self):
		del self._BBAN
		self._BBAN = None

	@property
	def DmstAcct(self):
		return self._DmstAcct

	@DmstAcct.setter
	def DmstAcct(self, value):
		self._DmstAcct = value if type(value) != base_types.auto else self.make_default("DmstAcct")

	@DmstAcct.deleter
	def DmstAcct(self):
		del self._DmstAcct
		self._DmstAcct = None

	@property
	def IBAN(self):
		return self._IBAN

	@IBAN.setter
	def IBAN(self, value):
		self._IBAN = value if type(value) != base_types.auto else self.make_default("IBAN")

	@IBAN.deleter
	def IBAN(self):
		del self._IBAN
		self._IBAN = None

	@property
	def UPIC(self):
		return self._UPIC

	@UPIC.setter
	def UPIC(self, value):
		self._UPIC = value if type(value) != base_types.auto else self.make_default("UPIC")

	@UPIC.deleter
	def UPIC(self):
		del self._UPIC
		self._UPIC = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BBAN', type=BBANIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DmstAcct', type=SimpleIdentificationInformation, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IBAN', type=IBANIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UPIC', type=UPICIdentifier, min=0, max=1, mutex_group=1, array=False),
	))

