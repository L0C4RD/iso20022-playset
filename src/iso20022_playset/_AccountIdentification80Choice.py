# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BBANIdentifier
from . import IBAN2007Identifier
from . import Max16Text
from . import Max256Text
from . import SimpleIdentificationInformation4
from . import UPICIdentifier

class AccountIdentification80Choice(base_types._BaseFieldType):

	__slots__ = ["_BBAN", "_DmstAcct", "_Email", "_IBAN", "_MSISDN", "_UPIC"]
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
	def DmstAcct(self):
		return self._DmstAcct

	@DmstAcct.setter
	def DmstAcct(self, value):
		self._DmstAcct = value if value is not None else base_types.UninitialisedField(self, 'DmstAcct', SimpleIdentificationInformation4, False)

	@DmstAcct.deleter
	def DmstAcct(self):
		del self._DmstAcct
		self._DmstAcct = base_types.UninitialisedField(self, 'DmstAcct', SimpleIdentificationInformation4, False)

	@property
	def Email(self):
		return self._Email

	@Email.setter
	def Email(self, value):
		self._Email = value if value is not None else base_types.UninitialisedField(self, 'Email', Max256Text, False)

	@Email.deleter
	def Email(self):
		del self._Email
		self._Email = base_types.UninitialisedField(self, 'Email', Max256Text, False)

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
		base_types.FieldEntry(name='DmstAcct', type=SimpleIdentificationInformation4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Email', type=Max256Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IBAN', type=IBAN2007Identifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MSISDN', type=Max16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UPIC', type=UPICIdentifier, min=0, max=1, mutex_group=1, array=False),
	))