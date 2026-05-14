# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Balance29 import Balance29
from ._ISO8583AccountTypeCode import ISO8583AccountTypeCode

class AccountBalance3(base_types._BaseFieldType):

	__slots__ = ["_AcctTp", "_Bal"]
	@property
	def AcctTp(self):
		return self._AcctTp

	@AcctTp.setter
	def AcctTp(self, value):
		self._AcctTp = value if type(value) != base_types.auto else self.make_default("AcctTp")

	@AcctTp.deleter
	def AcctTp(self):
		del self._AcctTp
		self._AcctTp = None

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != base_types.auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctTp', type=ISO8583AccountTypeCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bal', type=Balance29, min=1, max=None, mutex_group=None, array=True),
	))