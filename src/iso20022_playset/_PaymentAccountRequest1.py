# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardAccountType3Code
from . import CustomerOrder1
from . import Max35Text

class PaymentAccountRequest1(base_types._BaseFieldType):

	__slots__ = ["_AcctRef", "_AcctTp", "_CstmrOrdr"]
	@property
	def AcctRef(self):
		return self._AcctRef

	@AcctRef.setter
	def AcctRef(self, value):
		self._AcctRef = value if value is not None else base_types.UninitialisedField(self, 'AcctRef', Max35Text, False)

	@AcctRef.deleter
	def AcctRef(self):
		del self._AcctRef
		self._AcctRef = base_types.UninitialisedField(self, 'AcctRef', Max35Text, False)

	@property
	def AcctTp(self):
		return self._AcctTp

	@AcctTp.setter
	def AcctTp(self, value):
		self._AcctTp = value if value is not None else base_types.UninitialisedField(self, 'AcctTp', CardAccountType3Code, False)

	@AcctTp.deleter
	def AcctTp(self):
		del self._AcctTp
		self._AcctTp = base_types.UninitialisedField(self, 'AcctTp', CardAccountType3Code, False)

	@property
	def CstmrOrdr(self):
		return self._CstmrOrdr

	@CstmrOrdr.setter
	def CstmrOrdr(self, value):
		self._CstmrOrdr = value if value is not None else base_types.UninitialisedField(self, 'CstmrOrdr', CustomerOrder1, False)

	@CstmrOrdr.deleter
	def CstmrOrdr(self):
		del self._CstmrOrdr
		self._CstmrOrdr = base_types.UninitialisedField(self, 'CstmrOrdr', CustomerOrder1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTp', type=CardAccountType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrOrdr', type=CustomerOrder1, min=0, max=1, mutex_group=None, array=False),
	))