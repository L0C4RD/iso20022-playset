# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max2000Text
from . import Max35Text

class AdvisingPartyAdditionalInformation1(base_types._BaseFieldType):

	__slots__ = ["_BkToBnfcryInf", "_RefNb"]
	@property
	def BkToBnfcryInf(self):
		return self._BkToBnfcryInf

	@BkToBnfcryInf.setter
	def BkToBnfcryInf(self, value):
		self._BkToBnfcryInf = value if value is not None else base_types.UninitialisedField(self, 'BkToBnfcryInf', Max2000Text, True)

	@BkToBnfcryInf.deleter
	def BkToBnfcryInf(self):
		del self._BkToBnfcryInf
		self._BkToBnfcryInf = base_types.UninitialisedField(self, 'BkToBnfcryInf', Max2000Text, True)

	@property
	def RefNb(self):
		return self._RefNb

	@RefNb.setter
	def RefNb(self, value):
		self._RefNb = value if value is not None else base_types.UninitialisedField(self, 'RefNb', Max35Text, False)

	@RefNb.deleter
	def RefNb(self):
		del self._RefNb
		self._RefNb = base_types.UninitialisedField(self, 'RefNb', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BkToBnfcryInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='RefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))