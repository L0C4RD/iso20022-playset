from . import base_types
from ._BBANIdentifier import BBANIdentifier
from ._SimpleIdentificationInformation2 import SimpleIdentificationInformation2
from ._IBAN2007Identifier import IBAN2007Identifier
from ._UPICIdentifier import UPICIdentifier

class AccountIdentification55Choice(base_types._BaseFieldType):

	__slots__ = ["_BBAN", "_IBAN", "_PrtryAcct", "_UPIC"]
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
	def PrtryAcct(self):
		return self._PrtryAcct

	@PrtryAcct.setter
	def PrtryAcct(self, value):
		self._PrtryAcct = value if type(value) != base_types.auto else self.make_default("PrtryAcct")

	@PrtryAcct.deleter
	def PrtryAcct(self):
		del self._PrtryAcct
		self._PrtryAcct = None

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
		base_types.FieldEntry(name='IBAN', type=IBAN2007Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryAcct', type=SimpleIdentificationInformation2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UPIC', type=UPICIdentifier, min=0, max=1, mutex_group=1, array=False),
	))

