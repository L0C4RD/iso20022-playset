# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMService18
from . import ATMServiceType13Code
from . import ATMTransactionAmounts6

class ATMService29(base_types._BaseFieldType):

	__slots__ = ["_Lmts", "_SvcTp", "_SvcVarnt"]
	@property
	def Lmts(self):
		return self._Lmts

	@Lmts.setter
	def Lmts(self, value):
		self._Lmts = value if value is not None else base_types.UninitialisedField(self, 'Lmts', ATMTransactionAmounts6, True)

	@Lmts.deleter
	def Lmts(self):
		del self._Lmts
		self._Lmts = base_types.UninitialisedField(self, 'Lmts', ATMTransactionAmounts6, True)

	@property
	def SvcTp(self):
		return self._SvcTp

	@SvcTp.setter
	def SvcTp(self, value):
		self._SvcTp = value if value is not None else base_types.UninitialisedField(self, 'SvcTp', ATMServiceType13Code, False)

	@SvcTp.deleter
	def SvcTp(self):
		del self._SvcTp
		self._SvcTp = base_types.UninitialisedField(self, 'SvcTp', ATMServiceType13Code, False)

	@property
	def SvcVarnt(self):
		return self._SvcVarnt

	@SvcVarnt.setter
	def SvcVarnt(self, value):
		self._SvcVarnt = value if value is not None else base_types.UninitialisedField(self, 'SvcVarnt', ATMService18, True)

	@SvcVarnt.deleter
	def SvcVarnt(self):
		del self._SvcVarnt
		self._SvcVarnt = base_types.UninitialisedField(self, 'SvcVarnt', ATMService18, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Lmts', type=ATMTransactionAmounts6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcTp', type=ATMServiceType13Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcVarnt', type=ATMService18, min=0, max=None, mutex_group=None, array=True),
	))