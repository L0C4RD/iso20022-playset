# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Balance29
from . import ISO8583AccountTypeCode

class AccountBalance3(base_types._BaseFieldType):

	__slots__ = ["_AcctTp", "_Bal"]
	@property
	def AcctTp(self):
		return self._AcctTp

	@AcctTp.setter
	def AcctTp(self, value):
		self._AcctTp = value if value is not None else base_types.UninitialisedField(self, 'AcctTp', ISO8583AccountTypeCode, False)

	@AcctTp.deleter
	def AcctTp(self):
		del self._AcctTp
		self._AcctTp = base_types.UninitialisedField(self, 'AcctTp', ISO8583AccountTypeCode, False)

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if value is not None else base_types.UninitialisedField(self, 'Bal', Balance29, True)

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = base_types.UninitialisedField(self, 'Bal', Balance29, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctTp', type=ISO8583AccountTypeCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bal', type=Balance29, min=1, max=None, mutex_group=None, array=True),
	))