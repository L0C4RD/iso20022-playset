# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClearingAccountType3Code
from . import CollateralAccount5

class ClearingAccount1(base_types._BaseFieldType):

	__slots__ = ["_AcctTp", "_CollAcctOwnr"]
	@property
	def AcctTp(self):
		return self._AcctTp

	@AcctTp.setter
	def AcctTp(self, value):
		self._AcctTp = value if value is not None else base_types.UninitialisedField(self, 'AcctTp', ClearingAccountType3Code, False)

	@AcctTp.deleter
	def AcctTp(self):
		del self._AcctTp
		self._AcctTp = base_types.UninitialisedField(self, 'AcctTp', ClearingAccountType3Code, False)

	@property
	def CollAcctOwnr(self):
		return self._CollAcctOwnr

	@CollAcctOwnr.setter
	def CollAcctOwnr(self, value):
		self._CollAcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'CollAcctOwnr', CollateralAccount5, True)

	@CollAcctOwnr.deleter
	def CollAcctOwnr(self):
		del self._CollAcctOwnr
		self._CollAcctOwnr = base_types.UninitialisedField(self, 'CollAcctOwnr', CollateralAccount5, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctTp', type=ClearingAccountType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollAcctOwnr', type=CollateralAccount5, min=1, max=None, mutex_group=None, array=True),
	))