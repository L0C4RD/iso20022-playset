# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccount40
from . import GenericIdentification1
from . import UnderlyingPaymentInstruction11
from . import UnderlyingPaymentTransaction11
from . import UnderlyingStatementEntry11

class UnderlyingData13Choice(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Initn", "_IntrBk", "_Othr", "_StmtNtry"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', CashAccount40, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', CashAccount40, False)

	@property
	def Initn(self):
		return self._Initn

	@Initn.setter
	def Initn(self, value):
		self._Initn = value if value is not None else base_types.UninitialisedField(self, 'Initn', UnderlyingPaymentInstruction11, False)

	@Initn.deleter
	def Initn(self):
		del self._Initn
		self._Initn = base_types.UninitialisedField(self, 'Initn', UnderlyingPaymentInstruction11, False)

	@property
	def IntrBk(self):
		return self._IntrBk

	@IntrBk.setter
	def IntrBk(self, value):
		self._IntrBk = value if value is not None else base_types.UninitialisedField(self, 'IntrBk', UnderlyingPaymentTransaction11, False)

	@IntrBk.deleter
	def IntrBk(self):
		del self._IntrBk
		self._IntrBk = base_types.UninitialisedField(self, 'IntrBk', UnderlyingPaymentTransaction11, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', GenericIdentification1, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', GenericIdentification1, False)

	@property
	def StmtNtry(self):
		return self._StmtNtry

	@StmtNtry.setter
	def StmtNtry(self, value):
		self._StmtNtry = value if value is not None else base_types.UninitialisedField(self, 'StmtNtry', UnderlyingStatementEntry11, False)

	@StmtNtry.deleter
	def StmtNtry(self):
		del self._StmtNtry
		self._StmtNtry = base_types.UninitialisedField(self, 'StmtNtry', UnderlyingStatementEntry11, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Initn', type=UnderlyingPaymentInstruction11, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrBk', type=UnderlyingPaymentTransaction11, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StmtNtry', type=UnderlyingStatementEntry11, min=0, max=1, mutex_group=1, array=False),
	))