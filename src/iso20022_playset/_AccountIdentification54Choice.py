from . import base_types
from .Max35Text import Max35Text
from .Max256Text import Max256Text
from .UPICIdentifier import UPICIdentifier
from .Max16Text import Max16Text
from .BBANIdentifier import BBANIdentifier
from .Min8Max28NumericText import Min8Max28NumericText
from .IBAN2007Identifier import IBAN2007Identifier

class AccountIdentification54Choice(base_types._BaseFieldType):

	__slots__ = ["_UPIC", "_MSISDN", "_IBAN", "_Card", "_Othr", "_BBAN", "_Dmst", "_EMail"]
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
	def Card(self):
		return self._Card

	@Card.setter
	def Card(self, value):
		self._Card = value if type(value) != base_types.auto else self.make_default("Card")

	@Card.deleter
	def Card(self):
		del self._Card
		self._Card = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

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
	def Dmst(self):
		return self._Dmst

	@Dmst.setter
	def Dmst(self, value):
		self._Dmst = value if type(value) != base_types.auto else self.make_default("Dmst")

	@Dmst.deleter
	def Dmst(self):
		del self._Dmst
		self._Dmst = None

	@property
	def EMail(self):
		return self._EMail

	@EMail.setter
	def EMail(self, value):
		self._EMail = value if type(value) != base_types.auto else self.make_default("EMail")

	@EMail.deleter
	def EMail(self):
		del self._EMail
		self._EMail = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UPIC', type=UPICIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MSISDN', type=Max16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IBAN', type=IBAN2007Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Card', type=Min8Max28NumericText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BBAN', type=BBANIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dmst', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='EMail', type=Max256Text, min=0, max=1, mutex_group=1, array=False),
	))

