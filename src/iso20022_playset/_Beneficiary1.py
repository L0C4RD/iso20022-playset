# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AddressOrParty1Choice
from . import Max2000Text

class Beneficiary1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_NewAdrOrNewBnfcry"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, True)

	@property
	def NewAdrOrNewBnfcry(self):
		return self._NewAdrOrNewBnfcry

	@NewAdrOrNewBnfcry.setter
	def NewAdrOrNewBnfcry(self, value):
		self._NewAdrOrNewBnfcry = value if value is not None else base_types.UninitialisedField(self, 'NewAdrOrNewBnfcry', AddressOrParty1Choice, False)

	@NewAdrOrNewBnfcry.deleter
	def NewAdrOrNewBnfcry(self):
		del self._NewAdrOrNewBnfcry
		self._NewAdrOrNewBnfcry = base_types.UninitialisedField(self, 'NewAdrOrNewBnfcry', AddressOrParty1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='NewAdrOrNewBnfcry', type=AddressOrParty1Choice, min=1, max=1, mutex_group=None, array=False),
	))