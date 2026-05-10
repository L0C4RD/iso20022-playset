from . import base_types
from .Max16Text import Max16Text
from .IBAN2007Identifier import IBAN2007Identifier
from .SimpleIdentificationInformation4 import SimpleIdentificationInformation4
from .Max256Text import Max256Text
from .UPICIdentifier import UPICIdentifier
from .BBANIdentifier import BBANIdentifier

class AccountIdentification80Choice(base_types._BaseFieldType):

	__slots__ = ["_MSISDN", "_IBAN", "_DmstAcct", "_BBAN", "_UPIC", "_Email"]
	@property
	def MSISDN(self):
		return self._MSISDN

	@MSISDN.setter
	def MSISDN(self, value):
		self._MSISDN = value if type(value) != base_types.auto else self.make_default("MSISDN")

	@MSISDN.deleter
	def MSISDN(self):
		del self._MSISDN
		self._MSISDN = None

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
	def UPIC(self):
		return self._UPIC

	@UPIC.setter
	def UPIC(self, value):
		self._UPIC = value if type(value) != base_types.auto else self.make_default("UPIC")

	@UPIC.deleter
	def UPIC(self):
		del self._UPIC
		self._UPIC = None

	@property
	def Email(self):
		return self._Email

	@Email.setter
	def Email(self, value):
		self._Email = value if type(value) != base_types.auto else self.make_default("Email")

	@Email.deleter
	def Email(self):
		del self._Email
		self._Email = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MSISDN', type=Max16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IBAN', type=IBAN2007Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DmstAcct', type=SimpleIdentificationInformation4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BBAN', type=BBANIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UPIC', type=UPICIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Email', type=Max256Text, min=0, max=1, mutex_group=1, array=False),
	))

