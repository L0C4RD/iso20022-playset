# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Account23
from . import AdditionalReference13
from . import Max350Text
from . import Max35Text

class InvestmentAccountModification4(base_types._BaseFieldType):

	__slots__ = ["_AcctApplId", "_ClntRef", "_CtrPtyRef", "_ExstgAcctId", "_ModRsn"]
	@property
	def AcctApplId(self):
		return self._AcctApplId

	@AcctApplId.setter
	def AcctApplId(self, value):
		self._AcctApplId = value if value is not None else base_types.UninitialisedField(self, 'AcctApplId', Max35Text, False)

	@AcctApplId.deleter
	def AcctApplId(self):
		del self._AcctApplId
		self._AcctApplId = base_types.UninitialisedField(self, 'AcctApplId', Max35Text, False)

	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if value is not None else base_types.UninitialisedField(self, 'ClntRef', Max35Text, False)

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = base_types.UninitialisedField(self, 'ClntRef', Max35Text, False)

	@property
	def CtrPtyRef(self):
		return self._CtrPtyRef

	@CtrPtyRef.setter
	def CtrPtyRef(self, value):
		self._CtrPtyRef = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyRef', AdditionalReference13, False)

	@CtrPtyRef.deleter
	def CtrPtyRef(self):
		del self._CtrPtyRef
		self._CtrPtyRef = base_types.UninitialisedField(self, 'CtrPtyRef', AdditionalReference13, False)

	@property
	def ExstgAcctId(self):
		return self._ExstgAcctId

	@ExstgAcctId.setter
	def ExstgAcctId(self, value):
		self._ExstgAcctId = value if value is not None else base_types.UninitialisedField(self, 'ExstgAcctId', Account23, True)

	@ExstgAcctId.deleter
	def ExstgAcctId(self):
		del self._ExstgAcctId
		self._ExstgAcctId = base_types.UninitialisedField(self, 'ExstgAcctId', Account23, True)

	@property
	def ModRsn(self):
		return self._ModRsn

	@ModRsn.setter
	def ModRsn(self, value):
		self._ModRsn = value if value is not None else base_types.UninitialisedField(self, 'ModRsn', Max350Text, False)

	@ModRsn.deleter
	def ModRsn(self):
		del self._ModRsn
		self._ModRsn = base_types.UninitialisedField(self, 'ModRsn', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctApplId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyRef', type=AdditionalReference13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExstgAcctId', type=Account23, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModRsn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))