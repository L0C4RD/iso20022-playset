# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountAndBalance64
from . import AccountIdentification10

class AccountIdentification76Choice(base_types._BaseFieldType):

	__slots__ = ["_AcctsListAndBalDtls", "_ForAllAccts"]
	@property
	def AcctsListAndBalDtls(self):
		return self._AcctsListAndBalDtls

	@AcctsListAndBalDtls.setter
	def AcctsListAndBalDtls(self, value):
		self._AcctsListAndBalDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctsListAndBalDtls', AccountAndBalance64, True)

	@AcctsListAndBalDtls.deleter
	def AcctsListAndBalDtls(self):
		del self._AcctsListAndBalDtls
		self._AcctsListAndBalDtls = base_types.UninitialisedField(self, 'AcctsListAndBalDtls', AccountAndBalance64, True)

	@property
	def ForAllAccts(self):
		return self._ForAllAccts

	@ForAllAccts.setter
	def ForAllAccts(self, value):
		self._ForAllAccts = value if value is not None else base_types.UninitialisedField(self, 'ForAllAccts', AccountIdentification10, False)

	@ForAllAccts.deleter
	def ForAllAccts(self):
		del self._ForAllAccts
		self._ForAllAccts = base_types.UninitialisedField(self, 'ForAllAccts', AccountIdentification10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctsListAndBalDtls', type=AccountAndBalance64, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='ForAllAccts', type=AccountIdentification10, min=0, max=1, mutex_group=1, array=False),
	))