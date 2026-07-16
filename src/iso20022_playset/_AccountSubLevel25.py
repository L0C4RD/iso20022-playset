# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import PartyIdentification276
from . import ShareholdingBalance1

class AccountSubLevel25(base_types._BaseFieldType):

	__slots__ = ["_AcctHldr", "_SfkpgAcct", "_ShrhldgBal"]
	@property
	def AcctHldr(self):
		return self._AcctHldr

	@AcctHldr.setter
	def AcctHldr(self, value):
		self._AcctHldr = value if value is not None else base_types.UninitialisedField(self, 'AcctHldr', PartyIdentification276, False)

	@AcctHldr.deleter
	def AcctHldr(self):
		del self._AcctHldr
		self._AcctHldr = base_types.UninitialisedField(self, 'AcctHldr', PartyIdentification276, False)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', Max35Text, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', Max35Text, False)

	@property
	def ShrhldgBal(self):
		return self._ShrhldgBal

	@ShrhldgBal.setter
	def ShrhldgBal(self, value):
		self._ShrhldgBal = value if value is not None else base_types.UninitialisedField(self, 'ShrhldgBal', ShareholdingBalance1, True)

	@ShrhldgBal.deleter
	def ShrhldgBal(self):
		del self._ShrhldgBal
		self._ShrhldgBal = base_types.UninitialisedField(self, 'ShrhldgBal', ShareholdingBalance1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctHldr', type=PartyIdentification276, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldgBal', type=ShareholdingBalance1, min=1, max=None, mutex_group=None, array=True),
	))