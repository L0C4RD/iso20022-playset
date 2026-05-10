from . import base_types
from .Max35Text import Max35Text
from .Max52Text import Max52Text

class Reference21(base_types._BaseFieldType):

	__slots__ = ["_CmonTxId", "_RcvrCollTxId", "_SndrCollTxId", "_RcvrCollCtrctId", "_SndrCollCtrctId"]
	@property
	def CmonTxId(self):
		return self._CmonTxId

	@CmonTxId.setter
	def CmonTxId(self, value):
		self._CmonTxId = value if type(value) != base_types.auto else self.make_default("CmonTxId")

	@CmonTxId.deleter
	def CmonTxId(self):
		del self._CmonTxId
		self._CmonTxId = None

	@property
	def RcvrCollTxId(self):
		return self._RcvrCollTxId

	@RcvrCollTxId.setter
	def RcvrCollTxId(self, value):
		self._RcvrCollTxId = value if type(value) != base_types.auto else self.make_default("RcvrCollTxId")

	@RcvrCollTxId.deleter
	def RcvrCollTxId(self):
		del self._RcvrCollTxId
		self._RcvrCollTxId = None

	@property
	def SndrCollTxId(self):
		return self._SndrCollTxId

	@SndrCollTxId.setter
	def SndrCollTxId(self, value):
		self._SndrCollTxId = value if type(value) != base_types.auto else self.make_default("SndrCollTxId")

	@SndrCollTxId.deleter
	def SndrCollTxId(self):
		del self._SndrCollTxId
		self._SndrCollTxId = None

	@property
	def RcvrCollCtrctId(self):
		return self._RcvrCollCtrctId

	@RcvrCollCtrctId.setter
	def RcvrCollCtrctId(self, value):
		self._RcvrCollCtrctId = value if type(value) != base_types.auto else self.make_default("RcvrCollCtrctId")

	@RcvrCollCtrctId.deleter
	def RcvrCollCtrctId(self):
		del self._RcvrCollCtrctId
		self._RcvrCollCtrctId = None

	@property
	def SndrCollCtrctId(self):
		return self._SndrCollCtrctId

	@SndrCollCtrctId.setter
	def SndrCollCtrctId(self, value):
		self._SndrCollCtrctId = value if type(value) != base_types.auto else self.make_default("SndrCollCtrctId")

	@SndrCollCtrctId.deleter
	def SndrCollCtrctId(self):
		del self._SndrCollCtrctId
		self._SndrCollCtrctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmonTxId', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvrCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndrCollTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvrCollCtrctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndrCollCtrctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

