from . import base_types
from .RequestedIndicator import RequestedIndicator

class AccountCashEntryReturnCriteria3(base_types._BaseFieldType):

	__slots__ = ["_NtryAmtInd", "_AcctTpInd", "_AcctOwnrInd", "_AcctSvcrInd", "_NtryStsInd", "_AcctCcyInd", "_NtryRefInd", "_NtryDtInd"]
	@property
	def NtryAmtInd(self):
		return self._NtryAmtInd

	@NtryAmtInd.setter
	def NtryAmtInd(self, value):
		self._NtryAmtInd = value if type(value) != auto else self.make_default("NtryAmtInd")

	@NtryAmtInd.deleter
	def NtryAmtInd(self):
		del self._NtryAmtInd
		self._NtryAmtInd = None

	@property
	def AcctTpInd(self):
		return self._AcctTpInd

	@AcctTpInd.setter
	def AcctTpInd(self, value):
		self._AcctTpInd = value if type(value) != auto else self.make_default("AcctTpInd")

	@AcctTpInd.deleter
	def AcctTpInd(self):
		del self._AcctTpInd
		self._AcctTpInd = None

	@property
	def AcctOwnrInd(self):
		return self._AcctOwnrInd

	@AcctOwnrInd.setter
	def AcctOwnrInd(self, value):
		self._AcctOwnrInd = value if type(value) != auto else self.make_default("AcctOwnrInd")

	@AcctOwnrInd.deleter
	def AcctOwnrInd(self):
		del self._AcctOwnrInd
		self._AcctOwnrInd = None

	@property
	def AcctSvcrInd(self):
		return self._AcctSvcrInd

	@AcctSvcrInd.setter
	def AcctSvcrInd(self, value):
		self._AcctSvcrInd = value if type(value) != auto else self.make_default("AcctSvcrInd")

	@AcctSvcrInd.deleter
	def AcctSvcrInd(self):
		del self._AcctSvcrInd
		self._AcctSvcrInd = None

	@property
	def NtryStsInd(self):
		return self._NtryStsInd

	@NtryStsInd.setter
	def NtryStsInd(self, value):
		self._NtryStsInd = value if type(value) != auto else self.make_default("NtryStsInd")

	@NtryStsInd.deleter
	def NtryStsInd(self):
		del self._NtryStsInd
		self._NtryStsInd = None

	@property
	def AcctCcyInd(self):
		return self._AcctCcyInd

	@AcctCcyInd.setter
	def AcctCcyInd(self, value):
		self._AcctCcyInd = value if type(value) != auto else self.make_default("AcctCcyInd")

	@AcctCcyInd.deleter
	def AcctCcyInd(self):
		del self._AcctCcyInd
		self._AcctCcyInd = None

	@property
	def NtryRefInd(self):
		return self._NtryRefInd

	@NtryRefInd.setter
	def NtryRefInd(self, value):
		self._NtryRefInd = value if type(value) != auto else self.make_default("NtryRefInd")

	@NtryRefInd.deleter
	def NtryRefInd(self):
		del self._NtryRefInd
		self._NtryRefInd = None

	@property
	def NtryDtInd(self):
		return self._NtryDtInd

	@NtryDtInd.setter
	def NtryDtInd(self, value):
		self._NtryDtInd = value if type(value) != auto else self.make_default("NtryDtInd")

	@NtryDtInd.deleter
	def NtryDtInd(self):
		del self._NtryDtInd
		self._NtryDtInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtryAmtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTpInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryStsInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctCcyInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryRefInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryDtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))

