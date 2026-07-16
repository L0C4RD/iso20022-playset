# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import Max52Text

class Reference21(base_types._BaseFieldType):

	__slots__ = ["_CmonTxId", "_RcvrCollCtrctId", "_RcvrCollTxId", "_SndrCollCtrctId", "_SndrCollTxId"]
	@property
	def CmonTxId(self):
		return self._CmonTxId

	@CmonTxId.setter
	def CmonTxId(self, value):
		self._CmonTxId = value if value is not None else base_types.UninitialisedField(self, 'CmonTxId', Max52Text, False)

	@CmonTxId.deleter
	def CmonTxId(self):
		del self._CmonTxId
		self._CmonTxId = base_types.UninitialisedField(self, 'CmonTxId', Max52Text, False)

	@property
	def RcvrCollCtrctId(self):
		return self._RcvrCollCtrctId

	@RcvrCollCtrctId.setter
	def RcvrCollCtrctId(self, value):
		self._RcvrCollCtrctId = value if value is not None else base_types.UninitialisedField(self, 'RcvrCollCtrctId', Max35Text, False)

	@RcvrCollCtrctId.deleter
	def RcvrCollCtrctId(self):
		del self._RcvrCollCtrctId
		self._RcvrCollCtrctId = base_types.UninitialisedField(self, 'RcvrCollCtrctId', Max35Text, False)

	@property
	def RcvrCollTxId(self):
		return self._RcvrCollTxId

	@RcvrCollTxId.setter
	def RcvrCollTxId(self, value):
		self._RcvrCollTxId = value if value is not None else base_types.UninitialisedField(self, 'RcvrCollTxId', Max35Text, False)

	@RcvrCollTxId.deleter
	def RcvrCollTxId(self):
		del self._RcvrCollTxId
		self._RcvrCollTxId = base_types.UninitialisedField(self, 'RcvrCollTxId', Max35Text, False)

	@property
	def SndrCollCtrctId(self):
		return self._SndrCollCtrctId

	@SndrCollCtrctId.setter
	def SndrCollCtrctId(self, value):
		self._SndrCollCtrctId = value if value is not None else base_types.UninitialisedField(self, 'SndrCollCtrctId', Max35Text, False)

	@SndrCollCtrctId.deleter
	def SndrCollCtrctId(self):
		del self._SndrCollCtrctId
		self._SndrCollCtrctId = base_types.UninitialisedField(self, 'SndrCollCtrctId', Max35Text, False)

	@property
	def SndrCollTxId(self):
		return self._SndrCollTxId

	@SndrCollTxId.setter
	def SndrCollTxId(self, value):
		self._SndrCollTxId = value if value is not None else base_types.UninitialisedField(self, 'SndrCollTxId', Max35Text, False)

	@SndrCollTxId.deleter
	def SndrCollTxId(self):
		del self._SndrCollTxId
		self._SndrCollTxId = base_types.UninitialisedField(self, 'SndrCollTxId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmonTxId', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvrCollCtrctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvrCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndrCollCtrctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndrCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))