# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BBANIdentifier
from . import IBAN2007Identifier
from . import Max16Text
from . import Max256Text
from . import Max35Text
from . import Min8Max28NumericText
from . import UPICIdentifier

class AccountIdentification54Choice(base_types._BaseFieldType):

	__slots__ = ["_BBAN", "_Card", "_Dmst", "_EMail", "_IBAN", "_MSISDN", "_Othr", "_UPIC"]
	@property
	def BBAN(self):
		return self._BBAN

	@BBAN.setter
	def BBAN(self, value):
		self._BBAN = value if value is not None else base_types.UninitialisedField(self, 'BBAN', BBANIdentifier, False)

	@BBAN.deleter
	def BBAN(self):
		del self._BBAN
		self._BBAN = base_types.UninitialisedField(self, 'BBAN', BBANIdentifier, False)

	@property
	def Card(self):
		return self._Card

	@Card.setter
	def Card(self, value):
		self._Card = value if value is not None else base_types.UninitialisedField(self, 'Card', Min8Max28NumericText, False)

	@Card.deleter
	def Card(self):
		del self._Card
		self._Card = base_types.UninitialisedField(self, 'Card', Min8Max28NumericText, False)

	@property
	def Dmst(self):
		return self._Dmst

	@Dmst.setter
	def Dmst(self, value):
		self._Dmst = value if value is not None else base_types.UninitialisedField(self, 'Dmst', Max35Text, False)

	@Dmst.deleter
	def Dmst(self):
		del self._Dmst
		self._Dmst = base_types.UninitialisedField(self, 'Dmst', Max35Text, False)

	@property
	def EMail(self):
		return self._EMail

	@EMail.setter
	def EMail(self, value):
		self._EMail = value if value is not None else base_types.UninitialisedField(self, 'EMail', Max256Text, False)

	@EMail.deleter
	def EMail(self):
		del self._EMail
		self._EMail = base_types.UninitialisedField(self, 'EMail', Max256Text, False)

	@property
	def IBAN(self):
		return self._IBAN

	@IBAN.setter
	def IBAN(self, value):
		self._IBAN = value if value is not None else base_types.UninitialisedField(self, 'IBAN', IBAN2007Identifier, False)

	@IBAN.deleter
	def IBAN(self):
		del self._IBAN
		self._IBAN = base_types.UninitialisedField(self, 'IBAN', IBAN2007Identifier, False)

	@property
	def MSISDN(self):
		return self._MSISDN

	@MSISDN.setter
	def MSISDN(self, value):
		self._MSISDN = value if value is not None else base_types.UninitialisedField(self, 'MSISDN', Max16Text, False)

	@MSISDN.deleter
	def MSISDN(self):
		del self._MSISDN
		self._MSISDN = base_types.UninitialisedField(self, 'MSISDN', Max16Text, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', Max35Text, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', Max35Text, False)

	@property
	def UPIC(self):
		return self._UPIC

	@UPIC.setter
	def UPIC(self, value):
		self._UPIC = value if value is not None else base_types.UninitialisedField(self, 'UPIC', UPICIdentifier, False)

	@UPIC.deleter
	def UPIC(self):
		del self._UPIC
		self._UPIC = base_types.UninitialisedField(self, 'UPIC', UPICIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BBAN', type=BBANIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Card', type=Min8Max28NumericText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dmst', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='EMail', type=Max256Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IBAN', type=IBAN2007Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MSISDN', type=Max16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UPIC', type=UPICIdentifier, min=0, max=1, mutex_group=1, array=False),
	))