# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification1
from . import SecuritiesAccountPurposeType1Code

class AccountIdentificationAndPurpose(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Purp"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', AccountIdentification1, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', AccountIdentification1, False)

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if value is not None else base_types.UninitialisedField(self, 'Purp', SecuritiesAccountPurposeType1Code, False)

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = base_types.UninitialisedField(self, 'Purp', SecuritiesAccountPurposeType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=AccountIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=SecuritiesAccountPurposeType1Code, min=1, max=1, mutex_group=None, array=False),
	))