# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestedIndicator

class AccountCashEntryReturnCriteria3(base_types._BaseFieldType):

	__slots__ = ["_AcctCcyInd", "_AcctOwnrInd", "_AcctSvcrInd", "_AcctTpInd", "_NtryAmtInd", "_NtryDtInd", "_NtryRefInd", "_NtryStsInd"]
	@property
	def AcctCcyInd(self):
		return self._AcctCcyInd

	@AcctCcyInd.setter
	def AcctCcyInd(self, value):
		self._AcctCcyInd = value if value is not None else base_types.UninitialisedField(self, 'AcctCcyInd', RequestedIndicator, False)

	@AcctCcyInd.deleter
	def AcctCcyInd(self):
		del self._AcctCcyInd
		self._AcctCcyInd = base_types.UninitialisedField(self, 'AcctCcyInd', RequestedIndicator, False)

	@property
	def AcctOwnrInd(self):
		return self._AcctOwnrInd

	@AcctOwnrInd.setter
	def AcctOwnrInd(self, value):
		self._AcctOwnrInd = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnrInd', RequestedIndicator, False)

	@AcctOwnrInd.deleter
	def AcctOwnrInd(self):
		del self._AcctOwnrInd
		self._AcctOwnrInd = base_types.UninitialisedField(self, 'AcctOwnrInd', RequestedIndicator, False)

	@property
	def AcctSvcrInd(self):
		return self._AcctSvcrInd

	@AcctSvcrInd.setter
	def AcctSvcrInd(self, value):
		self._AcctSvcrInd = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcrInd', RequestedIndicator, False)

	@AcctSvcrInd.deleter
	def AcctSvcrInd(self):
		del self._AcctSvcrInd
		self._AcctSvcrInd = base_types.UninitialisedField(self, 'AcctSvcrInd', RequestedIndicator, False)

	@property
	def AcctTpInd(self):
		return self._AcctTpInd

	@AcctTpInd.setter
	def AcctTpInd(self, value):
		self._AcctTpInd = value if value is not None else base_types.UninitialisedField(self, 'AcctTpInd', RequestedIndicator, False)

	@AcctTpInd.deleter
	def AcctTpInd(self):
		del self._AcctTpInd
		self._AcctTpInd = base_types.UninitialisedField(self, 'AcctTpInd', RequestedIndicator, False)

	@property
	def NtryAmtInd(self):
		return self._NtryAmtInd

	@NtryAmtInd.setter
	def NtryAmtInd(self, value):
		self._NtryAmtInd = value if value is not None else base_types.UninitialisedField(self, 'NtryAmtInd', RequestedIndicator, False)

	@NtryAmtInd.deleter
	def NtryAmtInd(self):
		del self._NtryAmtInd
		self._NtryAmtInd = base_types.UninitialisedField(self, 'NtryAmtInd', RequestedIndicator, False)

	@property
	def NtryDtInd(self):
		return self._NtryDtInd

	@NtryDtInd.setter
	def NtryDtInd(self, value):
		self._NtryDtInd = value if value is not None else base_types.UninitialisedField(self, 'NtryDtInd', RequestedIndicator, False)

	@NtryDtInd.deleter
	def NtryDtInd(self):
		del self._NtryDtInd
		self._NtryDtInd = base_types.UninitialisedField(self, 'NtryDtInd', RequestedIndicator, False)

	@property
	def NtryRefInd(self):
		return self._NtryRefInd

	@NtryRefInd.setter
	def NtryRefInd(self, value):
		self._NtryRefInd = value if value is not None else base_types.UninitialisedField(self, 'NtryRefInd', RequestedIndicator, False)

	@NtryRefInd.deleter
	def NtryRefInd(self):
		del self._NtryRefInd
		self._NtryRefInd = base_types.UninitialisedField(self, 'NtryRefInd', RequestedIndicator, False)

	@property
	def NtryStsInd(self):
		return self._NtryStsInd

	@NtryStsInd.setter
	def NtryStsInd(self, value):
		self._NtryStsInd = value if value is not None else base_types.UninitialisedField(self, 'NtryStsInd', RequestedIndicator, False)

	@NtryStsInd.deleter
	def NtryStsInd(self):
		del self._NtryStsInd
		self._NtryStsInd = base_types.UninitialisedField(self, 'NtryStsInd', RequestedIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctCcyInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctTpInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryAmtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryDtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryRefInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtryStsInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))