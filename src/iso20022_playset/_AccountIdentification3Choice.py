# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BBANIdentifier
from . import IBANIdentifier
from . import SimpleIdentificationInformation2
from . import UPICIdentifier

class AccountIdentification3Choice(base_types._BaseFieldType):

	__slots__ = ["_BBAN", "_IBAN", "_PrtryAcct", "_UPIC"]
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
	def IBAN(self):
		return self._IBAN

	@IBAN.setter
	def IBAN(self, value):
		self._IBAN = value if value is not None else base_types.UninitialisedField(self, 'IBAN', IBANIdentifier, False)

	@IBAN.deleter
	def IBAN(self):
		del self._IBAN
		self._IBAN = base_types.UninitialisedField(self, 'IBAN', IBANIdentifier, False)

	@property
	def PrtryAcct(self):
		return self._PrtryAcct

	@PrtryAcct.setter
	def PrtryAcct(self, value):
		self._PrtryAcct = value if value is not None else base_types.UninitialisedField(self, 'PrtryAcct', SimpleIdentificationInformation2, False)

	@PrtryAcct.deleter
	def PrtryAcct(self):
		del self._PrtryAcct
		self._PrtryAcct = base_types.UninitialisedField(self, 'PrtryAcct', SimpleIdentificationInformation2, False)

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
		base_types.FieldEntry(name='IBAN', type=IBANIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryAcct', type=SimpleIdentificationInformation2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UPIC', type=UPICIdentifier, min=0, max=1, mutex_group=1, array=False),
	))