from . import base_types
from ._xs:IDREF import xs:IDREF

class FinancingNotificationParties1(base_types._BaseFieldType):

	__slots__ = ["_NtifngPty", "_AckRcvr", "_NtfctnRcvr"]
	@property
	def AckRcvr(self):
		return self._AckRcvr

	@AckRcvr.setter
	def AckRcvr(self, value):
		self._AckRcvr = value if type(value) != base_types.auto else self.make_default("AckRcvr")

	@AckRcvr.deleter
	def AckRcvr(self):
		del self._AckRcvr
		self._AckRcvr = None

	@property
	def NtfctnRcvr(self):
		return self._NtfctnRcvr

	@NtfctnRcvr.setter
	def NtfctnRcvr(self, value):
		self._NtfctnRcvr = value if type(value) != base_types.auto else self.make_default("NtfctnRcvr")

	@NtfctnRcvr.deleter
	def NtfctnRcvr(self):
		del self._NtfctnRcvr
		self._NtfctnRcvr = None

	@property
	def NtifngPty(self):
		return self._NtifngPty

	@NtifngPty.setter
	def NtifngPty(self, value):
		self._NtifngPty = value if type(value) != base_types.auto else self.make_default("NtifngPty")

	@NtifngPty.deleter
	def NtifngPty(self):
		del self._NtifngPty
		self._NtifngPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AckRcvr', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtfctnRcvr', type=XS_IDREF, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtifngPty', type=XS_IDREF, min=1, max=1, mutex_group=None, array=False),
	))

